#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
app = Flask(__name__)
GoogleMaps(app)

import twitter
import io
import json

#conectarse a twitter
def login():
    consumer_key = 'YAEs1DEFodUb3YcII8P8ajiL9'
    consumer_secret = 'Mdi1cil2ij89wWt1o7n1h8FTKY51CxQyot3pWhdcjaXIWVqgv5'
    oauth_token = '3108274757-bRKR5GuHGs40RgX10bRXo6sgkKBTAjkdwoXLHxb'
    oauth_token_secret = 'faEN9wLLogCoK839QickmNAo8xaFLBR3Sj1rPpcmzaRjZ'

    author = twitter.oauth.OAuth(oauth_token,oauth_token_secret,consumer_key,consumer_secret)
    api = twitter.Twitter(auth = author)
    return api
    
#guardar los datos en el fichero json
def guardar_datos(name,busqueda):
    with io.open('topic.json'.format(name),'w',encoding = 'utf-8') as data:
        data.write(unicode(json.dumps(busqueda,ensure_ascii = False)))
    
#leer los datos del fichero json
def leer_datos():
    with open('topic.json') as data:
        return json.load(data)

#obtener lista de coordenadas
def lista_coordenadas(topic):
	#se han cogido las coordenadas de la Puerta del Sol como referencia (km. 0 de España)
    busqueda = twitter.search.tweets(q = topic, geocode='40.4173175,-3.702233699999965,750km')
	#guardar datos de la busqueda en un fichero
    guardar_datos(topic,busqueda)
	#leer datos del fichero
    datos = leer_datos()
	#crear lista y guardar puntos
    puntos = []
    for estado in datos["statuses"]:
        if estado["coordinates"] != None :
            coordenadas = estado["coordinates"]
       	    xy = [coordenadas.values()[1][1] , coordenadas.values()[1][0]]
            puntos.append(xy)

	return puntos
	
#login en twitter
twitter = login()

print "introduzca tema"
topic = raw_input()

Coord_topic = lista_coordenadas(topic)

#crear mapa y marcar puntos
@app.route("/")
def mapview():
    mymap = Map(
	    identifier="view-side",
        lat=40.416947,
        lng=-3.703528,
        markers=Coord_topic1,
        style="height:400px;width:400px;margin:0;"
    )
    return render_template('template2.html', mymap=mymap)

if __name__ == "__main__":
    app.run(debug=True)



