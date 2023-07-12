from guizero import App, PushButton, Text, Picture
import random
import Caballero as C
import Princesa as P

def Inicio():
    inicio = App(title = "ADVENTURE CASTLE")
    inicio.full_screen = True
    text = Text(inicio, text= "\n--------------------------------")
    text = Text(inicio, text= "        ADVENTURE CASTLE        ")
    text = Text(inicio, text= "--------------------------------\n")
    text = Text(inicio, text= "¡Bienvenidos a 'Adventure Castle' una aventura narrativa donde podrás escoger tus propias decisiones y disfrutar de esta increible aventura!")
    text = Text(inicio, text= "A continuación deberás empezar escogiendo tu personaje. Para elegir Elige una de estas dos opciones. ¡Buena suerte y que no te pase nada!\n")
    fondo = Picture(inicio, image= "imagenes/fondo.png")
    text = Text(inicio, text= " ")

    def Elegir_Personaje():
        elegir.destroy()
        aleatorio.destroy()

        def Masculino():
            C.HistoriaCaballero(inicio, 'Caballero')

        def Femenino():
            P.historia_princesa(inicio)

        masculino = PushButton(inicio, text= "Masculino", command= Masculino) 
        femenino = PushButton(inicio, text="Femenino", command=Femenino)

    def Personaje_Aleatorio():
        elegir.destroy()
        aleatorio.destroy()
        personaje1 = 'caballero'
        personaje2 = 'princesa'
        personaje = random.choice([personaje1, personaje2])

        if personaje == personaje1:
            C.HistoriaCaballero(inicio, personaje)
        else:
            P.Historia_Princesa(inicio, personaje)
       
    elegir = PushButton(inicio, text= "Elegir personaje", command= Elegir_Personaje)
    aleatorio = PushButton(inicio, text= "Personaje aleatorio", command= Personaje_Aleatorio)

    inicio.display()

Inicio()