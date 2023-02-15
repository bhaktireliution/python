class Category:

    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products

    def show_details(self):
        print("-Name of category is:", self.name)
        print("-Code of category is:", self.code)
        print("-Number of products is:", self.no_of_products)

    @classmethod
    def category_count(cls):
        for x in product_list:
            for y in category_list:
                if (x.category == y.name):
                    y.no_of_products += 1

        for y in category_list:
            print(y.no_of_products, y.name, y.code)


class Product:

    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def show_products(self):
        print("-Name of product is:", self.name)
        print("-category of product is:", self.category)
        print("-Price of product is:", self.price)

    @classmethod
    def sort_low_to_high(cls):
        for i in range(len(product_list)):
            for j in range(i + 1, len(product_list)):
                if product_list[i].price > product_list[j].price:
                    product_list[i], product_list[j] = product_list[j], product_list[i]

        for i in product_list:
            i.show_products()

    @classmethod
    def sort_high_to_low(cls):
        for i in range(len(product_list)):
            for j in range(i + 1, len(product_list)):
                if product_list[i].price < product_list[j].price:
                    product_list[i], product_list[j] = product_list[j], product_list[i]

        for i in product_list:
            i.show_products()

    @classmethod
    def product_from_code(cls):
        val = int(input("Enter your value: "))

        for i in product_list:
            if (val == i.code):
                i.show_products()

ct1 = Category("soap", 101, 0)
ct2 = Category("shampoo", 102, 0)
ct3 = Category("conditioner", 103, 0)


print("****DIFFERENT CATEGORIES AND ITS PRODUCT'S INFORMATION......****")

p1 = Product('lux', 111, ct1.name, 115)
p2 = Product('dove', 112, ct1.name, 120)
p3 = Product('santoor', 113, ct1.name, 130)
p4 = Product('loreal', 114, ct2.name, 290)
p5 = Product('sunsilk', 115, ct2.name, 199)
p6 = Product('TRESmee', 116, ct2.name, 250)
p7 = Product('clinicplus', 117, ct2.name, 180)
p8 = Product('dove', 118, ct3.name, 150)
p9 = Product('loreal', 119, ct3.name, 195)
p10 = Product('sunsilk', 120, ct3.name, 185)

product_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
category_list = [ct1, ct2, ct3]

print("Category info with its number of products......")

Category.category_count()

print("Products based on low to high price.......")

Product.sort_low_to_high()


print("Products based on high to low price....")

Product.sort_high_to_low()


print("Product using its code......")

Product.product_from_code()







