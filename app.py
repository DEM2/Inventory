from archivos import guardar_csv
from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto,eliminar_producto

"""try:
   df=pd.read_csv('datos.csv')
   print("Datos Cargados")
except FileNotFoundError:
     df =pd.DataFrame(columns=['Producto', 'Precio', 'Cantidad'])
df.to_csv('datos.csv', index=False)

print(df)"""
inventario=[]

while True :

 print ("-"* 30)
 print ("      SISTEMA DE INVENTARIO")
 print ("-"* 30)

 print("1. Agregar")
 print("2. Mostrar")
 print("3. Buscar")
 print("4. Actualizar")
 print("5. Eliminar")
 print("6. Estadísticas")
 print("7. Guardar CSV")
 print("8. Cargar CSV")
 print("9. Salir")

 try:
     opcion = int(input("\n Ingresa la opcion del menu: "))
     if opcion in range(1,10):
        match opcion:
             case 1:
       
                nombre = input("\n Escriba el nombre del producto: ")
                try:

                   precio = float(input("\n Escriba el precio: "))
                   cantidad = float(input("\n Escriba la cantidad del producto: "))
                   if precio<0 or cantidad<0: 
                      print("\n La cantidad o el precio asignado debe ser un nummero valido")
                   else :
                      agregar_producto(inventario, nombre , precio, cantidad)

                except ValueError :
                 print("La informacion digitada es invalida ")
             case 2: 
              mostrar_inventario(inventario)
             case 3:
               try:
                  nombre= input("\n ¿Que producto deseas buscar?: ")
                  if buscar_producto(inventario, nombre) != None :
                      print("\n {producto}")
                  else:
                     print("\nNo se encontro informacion")
               except ValueError :
                 print("")
             case 4:
                  nombre= input("\n Ingresar el nombre del producto a actualizar: ")
                  nuevo_precio = input("\n Ingresar el precio nuevo: ")
                  nueva_cantidad = input("\n Ingresar la cantidad nueva del producto: ")
                  actualizar_producto(inventario, nuevo_precio, nueva_cantidad)
             case 5:
              nombre = input("\n Nombre del producto a eliminar: ")
              eliminar_producto(nombre)
             case 7: 
              guardar_csv(inventario)
             case 9:
              print("SECCION CERRADA")
              break

     else: 
        print("la opcion elegida no es valida")
     
 except ValueError :
    print("Valor invalido")

 