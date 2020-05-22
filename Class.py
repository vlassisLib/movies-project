food_menu = ["Pizza","Burger","Tortilla"]
drink_menu = ["Coca-cola","Water"]
class Order:
    def __init__(self,menu):
        self.menu = menu
   
    def food_order(self):
        print(self.menu)
        food_selection = input("Select your food: ")
        if food_selection in self.menu:
            print("Your ordered {}".format(food_selection))
    
    def drink_order(self):
        print(self.menu)
        drink_selection = input("Select your drink: ")
        if drink_selection in self.menu:
            print("You ordered {}".format(drink_selection))


def order():
    food = Order(food_menu)
    food.food_order()
    drink = Order(drink_menu)
    drink.drink_order()

order()





