command = input()
counter_film = 0
the_best_score = 0
the_best_film = ""

while command != "STOP":
    counter_score = 0
    name = command
    counter_film += 1
    if counter_film == 7:
        print("The limit is reached.")
        break
    for ch in name:
        counter_score += ord(ch)
        if ch.islower():
            counter_score -= 2 * len(name)
        if ch.isupper():
            counter_score -= len(name)
    if counter_score > the_best_score:
        the_best_score = counter_score
        the_best_film = name
    command = input()
print(f"The best movie for you is {the_best_film} with {the_best_score} ASCII sum.")


