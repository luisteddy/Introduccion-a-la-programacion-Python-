#LIBRERIAS  ##########################################################
import turtle
from random import randint
import random
from time import sleep
import Dibujos

#FUNCIONES INICIALIZADORAS ###########################################
window = turtle.Screen()
window.setup(width = 800, height= 400)
flecha = turtle.Turtle()
flecha.hideturtle()

#BIBLIOTECA DE FIGURAS                                   #############

#A IMPORTAR....       ###

# TABLERO                                                #############

#A IMPORTAR...        ###


### FUNCIONES DE APOYO #############################################

def menu():
  numelementos = 11
  x = lista_no_repetidos(numelementos, numelementos)
  return x
        
def lista_no_repetidos(num,o):
    lista = []
    for i in range (0,12):
        numero = randint(0,o)
        x = True
        while x:
            if valor_lista(lista, numero):
                numero = randint(0,o)
            else:
                lista.append(numero)
                x = False
    return lista
    
def valor_lista(lista,num):
    i = 0
    while i < len(lista):
        if lista[i] == num:
            return True
        i += 1
    return False

def Genera_newlist(lista,cantidad):
  x = 0
  i = 0
  j = 0
  lista2 = []
  while x < cantidad:
    if lista[i] == 0:  
      lista2.append(0)
    if lista[i] == 1:
      lista2.append(1)
    if lista[i] == 2:
      lista2.append(2)
    if lista[i] == 3:    
      lista2.append(3)
    if lista[i] == 4:
      lista2.append(4)
    if lista[i] == 5:
      lista2.append(5)
    if lista[i] == 6:
      lista2.append(6)
    if lista[i] == 7:    
      lista2.append(7)
    if lista[i] == 8:
      lista2.append(8)
    if lista[i] == 9:
      lista2.append(9)
    if lista[i] == 10:
      lista2.append(10)
    if lista[i] == 11:    
      lista2.append(11)
    i +=1
    j +=1
    x +=1
  lista2 = lista2 * 2
  random.shuffle(lista2, random.random) ### REORGANIZA LA LISTA NUEVA ###
  return lista2

### REFERENCIA DE LAS POSICIONES ###################################
'''
POSICIONES
NUMERO     X     Y
  1      -300   100
  2      -200   100
  3      -100   100
  4        0    100
  5       100   100
  6       200   100

  7      -300    0
  8      -200    0
  9      -100    0
  10       0     0
  11      100    0
  12      200    0

  13     -300  -100
  14     -200  -100
  15     -100  -100
  16       0   -100
  17      100  -100
  18      200  -100

  19     -300  -200
  20     -200  -200
  21     -100  -200
  22       0   -200
  23      100  -200
  24      200  -200

def esconder_p1(x , y):
  flecha.penup()
  flecha.goto(x - 1,y + 1)
  flecha.color('#ffffff')
  flecha.begin_fill()
  flecha.goto(x - 100, y + 1)
  flecha.goto(x - 100,y + 99)
  flecha.goto(x - 100,y + 99)
  flecha.goto(x - 1,y +1)
  flecha.end_fill()

def esconder_p2():
  flecha.penup()
  flecha.goto(-199,101)
  flecha.color('#ffffff')
  flecha.begin_fill()
  flecha.goto(-100,101)
  flecha.goto(-100,199)
  flecha.goto(-199,199)
  flecha.goto(-199,101)
  flecha.end_fill()


'''
posiciones = [[-300,100], #1
              [-200,100], #2
              [-100,100], #3
              [0,100],    #4
              [100,100],  #5
              [200,100],  #6

              [-300,0],   #7
              [-200,0],   #8
              [-100,0],   #9
              [0,0],      #10
              [100,0],    #11
              [200,0],    #12

              [-300,-100],#13
              [-200,-100],#14
              [-100,-100],#15
              [0,-100],   #16
              [100,-100], #17
              [200,-100], #18
              
              [-300,-200],#19
              [-200,-200],#20
              [-100,-200],#21
              [0,-200],   #22
              [100,-200], #23
              [200,-200]] #24


def show_hide_repeat(lista):
  print(lista)
  lista1 = []
  lista3 = []
  contador = 0
  while len(lista1) != len(lista):
    i = 0
    while i == 0: 
      pos1 = int(input("Ingrese posición 1: "))
      pos2 = int(input("Ingrese posición 2: "))
      if pos1 <= len(lista)-1 and pos1 >= 0 and pos2 <= len(lista)-1 and pos2 >= 0 :
        print()
        nuevo_dibujo(pos1,lista)
        nuevo_dibujo(pos2,lista)     
        i += 1   
      else:
        print("Debe ingresar numeros entre: 0 y ",len(lista)-1)
        i = 0
    if lista[pos1] == lista[pos2]:
      lista1.append(lista[pos1])
      lista1.append(lista[pos2])
      x = revisor(pos1, pos2, lista3)
      if x == False:
        lista1.remove(lista[pos2])
        lista1.remove(lista[pos1])
      # SUMAR PUNTOS Y DEJAR FICHAS DESTAPADAS
      contador += 2
    else:
      sleep(1)
      if pos1 in lista3:
        1
      else:
        esconder_p(posiciones[pos1][0], posiciones[pos1][1])
        numeros(pos1)
      if pos2 in lista3:
        1
      else:
        esconder_p(posiciones[pos2][0], posiciones[pos2][1])
        numeros(pos2)
      contador -= 3
  print("Puntaje total del juego: ",contador)

def esconder_p(x , y): #
  flecha.penup()
  flecha.goto(x + 1,y + 1)
  flecha.color('#ffffff')
  flecha.begin_fill()
  flecha.goto(x + 100, y + 1)
  flecha.goto(x + 100,y + 99)
  flecha.goto(x + 1,y + 99)
  flecha.goto(x + 1,y +1)
  flecha.end_fill()

def nuevo_dibujo(pos,lista2):
  flecha.color('#000000')
  if pos == 0:
    dibuja_en_base_a(0,lista2)
  if pos == 1:
    dibuja_en_base_a(1,lista2)
  if pos == 2:
    dibuja_en_base_a(2,lista2)
  if pos == 3:
    dibuja_en_base_a(3,lista2)
  if pos == 4:    
    dibuja_en_base_a(4,lista2)
  if pos == 5:
    dibuja_en_base_a(5,lista2)
  if pos == 6:
    dibuja_en_base_a(6,lista2)
  if pos == 7:    
    dibuja_en_base_a(7,lista2)
  if pos == 8:
    dibuja_en_base_a(8,lista2)
  if pos == 9:
    dibuja_en_base_a(9,lista2)
  if pos == 10:    
    dibuja_en_base_a(10,lista2)
  if pos == 11:
    dibuja_en_base_a(11,lista2)
  if pos == 12:
    dibuja_en_base_a(12,lista2)
  if pos == 13:
    dibuja_en_base_a(13,lista2)
  if pos == 14:
    dibuja_en_base_a(14,lista2)
  if pos == 15:
    dibuja_en_base_a(15,lista2)
  if pos == 16:    
    dibuja_en_base_a(16,lista2)
  if pos == 17:
    dibuja_en_base_a(17,lista2)
  if pos == 18:
    dibuja_en_base_a(18,lista2)
  if pos == 19:    
    dibuja_en_base_a(19,lista2)
  if pos == 20:
    dibuja_en_base_a(20,lista2)
  if pos == 21:
    dibuja_en_base_a(21,lista2)
  if pos == 22:    
    dibuja_en_base_a(22,lista2)
  if pos == 23:
    dibuja_en_base_a(23,lista2) 


def dibuja_en_base_a(x,lista2):
  if lista2[x] == 0:
    Dibujos.casa(posiciones[x][0], posiciones[x][1])  
  if lista2[x] == 1:
    Dibujos.bote(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 2:
    Dibujos.piramide(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 3:    
    Dibujos.poker(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 4:
    Dibujos.steve(posiciones[x][0], posiciones[x][1]) 
  if lista2[x] == 5:
    Dibujos.llave(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 6:
    Dibujos.cubo3d(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 7:    
    Dibujos.gatito(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 8:
    Dibujos.bola_abs(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 9:
    Dibujos.corona(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 10:
    Dibujos.espada(posiciones[x][0], posiciones[x][1])
  if lista2[x] == 11:    
    Dibujos.chile(posiciones[x][0], posiciones[x][1])


def numeros(num):
  if num <= 9:
    flecha.color("#000000")
    flecha.penup()
    flecha.goto(posiciones[num][0] + 48,posiciones[num][1] + 10)
    flecha.pendown()
    flecha.write(num, font=("Rockwell", 12, "normal"))
    flecha.penup()  
    return 1
  if num > 9:
    flecha.color("#000000")
    flecha.penup()    
    flecha.goto(posiciones[num][0] + 42,posiciones[num][1] + 10)
    flecha.pendown()
    flecha.write(num, font=("Rockwell", 12, "normal"))      
    flecha.penup()  
    return 1

def numeros1(lista):
  if lista == False:
    return False
  x = 0
  while x < len(lista): 
    if x <= 9:
      flecha.penup()   
      flecha.goto(posiciones[x][0] + 48,posiciones[x][1] + 10)
      flecha.pendown()  
      flecha.write(x, font=("Rockwell", 12, "normal"))
      flecha.penup()  
    if x > 9:
      flecha.penup()   
      flecha.goto(posiciones[x][0] + 42,posiciones[x][1] + 10)
      flecha.pendown()  
      flecha.write(x, font=("Rockwell", 12, "normal"))
      flecha.penup()  
    x += 1

def revisor(pos1, pos2, lista3):
  lista3.append(pos1)
  lista3.append(pos2)
  i = 2
  y = 0
  z = 1
  contador = 0
  while i < len(lista3):
    j = pos1
    k = pos2
    if j == lista3[y]:
      contador += 1
    if k == lista3[y]:
      contador += 1 
    y += 1
    z += 1
    i += 1
  if contador > 1:
    print("No puede ingresar una posicion ya descubierta")
    return False
  return True

def verificar_entrada(cantidad,lista):
  i = 0
  while i == 0:
    if cantidad > 12 or cantidad <= 1:
      print ("Cantidad fuera de rango")
      print()
      cantidad = int(input("Cantidad De Figuras: "))
    else:
      lista2 = Genera_newlist(lista,cantidad)
      numeros1(lista2)
      show_hide_repeat(lista2)
      i += 1

### PROGRAMA CENTRAL #################################################

print("El minimo de figuras es 2, el maximo es 12...")
lista = menu()
flecha.speed(0)
Dibujos.tablero()
cantidad = int(input("Cantidad De Figuras: "))
verificar_entrada(cantidad,lista)

