film = input()
free_seats = int(input())
ticket = input()
seats = 0
all_ticket = 0
counter_ticket_stud = 0
counter_ticket_stand = 0
counter_ticket_kid = 0

while film != "Finish":
    while ticket != "End":
        if ticket == "student":
            seats += 1
            counter_ticket_stud += 1
            all_ticket += 1
        elif ticket == "standard":
            seats += 1
            counter_ticket_stand += 1
            all_ticket += 1
        elif ticket == "kid":
            seats += 1
            counter_ticket_kid += 1
            all_ticket += 1
        if seats == free_seats:
            break
        ticket = input()
    prc_hall = seats / free_seats * 100
    print(f"{film} - {prc_hall:.2f}% full.")
    seats = 0
    film = input()
    if film == "Finish":
        prc_stud = counter_ticket_stud / all_ticket * 100
        prc_stand = counter_ticket_stand / all_ticket * 100
        prc_kid = counter_ticket_kid / all_ticket * 100
        print(f"Total tickets: {all_ticket}")
        print(f"{prc_stud:.2f}% student tickets.")
        print(f"{prc_stand:.2f}% standard tickets.")
        print(f"{prc_kid:.2f}% kids tickets.")
    else:
        free_seats = int(input())
        ticket = input()