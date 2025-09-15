TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(num_of_tickets):
    return (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue, {}. Please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("Your Total, {}, for {} tickets, is: {}".format(name, num_tickets, amount_due))
        should_proceed = input("Do you want to proceed?  Y/N. ")
        if should_proceed.lower() == "y":
            # TODO: Gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}".format(name))
else:
    print("Sorry, there are no more tickets available")
