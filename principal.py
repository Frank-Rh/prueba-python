import os
#import socket
#import sys
import time
import colorama
from colorama import *

os.system("cls || clear") # limpiar consola
print(Fore.BLUE + "1 ver el estado de tu conexion") # imprimira en color azul
print("")
x = input("Selecciona la opcion 1-1") #selecionar opcion

if x == "1": #si la opcion es 1
    print(Fore.MAGENTA + "Porfavor espere....") # imprimira en la consola con color magenta
    print("")
    time.sleep(5) #en 5 segndos
    os.system("netstat -a") # status de tu red de sistema 

while True: 
    pass
