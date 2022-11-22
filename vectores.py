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
        return "El resultado del primer vector multiplicado por 6 es: {}".format(r)
    
    def divi(self,b):
        x = self.x / b
        y = self.y / b
        z = self.z / b
        r = (x,y,z)
        return "El resultado del primer vector dividido por 8 es: {}".format(r)
    
    def mostrar(self):
        print(vector1.suma(vector2))
        print(vector1.resta(vector2))
        print(vector1.multi(6))
        print(vector1.divi(8))
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

vector1 = Vector(5,1,4)
vector2 = Vector(4,5,2)

print(vector1.showvector())
print(vector2.showvector())
vector1.mostrar()
