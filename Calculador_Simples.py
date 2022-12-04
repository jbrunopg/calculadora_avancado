class Calculadora:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def somar(self):
        return self.a+self.b
    def subtrair(self):
        return self.a-self.b
    def multipiclicar(self):
        return self.a*self.b
    def dividir(self):
        return self.a/self.b

c = Calculadora(10,2)
print(c.somar())#12
print(c.subtrair())#8
print(c.multipiclicar())#20
print(c.dividir(:.f))#5