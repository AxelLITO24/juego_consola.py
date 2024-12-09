import random

class Jugador:
    def __init__(self,nombre):
        self.nombre=nombre
        self.salud=100
        self.nivel=1
        self.experiencia=0
    
    def atacar(self):
        return random.randint(10,20)* self.nivel
    
    def recibir_dano(self,dano):
        self.salud-=dano
        if (self.salud)<=0:
            print(f"{self.nombre} ha perdido ")
        else:
            print(f"te quedan{self.salud} puntos de salud ")
    
    def ganar_exp(self,exp):
        print(f"{self.nombre} gano {exp} puntos por experiencia")
        self.experiencia+= exp
        if self.experiencia>=100:
            self.nivel+=1
            self.experiencia=0
            print(f"{self.nombre} subio de nivel a {self.nivel} ")
    

