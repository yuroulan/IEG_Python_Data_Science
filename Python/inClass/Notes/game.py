import random

class Pokemon:
    def __init__(self, name, health, element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self):
        print("Pokemon move.")
    
    def doEat(self):
        print("Pokemon eat.")

    '''def doSleep(self):
        print("Pokemon can sleep.")
        pass'''

class Jigglypuff(Pokemon):
    def __init__(self, name, health, element, lungCapacity):
        super().__init__(name, health, element)
        self.lungCapacity = lungCapacity

    def doMove(self):  # Overriding
        super().doMove()
        print("Jigglypuff can float.")
    
    def __str__(self):
        return f"Name: {self.name}\n\
Health: {self.health}\n\
Element: {self.element}\n\
Lung Capacity: {self.lungCapacity}"

class Pikachu(Pokemon):
    def __init__(self, name, health, element, electricity):
        super().__init__(name, health, element)
        self.electricity = electricity

    def __str__(self):
        return f"Name: {self.name}\n\
Health: {self.health}\n\
Element: {self.element}\n\
Electricity: {self.electricity}"

'''class Weapon:
    def __init__(self):
        pass

class Thunderbolt(Weapon):
    def __init__(self):
        super().__init__()

class Fireball(Weapon):
    def __init__(self):
        super().__init__()'''

'''pokemon = Jigglypuff("J1", 75, "fairy", 92)
pokemon.doMove()    # -->> under Jigglypuff'''

class Game:
    def __init__(self):
        self.elements = ["thunder", "fire", "water", "ice", "ghost"]
        self.pokemon = {
            "Jigglypuff": [
                Jigglypuff(
                    f"J{i}",
                    random.randint(50, 100),
                    random.choice(self.elements),
                    random.randint(50, 200)
                ) for i in range(random.randint(5, 20))
            ],
            "Pikachu": [
                Pikachu(
                    f"P{i}",
                    random.randint(50, 100),
                    random.choice(self.elements),
                    random.randint(50, 200)
                ) for i in range(random.randint(5, 20))
            ]
        }
    
    def __str__(self):
        message = ""
        for pokemonName, pokemonList in self.pokemon.items():
            for pokemon in pokemonList:
                message += pokemon.__str__() + "\n" + ("-" * 20) + "\n"
        return message

game = Game()
print(game)
