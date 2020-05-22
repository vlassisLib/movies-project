import App1
# 1.1 having a list with movies : movies_list
# 1.2 showing him that list (movies_list), so he can choose a movie
movies_list = ["Iron Man","Batman","Spider Man","Black Panther","Cat Woman"]
print(movies_list)

# 1.3 checking if that movie belongs to the movies_list
# 1.4 the function: find_movie_index returns me the INDEX of the movie
# 1.5 and if that movie doesnt belong to the list, tells you that its not in, and asks you again
select_movie = input("Select your movie: ")
index_of_movie = App1.find_movie_index(movies_list,select_movie)

import App4

# 4.1 Showing the rooms 

dict_rooms = {"A" : 0 , "B" : 0 , "C" : 0, "D" : 0 , "E" : 0}
rooms = ["A" , "B" , "C" , "D" , "E"]
print(rooms)

# 4.2 Choosing a room
room_choice = input("Pick your room here: ")
upper_room_choice = room_choice.upper()

# 4.3 Checking if that room has available sits
# 4.4 If the room isn't available, choosing diff room
App4.check(dict_rooms,room_choice)


import App2

# 2.1 making a list with the sits and showing it to him/her
room_sits =  {"A": ["A1","A2","A3","A4","A5"] ,
              "B":["B1","B2","B3","B4","B5"] ,
              "C":["C1","C2","C3","C4","C5"] ,
              "D":["D1","D2","D3","D4","D5"] ,
              "E":["E1","E2","E3","E4","E5"] }

print(room_sits[room_choice])

# 2.2 telling him to pick a sit
pick_a_sit = input("Pick your sit: ")


# 2.3 checking if that sit is closed
# 2.4 if they are, asking them for another sit
# 2.5 appending the booked sits in a list : booked_sits
booked_sits = []
print(App2.check_sit(pick_a_sit,room_sits,booked_sits,room_choice))


# 2.6 incrising the key values of dict_rooms according to sit that he booked
letter = "{}".format(pick_a_sit[0])

if letter in dict_rooms:
    dict_rooms[letter] += 1

import App3
# 3.1 Showing him/her the list with the food, and the list with the drinks
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

# 3.2 Option 1 : Selecting only a type of food, or a drink 
# 3.3 Option 2 : Selecting a combination of food and drink
option1 = input("If you want to eat somethin, type food. If you want to drink somethin, type drink. If you want a combined order, type option 2 ")
upper_option1 = option1.upper()

# 3.4 If he choose Option 2 , he gets a discount
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

















