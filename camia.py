class Usuario():
	def __init__(self,correo,clave,nombre,apellido):
		self.correo=correo
		self.clave=clave
		self.nombre=nombre
		self.apellido=apellido
		
	def registrar(self):
		Camila= open('usuarios.txt','a')
		Camila.write(f'''
Correo: {self.correo}
Clave: {self.clave}
Nombre: {self.nombre}
Apellido: {self.apellido}
''')
		Camila.close()
		
def BuscarUusarios(correo):
	Camila= open('usuarios.txt','a')
	Camila.close()
	Camila= open('usuarios.txt','r')
	Jop=Camila.readlines()
	Camila.close()
	for Pop in Jop:
		if (Pop == 'Correo: '+correo+'\n'): 
			print('El Correo Ingresado Ya Existe:"ERROR"')
			return False

Exit1=False
Val=False
while Exit1== False:
	print('''Bienvenido al Menu de camila
1-Registrar Nuevo Usuario
2-Iniciar sesion
3-Salir''')
	opc1 =input('OPCION: ')
	if (opc1=="1"):
		print('Ingrese "Salir" para salir al menu')
		correo = input('Correo: ')
		if correo == 'salir' or BuscarUusarios(correo) == True:
			continue
		clave=input('clave :')
		nombre=input('nombre: ')	
		apellido=input('apellido: ')
		UsuarioCreado = Usuario(correo,clave,nombre,apellido)
		UsuarioCreado.registrar()
		print("Ha sido guardado el nuevo usuario")
	elif (opc1=="2"):
		Camila=open('usuarios.txt','r')	
		Pro=Camila.readlines()
		Camila.close()
		correo=input('Ingrese su Correo: ')
		if (correo=='admin'):
			clave=input('Ingrese la contraseña: ')
			if (clave=='admin'):
				Camila=open('usuarios.txt','r')
				print("Usuarios Registrados: ")
				print(Camila.read())
				Camila.close()
				continue
		for 	x in Pro:
			SesionI=False
			if (x == 'Correo: '+correo+'\n'):
				clave = input('Ingrese la contraseña: ')
				for x in Pro:
					if (x == 'Clave: '+clave+'\n'):
						salida = False
						SeccionI = True
				if SeccionI == True:
					print('Has iniciado sesion correctamente!')
					while salida==False:
						print('Calculadora')
						print('1-Sumar:')
						print('2-Restar:')
						print('3-Multiplicar:')
						print('4-Dividir:')				
						opc = input('Opcion: ')
						try:
							n1 = int(input('primer numero: '))
							n2 = int(input('segundo numero: '))
							Val = True
						except:
							print('No se puede ingresar letras, ni caracteres ')			
						if (opc == '1'):
							resultado = n1+n2
						elif (opc == '2'):
							resultado = num1-num2
						elif (opc== '3'):
							resultado = n1*n2
						elif (opc == '4'):
							try: 
								resultado = n1/n2
							except:
									print('Imposible dividir entre cero')
									Val = False
									continue
						else:
							print("Opcion invalida")	
						print('El resutlado de su operacion es: ',resultado)
						print('Desea cerrar sesion S/N')
						cerrar=input()	
						if  (cerrar=='s'):
							salida=True
							break
						elif  (cerrar=='n'):
							continue
	
	elif (opcion=='3'):
		break
	else:
		print("Esta opcion no exite"+"\n")
		print("Ingrese otra opcion")
				
