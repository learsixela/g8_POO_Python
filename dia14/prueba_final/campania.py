from datetime import date

class Campania():
    def __init__(self,nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios =[self.__instancia_de_anuncios(dicc)  for dicc in anuncios  ]
        # self.__anuncios =[Video, Video, Display, Social]
    #[{},{},{}]

    def __instancia_de_anuncios(self,anuncio: dict):
        
        #return Video()
        #return Social()
        #return Display()
        pass