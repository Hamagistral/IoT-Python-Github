class Animal: 
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age
        
    def vieillir(self):
        self.age = self.age + 1

    def get_type(self):
        return self.type 
    
    def set_type(self, valeur):
        self.type = valeur

    def get_name(self):
        return self.name 
    
    def set_name(self, valeur):
        self.name = valeur
        
    def get_age(self):
        return self.age
    
    def set_age(self, valeur):
        if type(valeur) == int:
            self.age = valeur
        else:
            print('Erreur! Veuillez entrer un nombre entier!')
        
        
koala = Animal("Koala", "Cooper", 2)
lion = Animal("Lion", "Snow", 6)

print(f"Dans le zoo, les deux animaux favoris par le public sont:\n 1. Le {koala.get_type()} nommé {koala.get_name()} qui {koala.get_age()} ans. \n 2. Le {lion.get_type()} nommé {lion.get_name()} qui {lion.get_age()} ans.\n")

lion.vieillir()

print(f"Quand le lion {lion.get_name()} aura {lion.get_age()} ans, il sera déplaçer à un autre Zoo.\n")

koala.set_name("Max")
koala.set_age(4)

print(f"Le Koala Cooper vient d'être remplacé par {koala.get_name()} qui a {koala.get_age()} ans.\n")

# Generation d'une erreur
lion.set_age(2.5)