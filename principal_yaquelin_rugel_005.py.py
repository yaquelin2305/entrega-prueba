from funciones_yaquelin_rugel_005 import *


BD=[
    {
        "nombre": "yaquelin",
        "apellido": "Perez",
        "correo": "yaquelin2405@gmail.com",
        "ID": 1,
        "compras": [{"fecha": "2024-07-01", "monto":5000}, {"fecha": "2024-07-03", "monto": 5000}]
    }
]









while True:



    menu()
    opcion = input("Ingrese la opción a ejecutar: ")

    

    if opcion=="1":
        registrar_cliente(BD)

    elif opcion=="2":
        listar_cliente_registrado(BD)

    elif opcion=="3":
        registrar_compra(BD)

    elif opcion=="4":
        listar_compra(BD)

    elif  opcion=="5":
        print("gracias por su registro y compra")
