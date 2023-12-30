lines = open("input", "r").readlines()

all_games = {}
for line in lines:
    game_id = int(line.split(":")[0].split()[1])
    games = []
    for sub_game_raw in line.split(":")[1].split(";"):
        sub_game_raw = sub_game_raw.strip()
        sub_game = {}
        for values in sub_game_raw.split(","):
            if values.split()[1][0] == "b":
                sub_game["blue"] = int(values.split()[0])
            elif values.split()[1][0] == "g":
                sub_game["green"] = int(values.split()[0])
            elif values.split()[1][0] == "r":
                sub_game["red"] = int(values.split()[0])
        games.append(sub_game)
            
    all_games[game_id] = games

result = 0
for game_id, games in all_games.items():
    num_red = 1
    num_blue = 1
    num_green = 1
    for subset in games:
        if 'green' in subset and subset['green'] > num_green:
            num_green = subset['green']
        if 'blue' in subset and subset['blue'] > num_blue:
            num_blue = subset['blue']
        if 'red' in subset and subset['red'] > num_red:
            num_red = subset['red']
    result += (num_red * num_blue * num_green)
print(result)
