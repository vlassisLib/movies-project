# # # room_sits = []
# # # for i in range(1,6):
# # #     for y in range(1,6):
# # #         if i == 1 :
# # #             room_sits.append("{}{}".format("A",y))
# # #         elif i == 2:
# # #             room_sits.append("{}{}".format("B",y))
# # #         elif i == 3:
# # #             room_sits.append("{}{}".format("C",y))
# # #         elif i == 4:
# # #             room_sits.append("{}{}".format("D",y))
# # #         elif i == 5:
# # #             room_sits.append("{}{}".format("E",y))
# # # upper_room_choice = input()


# # room_sits = {"A": ["A1","A2","A3","A4","A5"] ,
# #               "B":["B1","B2","B3","B4","B5"] ,
# #               "C":["C1","C2","C3","C4","C5"] ,
# #               "D":["D1","D2","D3","D4","D5"] ,
# #               "E":["E1","E2","E3","E4","E5"] }
# # sit_booked = ["A1"]
# # pick_a_room = input("pick your room ")
# # print(room_sits)
# # pick_a_sit = input("pick your sit ")


# # # print(pick_a_sit in room_sits[room_choice])
# # def check_sit(pick,sit_list,closed_sit,room):
# #     if pick in sit_list[room]:
# #         sit_booked.append(pick)
# #         print(room_sits)
# #     elif pick  in sit_booked:
# #         while pick in sit_booked:
# #             change_sit = input("That sit was booked, pick a different sit: ")
# #             if change_sit in sit_list[room]:
# #                 sit_booked.append(change_sit)
# #                 break
# #     return "Your sit is booked" 
# # print(check_sit(pick_a_sit,room_sits,sit_booked,pick_a_room))
# # print(sit_booked)

# option1 = input("If you want to eat somethin, type food. If you want to drink somethin, type drink. If you want a combined order, type option 2 ")
# upper_option1 = option1.upper()

# def option(pick):
#     if pick != "OPTION 2":

#         def food_order(pick):
#             if pick == "FOOD":
#                 print(food)
#                 food_choise = input("Choose your food: ")
#                 if food_choise in food_prices:
#                     print ("You ordered {} and the price is {}$".format(food_choise,food_prices[food_choise]))
#         food_order(upper_option1)

#         def drink_order(upper_option):
#             if upper_option == "DRINK":
#                 print(drink)
#                 drink_choise = input("Choose your drink: ")
#                 if drink_choise in drink_prices:
#                     print("You ordered {} and the price is {}$".format(drink_choise,drink_prices[drink_choise]))

#         drink_order(upper_option1)
#     elif upper_option1 == "OPTION 2":
#         print("If you choose any Burger and any Soda, your discount is 5$")
#         print("If you choose any Burger and any Water, your discount is 3$")
#         print("If you choose any Pop Corn and any Soda, your discount is 4$")
#         print("If you choose any Pop Corn and any Water, your discount is 2$")
#         combination_choice = input("Type your combination here, by typing your food and your dring! (E.g  Burger Soda) " )
#         upper_combination_choice = combination_choice.upper()
        
#         if upper_combination_choice == "BURGER SODA":
#             print(food["Burger"])
#             print(drink["Soda"])
#             food_selection = input("Choose your food here: ")
#             drink_selection = input("Choose your drink here: ")
#             if food_selection in food_prices:
#                 if drink_selection in drink_prices:
#                     print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-5)))
#         elif upper_combination_choice == "BURGER WATER":
#             print(food["Burger"])
#             print(drink["Water"])
#             food_selection = input("Choose your food here: ")
#             drink_selection = input("Choose your drink here: ")
#             if food_selection in food_prices:
#                 if drink_selection in drink_prices:
#                     print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-3)))
#         elif upper_combination_choice == "POP CORN SODA":
#             print(food["Pop-Corn"])
#             print(drink["Soda"])
#             food_selection = input("Choose your food here: ")
#             drink_selection = input("Choose your drink here: ")
#             if food_selection in food_prices:
#                 if drink_selection in drink_prices:
#                     print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-4)))
#         elif upper_combination_choice == "POP CORN WATER":
#             print(food["Pop-corn"])
#             print(drink["Water"])
#             food_selection = input("Choose your food here: ")
#             drink_selection = input("Choose your drink here: ")
#             if food_selection in food_prices:
#                 if drink_selection in drink_prices:
#                     print("Your order is {} and {} and the price is {}$".format(food_selection,drink_selection,((food_prices[food_selection]+drink_prices[drink_selection])-2)))



food_prices = {"Cheese Burger" : 10,
                "Chicken Burger" : 15,
                "Vegan Burger" : 8,
                "Simple Burger" : 5,
                "Simple Pop-corn" : 5,
                "Chocolate Pop-corn" : 8,
                "Syrup Pop-corn" : 8
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

drink_prices = {"Coca-Cola" : 3,
                "Pepsi-Cola" : 3,
                "No Sugar-Cola" : 3,
                "Simple Water" : 2,
                "Water with taste" : 3
                }


option1 = input("If you want to eat somethin, type food. If you want to drink somethin, type drink. If you want a combined order, type option 2 ")
upper_option1 = option1.upper()
import App3

def option(pick):
    if pick == "FOOD":
        App3.food_order(upper_option1,food,food_prices)
    elif pick == "DRINK":
        App3.drink_order(upper_option1,drink,drink_prices)
    elif pick == "OPTION 2":
        combination_choice = input("Type your combination here, by typing your food and your dring! (E.g  Burger Soda) " )
        upper_combination_choice = combination_choice.upper()
        App3.combination(upper_combination_choice,food,drink,food_prices,drink_prices)
option(upper_option1)
