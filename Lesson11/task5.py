"""
1.	Создайте класс fraction. Данные класса должны быть представлены двумя полями:
числителем и знаменателем. Методы класса должны получать от пользователя значения числителя и знаменателя дроби и
выводить значение дроби в форме 3/5. Кроме того, должен быть разработан метод,
складывающий значения двух дробей и метод для сокращения дробей.
"""


class Fraction:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def output_fraction(self):
        self.numerator = int(input("Введите числитель "))
        self.denominator = int(input("Введите Знаменатель "))
        if self.denominator == 0:
            raise ZeroDivisionError("Ноль не может находиться в знаменателе дроби ")
        else:
            print(f'Дробь на выходе равна {self.numerator}/{self.denominator}')

    def sum_fraction(self):
        print("Введите первую дробь")
        self.numerator = int(input("Введите числитель "))
        self.denominator = int(input("Введите Знаменатель "))
        if self.denominator == 0:
            raise ZeroDivisionError("Ноль не может находиться в знаменателе дроби ")
        else:
            val1 = self.numerator / self.denominator

        print("Введите вторую дробь")
        self.numerator = int(input("Введите числитель "))
        self.denominator = int(input("Введите Знаменатель "))
        if self.denominator == 0:
            raise ZeroDivisionError("Ноль не может находиться в знаменателе дроби ")
        else:
            val2 = self.numerator / self.denominator
        print(f'Сумма дробей равна {val1 + val2}')

    def fraction_reduction(self):
        self.numerator = int(input("Введите числитель "))
        self.denominator = int(input("Введите Знаменатель "))
        if self.denominator == 0:
            raise ZeroDivisionError("Ноль не может находиться в знаменателе дроби ")
        else:
            if self.denominator % self.numerator == 0:
                numerator = self.numerator / self.numerator
                denominator = self.denominator / self.numerator
        print(f'Исходная дробь {self.numerator}/{self.denominator}')
        print(f'Дробь после сокращения {numerator}/{denominator}')


obj = Fraction(2, 2)
obj.output_fraction()
obj.sum_fraction()
obj.fraction_reduction()

