class Vector:
    pass
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def showvector(self):
        return "Vector : ({}, {}, {})".format(self.x,self.y,self.z)
        
    def suma(self,b):
        sumarx =  self.x + b.x
        sumary =  self.y + b.y
        sumarz =  self.z + b.z
        r = (sumarx,sumary,sumarz)
        return "El resultado de la suma de ambos vectores es: {}".format(r)

    def resta(self,b):
        restarx = self.x - b.x
        restary = self.y - b.y
        restarz = self.z - b.z
        r = (restarx,restary,restarz)
        return "El resultado de la resta de ambos vectores es: {}".format(r)

    def multi(self,b):
        x = self.x * b
        y = self.y * b
        z = self.z * b
        r = (x,y,z)
        return "El resultado del primer vector multiplicado por {} es: {}".format(b,r)
    
    def divi(self,b):
        x = self.x / b
        y = self.y / b
        z = self.z / b
        r = (x,y,z)
        return "El resultado del primer vector dividido por {} es: {}".format(b,r)
    
    def mostrar(self):
        print(vector1.suma(vector2))
        print(vector1.resta(vector2))
        print(vector1.multi(g))
        print(vector1.divi(h))
        print(vector1.prod_punto(vector2))
        print(vector1.prod_cruz(vector2))

    def prod_punto(self,b):
        x = self.x * b.x
        y = self.y * b.y
        z = self.z * b.z
        r = (x+y+z)
        return "El producto punto entre ambos vectores es: {}".format(r)
    
    def prod_cruz(self,b):
        x = (self.y * b.z) - (self.z * b.y)
        y = (self.x * b.z) - (self.z * b.x)
        z = (self.x * b.y) - (self.y * b.x)
        r = (x,-y,z)
        return "El producto cruz entre ambos vectores es: {}".format(r)

i = int(input("Ingrese valor x del primer vector: "))
j = int(input("Ingrese valor y del primer vector: "))
k = int(input("Ingrese valor z del primer vector: "))

vector1 = Vector(i,j,k)

o = int(input("Ingrese valor x del segundo vector: "))
p = int(input("Ingrese valor y del segundo vector: "))
q = int(input("Ingrese valor z del segundo vector: "))

vector2 = Vector(o,p,q)

g = int(input("Ingrese número para multiplicar el primer vector: "))
h = int(input("Ingrese número para dividir el primer vector: "))
print(vector1.showvector())
print(vector2.showvector())
vector1.mostrar()
