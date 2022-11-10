from app import mqtt, db
from flask import json
from app.schemas.sensors import sensor1,sensor2,sensor3,sensor4


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('duvan/sensores')
    mqtt.subscribe('manuel/sensores')
    mqtt.subscribe('eudes/sensores')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    
    if (message.topic == 'duvan/sensores'):
        my_json1 = message.payload.decode('utf8')
        data1 = json.loads(my_json1)
        Datos_recibido = sensor1(dato = data1['nivel'])
        db.session.add(Datos_recibido)
        db.session.commit()

    elif(message.topic == 'manuel/sensores'):
        my_json2 = message.payload.decode('utf8')
        data2 = json.loads(my_json2)
        Datos_recibido2 = sensor2(dato = data2['nivel'])
        db.session.add(Datos_recibido2)
        db.session.commit()
       
       
    elif(message.topic == 'eudes/sensores'):
        my_json3 = message.payload.decode('utf8')
        data3 = json.loads(my_json3)
        Datos_recibido = sensor3(dato = data3['nivel'])
        db.session.add(Datos_recibido)
        db.session.commit()
        Datos_recibido2 = sensor4(dato = data3['nivel'])
        db.session.add(Datos_recibido2)
        db.session.commit()

    
# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#     print(level,buf)