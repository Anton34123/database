class Product:
    def __init__(self, name = "NoData", count = "0", price = "0", time = "NoData", par = "0"):
        self.name = name
        self.count = int(count)
        self.price = int(price)
        self.time = time
        self.par = int(par)

    def __str__(self):
        return f"{self.name}:{self.count}:{self.price}:{self.time}:{self.par}"





if __name__ == "__main__":
    base = []
    with open("goods2.info", encoding="utf-8") as faile_info:
        for f in faile_info:
            parse_prod = f.replace("\n", "").split(":")

            if len(parse_prod) == 5:
                name = parse_prod[0]
                count = parse_prod[1]
                price = parse_prod[2]
                time = parse_prod[3]
                par = parse_prod[4]

                product = Product(name, count, price, time, par)
                base.append(product)
            else:
                product = Product()
                base.append(product)

    for product in base:
        print(product)
