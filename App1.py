# 1. SELECTING MOVIES 

# 1.1 having a list with movies : movies_list
# 1.2 showing him that list (movies_list), so he can choose a movie
# 1.3 choosing a movie 
# 1.3 checking if that movie belongs to the movies_list
# 1.4 the function: find_movie_index returns me the index of the movie
# 1.5 and if that movie doesnt belong to the list, tells you that its not in, and asks you again

movies_list = ["Batman" , "Superman" , "Avengers" , "Iron Man" , "Black Panther" , "Thor"]
print(movies_list)
select_movie = input("Select the movie you want to see: ")
def find_movie_index(list,movie_name):
    if select_movie in movies_list:
        return movies_list.index(select_movie)
    elif select_movie not in movies_list:
        return "The movie {} was not in the list!".format(movie_name)
print(find_movie_index(movies_list,select_movie))

while select_movie not in movies_list:
    select_movie = input("Select the movie you want to see: ")
    print(find_movie_index(movies_list,select_movie))
    if select_movie in movies_list:
        break
