
# Task 1: Customer Service Ticket Tracker

######## Open a new service ticket#############

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(ticket_id, customer, issue, status="open"):
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": status}
    print(f"Ticket {ticket_id} added successfully.")


######## Update the status of an existing ticket#########

def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["status" ]= status
        print(f"Status of ticket {ticket_id} update to {status}.")
    else:
        print(f"Ticket {ticket_id} not found.")

########## Display all tickets or filter by status###########

def display_tickets(status=None):
    print("\nService Tickets:")
    for ticket_id, ticket_info in service_tickets.items():
        if status is None or ticket_info["Status"] == status:
            print(f"{ticket_id} - Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

add_ticket("Ticket003", "Bdada", "Need Access")

update_ticket_status("Ticket002", "Processing")

display_tickets()

display_tickets(status="open")