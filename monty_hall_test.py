print("Hello dear user!\n\n During this quarantine time, while I was lying down in my couch and watching a bunch of Netflix shows, I have finally watched that movie called '21' which is about some cool MIT kids killin' their way out at Vegas.\n\n At the beginning, Kevin Spacey (who is the cool math tutor) asks class a question about a game which is a basic TV show where you can either win a Ferrari or a good ol' Goat!\n\n In the game, you are asked to pick a door out of three options: two of them containing a goat and one containing a brand new Ferrari behind.\n After you choose one of the doors, the host opens one of the doors which has a goat behind it and asks you to make a second decision: 'Would you want to hold on to your door or switch it with the other still closed one?'.\n\n Our protagonist, while playing with his cool pencil, stands and says 'I would change it, since it would increase my chances from 33.33..% to 66.66..%.'\n\n Which pretty much explains the entire point of this experiment. You go type the amount of shows you want to play, and this program would yield how well would you do by hanging on to or switching your door, in terms of winning a Ferrari for each show\n\nSooo Let's GO!\n")
import random
print("How many games would you like us to run for testing the hypothesis?\n")

iterations = int(input())
total_case = iterations
if_changed = if_yes = if_no = 0

while(0 < iterations):
    iterations -= 1
    answer = random.randint(1,3)
    initial_door = random.randint(1,3)
    cases = [1,2,3]
    dustbin = [1,2,3]

    if (initial_door == answer):
        dustbin.remove(answer)
        to_remove = dustbin[0]

    elif (initial_door != answer):
        dustbin.remove(answer)
        dustbin.remove(initial_door)
        to_remove = dustbin[0]

    cases.remove(to_remove)
    cases.remove(initial_door)
    if (cases[0] == answer):
        if_yes += 1
    else:
        if_no += 1
        
print(f"Out of {total_case} cases, {if_yes} of them resulted with a Ferrari for those who changed their doors and {if_no} of them resulted with a Goat.\n")
print(f"So we can say that {if_yes/total_case*100}% of the cases would result with a Ferrari if you change your door")
