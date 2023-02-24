class Product:

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = {}


    def show_products(self):
        print("Product:", self.name, "||", "Code:", self.code, "||", "Price:", self.price, "||", "stock:", self.stock_at_locations)

    @classmethod
    def dictionary(cls):
        for i in product_list:
            i.show_products()


class Location:

    def __init__(self, name, code):
        self.name = name
        self.code = code

    @classmethod
    def sort_name(cls):
        for i in range(len(location_list)):
            for j in range(i + 1, len(location_list)):
                if location_list[i].name > location_list[j].name:
                    location_list[i], location_list[j] = location_list[j], location_list[i]

        for i in location_list:
            print("Location of product:", i.name)
            for j in movement_list:
                if i == j.from_location:
                    print("Product:", j.product.name, "||", "Code:", j.product.code, "||", "Price:", j.product.price, "||", "stock:", j.product.stock_at_locations)


class Movement:

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        product.stock_at_locations.update({self.from_location.name: self.quantity})


    def show_movement(self):
        print(str(self.quantity) + " " + str(self.product.name) + " from " + str(self.from_location.name) + " to " + str(self.to_location.name))


    @staticmethod
    def movement_by_product(product):
        for j in movement_list:
            if product == j.product:
                return j.show_movement()

stock_list = [20, 30, 45, 60]

p1 = Product("BAG", 10, 400)
p2 = Product("SHOE", 11, 600)
p3 = Product("JEANS", 12, 1000)
p4 = Product("T-SHIRT", 13, 10000)
p5 = Product("WATCH", 14, 14000)


l1 = Location("Rajkot", 101)
l2 = Location("Vadodara", 102)
l3 = Location("Ahmedabad", 103)
l4 = Location("Surat", 104)


m1 = Movement(l1, l4, p1, 15)
m2 = Movement(l2, l1, p2, 10)
m3 = Movement(l4, l3, p3, 20)
m4 = Movement(l3, l2, p4, 45)


product_list = [p1, p2, p3, p4, p5]

location_list = [l1, l2, l3, l4]

movement_list = [m1, m2, m3, m4]


print("*** Movements of product.....***")

Movement.movement_by_product(p1)


print(">>>")

print("*** Product details with its stock at location.....***")

Product.dictionary()


print(">>>")

print("*** Product list by location.....***")

Location.sort_name()

