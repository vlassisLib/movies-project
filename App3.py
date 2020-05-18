# 3. SELECTIN THEIR FOOD/DRING

# 3.1 Showing him/her the list with the food, and the list with the drinks
# 3.2 Option 1 : Selecting only a type of food, or a drink 
# 3.3 Option 2 : Selecting a combination of food and drink
# 3.4 If he choose Option 2 , he gets a discount 

# 3.1 Showing him/her the list with the food , and the list with the drinks
food_prices = {"Cheese Burger" : 10,
                "Chicken Burger" : 15,
                "Vegan Burger" : 8,
                "Simple Burger" : 5,
                "Simple Pop-corn" : 5,
                "Chocolate Pop-corn" : 8,
                "Syrup Pop-corn" : 8
                }

drink_prices = {"Coca-Cola" : 3,
                "Pepsi-cola" : 3,
                "No Sugar-Cola" : 3,
                "Simple Water" : 2,
                "Water with taste" : 3
                }


food = {"Burger" :  "Cheese Burger 10$,"
                    " Chicken Burger 15$,"
                    " Vegan Burger 8$,"
                    " Simple Burger 5$",

        "Pop-corn": " Simple Pop-corn 5$,"
                    " Chocolate Pop-corn 8$,"
                    " Syrup Pop-corn 8$"
        }



drink = {"Soda" :   "Coca-Cola 3$," 
                    " Pepsi-Cola 3$,"
                    " No Sugar-Cola 3$",

        "Water" :   " Simple Water 2$,"
                    " Water with Taste 3$"
        }

# print("Option 1 : you can choose only food or only drink")
# print("Option 2 : you can choose a combination")
# print(food)
# print(drink)

# 3.2 Option 1 : Selecting only a type of food or a drink
# 3.2.1 Showing what he ordered and the sum of the price

option1 = input("If you want to eat somethin, type food. If you want to drink somethin, type drink. If you want a combined order, type option 2 ")
upper_option1 = option1.upper()

if upper_option1 != "OPTION 2":

    def food_order(upper_option):
        if upper_option == "FOOD":
            print(food)
            food_choise = input("Choose your food: ")
            if food_choise in food_prices:
                print ("You ordered {} and the price is {}$".format(food_choise,food_prices[food_choise]))
    food_order(upper_option1)

    def drink_order(upper_option):
        if upper_option == "DRINK":
            print(drink)
            drink_choise = input("Choose your drink: ")
            if drink_choise in drink_prices:
                print("You ordered {} and the price is {}$".format(drink_choise,drink_prices[drink_choise]))

    drink_order(upper_option1)
elif upper_option1 == "OPTION 2":
    print("If you choose any Burger and any Soda, your discount is 5$")
    print("If you choose any Burger and any Water, your discount is 3$")
    print("If you choose any Pop Corn and any Soda, your discount is 4$")
    print("If you choose any Pop Corn and any Water, your discount is 2$")
    combination_choice = input("Type your combination here, by typing your food and your dring! (E.g  Burger Soda) " )
    upper_combination_choice = combination_choice.upper()
    def option2(upper_combination_choice):
        if upper_combination_choice == "BURGER SODA":
            print(food["Burger"])
            print(drink["Soda"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            if food_selection in food_prices:
                if drink_selection in drink_prices:
                    print("Your order is {} and {} and the price is {}".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-5)))
        elif upper_combination_choice == "BURGER WATER":
            print(food["Burger"])
            print(drink["Water"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            if food_selection in food_prices:
                if drink_selection in drink_prices:
                    print("Your order is {} and {} and the price is {}".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-3)))
        elif upper_combination_choice == "POP CORN SODA":
            print(food["Pop-Corn"])
            print(drink["Soda"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            if food_selection in food_prices:
                if drink_selection in drink_prices:
                    print("Your order is {} and {} and the price is {}".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-4)))
        elif upper_combination_choice == "POP CORN WATER":
            print(food["Pop-corn"])
            print(drink["Water"])
            food_selection = input("Choose your food here: ")
            drink_selection = input("Choose your drink here: ")
            if food_selection in food_prices:
                if drink_selection in drink_prices:
                    print("Your order is {} and {} and the price is {}".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-2)))
option2(upper_combination_choice)







