# -*- coding: utf-8 -*-
"""triqui.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17muYXzlVmXae_UlYUk_uZ06UgG-35dX6
"""

#Variables globales
tablero = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
jugador = "X"

#Función para mostrar un menú
def menu():

  """
  Función que muestra unas opciones de menú
  """

  opc = -1

  while opc !=0:
    opc = int(input("Digite 1 para ingresar, 0 para salir"))

    if opc == 1:
      while True:
        mostrar_tablero()
        opc1 = input("Ingrese del 1 al 9 la pocisión que desea en el triqui")
        opc1 = int(opc1) - 1
        if movimiento(opc1):
            ganadors = ganador()
            if ganadors is not None:
                mostrar_tablero()
                print(imprimir_color("morado claro", "¡El ganador es " + ganadors + ", ""fin del juego!"))
                opc = 0
                break



# Función para mostrar tablero
def mostrar_tablero():
  """
  Función que muestra un tablero parecido al triqui
  """
  for i in range(3):
      print(" ".join(tablero[i * 3:(i + 1) * 3]))


#Función para validar moviento
def movimiento(opc1):
  """
  Función que valida el movimiento cambiando de jugador
  @param: opc1 (str)  Movimiento del usuario.
  """
  global tablero
  global jugador

  if tablero[opc1] == "-":
        tablero[opc1] = jugador
        jugador = "O" if jugador == "X" else "X"
        return True
  else:
      return False

def ganador():
  """
  Función que valida por fila, columna y diagonal el respectivo ganador
  """
  global tablero

  #Ganador por fila
  for i in range(3):
    if tablero[i * 3] == tablero[i * 3 + 1] == tablero[i * 3 + 2] != "-":
      return tablero[i * 3]

  #Ganador por columna

  for i in range(3):
    if tablero[i * 3] == tablero[i + 3] == tablero[i + 6] != "-":
      return tablero[i]

  #Ganador por diagonal

  if tablero[0] == tablero[4] == tablero[8] != "-":
    return tablero[0]

  else :
    if tablero[0] == tablero[3] == tablero[6] != "-":
      return tablero[0]
    else:
      if tablero[0] == tablero[1] == tablero[2] != "-":
        return tablero[0]


  if tablero[2] == tablero[4] == tablero[6] != "-":
   return tablero[2]

  else:
    if tablero[2] == tablero[5] == tablero[8] != "-":
      return tablero[2]



  if tablero[1] == tablero[4] == tablero[7] != "-":
    return tablero[1]

  if tablero[6] == tablero[7] == tablero[8] != "-":
    return tablero[6]



def imprimir_color(color, mensaje):
    """
    Función que imprime un mensaje del usuario en el color especificado.
    @param: color (str)    Color del texto ("rojo" o "verde").
    @param: mensaje (str)  Mensaje del usuario.
    """

    if color == "rojo":
        print("\x1b[1;31m" + mensaje)
    elif color == "verde":
        print("\x1b[1;32m" + mensaje)
    elif color == "morado claro":
        print("\x1b[1;35m" + mensaje)
    else:
        print("Color no válido. Utilizando color predeterminado.")
        print(mensaje)
    print("\x1b[0m")



menu()