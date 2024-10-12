class Animal:
    def __init__(self, name, age, diet):
        self.name = name
        self.age = age
        self.diet = diet
        self.hunger = 50
        self.energy = 50

    def make_sound(self):
        self.energy -= 5
        return f"{self.name} издает звук. Энергия: {self.energy}"

    def move(self):
        self.energy -= 25
        self.hunger += 25
        return f"{self.name} передвигается. Энергия: {self.energy}, Голод: {self.hunger}"

    def eat(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        return f"{self.name} поел(а). Голод: {self.hunger}"

    def sleep(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
        return f"{self.name} поспал(а). Энергия: {self.energy}"

    def info(self):
        return f"{self.name} ({self.age} лет) - {self.diet}. Голод: {self.hunger}, Энергия: {self.energy}"

    def is_alive(self):
        return self.hunger < 100 and self.energy > 0


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "плотоядное")

    def make_sound(self):
        self.energy -= 5
        return f"{self.name} издает рык: Ррррр! Энергия: {self.energy}"


class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "травоядное")

    def make_sound(self):
        self.energy -= 5
        return f"{self.name} трубит: Тууу! Энергия: {self.energy}"


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "всеядное")

    def make_sound(self):
        self.energy -= 5
        return f"{self.name} чирикает: Чик-чирик! Энергия: {self.energy}"


def game():
    lion = Lion("Биба", 5)
    elephant = Elephant("Боба", 10)
    bird = Bird("Сиба", 2)

    animals = [lion, elephant, bird]

    print("Добро пожаловать в зоопарк!")

    while any(animal.is_alive() for animal in animals):
        print("\nИнформация о животных:")
        for animal in animals:
            print(animal.info())

        print("\nВыберите животное:")
        for i, animal in enumerate(animals, 1):
            print(f"{i}. {animal.name}")

        choice = int(input("Введите номер животного: ")) - 1
        selected_animal = animals[choice]

        print("\nВыберите действие:")
        actions = ["1. Поесть", "2. Поспать", "3. Передвигаться", "4. Издать звук"]
        for action in actions:
            print(action)

        action_choice = int(input("Введите номер действия: "))

        if action_choice == 1:
            print(selected_animal.eat())
        elif action_choice == 2:
            print(selected_animal.sleep())
        elif action_choice == 3:
            print(selected_animal.move())
        elif action_choice == 4:
            print(selected_animal.make_sound())

        if not selected_animal.is_alive():
            print(f"{selected_animal.name} умер от усталости или голода... Игра окончена!")
            break

    print("Игра завершена!")


game()