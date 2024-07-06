
def saludo():
    print("hola cliente")




def menu():
    """ CREAMOS EL MENU """
    opciones = [
        "Registrar cliente",
        "Listar cliente registrados",
        "Registrar compra",
        "Listar compra",
        "Salir",
    ]

    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")



def registrar_cliente(bd):
    nombre = input("Ingrese primer nombre del cliente: ").upper()
    apellido = input("Ingrese primer apellido del cliente: ").upper()
    correo_electronico=input("ingrese su correo electronico: ")
    
    

    id_cliente = len(bd) + 1

    bd.append(
        {
            "nombre":nombre,
            "apellido": apellido,
            "correo electronico": correo_electronico,
            "ID": id_cliente,
            "compra": []
        }
    )



    print("\nSE HA AGREGADO UN CLIENTE NUEVO A LA BD!\n")

    

    








def listar_clientes(bd):
    print("\nLos clientes registrados son:\n")
    print("Nombre\t\t\tID\t\tSede")
    for cliente in bd:
        print(f'{cliente["nombre"]} {cliente["apellido"]}\t\t{cliente["ID"]}\t\t{cliente["sede"]}')

    print("\nListado creado con éxito!\n")




def registrar_compra(bd):
    id = int(input("Ingrese el ID del cliente que desea comprar: "))

    for cliente in bd:
        if cliente["ID"] == id:
            
            
            fecha = input("Ingrese fecha de compra (AAAA-MM-DD): ")
            total_compra=int(input("ingrese el total de su compra:"))

            cliente["compra"].append(
                {
                    "fecha": fecha,
                    
                    "total": total_compra
                }
            )
            print(f'\nSe ha agregado la compra a {cliente["nombre"]} {cliente["apellido"]}.')
            break
        else:
            print(f"El cliente de ID = {id} no existe.")




def listar_compra(bd):
        id = int(input("Ingrese el ID del cliente que compra: "))

        for cliente in bd:
            if cliente["ID"] == id:
                texto = f"ID Socio: {id}\n"
                texto += f'NOMBRE SOCIO: {cliente["nombre"]} {cliente["apellido"]}\n'
                texto += f"Fecha de compra\t\tcompra\n"

                

                


