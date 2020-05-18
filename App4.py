# 4. SELECTING THE ROOM FOR THE MOVIE

# 4.1 Showing the rooms
# 4.2 Choosing a room
# 4.3 Checking if that room has available sits
# 4.4 If the room isn't available, choosing diff room


# 4.1 Showing the rooms 

dict_rooms = {"A" : 25 , "B" : 25 , "C" : 25 , "D" : 25 , "E" : 25}
rooms = ["A" , "B" , "C" , "D" , "E"]
print(rooms)

# 4.2 Choosing a room
room_choice = input("Pick your room here: ")
upper_room_choice = room_choice.upper()

# 4.3 Checking if that room has available sits
# 4.4 If the room isn't available, choosing diff room

def check(room):
    if dict_rooms[room] < 25:
        print("There is room for you! Pick  your sit ")
    elif dict_rooms[room] == 25:
        print("Get a room! Another room! ")
        diff_room_choice = input("Did they just knocked you out? We are here! ")
        upper_dif_room_choice = diff_room_choice.upper()
        check(upper_dif_room_choice)
check(upper_room_choice)

