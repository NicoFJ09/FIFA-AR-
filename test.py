
import serial

Rpi = serial.Serial(port = "COM8", baudrate=115200)
#Rpi.open()
try:
    Rpi.open()
    print("Conectado")
except:
    if (Rpi.isOpen):
        print("Conectado")
    else:
        print("No conectado")



while True :
    if (Rpi.isOpen()):

        READ=Rpi.readline() #Esto se recibe en bytes.
        TRANSLATED = READ.decode('UTF-8') #Conversión de Byte a String
        print(TRANSLATED)


