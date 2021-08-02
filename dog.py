class Dog:
    species = 'Canis Familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks {sound}"

class JackRussel(Dog):
        def speak(self, sound="Arf"):
            return super().speak(sound)
            ##return f"{self.name} says {sound}"

class Dashshound(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever:
        def speak(self, sound="Bark"):
            return super().speak(sound)

    
