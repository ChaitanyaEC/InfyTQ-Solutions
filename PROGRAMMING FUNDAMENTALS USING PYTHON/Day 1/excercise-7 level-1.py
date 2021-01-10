#PF-Exer-7
rate_per_adult = 37550
rate_per_child = rate_per_adult / 3 

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    ticket_cost = (no_of_adults * rate_per_adult) + (no_of_children * rate_per_child)
    ticket_cost_with_service_tax = ticket_cost + (ticket_cost * 0.07)
    total_ticket_cost = ticket_cost_with_service_tax - (ticket_cost_with_service_tax * 0.1)
    
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)