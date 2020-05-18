# 2. SELECTING THEIR SIT


# 2.1 showing the sits 
# 2.2 choosing a sit
# 2.3 checking if the sit that they chose is booked
# 2.4 if they are, asking them for another sit
# 2.5 appending the booked sits in a list : booked_sits

# 2.1 making a list with the sits and showing it to him/her
room_sits = []
for i in range(1,6):
    for y in range(1,6):
        if i == 1 :
            room_sits.append("{}{}".format("A",y))
        elif i == 2:
            room_sits.append("{}{}".format("B",y))
        elif i == 3:
            room_sits.append("{}{}".format("C",y))
        elif i == 4:
            room_sits.append("{}{}".format("D",y))
        elif i == 5:
            room_sits.append("{}{}".format("E",y))



# 2.2 telling him to pick a sit
pick_a_sit = input("Pick your sit: ")


# 2.3 checking if that sit is closed
# 2.4 if they are, asking them for another sit
# 2.5 appending the booked sits in a list : booked_sits
booked_sits = []
def check_sit(pick,list):
    if pick in list:
        booked_sits.append(pick)
        index_of_sit =pick.index(pick)
        room_sits.pop(index_of_sit)
    elif pick not in list:
        while pick not in list:
            change_sit = input("That sit was booked, pick a different sit: ")
            if change_sit in list:
                booked_sits.append(change_sit)
                index_of_sit = change_sit.index(change_sit)
                room_sits.pop(index_of_sit)
                break
    return "Your sit is booked" 
print(room_sits)
print(check_sit(pick_a_sit,room_sits))
print(booked_sits)

    




    
        









