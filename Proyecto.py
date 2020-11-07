import swowpy
from fun import funcion 
api_key ="e15c9bbb0449a7f39b8f848de5d01b6f"
Ciudades=[]
N=1
for i in range(N):
    Ciudades.append(swowpy.Swowpy(api_key,input("Escriba el nombre de una ciudad\n")))

for ciudad in Ciudades:
    print("El tiempo en "+ciudad.city+" es:")
    print(ciudad.current_weather("Description"))
    print("Con una temperatura de:",round(ciudad.temperature()-273.15,2),"ºC")
    print("Un",ciudad.humidity(),"% de humedad relativa")
    print("Una presión de",ciudad.pressure(),"mbar")
    print("Vientos con una velocidad de",ciudad.wind()[0]*3.6,"km/h y dirección de",ciudad.wind()[1],"grados")
    print(funcion(ciudad))
