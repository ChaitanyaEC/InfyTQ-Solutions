#PF-Exer-11

def display(num):
    message=""
    #write your logic here
    if num%3==0 and num%5==0:
    	return "Zoom"
    elif num%5==0:
    	return "Zap"
    elif num%3==0:
    	return "Zip"
    else:
    	return "Invalid"
    return message

#Provide different values for num and test your program
message=display(9)
print(message)