# station_ioc
#ENG
General Description:
This IoT project aims to create a platform that allows communication between sensors connected to an ESP32 and a base station consisting of a Raspberry Pi. The goal is to design a dynamic website, accessible via the Internet, which displays data collected from these remote sensors. The base station acts as a gateway between the wireless sensor network and the Internet, using protocols like MQTT for data transmission. The web server, hosted on the Raspberry Pi, integrates an HTTP server, an application gateway for sensor access, and a database.

Materials Used:
  - ESP32: Microcontroller module for reading sensor data and sending it to the broker.
  - Raspberry Pi 3: Used as a server to host the MQTT broker and the web server.
  - Sensors :
              - Light sensor (photoresistor) to measure brightness.
              - Button to capture a binary state (pressed or not).
  - Mosquitto: MQTT broker installed on the Raspberry Pi to manage message flow.
  - Python: Used to develop the MQTT subscriber and the HTTP server.

Problems Encountered and Solutions
- SSH Connection to the Raspberry Pi:
    Problem: Difficulty connecting to the Raspberry Pi without a screen or keyboard.
    Solution: Enabled SSH by creating an empty file named "ssh" on the SD card, then connected via Ethernet and Putty.

- Displaying Data on the Website :
    Problem: Manual refreshing was needed to update the webpage with new data.
    Solution: Implemented automatic page refreshing every second to show updated sensor readings.
  
#FR
Description Générale:
Ce projet IoT vise à créer une plateforme permettant la communication entre des capteurs connectés sur une ESP32 et une station de base constituée d'une Raspberry Pi. Le but est de concevoir un site web dynamique, accessible via Internet, qui affiche les données collectées par ces capteurs distants. La station de base joue le rôle de passerelle entre le réseau de capteurs sans fil et l'Internet en utilisant des protocoles comme MQTT pour assurer la transmission des données. Le serveur web, hébergé sur la Raspberry Pi, intègre un serveur HTTP, une gateway applicative pour accéder aux capteurs, et une base de données.

Matériel Utilisé:
  - ESP32: Module microcontrôleur pour la lecture des capteurs et l'envoi des données.
  - Raspberry Pi 3 : Utilisée comme serveur pour héberger le broker MQTT et le serveur web.
  - Capteurs :
              - Photoresistance pour mesurer la luminosité.
              - Bouton pour capter un état binaire (appuyé ou non).
  - Mosquitto : Broker MQTT installé sur la Raspberry Pi pour la gestion des messages.
  - Python : Utilisé pour le développement du Subscriber MQTT et du serveur HTTP

Problèmes Rencontrés et Solutions
- Connexion à la Raspberry Pi via SSH :
    Problème : Difficulté à se connecter à la Raspberry Pi sans écran ni clavier.
    Solution : Activation de SSH en créant un fichier vide nommé "ssh" sur la carte SD, puis connexion via Ethernet et Putty.

- Affichage des données sur le site web :
    Problème : Difficulté à actualiser manuellement la page web pour voir les nouvelles données.
    Solution : Mise en place d'un rafraîchissement automatique de la page toutes les secondes.
