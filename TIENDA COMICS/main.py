import random

zonas=[
    [],
    [],
    [],
    []
]
maxProductosA = 50
maxProductosB= 50
maxProductosC = 50
maxProductosD = 50

print("Bienvenido a la tienda de comics")
opcion=100
opcionB=100

while(opcion!=6):
    
    print("1. Registrar producto")
    print("2. Buscar información de un Producto")
    print("3. Modificar un producto")
    print("4. Eliminar  un producto")
    print("5. Totalizar Inventario")
    print("6. SALIR")

    opcion=int(input("Ingrese una opción: "))

    if  (opcion==1):
            producto = {}
            while True:
                print(f"Zonas disponibles: A/B/C/D")
                print(f"1. Zona A, espacio de almacenamiento disponible= {maxProductosA}")
                print(f"2. Zona B, , espacio de almacenamiento disponible= {maxProductosB}")
                print(f"3. Zona C,, espacio de almacenamiento disponible= {maxProductosC}")
                print(f"4. Zona D, , espacio de almacenamiento disponible= {maxProductosD}")
                print(f"5. SALIR")
                zonaopcion= int(input("Ingrese la zona a la que pertenece el producto: "))
                if zonaopcion == 5:
                     break
                elif zonaopcion > 5:
                    print ("Opcion no valida, por favor ingrese nuevamente.")
                    
                    
                elif zonaopcion ==1:
                    bandera=True
                    id =random.randint(1,100)
                    nombre =input("Nombre del producto: ")
                    precio=int(input("Ingrese precio unitario: "))
                    ubicacion="1"
                    descripcion=input("Descripción del producto: ")
                    casa=input("¿De qué casa editorial es?: ")
                    referencia =input("Referencia del producto: ")
                    pais=input("País de origen: ")
                    unidades=int(input("Unidades a guardar: "))
                    print(unidades)
                    '''print(f"Almacenamiento disponible en zona A {maxProductosA}")
                    print(f"Almacenamiento disponible en zona B {maxProductosB}")
                    print(f"Almacenamiento disponible en zona C {maxProductosC}")
                    print(f"Almacenamiento disponible en zona D {maxProductosD}")'''
                    if(unidades<=maxProductosA):
                         bandera=True
                         #restar la cantidad de unidades a maxproductosa
                         maxProductosA=maxProductosA-unidades
                         garantia=bool(input("¿Tiene garantía? [S/N]: "))
                         producto["id"]=id
                         producto["nombre"]=nombre
                         producto["precio"]=precio
                         producto["ubicacion"]=ubicacion
                         producto["descripcion"]=descripcion
                         producto["casa"]=casa
                         producto["referencia"]=referencia
                         producto["pais"]=pais
                         producto["unidades"]=unidades
                         producto["garantia"]=garantia
                        #agregarndo elproducto a la zona respectiva
                         
                         zonas[0].append(producto)
                         
                    else:
                         bandera=False
                         print("no hay espacio")
                elif zonaopcion ==2:
                    id =random.randint(1,100)
                    nombre =input("Nombre del producto: ")
                    precio=int(input("Ingrese precio unitario: "))
                    ubicacion="2"
                    descripcion=input("Descripción del producto: ")
                    casa=input("¿De qué casa editorial es?: ")
                    referencia =input("Referencia del producto: ")
                    pais=input("País de origen: ")
                    unidades=int(input("Unidades a guardar: "))
                    if(unidades<=maxProductosB):
                         #restar la cantidad de unidades a maxproductosa
                         maxProductosB=maxProductosB-unidades
                         garantia=bool(input("¿Tiene garantía? [S/N]: "))
                         producto["id"]=id
                         producto["nombre"]=nombre
                         producto["precio"]=precio
                         producto["ubicacion"]=ubicacion
                         producto["descripcion"]=descripcion
                         producto["casa"]=casa
                         producto["referencia"]=referencia
                         producto["pais"]=pais
                         producto["unidades"]=unidades
                         producto["garantia"]=garantia
                        #agregando elproducto a la zona respectiva
                        
                         zonas[1].append(producto)
                         
                    else:
                         print("no hay espacio")         
                         
                elif zonaopcion ==3:
                    id =random.randint(1,100)
                    nombre =input("Nombre del producto: ")
                    precio=int(input("Ingrese precio unitario: "))
                    ubicacion="3"
                    descripcion=input("Descripción del producto: ")
                    casa=input("¿De qué casa editorial es?: ")
                    referencia =input("Referencia del producto: ")
                    pais=input("País de origen: ")
                    unidades=int(input("Unidades a guardar: "))
                    if(unidades<=maxProductosC):
                         #restar la cantidad de unidades a maxproductosa
                         maxProductosC=maxProductosC-unidades
                         garantia=bool(input("¿Tiene garantía? [S/N]: "))
                         producto["id"]=id
                         producto["nombre"]=nombre
                         producto["precio"]=precio
                         producto["ubicacion"]=ubicacion
                         producto["descripcion"]=descripcion
                         producto["casa"]=casa
                         producto["referencia"]=referencia
                         producto["pais"]=pais
                         producto["unidades"]=unidades
                         producto["garantia"]=garantia
                        #agregarndo elproducto a la zona respectiva
                        
                         zonas[2].append(producto)

                    else:
                         print("no hay espacio")    
                elif zonaopcion ==4:
                    id =random.randint(1,100)
                    nombre =input("Nombre del producto: ")
                    precio=int(input("Ingrese precio unitario: "))
                    ubicacion="4"
                    descripcion=input("Descripción del producto: ")
                    casa=input("¿De qué casa editorial es?: ")
                    referencia =input("Referencia del producto: ")
                    pais=input("País de origen: ")
                    unidades=int(input("Unidades a guardar: "))
                    if(unidades<=maxProductosD):
                         #restar la cantidad de unidades a maxproductosa
                         maxProductosD=maxProductosD-unidades
                         garantia=bool(input("¿Tiene garantía? [S/N]: "))
                         producto["id"]=id
                         producto["nombre"]=nombre
                         producto["precio"]=precio
                         producto["ubicacion"]=ubicacion
                         producto["descripcion"]=descripcion
                         producto["casa"]=casa
                         producto["referencia"]=referencia
                         producto["pais"]=pais
                         producto["unidades"]=unidades
                         producto["garantia"]=garantia
                        #agregando elproducto a la zona respectiva
                        
                         zonas[3].append(producto)

                    else:
                         print("no hay espacio")
                else:
                     break
    if opcion == 2:
        productoBuscar = input("Digita el nombre del producto que estas buscando: ")
        encontrado = False
        for zona in zonas:
            for productoB in zona:
                if productoB["nombre"] == productoBuscar:
                    print(f"id: {productoB['id']} ---- nombre: {productoB['nombre']} ---- precio: {productoB['precio']} ---- descripción: {productoB['descripcion']}")
                    encontrado = True
                break    
        if not encontrado:
            print("Producto no encontrado")

    if  (opcion==3):
        productoModificar = input("Digite el nombre del producto a modificar: ")
        encontradoM = False
        for zona in zonas:
            for productoM in zona:
                if productoM["nombre"] == productoModificar:
                    unidadesModificar = int(input("Digite la nueva cantidad de unidades: "))
                    productoM["unidades"] = unidadesModificar
                    encontradoM = True
                    print("Cantidad de unidades modificada exitosamente.")
                break
            if not encontradoM:
                print(f"Artículo {productoModificar} no encontrado.")
    if  (opcion==4):
            eliminarArticulo = input("Digita el nombre del articulo que deseas eliminar: ")
            articuloEliminado = False  
            for zona in zonas:
                for eliminarArt in zona:
                    if  eliminarArt ["nombre"] == eliminarArticulo:
                        zona.remove(eliminarArt)
                        print(f"Producto {eliminarArticulo} eliminado correctamente.")
                        articuloEliminado = True
                    break  
                if not articuloEliminado:
                    print(f"Articulo {eliminarArticulo} no encontrado.")
    if  (opcion==5):
             inventario=0
             for zona in zonas:
                for contarZona in zona:
                    inventario +=contarZona["unidades"]
             print(f"El total de unidades en bodega es: {inventario}") 
    if  (opcion==6):
         print("Saliendo del programa, SUERTE ES QUE LE DIGO...")
         break

