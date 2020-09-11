tv_shows = {
	"X-files": {
		"Season 1": {
			"Episodes": ["Scary Monster", "Scary Alien"],
			"Genre": "Sci Fi",
			"Year": 1993,
		},

		"Season 2": {
			"Episodes": ["Scary Conspiracy"],
			"Genre": "Horror",
			"Year": 1994, 
		}
	},
	"Lost": {
		"Season 1": {
			"Episodes": ["What the heck is happening on this island?"],
			"Genre": "Sci-Fi",
			"Year": 2004,
		}
	}
}

print(tv_shows["X-files"]["Season 1"]["Episodes"][1])
print(tv_shows["X-files"]["Season 2"]["Year"])
print(tv_shows["Lost"]["Season 1"]["Genre"])
print()

my_dict = {

  "a": {

    1: 2,

    3: 4,

    5: {

      6: 7,

      8: 9

    }

  }

}

mystery = {

  "a": 2

}



mystery.setdefault("A", 5)

mystery.setdefault("a", 10)

mystery.setdefault("B", 30)

mystery.setdefault("B", 40)

print(mystery)