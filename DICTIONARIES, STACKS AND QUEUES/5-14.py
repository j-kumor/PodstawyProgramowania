import queue

# Function to simulate the customer service system
def customer_service():
    # Create a queue to hold the customers
    customer_queue = queue.Queue()

    # Variable to keep track of the next ticket number
    ticket_number = 1

    while True:
        # Display the menu to the user
        print("Customer Service Menu:")
        print("1. New customer arrives")
        print("2. Serve a customer")
        print("0. Exit")
        
        # Get the user's choice
        choice = input("Select an option: ")
        
        if choice == "1":
            # New customer arrives, assign a ticket number
            customer_name = input("Enter the customer's name: ")
            # Add the customer to the queue with their ticket number
            customer_queue.put((ticket_number, customer_name))
            print(f"Customer {customer_name} has received ticket number {ticket_number}.")
            ticket_number += 1  # Increment the ticket number for the next customer

        elif choice == "2":
            if customer_queue.empty():
                print("No customers in the queue.")
            else:
                # Serve the customer at the front of the queue
                ticket, name = customer_queue.get()
                print(f"Serving customer {name} with ticket number {ticket}.")
        
        elif choice == "0":
            print("Exiting the customer service system.")
            break
        
        else:
            print("Invalid option, please try again.")

# Run the customer service program
customer_service()
