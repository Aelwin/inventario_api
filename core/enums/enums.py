from enum import Enum

class Idioma(str, Enum) :
    CASTELLANO = 'CASTELLANO'
    INGLES = 'INGLES'
    EUSKERA = 'EUSKERA'
    JAPONES = 'JAPONES'
    CATALAN = 'CATALAN'

class Formato (str, Enum) :
    FISICO = 'FISICO'
    DIGITAL = 'DIGITAL'
    AUDIOLIBRO = 'AUDIO LIBRO'