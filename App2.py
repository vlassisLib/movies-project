# 2. SELECTING THEIR SIT


# 2.1 showing the sits 
# 2.2 choosing a sit
# 2.3 checking if the sit that they chose is booked
# 2.4 if they are, asking them for another sit
# 2.5 appending the booked sits in a list : booked_sits





# 2.3 checking if that sit is closed
# 2.4 if they are, asking them for another sit
# 2.5 appending the booked sits in a list : booked_sits
def check_sit(pick,sit_list,closed_sit,room):
    if pick in sit_list[room]:
        closed_sit.append(pick)
    elif pick  in closed_sit:
        while pick in closed_sit:
            change_sit = input("That sit was booked, pick a different sit: ")
            if change_sit in sit_list[room]:
                closed_sit.append(change_sit)
                break
    return "Your sit is booked"  

    




    
        









