# Now on day 6 we get some hands on operators :
# 1. Membership operators : {in , not in }

user = input("Enter your name :")
if "a" in user :
    print("letter found")
elif "z" not in user :
    print("yes it is")
else :
    print("letter not found")

# 2. logical operators :

user = input("Please enter user name : ")
password = input("Please enter password : ")
if user == "Bhammo" and password == "Bhammo_2510" :
    print("login successful ")
else : 
    print("Please try again")

# 3. Shopping list :
 
shopping_list = ["rice", "flour", "salt", "sugar" , "gram flour", "saboo danna"]
user = input("Enter a item to check that is in the list or not : ")
if user in shopping_list :
    print("item is already in shoppong list ")
else :
    print("Added in the list")

# 4. identity checker : 

a = [1,2,3,4]
b = (a)
c = [1,2,3,4]

print(a is b) # check identity 
print(a is c) 
print(a == c) # check values 

# 5. Student eligibility criteria :

age = (18)
user_age = int(input("please enter your age : "))
if age == 18 and age == user_age :
    print("you are under in age criteria ")
marks = (50)
user_marks = int(input("please enter your marks :"))
if marks == 50 and marks == user_marks :
    print("your marks are eligible")
course = ["python" , "english learning ", "basic cs", "speak improvement"]
user_course = input("enter your intreasting course :")
if course == user_course :
    print("you course is in course list ")
else :
    print("not eligible")