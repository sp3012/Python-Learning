
# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
# encapsulation matlab apne aap me samet lena ya private kr dena. mtlb apne class k ander to available hai lekin bahar wali duniya isko access nahi kr sakti uske lye getter method ka use krna hoga.

# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.
# property decorator ki help se hum kisi bhi attribute ke over write krne wali property pr rok lga sakte hai.

# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
# check krna hai ki my_tesla jo h wo inheritence hai Car ka and ElectricCar ka.

# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Car:
    
    # ques 6 (to calculate total number of objects created from car)
    total_car = 0
    
    def __init__ (self, brand, model):
        self.brand = brand
        # self.__brand = brand  # kisi bhi attribute k aage do __ laga dete hai to wo private ho jata h. fir hum us attribute ko bahar wale object se . krke nahi bula sakte. uske lye alag se get method bnana hota hai. fir wo kewal get method se hi call kiya ja sakta hai. (for ques 4)
        # self.model = model
        self.__model = model
        Car.total_car += 1  #(total_car variable ko access krne k lye Car. use krna hoga.)
    
    
  
    # for ques 2  (is function ko internally link krne k lye self parameter me dena hoga)
    def full_name(self):
        return (f"{self.brand} {self.model}")
    
    # ques 4
    
    def get_brand(self):
        return self.__brand
    
    #ques 5
    def fuel_type(self):
        return ("Petrol or Diesel")
    
    # ques 7
    @staticmethod
    def general_description():
        return "Car is used for travelling"
    
    # @staticmethod use krne se hume parameter me self dene ki jrurrat nahi hai. Plus ab is method ko call krne k lye instance (object) ki bhi jrurat nahi hai, hum direct class k naam (Car) se bhi is method ko le sakte hai.
 
    # ques 8
    
    @property
    def model (self):
        return self.__model
    
    
# ques 3 solution
    
class ElectricCar (Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
        # ab yaha per (ques 3) humne ek new class bnai lekin wo apne inheritance ka access lena chahiye, yani Car class ka access. To isiliye humne ElectricCar ke parameter me Car ko pass kr dya. ab humne method bnaya __init__ method se. to pehle to self lya(jo ki main hai), then inheritance k model or brand jaise attributes ka bhi access hona chahiye to wo bhi le lya, then as per ques battery_size bhi le lya. Ab kuki battery_size new hai to self.battery_size = battery_size krna hoga waki puarne attributes ko hum super() method se call kr sakte h. to humne super se bola ki tum __init__ k brand or model me jao or unhe leke aao.
     
     #ques 5   
    def fuel_type(self):
        return "Electric Charge"
        




#for ques 1
# my_car = Car("Tata", "Nexon")
# print(my_car.brand)
# print(my_car.model)

# storing object in another storage.
my_new_car = Car("Hyundai", "i20")
# print(my_new_car.model)


# for ques 2
# print(my_car.full_name())

# (ques 2) ab kuki ye function Car class me hai, or Car class ko run krne pe object ko humne my_car me store kr rakkha hai, isliye is method ko run krne k lye my_car.fullname() krna hoga. or () isliye lgae kuki fullname ek function hai usko run krana hoga.



# for ques 3
my_tesla = ElectricCar("Tesla", "S class", "85kWH")
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())

# ab hum yaha per brand, model, battery_size ko access kr pa rahe h. Sath hi me humne fullNAme wala jo method define kiya tha usko bhi access kr pa rahe hai. kuki ElectricCar k paramter me humne Car ko dya tha jisse wo uske ander k sabhi methods ko acess kr pa raha hai. 



# for ques 4
# print(my_car.__brand)         # --> it will throw an error. Kuki private ko ese access nahi kr sakte hai.
# print(my_car.get_brand())

# ab ooper humne ques 4 ka output lya get method se. lekin agar hum print(my_car.brand) to nhi aaega.


# ques 5
my_car = Car("Suzuki", "Swift")
# print(my_car.fuel_type())

my_electric = ElectricCar("Tata", "Nexon EV", "80kWh")
# print(my_electric.fuel_type())

# ab ye dono function ek jaise hai lekin output alag alag dere hai. yahi polymorphism hai. Matlab jo anek roop dharan kar sake. jaise fuel_type ek jaisa hi function hai pr kaam alag alag kr raha hai.



# ques 6
# print(Car.total_car)

# ElecticCar wale object bhi Car class ko use krke ban rahe h isliye wo bhi count honge



# ques 7
# print(my_car.general_description())
# print(Car.general_description())


# ques 8

# print(my_car.model)   

# abhi car me swift hai, to kya hum model ki value ko over write kr sakte hai.
# my_car.model = "nano"

# print(my_car.model) 

# ab yaha per humne model ko over write kr dya hai. lekin hum chahte h ki usko over write na kiya jae. uske lye hum model ko __ se pvt kr denge, or baki jaha jaha model ko access kiya jara h waha bhi __ lgana hoga wrna waha pr value fir access nahi hogi, kuki hum over write se bachana h na ki uske access se.
# to ab over write se bachane k llye hume ek method bnana hoga, or us per @property method(decorator) lgana hoga.

# ab bhale se hi humne model ko function bnaya ho per ye method h, or is () call kiye execute krna hoga.



# ques 9

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(isinstance(my_car, ElectricCar))












# ************** SETTER **************

