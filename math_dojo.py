class MathDojo:
    def __init__(self):
        self.result = 0

    def adicion(self, num, *nums):
        self.result+=num
        for numero in nums:
            self.result+=numero
        return self
        
    
    def sustraccion(self, num, *nums):
        self.result-=num
        for numero in nums:
            self.result-=numero
        return self
md = MathDojo()
# para probar:
x = md.adicion(2).adicion(2,5,1).sustraccion(3,2).result
print(x)	# debería imprimir 5
# ejecuta cada uno de los métodos unas cuantas veces más y verifica el resultado

