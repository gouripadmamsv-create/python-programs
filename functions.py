
'''def function_name(parameteres):

def greeting(user_name,age):
    print(f"Welcome  {user_name}You are {age}years old.")
user_name=input("Enter Name:")
age=int(input("Entegrer Age:"))
greeting(user_name,age)

def addition(num1,num2):
    return num1+num2
num1=int(input("Enter first numbers:"))
num2=int(input("Enter second number:"))
print(addition(num1,num2))


def Welcome():
    print("Welcome Gouri")
Welcome()

def book_ticket(movie_name,customer_name,seat,ticket_price):
    total=seat*ticket_price
    return (f"{customer_name} booked{seat} tickets for {movie_name}\n Total Amount:{total}")
print(book_ticket("gouri","malu",3,500))

print("\nkeyword arguements")
def customer_details(customer_name,age,city):
    print(f"Customer Name {customer_name}")
    print(f"Customer Age {age}:")  
    print(f"City {city}")
customer_details(age=20,city="thrissur",customer_name="gouri")
           
#default arguements
print("\ndefault arguements") 
def booking_status(customer_name,status="confirmed",screen="screen1"):
    print(f"{customer_name}'s booking status: {status}") 
    print(f"screen allocated : {screen}")
booking_status("gouri") 
booking_status("malu","pending")
booking_status("aishu","pending","screen3")

#multiple arguements
def calculate_bill(*ticket_prices):
    print(f"ticket prices: {ticket_prices}")
    print(f"total bill: {sum(ticket_prices)}")
calculate_bill(140,170,180,200)  

print('\nmultiple arguements')
def passenger_info(**details):
    print("customer informtion")
    for key,value in details.items():
        print(f"{key} : {value}")

passenger_info(
    customer_name="gouri",
    seats=2,
    destination="mumbai",
    payment_status="pending"
)  '''

#builtin function
print(len("gouri"))
print(sum([2,5]))
print(max([10,12,14,16]))
print(min([1,2,3,4]))
print(sorted([9,4,7,3,6]))
print(sorted([9,4,7,3,6],reverse=True))      
    










