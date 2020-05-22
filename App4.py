# 4. SELECTING THE ROOM FOR THE MOVIE

# 4.1 Showing the rooms
# 4.2 Choosing a room
# 4.3 Checking if that room has available sits
# 4.4 If the room isn't available, choosing diff room





# 4.3 Checking if that room has available sits
# 4.4 If the room isn't available, choosing diff room

def check(dic,room):
    if dic[room] < 25:
        print("There is room for you!")
    while dic[room] == 25:
        print("Get a room! Another room! ")
        diff_room_choice = input("Did they just knocked you out? We are here! ")
        upper_dif_room_choice = diff_room_choice.upper()
        if dic[upper_dif_room_choice] < 25:
            print("There is room for you! Pick your sit ")
            break


