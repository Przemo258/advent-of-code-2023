# FILE_PATH = "ex.txt"
FILE_PATH = "input.txt"

MAX_VALUE_RED = 12
MAX_VALUE_GREEN = 13
MAX_VALUE_BLUE = 14

p1_sum = 0
p2_sum = 0
game_idx = 0

with open(FILE_PATH, 'r') as f:
    for raw in f.readlines():
        game = raw.strip().split(':')[1].split(";")

        game_idx += 1
        is_game_valid = True
        min_red, min_green, min_blue = 0, 0, 0

        for draft_idx, draft in enumerate(game):
            red, green, blue = 0, 0, 0

            for dice_raw in draft.split(","):
                dice = dice_raw.strip()

                if "red" in dice:
                    red = int(dice.split(" ")[0])
                    if red > min_red:
                        min_red = red

                if "green" in dice:
                    green = int(dice.split(" ")[0])
                    if green > min_green:
                        min_green = green

                if "blue" in dice:
                    blue = int(dice.split(" ")[0])
                    if blue > min_blue:
                        min_blue = blue

            if red > MAX_VALUE_RED or green > MAX_VALUE_GREEN or blue > MAX_VALUE_BLUE:
                is_game_valid = False

        if is_game_valid:
            p1_sum += game_idx

        p2_sum += min_red * min_green * min_blue

print(f"Sum of all valid games ids is: {p1_sum}")
print(f"Sum of all power of sets is: {p2_sum}")

# p1: 2377
# p2: 71220
