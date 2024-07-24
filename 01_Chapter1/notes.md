# python k ander hum varibale me data type ko store nahi krte hai, balki hum MEMORY me hi kisi data type ko store krte hai.
# fir us datatype ko hum kisi bhi varibale se refrence deke usko allocate ker sakte hai.

# hamesa suru me memories banti hai or fir uske baad kisi variable ka use reference dya jata hai. 

# immutable and mutable kafi important hai. 
# string, numbers, boolean, float, tuples. ye sab immutable hote hai. mtlb ek baar ye memory me create ho gae to fir inko nahi badal sakte hai.  

ex a = 5
a = 4
then yaha pe ab 4 ka refrence a ho gya or purane 5 ko koi refrence nahi mila to wo thori der k baad garbage collector me chala jaega. lekin hum yaha pe 5 wali memory k andr usko change nahi ker rahe hai balki ek nai 4 k naam se memory ban gai hai.

# ab agar hum mutable ki baat kare to list, dictionary, set, bytearray jo hai ye mutable hoti hai matlab ye change ho sakti hai. 

ex1
listOne = [1, 2, 3]
listTwo = [1, 2, 3]

listOne[0] = 22
output: listOne = [22, 2, 3]
but listTwo = [1, 2, 3]
# kuki listOne ko mutate kiya humne lekin listTwo ka mana refrence same tha but listTwo ko change nahi kiya balki wo same hai.

ex2 
listOne = [1, 2, 3]
listTwo = listOne

listOne[0] = 33
ooutput: listOne = [33, 2, 3]
listTwo = [33, 2, 3]
# kuki list ka refrence wahi same list thi koi alag se list banake usko refrence nahi dya tha. jaise ooper wale example me dya tha. to kuki list mutable hoti hai or ek hi list hai or usko humne change kr dya hai isliye dono ka output same hai.

# lekin agar hum listTwo = listOne.copy() 
is method se agar hum listTwo me listOne ki copy bnaenge to ab ek alag se copy ban gai h litsTwo ki. wo same hi list ko refrence nahi deta hai.

EX3 
listOne = [1, 2, 3]
listTwo = listOne
listTwo = [1, 2, 3]

listOne[0] = 33
output: listOne = [33, 2, 3]
listTwo = [1, 2, 3]
# ab kuki bhale hi humne starting me ek hi list ka refrence dya tha starting me but fir angli line me ek or new list create krke uska refrence dya listTwo ko. isliye listOne change hui na ki listTwo.

EX4
listOne = [1, 2, 3]
listTwo = listOne[ : ]

listOne[0] = 33
ooutput: listOne = [33, 2, 3]
listTwo = [1, 2, 3]
# aba yaha per humne listTwo ko slicing of listOne dya hai, matlab humne lisOne ka ek or copy bana dya hai. Hence listOne me change hhua na ki listTwo me kuki uske pass alag se same (copy) ka refrence hai.


setOne = {1, 2, 3, 4}
setOne - {1, 2, 3, 4}

Output: set()
# yaha per empty set me paranthesis milte hai naki braces {}. kuki empty braces dictinory ko denote karte hai. isliye ye paranthesis() milte hai.

# string k find method me agar hum jis cheez ko find kr rahe hai agar wo nahi milta hai to output  -1 aata hai.

# format method is used to add any variable in the string. String add karne ke liye pehle {} dene hote h string me or fir us string me kisi bhi variable ko agar add karna hai to format() method ka use krna hota hai.

# split method is used to split the content of string. or output  jo hai wo list(array) ki format me aaega.

# ab hume kisi list(array) ko string me convert krna hai to uske liye join method use kiya jata hai.

# ab maan lo hume /n ko string me likha or usko as output mme print bhi karwana hai. 
EX str = "Shubham/nKumar"
output: Shubham
kumar
Per hume to Shubham/nKumar ye output chahiye tha. (kabhi kabhi windows ka path dene k lye slash ka use aata h to waha use hota h). to uske lye hum starting me r (r ka matlab hai raw)use krte hai. like r"Shubham/nKumar"

# ********** LIST ************
 
List comprehension: We can also apply for loop in list. 
Ex. square_0f_num = [ x**2 for x in range(10)]
So here range is 10. so it will give numbers from (0, 10) means 0 to 9, 10 exclusive.
to ooper wala comprehensive jo h wo x ko lega 0 to 9 then it will perform its square and give list of squares from 0 to 9.

# *********** DICTIONARY **********

--- .pop(key) me hume kis key ko remove krna usko dena hota h.
--- .popitem() isme hume item nahi dena hota h, blki ye khudse last wale key value ko hata deta hai.

--- comprehensive dictionary bhi hum likh sakte hai. Like
--- square_num = { x:x**2 for x in range(5)}
yaha per hume key ko bhi dena hota hai kuki dictionary me list k jaise by default key nahi milti hume assign krni hoti hai.

# ********** TUPLES **********

Same as List, But tuples are immutable.