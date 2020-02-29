class Nadador:
   def__Init__(self,nombre,apellido,especialidad,marca):
        self.nombre=nombre
        self.apellido=apellido
        self.especialidad=especialidad
        self.marca=marca


   #metodos 
   def getNombre(self):
   	   return self.nombre

   def getApellido(self):
   	   return self.apellido
   	   
   def getEspecialidad(self):
   	   return self.especialidad

   def getMarca(self):
   	   return self.marca


   def turnoentrenamiento(self):
       self.hora= int(input("ingrese hora de entrenamiento"))


       if self.hora < 12:
       	  print("el nadador pertenece al turno de la tarde")


       else:
       	  print("el nadador pertenece al turno de la mañana")
       	  pass


   def nivelNadador(self):
       self.nivel=int(input("ingrese nivel de natacion de nadador"))


      if self.nivel > 4:
          print("el nadador pertenece al rango federado")


      else:
          print("el nadador pertenece al rango no federado")
          pass




   def registroNadador(self):
   	   print(" \nNombre: "+self.getNombre()+"\nApellido: "+self.getApellido()+"\nEspecialidad: "+self.getEspecialiadad()+"\nMarca: "+str(self.getMarca()) )

nombre= raw_input("por favor,ingrese nombre del nadador")
apellido= raw_input("por favor,ingrese el apellido del nadador")
especialidad= raw_input("por favor,ingrese la especialidad del nadador")
marca= input("por favor ingrese la marca del nadador ")


n = Nadador(nombre,apellido,especialidad,marca)
n.registroNadador()
n.turnoentrenamiento()
n.nivelNadador()
