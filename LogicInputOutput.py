import pathlib
import Core

def file_in_list(products_list_name):
    result = False
    products_list_path = pathlib.Path(products_list_name + ".txt")
    for f in pathlib.Path(".").iterdir():
        if f == products_list_path:
            result = True
    return result

def new_product(products_list_name: str, product: Core.Product):
    """
    Добавляет product: Product в список products_list_name
    """

    products_list_path = pathlib.Path(products_list_name + ".txt")

    if not file_in_list(products_list_name):
        with open(products_list_path, "a", encoding="utf-8") as pl:
            pl.writelines(f"{product.get_product()[0]}\t{product.get_product()[1]}"
                          f"\t{product.get_product()[2]}\n")
        print(f"файл {products_list_name}.txt создан")
        print(f"{product.name} добавлен в список {products_list_name}")
    else:
        cash = False
        with open(products_list_path, "r", encoding="utf-8") as pl:
            for line in pl.readlines():
                if line.split("\t")[0] == product.name:
                    cash = True

        if cash:
            print("Такой товар уже есть в списке")
        else:
            with open(products_list_path, "a", encoding="utf-8") as pl:
                pl.writelines(f"{product.get_product()[0]}\t{product.get_product()[1]}"
                              f"\t{product.get_product()[2]}\n")
            print(f"{product.name} добавлен в список {products_list_name}")


def InOut():
    exit = ""
    while exit != "exit":
        file_name = input("Введте название файла чтобы зайти в него\nили создать: ")
        if not file_in_list(file_name):
            open(file_name + ".txt", "w")
        products_list = Core.Get_products(file_name)
        print(f"Вы в файле {file_name}: ")
        products_list.get_list()
        product = Core.Product(input("Чтобы создать товар введите его название: "),
                               input("количество: "),
                               input("и стоимость: "))
        new_product(file_name, product)
        exit = input("Введите exit для выходя из файла: ")
