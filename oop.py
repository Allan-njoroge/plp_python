class Person:
    def __init__(self, name, age, gender):
        self.name = name;
        self.age = age;
        self.gender = gender

    def introduce(self):
        print(f"My name is {self.name}, I am a {self.age} year old {self.gender}")

first_person = Person("Kamau", 20, "female")
first_person.introduce()