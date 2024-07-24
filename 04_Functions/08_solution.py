
# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# ab humne multiple arguments dene to seekh lye lekin agar maan lo ki hume argument me key or value pair dene hai, lekin kitne dene hai wo define nahi hai. 

# Fir uske lye method hota hai, **kwargs
# isme hume andr for loop lgana hota h, lekin ye multiple key value k pair ko handle kr leta hai.

def superheros_powers (**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

superheros_powers( Name ="Ironman", Power = "Fighting")
superheros_powers( Name ="Superman")
superheros_powers( Name = "Spiderman", Power = "Fighting", place = "Hollywood")

# yaha per hum jo argument dere hai wo ek key or value ki form mr dere hai.