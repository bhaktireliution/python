class Product:

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = {}
        

class Location:

    def __init__(self, name, code):
        self.name = name
        self.code = code


class Movement:

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    def show_movement(self):
        print(str(self.quantity) + " " + str(self.product.name) + " from " + str(self.from_location.name) + " to " + str(self.to_location.name))


    @staticmethod
    def movement_by_product(product):
        for j in movement_list:
            if product == j.product:
                return j.show_movement()




p1 = Product("BAG", 10, 400)
p2 = Product("SHOE", 11, 600)
p3 = Product("JEANS", 12, 1000)
p4 = Product("T-SHIRT", 13, 10000)
p5 = Product("WATCH", 14, 14000)


l1 = Location("Rajkot", 101)
l2 = Location("Vadodara", 102)
l3 = Location("Ahmedabad", 103)
l4 = Location("Surat", 104)


m1 = Movement(l1, l4, p1, 3)
m2 = Movement(l2, l1, p2, 2)
m3 = Movement(l1, l3, p3, 4)
m4 = Movement(l4, l2, p4, 5)
m5 = Movement(l3, l4, p5, 2)

product_list = [p1, p2, p3, p4, p5]

location_list = [l1, l2, l3, l4]

movement_list = [m1, m2, m3, m4, m5]

print("***Movements of product.....***")

Movement.movement_by_product(p5)








