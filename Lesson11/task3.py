"""
3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов,
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
"""


class Shop:
    def __init__(self, products=None):
        if products is None:
            products = {}
        self.products = products

    def add_products(self):
        ans = ' '
        while ans != 'н':
            name = input("Введите наименование продукта ")
            cnt = float(input("Введите кол-во продуктов "))
            self.products[name] = cnt
            ans = input("Желаете продолжить? д/н ")

    def search_products(self):
        ans = ' '
        while ans != 'н':
            search = input("Введите наименование продукта для поиска ")
            if search in self.products.keys():
                print(f'Продукт {search}: кол-во: {self.products[search]}')
            else:
                print(f'Такого продукта {search} -  нет')
            ans = input("Желаете продолжить? д/н ")

    def remove_products(self):
        ans = ' '
        while ans != 'н':
            search = input("Введите наименование продукта для удаления ")
            if search in self.products.keys():
                del self.products[search]
                print(f'Продукт {search}удален')
            if self.products:
                ans = input("Желаете продолжить? д/н ")
            else:
                print(f'В магазине больше нет продуктов')
                break

    def get_state(self):
        if self.products:
            print(f'В наличии в магащине {self.products}')
        else:
            print(f'В магазине нет продуктов')


obj = Shop()
obj.add_products()
obj.search_products()
obj.remove_products()
obj.get_state()


