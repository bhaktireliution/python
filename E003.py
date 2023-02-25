class Product:

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = {}


    def show_products(self):
        print("Product:", self.name, "||", "Code:", self.code, "||", "Price:", self.price, "|", "stock_at_location:", self.stock_at_locations)

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
                    print("Product:", j.product.name, "||", "Code:", j.product.code, "||", "Price:", j.product.price, "||", "stock_at_location:", j.product.stock_at_locations)


class Movement:

    def __init__(self, from_location, to_location, product, quantity, stock):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.stock = stock
        self.stock_location()
        # product.total_stock.update({str(self.from_location.name): str(self.stock)})
        # product.stock_at_locations.update({str(self.from_location.name): str(self.stock)})
        product.stock_at_locations.update({str(self.to_location.name): str(self.quantity)})
        product.stock_at_locations.update({str(self.from_location.name):str(self.stock_location())})


    def show_movement(self):
        print(str(self.quantity) + " " + str(self.product.name) + " from " + str(self.from_location.name) + " to " + str(self.to_location.name))

    def stock_location(self):
        x = int(self.stock) - int(self.quantity)
        return x


    @staticmethod
    def movement_by_product(product):
        for j in movement_list:
            if product == j.product:
                return j.show_movement()


bag = Product("BAG", 10, 400)
shoe = Product("SHOE", 11, 600)
jeans = Product("JEANS", 12, 1000)
tshirt = Product("T-SHIRT", 13, 10000)
watch = Product("WATCH", 14, 14000)



rajkot = Location("Rajkot", 101)
vadodara = Location("Vadodara", 102)
ahmedabad = Location("Ahmedabad", 103)
surat = Location("Surat", 104)


m1 = Movement(rajkot, vadodara, bag, 15, 25)
m2 = Movement(vadodara, ahmedabad, watch, 10, 20)
m3 = Movement(ahmedabad, surat, jeans,20, 45)
m4 = Movement(surat, rajkot, shoe, 6, 60)
m5 = Movement(ahmedabad, rajkot, tshirt, 16, 30)


product_list = [bag, shoe, jeans, tshirt, watch]

location_list = [rajkot, vadodara, ahmedabad, surat]

movement_list = [m1, m2, m3, m4, m5]


print("*** Movements of product.....***")

Movement.movement_by_product(bag)


print(">>>")

print("*** Product details with its stock at location.....***")

Product.dictionary()


print(">>>")

print("*** Product list by location.....***")

Location.sort_name()



