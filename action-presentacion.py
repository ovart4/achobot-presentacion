#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    if intent_message.intent.intent_name == 'josenka:presentacion':
        sentence = 'Hola, soy Lola. Soy una plataforma robótica de asistencia a personas de edad avanzada. He sido diseñado por un estudiante de la UPCT y dispongo de una interfaz de voz, una interfaz gráfica y un diseño muy bonito.'
    else:
        return
    
    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
