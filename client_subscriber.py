import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

MQTT_TOPIC_LUM = "lum"
MQTT_TOPIC_BTN = "btn"

DATA_BASE = "BDDtoWEB.txt"

#initialisation des valeurs 
lum_val = 0
btn_val = 0

#vecteur des valeurs qu'on veut ecrire dans la Base de données
data = [lum_val, btn_val]

#ecriture dans la base de données
def writefile(data,filename):

  file = open(filename, "w")
  
  file.write("lum: ") 
  file.write(str(data[0]))
  file.write("%") 
  file.write("\n")

  file.write("btn: ") 
  file.write(str(data[4]))
  file.write("\n")
  
  file.close()

#fonction connexion
def on_connect(client, userdata, flags, rc):
    print("Connected to topic lumiere "+str(rc))
    client.subscribe(MQTT_TOPIC_LUM) 
    print("Connected to topic bouton "+str(rc))
    client.subscribe(MQTT_TOPIC_BTN)  

#fonction reception de message
def on_message(client, userdata, msg):
    topic_name = str(msg.topic) 
    payload = msg.payload.decode("utf-8")
    print(f"Received message on topic {topic_name}: {payload}")
    if(topic_name == "lum"): #si il s'agit du topic lum on enregistre la valeur dans lum_val
        print("lum_val = ", int(msg.payload.decode("utf-8")))
        global lum_val
        lum_val = int(msg.payload.decode("utf-8"))
  
    if(topic_name == "btn"): #s"il s'agit du topic bouton on enregiste sa valeur dans btn_val
        print("btn_val = ", int(msg.payload.decode("utf-8")))
        global btn_val
        btn_val = int(msg.payload.decode("utf-8"))
    #on met les nouvelles valeurs dans le vecteur data 
    data = [lum_val,btn_val]
    #ecrire data dans le fichier
    writefile(data,DATA_BASE)

#création de client: subscriber
client = mqtt.Client()

#assigner les fonctions à notre subscriber(raspberry pi3)
client.on_connect = on_connect
client.on_message = on_message

#connecter le subscriber au broker
client.connect(MQTT_BROKER, MQTT_PORT)

#boucle infinie
client.loop_forever()  