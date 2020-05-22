# 3. SELECTIN THEIR FOOD/DRING

# 3.1 Showing him/her the list with the food, and the list with the drinks
# 3.2 Option 1 : Selecting only a type of food, or a drink 
# 3.3 Option 2 : Selecting a combination of food and drink
# 3.4 If he choose Option 2 , he gets a discount 

# 3.1 Showing him/her the list with the food , and the list with the drinks

# print("Option 1 : you can choose only food or only drink")
# print("Option 2 : you can choose a combination")
# print(food)
# print(drink)

# 3.2 Option 1 : Selecting only a type of food or a drink
# 3.2.1 Showing what he ordered and the sum of the price


# FUNTION FOOD ORDER ALONE
def food_order(option,food_menu,food_price):
            if option == "FOOD":
                print(food_menu)
                food_choise = input("Choose your food: ")
                while food_choise not in food_price:
                    print("{} is not in the food menu".format(food_choise))
                    food_choise = input("Choose your food: ")
                print("Your ordered {} and the price is {}$".format(food_choise,food_price[food_choise]))

# FUNCTION DRINK ORDER ALONE
def drink_order(option,drink_menu,drink_price):
            if option == "DRINK":
                print(drink_menu)
                drink_choise = input("Choose your drink: ")
                while drink_choise not in drink_price:
                    print("{} is not in the drink menu!")
                    drink_choise = input("Choose your drink: ")
                print("You ordered {} and the price is {}$".format(drink_choise,drink_price[drink_choise]))

# FUNTION COMBINATION
def combination(option,food_menu,drink_menu,food_price,drink_price):
    if option == "BURGER SODA":
            print("Burger and Soda, is a discount of 5$")
            print(food_menu["Burger"])
            print(drink_menu["Soda"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            while food_selection not in food_price:
                print("{} is not in the food menu".format(food_selection))
                food_selection = input("Choose your food here: ")
                drink_selection = input("Choose your drink here: ")
            while drink_selection not in drink_price:
                print("{} is not in the drink menu".format(drink_selection))
                food_selection = input("Choose your food here: ")
                drink_selection = input("Choose your drink here: ")
            print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_price[food_selection]+drink_price[drink_selection])-5)))
    elif option == "BURGER WATER":
            print("Burger and Water, is a discount of 3$")
            print(food_menu["Burger"])
            print(drink_menu["Water"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            while food_selection not in food_price:
                print("{} is not in the food menu".format(food_selection))
            while drink_selection not in drink_price:
                print("{} is not in the drink menu".format(drink_selection))
            print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_price[food_selection]+drink_price[drink_selection])-3)))
    elif option == "POP CORN SODA":
            print("Pop Corn and Soda, is a discount of 4$")
            print(food_menu["Pop-Corn"])
            print(drink_menu["Soda"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            while food_selection not in food_price:
                print("{} is not in the food menu".format(food_selection))
            while drink_selection not in drink_price:
                print("{} is not in the drink menu".format(drink_selection))
            print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_price[food_selection]+drink_price[drink_selection])-4)))
    elif option == "POP CORN WATER":
            print("Pop Corn and Water, is a discount of 2$")
            print(food_menu["Pop-corn"])
            print(drink_menu["Water"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            while food_selection not in food_price:
                print("{} is not in the food menu".format(food_selection))
            while drink_selection not in drink_price:
                print("{} is not in the drink prices".format(drink_selection))
            print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_price[food_selection]+drink_price[drink_selection])-2)))
               




        


