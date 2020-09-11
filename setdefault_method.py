# example 1
film_directors = {
    "The Godfather": "Francis Ford Coppela",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese",
}

print(film_directors.get("The Godfather"))
print(film_directors.get("Bad Santa", "Michael Bay"))
print(film_directors)
print()

# setdefault will create a key if it does not exist and assign it the value of the second parameter passed into it.
film_directors.setdefault("Bad Santa", "Michael Bay")
print(film_directors)

# if you use setdefault without a second parameter passed the value for the first parameter will be None.
film_directors.setdefault("Sad Soul")
print(film_directors)
