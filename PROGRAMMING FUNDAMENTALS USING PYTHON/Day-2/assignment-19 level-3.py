#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
	if quantity_ordered >= 1 and distance_in_kms > 0:
	    bill_amount=0
	    delivery_charges = 0
	    distance_charges = [(3,0), (6,3), (7,6)]
	    #write your logic here
	    if food_type == 'V':
	    	cost_of_food = 120*quantity_ordered
	    elif food_type == 'N':
	    	cost_of_food = 150*quantity_ordered
	    else:
	    	return -1

	    distance_covered = 0
	    while distance_covered <= distance_in_kms:
	    	for distance in distance_charges:
	    		if distance_covered <= distance[0]:
	    			value = distance[1]
	    			break
	    	delivery_charges = delivery_charges + value
	    	distance_covered = distance_covered + 1

	    bill_amount = cost_of_food + delivery_charges
	    return bill_amount
	else:
		return -1

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",1,7)
print(bill_amount)