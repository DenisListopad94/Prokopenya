"""
1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных,
и функцию которая находит наибольшее значение из этих двух переменных.
"""


class TestSumVariables:

    def __init__(self, var1=1, var2=2):
        self.var1 = var1
        self.var2 = var2

    def get_variables(self):
        print(f'Первая переменная var1 {self.var1}, Втоаря var2 {self.var2}')

    def set_variables(self, new_var1, new_var2):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_variables(self):
        print(f'Сумма переменных равна {self.var1 + self.var2}')

    def find_max(self):
        if self.var1 > self.var2:
            print(f'Пременная var1 больше чем var2 - {self.var1}')
        else:
            print(f'Пременная var2 больше чем var1 - {self.var2}')


obj = TestSumVariables(10, 11)
obj.get_variables()
obj.sum_variables()
obj.find_max()

