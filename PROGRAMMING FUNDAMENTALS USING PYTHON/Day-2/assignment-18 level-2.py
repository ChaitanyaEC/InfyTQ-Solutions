#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    #write your logic here
    currency = {
    	'Euro': 0.01417,
    	'British Pound': 0.0100,
    	'Australian Dollar': 0.02140,
    	'Canadian Dollar': 0.02027
    }

    for Currency,Equivalent_amount in currency.items():
    	if Currency == current_currency_name:
    		current_currency_amount = amount_needed_inr * Equivalent_amount
    		return current_currency_amount

    return -1


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"British Pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")