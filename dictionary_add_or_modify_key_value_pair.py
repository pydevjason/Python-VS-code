sports_team_roster = {
    "New England Patriots":["Tom Brady", "Rob Gronkowski", "Jean Edelmen"],
    "New York Giants":["Eli Manning", "Odell Beckham"]
}

sports_team_roster["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]
print(sports_team_roster)
print()
sports_team_roster["New York Giants"] = ["Eli Manning"]
print(sports_team_roster)

for k,v in sports_team_roster.items():
    print(f"{k} players are: {', '.join(v)}")
    
print()

video_game_settings = {}
video_game_settings["subtitles"] = True
video_game_settings["difficulty"] = "medium"
video_game_settings["volume"] = 7

print(video_game_settings)
print()

video_game_settings["difficulty"] = "hard"
video_game_settings["subtitles"] = False
print(video_game_settings)
print()

words = ["danger", "beware", "danger",]
def count_words(words):
    count = {}
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count

print(count_words(words))
        


