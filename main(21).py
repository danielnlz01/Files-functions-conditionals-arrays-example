ventas=[]
ventas_file=open("Ventas.txt","r")

while True:
  ventas_read=ventas_file.readline()
  if len(ventas_read)==0:
    break
  ventas_convertido=ventas_read.replace(" ","")
  ventas_convertido=ventas_read.replace("\n","")
  ventas_div=ventas_convertido.split(";")
  ventas.append(ventas_div)


def calcular_ventas_totales(ventas):
  suma=0
  for i in range(len(ventas)):
    venta=float(ventas[i][1])
    suma+=venta
  return suma


def calcular_utilidad(ventas):
  suma=0
  for i in range(len(ventas)):
    venta2=float(ventas[i][1])
    venta1=float(ventas[i][2])
    suma=suma+(venta2-venta1)
  return suma


def calcular_mas_caro(ventas):
  lista=[]
  for i in range(len(ventas)):
    lista.append(float(ventas[i][1]))
  for i in range(len(ventas)):
    if (int(ventas[i][1]))==(max(lista)):
      maxi=(ventas[i])
      return maxi


print(round(calcular_ventas_totales(ventas),2))
print(round(calcular_utilidad(ventas),2))
print(calcular_mas_caro(ventas))

##

