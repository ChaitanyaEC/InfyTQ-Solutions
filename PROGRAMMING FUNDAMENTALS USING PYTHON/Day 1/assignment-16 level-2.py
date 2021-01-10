#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
	remaining_fives = no_of_five
	remaining_ones = no_of_one
	five_needed = 0
	one_needed = 0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
	five_needed = rupees_to_make // 5
	one_needed = rupees_to_make % 5

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
	if five_needed <= remaining_fives and one_needed <= remaining_ones:
		print("No. of Five needed :", five_needed)
		print("No. of One needed  :", one_needed)
	elif ((remaining_fives - five_needed)*5) <= (remaining_ones - one_needed):
		one_needed = one_needed + ((five_needed - remaining_fives)*5)
		five_needed = remaining_fives
		if five_needed <= remaining_fives and one_needed <= remaining_ones:
			print("No. of Five needed :", five_needed)
			print("No. of One needed  :", one_needed)
		else:
			print(-1)
	else:
		print(-1)

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,4,8)