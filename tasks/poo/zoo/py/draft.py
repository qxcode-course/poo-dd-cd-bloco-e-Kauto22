from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self._nome = nome

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def getNome(self):
        pass

class Leao(Animal):
    def __init__(self):
        super().__init__("Lion")

    def fazer_som(self):
        print("Roaaaaahhw")

    def mover(self):
        print("Andou 20 metros")

    def getNome(self):
        return self._nome

    def __str__(self):
        return "Leão"

class Elefante(Animal):
    def __init__(self):
        super().__init__("Elephant")

    def fazer_som(self):
        print("Barulho de Elefante")

    def mover(self):
        print("Andou 10 metros")

    def getNome(self):
        return self._nome
    
    def __str__(self):
        return "Elefante"

class Cobra(Animal):
    def __init__(self):
        super().__init__("Snake")

    def fazer_som(self):
        print("ssssssssssssssssssss")

    def mover(self):
        print("Rastejou 5 metros")

    def getNome(self):
        return self._nome
    
    def __str__(self):
        return "Cobra"

def main():
    animais = [Leao(), Elefante(), Cobra()]
    print(animais)
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            for animal in animais:
                print(animal)

        else:
            print("fail: comando invalido")
