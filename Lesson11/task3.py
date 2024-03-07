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
            search = input("Введите наименование продукта")
            if search in self.products.keys():
                print(f'Продукт {search}: кол-во: {self.products[search]}')
            else:
                print(f'Такого продукта {search} -  нет')
            ans = input("Желаете продолжить? д/н ")

    def remove_products(self):
        pass

    def get_state(self):
        print(self.products)


obj = Shop()
obj.add_products()
obj.search_products()
obj.get_state()


