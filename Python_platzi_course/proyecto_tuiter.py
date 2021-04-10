import numpy as np 
import pandas as pd
#Definimos los tuits 
tuit1 = "Gran mexicano y excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!"
tuit2 = "Vaya serñora, que bueno que se asesora por alguien inteligente, no por el ignorante del Gatt."
tuit3 = "Se me ocurre y sin ver los videos de Platz que me informéis por donde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo"
tuit4 = "Soy docente universitario, estoy intentando preparar mis clases en modo platzi, bien didáctico, (le llamo modo noticiero), descargue un plataforma gratuita de grabación y transmisión de video, se llama Obs estudio! bueno la sigo remando con sus funciones pero sé que saldrá algo."

def feeling_analyzer(tuit):
    tuit.replace("!","").replace(",","").replace(".","").split(" ")


