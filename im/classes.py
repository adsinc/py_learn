# 3. Далее запускается метод класса Ферма "прошелМесяц".
# Там циклом проходим по всем животным, запуская их собственный метод "прошелМесяц"
# (какое животное сколько раз делает продукт, как успешно, где использовать random,
# какие случайные факторы внести в жизнь фермы, решайте сами).
#
# 4. Далее запускается метод класса Ферма "своднаяИнформация", который расскажет нам об изменениях на ферме


class Animal:
    def run(self):
        pass

    def voice(self):
        pass

    def product(self):
        pass

    def month_passed(self):
        pass


class Duck(Animal):
    def voice(self):
        print("Clack Clack")


class Cow(Animal):
    def voice(self):
        print("Mu")


class Dog(Animal):
    def voice(self):
        print("Woof woof")


class Farm:
    def __init__(self, duck_count, cow_count, dog_count):
        self.animals = [Duck() for _ in range(duck_count)]
        self.animals.extend([Cow() for _ in range(cow_count)])
        self.animals.extend([Dog() for _ in range(dog_count)])

    def month_passed(self):
        for animal in self.animals:
            animal.month_passed()


if __name__ == '__main__':
    farm = Farm(2, 3, 4)
    for animal in farm.animals:
        animal.voice()
