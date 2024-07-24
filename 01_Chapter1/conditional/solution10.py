# Pet food recomendation 
# recomend a type of food based on pet's species and age: (dog <2 years: puppy food, else adult food, cat <5 years junior cat food, else senior cat food)

pet_type = input("Enter either cat or dog: ")
pet_type_lower = pet_type.lower()
age = int(input("Enter age of your pet: "))

if (pet_type_lower != "cat") and (pet_type_lower != "dog"):
    print("This app is only for cat and dog")
    exit()

if pet_type_lower == "dog":
    if age < 2:
        print("Food for your pet is Puppy Food")
    else:
        print("Food for your pet is Adult dog Food")
        
if pet_type_lower == "cat":
    if age < 5:
        print("Food for your pet is Junior Cat Food")
    else:
        print("Food for your pet is Senior Cat Food")