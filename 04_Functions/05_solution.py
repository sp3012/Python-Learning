# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet (name = "User"):
    letter = ("Hello {}, Good Afternoon").format(name)
    return letter
    
print(greet("Shubham"))

# Ab humne isse ye seekha ki agar hum ek parameter dete h function ko to fir argument me dena jruri hota hai. Lekin hum parameter ko as a variable bhi treat kr sakte hai. isliye humne name = 'User' rakh lya. to agar humne argumnet me koi string di to fir name nam ka variable ab usko refer krega, or agar humne bina argument k function ko run kiya to user ko hi wo name refer krega or usi k according hmara result print hoga.