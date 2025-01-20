from enum import Enum, auto

class Bioma(Enum):
    AGUA = auto()
    TIERRA = auto()
    MONTANA = auto()
    BOSQUE = auto()

class TexturaAgua(Enum): 

    DEFAULT = (0, 0, 255)
    AGUACALMADA = (0, 191, 255)
    AGUARIO = (0, 255, 255)


class TexturaTierra(Enum):

    DEFAULT =  (139, 69, 19)
    ARENACLARA = (255, 228, 181)
    TIERRAHUMERA = (160, 82, 45)
    CESPED = (60, 139, 113)



class TexturaMontana(Enum):
    DEFAULT = (169, 169, 169)
    ROCA = (128, 128, 128)
    NIEVE = (255, 255, 255)
    ROCAVOLCANICA = (80, 80, 80)

class texturaBosque(Enum):
     DEFAULT = (34, 139, 34)
     CESPED = (0, 255, 0)
     PRADERA = (0, 128, 0)
     MUSGO = (124, 252, 0)


bioma_data = {
    Bioma.AGUA: {
        "probabilidad": 0.3,
        "texturas": [TexturaAgua.DEFAULT, TexturaAgua.AGUACALMADA, TexturaAgua.AGUARIO]
    },
    Bioma.TIERRA: {
        "probabilidad": 0.4,
        "texturas": [TexturaTierra.DEFAULT, TexturaTierra.ARENACLARA, TexturaTierra.TIERRAHUMERA, TexturaTierra.CESPED]
    },
    Bioma.MONTANA: {
        "probabilidad": 0.2,
        "texturas": [TexturaMontana.DEFAULT, TexturaMontana.ROCA, TexturaMontana.NIEVE, TexturaMontana.ROCAVOLCANICA]
    },
    Bioma.BOSQUE: {
        "probabilidad": 0.1,
        "texturas": [texturaBosque.DEFAULT, texturaBosque.CESPED, texturaBosque.PRADERA, texturaBosque.MUSGO]
    },
}