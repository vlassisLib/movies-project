# 1. SELECTING MOVIES 

# 1.1 having a list with movies : movies_list
# 1.2 showing him that list (movies_list), so he can choose a movie
# 1.3 choosing a movie 
# 1.3 checking if that movie belongs to the movies_list
# 1.4 the function: find_movie_index returns me the index of the movie
# 1.5 and if that movie doesnt belong to the list, tells you that its not in, and asks you again


# 1.1 having a list with movies : movies_list
# 1.2 showing him that list (movies_list), so he can choose a movie
# 1.3 checking if that movie belongs to the movies_list
# 1.4 the function: find_movie_index returns me the index of the movie
def find_movie_index(list_of_movies,movie_name):
    if movie_name in list_of_movies:
        return list_of_movies.index(movie_name)
    elif movie_name not in list_of_movies:
# 1.5 and if that movie doesnt belong to the list, tells you that its not in, and asks you again
        while True:
            print("The movie {} is not in the list".format(movie_name))
            movie_name = input("Select the movie you want to see: ")
            if movie_name in list_of_movies:
                return list_of_movies.index(movie_name)


            




