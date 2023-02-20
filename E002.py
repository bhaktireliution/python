class Category:

    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = []


    def show_category(self):
        print("name of category:", self.name)
        print("code of category:", self.code)
        print("no. of products:", self.no_of_products)
        print("products:", self.products)
        print("display name:", self.display_name)


    def generate_display_name(self):
        if self.parent is None:
            print(self.name)
        else:
            print(str(self.parent.generate_display_name()) + " > " + str(self.name))


    @classmethod
    def category_info(cls):
        for i in category_list:
            print("Name of category:", i.name)
            print("Code of category:", i.code)



    @classmethod
    def sort_name(cls):
        for i in range(len(category_list)):
            for j in range(i + 1, len(category_list)):
                if category_list[i].name > category_list[j].name:
                    category_list[i], category_list[j] = category_list[j], category_list[i]

        for i in category_list:
            print(i.show_category())



class Product:

    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        category.no_of_products = category.no_of_products + 1
        category.products.append(self)
        self.price = price




    def __repr__(self):
        return (self.name + " | " + str(self.code) + " | " + self.category.name + " | " + str(self.price))




# parent category
c1 = Category("vehicle", 101)

# child category
c2 = Category("car", 102, c1)
c3 = Category("bike", 103, c1)

# sub-child category
c4 = Category("diesel", 104, c2)
c5 = Category("petrol", 105,  c3)


p1 = Product("bus", 1001, c1, 500000)
p2 = Product("truck", 1002, c1, 600000)
p3 = Product("helicopter", 1003, c1, 4000000)
p4 = Product("SUV", 1004, c2, 1000000)
p5 = Product("swift", 1005, c2, 500000)
p6 = Product("endeavour", 1006, c2, 3300000)
p7 = Product("road bike", 1007, c3, 300000)
p8 = Product("mountain bike", 1008, c3, 400000)
p9 = Product("touring bike", 1009, c3, 500000)
p10 = Product("HP", 1010, c4, 200)
p11 = Product("Indian oil", 1011, c4, 250)
p12 = Product("Reliance", 1012, c4, 150)
p13 = Product("Hp", 1013, c5, 160)
p14 = Product("Indian oil", 1014, c5, 200)
p15 = Product("Reliance", 1015, c5, 180)

category_list = [c1, c2, c3, c4, c5]


Category.category_info()

print("***category information order by name with its products......***")

Category.sort_name()


