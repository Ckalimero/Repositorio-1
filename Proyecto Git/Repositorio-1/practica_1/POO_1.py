class Usuario():
    nombre="Nombre"
    edad=18
    login="Login"
    password="Password"
    email="Email@email.ccc"
    telefono=000000

    def resumen(self):
        print("Los datos del cliente son los siguienes: ")
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Login: ",self.login)
        print("Email: ",self.email)
        print("Teléono: ",self.telefono)

    def cambiaedad(self):
        edadIntroducida=int(input("Introduzca su edad entre 18 y 100: "))
        if 17<edadIntroducida<100:
            self.edad=edadIntroducida
            print("La edad es correcta")
            return ""
        else:
            print("La edad no es correcta")
            self.cambiaedad()
            return ""

    def muestraedad(self):
        print("La edad de",self.nombre, "es", self.edad, "años")
        print(f"La edad de {self.nombre} es {self.edad} años")

administrador=Usuario()
administrador.resumen()
print(administrador.cambiaedad())
print(administrador.muestraedad())