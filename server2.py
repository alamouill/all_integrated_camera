# -*- coding: utf-8 -*-

# Définition d'un serveur réseau gérant un système de CHAT simplifié.
# Utilise les threads pour gérer les connexions clientes en parallèle.

HOST = '192.168.43.222'
PORT = 12800

import socket, sys, threading

#My module
from servo import *
from camera import *
from ultimate_gps import *
from imu import *

class ThreadClientReceive(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.verrou=threading.Lock()
        
    def run(self):
        # Dialogue avec le client :
        nom = self.getName()        # Chaque thread possède un nom
        while True:
            print("Waiting For new message \n")
            msgClient = self.connexion.recv(1024)
            msgClient = msgClient.decode('utf-8')
            print ("**%s** de %s \n" % (msgClient, nom))
            deb = msgClient.split(',')[0]
            if deb == "FIN" or msgClient =="":
               break
            elif deb =="servo_pan_left":
                print("servo_pan_left")
                servo_pan_left()
            elif deb =="servo_pan_right":
                print("servo_pan_lright")
                servo_pan_right()
            elif deb =="servo_tilt_up":
                print("servo_tilt_up")
                servo_tilt_up()
            elif deb =="servo_tilt_down":
                print("servo_tilt_down \n")
                servo_tilt_down()
            elif deb =="camera_take_picture":
                print("camera_take_picture \n")
                camera_take_picture()
            elif deb =="calibrate":
                #servo_calibrate()
                print('calibrate \n')
            elif deb =="thymio_go_left":
                #thymio_go_left()
                print('left \n')
            elif deb =="thymio_go_right":
                #thymio_go_right()
                print('right \n')
            elif deb =="thymio_go_straight":
                #thymio_go_straight()
                print('Straight \n')
            elif deb =="thymio_go_backward":
                #thymio_go_backward()
                print('Back \n')
            elif deb =="thymio_stop":
                #thymio_stop()
                print('Stop \n')
            else:
                print("Unknown Command %s  \n" %msgClient)
        # Fermeture de la connexion :
        print('exiting receiver thread\n')
        self.connexion.close()      # couper la connexion côté serveur
        del conn_client[nom]        # supprimer son entrée dans le dictionnaire
        print ("Client %s déconnecté." % nom)
        # Le thread se termine ici    

class ThreadClientSend(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.verrou=threading.Lock()
        
    def run(self):        
        # Envoyer les data à tous les autres clients :
        while True:
            print("Begining Data Transmission \n")
            imu="IMU,"+imu_current_value()+"\n"
            gps="GPS,"+gps_current_value()+"\n"
            for cle in conn_client:
                self.verrou.acquire()
                conn_client[cle].send(imu.encode('utf-8'))
                self.verrou.release()
                self.verrou.acquire()
                conn_client[cle].send(gps.encode('utf-8'))
                self.verrou.release()
            print("Data Transmission ACheived \n")
        print('Exiting send thread \n')
        

if __name__ == '__main__':
    # Initialisation du serveur - Mise en place du socket :
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.bind((HOST, PORT))
    except socket.error:
        print ("La liaison du socket à l'adresse choisie a échoué. \n")
        sys.exit()
    print ("Serveur prêt, en attente de requêtes ... \n")
    mySocket.listen(5)

    # Attente et prise en charge des connexions demandées par les clients :
    conn_client = {}                # dictionnaire des connexions clients
    # Initialises other threads
    init_servo()
    init_imu()
    init_gps()
    while 1:    
        connexion, adresse = mySocket.accept()
        # Créer un nouvel objet thread pour gérer la connexion :
        thR = ThreadClientReceive(connexion)
        thR.start()
        thS = ThreadClientSend(connexion)
        thS.start()

        # Mémoriser la connexion dans le dictionnaire : 
        it = thR.getName()        # identifiant du thread
        conn_client[it] = connexion
        print ("Client %s connecté, adresse IP %s, port %s. \n" %\
               (it, adresse[0], adresse[1]))
        # Dialogue avec le client :
        connexion.send("Vous etes connecte. Envoyez vos messages. \n".encode('utf-8'))

