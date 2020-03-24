global listaniño, listaadulto ,listadultom,listafallecido
listaniño =  list()
listaadulto = list()
listaadultom = list()
listafallecido = list()


class usuario:
    def __init__(self, nombre, apellido, id, fecha_nacimiento, edad, genero, pais_residencia,estado):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.genero = genero
        self.pais_residencia = pais_residencia
        self.estado = estado
        
      


    def registrar(self):
        print("nombre: ", self.nombre)
        print("apellido: ", self.apellido)
        print("id: ", self.id)
        print("fecha de nacimiento: ", self.fecha_nacimiento)
        print("edad: ", self.edad)
        print("genero: ", self.genero)
        print("pais de residencia",self.pais_residencia)
        print("estado: ", self.estado)
       
        
       


def menu():
    global option
    while True:
        print("\n--------*BIENVENIDO AL MENU CORONAVIRUS*-----------")
        print("")
        print("1.REGISTRAR")
        print("2. CAMBIAR ESTADO")
        print("3. CASOS REGISTRADOS")
        print("4.BUSCAR CASOS")
        print("5.PRUEBA PARA DETECTAR EL COVID-19")
        print("\n6. SALIR")
        try:
            option = int(input("ELIJA UNA DE LAS OPCIOINES MOSTRADAS  (1-5): "))

        except:
            print("")
            continue

        if option in range(1, 6):

            process(option)

        elif option == 6:
            break

        else:
            print("POR FAVOR,INGRESE UNA OPCION VALIDA")


def menu1():
    global option1
    print("\n*REGISTRAR EN EL SISTEMA*")
    print("\n1. NIÑOS")
    print("2. ADULTOS")
    print("3. ADULTOS MAYORES")
    print("4. FALLECIDO")
    print("\n5. VOLVER")

    try:
        option1 = int(input("POR FAVOR,INGRSE UNA OPCION PARA CONTINUAR(1-5): "))
    except:
        print(" POR FAVOR,INGRESE UNA OPCION VALIDAD")

    if option1 in range(1, 5):
        process1(option1)

    elif option1 == 5:
        menu()

    else:
        
        print("POR FAVOR,INGRSE UNA OPCION VALIDA ")

def buscarcaso():
    id = input("id: ")
    for a in listaniño:
        if a.id == id:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")

    for a in listaadulto:
        if a.id == id:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")
 
           
    for a in listaadultom:
        if a.id == id:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")


    menu()


def menu3():
    while True:
        print("*\nVER CASOS*")
        print("\n1. INFECTADOS ")
        print("2. NO INFECTADOS")
        print("3. FALLECIDOS")
        print("4. NIÑOS")
        print("5. ADULTOS")
        print("6.ADULTOS MAYORES ")
        print("\n7.VOLVER")
        try:
            option3 = int(input("POR FAVOR,INGRESE UNA OPCION  (1-7): "))
        except:
            print("POR FAVOR,INGRESE UNA OPCION VALIDA")
            continue

        if option3 in range(1, 7):
            process3(option3)

        elif option3 == 7:
            menu()

        else:

            print("POR FAVOR,INGRESE UNA OPCION VALIDA")


def agregarniños():
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("fecha de nacimiento: ")
    edad = int(input("edad: "))
    genero = input("genero: ")
    pais_residencia = input("pais de residencia: ")
    estado = input("estado? (infectado/no infectado): ")
    Nniño = usuario(nombre, apellido, id, fecha_nacimiento, edad, genero, pais_residencia, estado)
    listaniño.append(Nniño)
    menu()


def agregaradultos():
    
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("fecha de nacimiento: ")
    edad = int(input("edad: "))
    genero = input("genero: ")
    pais_residencia = input("pais de residencia: ")
    estado = input("estado? (infectado/no infectado): ")
    Nadulto = usuario(nombre, apellido, id, fecha_nacimiento, edad, genero, pais_residencia, estado)
    listaadulto.append(Nadulto)
    menu()


def agregaradultosm():
    
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("fecha de nacimiento: ")
    edad = int(input("edad: "))
    genero = input("genero: ")
    pais_residencia = input("pais de residencia: ")
    estado = input("estado? (infectado/no infectado): ")
    Nadultom = usuario(nombre, apellido, id, fecha_nacimiento, edad, genero, pais_residencia, estado)
    listaadultom.append(Nadultom)
    menu()


def agregarfallecidos():
    
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("fecha de nacimiento: ")
    edad = int(input("edad: "))
    genero = input("genero: ")
    pais_residencia = input("pais de residencia: ")
    estado = input("estado: muerto")
    Nfallecido = usuario(nombre, apellido, id, fecha_nacimiento, edad, genero, pais_residencia, estado)
    listafallecido.append(Nfallecido)
    menu()    


def registrarcasoniños():
    for niños in listaniño:
        niños.registrar()
    menu()

def registrarcasoadultos():
    for adultos in listaadulto:
        adultos.registrar()
    menu()


def registrarcasoadultosm():
    for adultosm in listaadultom:
        adultosm.registrar()
    menu()
    
def registrarcasofallecidos():
    for muertos in listafallecido:
        muertos.registrar()
    menu()



def registrarcasoinfectados():
    estado = "infectado"
    for a in listaniño:
        if a.estado == estado:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")
  

    for a in listaadulto:
        if a.estado == estado:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")
 

    for a in listaadultom:
        if a.estado == estado:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")
 

    menu()

def registrarcasonoinfectados():
    estado = "no infectado"
    for a in listaniño:
        if a.estado == estado:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")
  
    for a in listaadulto: 
        if a.estado == estado:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")
 


    for a in listaadultom:
        if a.estado == estado:
            print("\nnombre: ", a.nombre)
            print("apellido: ", a.apellido)
            print("id: ", a.id)
            print("fecha de nacimiento: ", a.fecha_nacimiento)
            print("edad: ", a.edad)
            print("genero: ", a.genero, "\n")

    menu()

    

def process(option):
    if option == 1:
        menu1()

    elif option == 2:
        pass

    elif option == 3:
        menu3()
        
    elif option == 4:
        buscarcaso()

    elif option == 5:
        pass
    
        


def process1(option1):
    if option1 == 1:
        agregarniños()

    elif option1 == 2:
        agregaradultos()

    elif option1 == 3:
        agregaradultosm()

    elif option1 == 4:
        agregarfallecidos()
 


def process3(option3):
    if option3 == 1:
        registrarcasoinfectados()

    elif option3 == 2:
        registrarcasonoinfectados()

    elif option3 == 3:
        registrarcasofallecidos() 

    elif option3 == 4:
        registrarcasoniños()

    elif option3 == 5:
        registrarcasoadultos()

    elif option3 == 6:
        registrarcasoadultosm()


menu()


