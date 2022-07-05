import pathlib


class Product:
    """
    содержит 3 поля:
    name,
    count,
    price,
    """

    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

    def get_product(self):
        return self.name, str(self.count), str(self.price)


class Get_products:
    """
    Создаёт список товаров, востановленных из файла
    """

    def __init__(self, products_list_name):
        self.list_product = []
        products_list_path = pathlib.Path(products_list_name + ".txt")

        file_in_list = False
        for f in pathlib.Path(".").iterdir():
            if f == products_list_path:
                file_in_list = True
        if file_in_list:
            with open(products_list_name + ".txt", "r", encoding="utf-8") as pl:
                for line in pl.readlines():
                    self.list_product.append(Product(line.split("\t")[0],
                                                     int(line.split("\t")[1]),
                                                     float(line.split("\t")[2])))
        else:
            print(f"{products_list_name} файла нет")

    def get_list(self):
        """
        Выводит сисок товаров
        """
        print("Товар\tколичество\tстоимость")
        for line in self.list_product:
            print(f"{line.name}\t{line.count}\t{line.price}")

    def get_product(self, name: int):
        for product in self.list_product:
            if product.name == name:
                return product

    def get_average_cost(self):
        """
        Возвращает среднюю стоимость товаров
        """
        count = 0
        sum_price = 0
        for product in self.list_product:
            sum_price += product.price
            count += 1

        return sum_price / count

    def get_product_max(self):
        """
        Возвращает товар с максимальной ценой
        """
        product = self.list_product[0]
        for pr in self.list_product:
            if pr.price > product.price:
                product = pr
        return product

    def get_product_min(self):
        """
        Возвращает товар с минимальной ценой
        """
        product = self.list_product[0]
        for pr in self.list_product:
            if pr.price < product.price:
                product = pr
        return product

    def get_count_max(self):
        """
        Возвращает товар с максимальным количеством
        """
        product = self.list_product[0]
        for pr in self.list_product:
            if pr.count > product.count:
                product = pr
        return product

    def get_count_min(self):
        """
        Возвращает товар с минимальным количеством
        """
        product = self.list_product[0]
        for pr in self.list_product:
            if pr.count < product.count:
                product = pr
        return product
