from os import system

class Persona:

    def __init__ (self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente (Persona):
    
    def __init__ (self,nombre, apellido,numero_cuenta, saldo = 0):
        super(). __init__ (nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__ (self):
        return(f"""\nNombre: {self.nombre}
Apellido: {self.apellido}
Numero de Cuenta: {self.numero_cuenta}
Saldo: ${self.saldo}""")

    def depositar (self, monto_depositar):
        self.saldo += monto_depositar
        print("Su depósito ha sido aceptado")

    def retirar (self, monto_retirar):
        if monto_retirar <= self.saldo:
            self.saldo -=monto_retirar
            print("Su retiro ha sido aceptado")
        else:
            print("Saldo insuficiente")

def crear_cliente():
    nombre= input("\nIngrese su nombre: ")
    apellido= input("Ingrese su apellido: ")
    numero_cuenta= int(input("Ingrese su número de cuenta: "))
    cliente = Cliente(nombre,apellido,numero_cuenta)
    return cliente

def inicio ():
    mi_cliente = crear_cliente()
    system("cls")

    mi_opcion = 0
    while mi_opcion != 3:
        print("""\n1- Depositar Efectivo
2- Retirar Efectivo
3- Salir\n    """)

        mi_opcion= int(input("Elige una opción: "))

        if mi_opcion == 1:
            system("cls")
            monto_depositado=int(input("Ingrese cuanto desea depositar en su cuenta: "))
            mi_cliente.depositar(monto_depositado)
        elif mi_opcion == 2:
            system("cls")
            monto_retirado=int(input("Ingrese cuanto desea retirar de su cuenta: "))
            mi_cliente.retirar(monto_retirado)
        else:
            print("El valor ingresado no es correcto")
        print(mi_cliente)
    system("cls")

    return(f"\nMuchas gracias por su operación")

print(inicio())

