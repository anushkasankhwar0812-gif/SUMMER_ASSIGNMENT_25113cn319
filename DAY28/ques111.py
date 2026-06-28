#write a program to create ticket booking system
total_seats = 10
booked_tickets = []

while True:
    print("\n===== Ticket Booking System =====")
    print("1. Book Ticket")
    print("2. View Available Seats")
    print("3. Cancel Ticket")
    print("4. Display Booked Tickets")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(booked_tickets) < total_seats:
            name = input("Enter passenger name: ")
            booked_tickets.append(name)
            print("Ticket booked successfully!")
        else:
            print("No seats available.")

    elif choice == 2:
        available = total_seats - len(booked_tickets)
        print("Available Seats:", available)

    elif choice == 3:
        name = input("Enter passenger name to cancel ticket: ")

        if name in booked_tickets:
            booked_tickets.remove(name)
            print("Ticket cancelled successfully.")
        else:
            print("Ticket not found.")

    elif choice == 4:
        if len(booked_tickets) == 0:
            print("No tickets booked.")
        else:
            print("\nBooked Tickets:")
            for i in range(len(booked_tickets)):
                print(i + 1, ".", booked_tickets[i])

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")