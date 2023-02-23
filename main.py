import random as r

class Bank():
    print("Welcome TO Fino Bank")
    print()
    def __init__(self,name,account_number,ifsc_code):
        self.name=name
        self.account_number =account_number
        self.ifsc_code = ifsc_code


    def show(self):
        print("Name: ",self.name)
        print("Account Number: ",self.account_number)
        print("Ifsc code: ",self.ifsc_code)


    def login(self,userid,password):
        userid = int(input("Userid: "))
        password = int(input("Password: "))
        if userid == 123 and password==456:
            print("Verification--> you will get an OTP ")
        else:
            print("Enter the Valid UerName And Password")

    def otp(self):
        otp=r.randrange(0,9999)
        print("Your One Time Password: ",otp)
        
        a=int(input("Enter the OTP : "))
        if a == otp:
             print("Verified --> Access Granted")
        else:
            print("Wrong OTP --> Please Check Your OTP once again")
           


   
class menu:
    def Moneytransfer(self):
        balance = 10000
        numbers = int(input('''
            1  8070244909
            2  9845621312
            3  5648945645
            4  5647992131
            5  9456321455
            6  9845621312
            8  5648945565
            9  5647992131
            10 9455632145
            '''))
        
        if numbers == 1:
            print("Confirm This Number you want send Money")
        
        elif numbers == 2:
            print("Confirm This Number you want send Money")
            
        elif numbers == 3:
            print("Confirm This Number you want send Money")
            
        elif numbers == 4:
            print("Confirm This Number you want send Money")
        elif numbers == 5:
            print("Confirm This Number you want send Money")
        elif numbers == 6:
            print("Confirm This Number you want send Money")    
        elif numbers == 7:
            print("Confirm This Number you want send Money")
        elif numbers == 8:
            print("Confirm This Number you want send Money")
        elif numbers == 9:
            print("Confirm This Number you want send Money")    
        elif numbers == 10:
            print("Confirm This Number you want send Money")
        else:
            print("Enter the Valid Number")
        
        amount = int(input("Enter amount : "))
        if amount > 0 and amount <= balance:
            new_bal = balance - amount
            print("Amount", amount, "successfully debited in your account")
        else:
            print("Not enough cash in your account ")
                
     
    
    def checkBalance(self):
        balance = 10000
        checkBalance=int(input("Enter The Pin : "))
        if checkBalance == 123456:
            print('you have Rs',balance,'In Your Bank Account')
        else:
            print("Enter the 6 Digit Correct Pin")
        
      
         
    


Details=Bank("Krishna Vishwakarma","56451 2652 2321 5654","UNION56")


Details.login(123,456)
Details.otp()
print()
Details.show()


while True:
    app =menu()
    print()
    print("MENU")
    User_Choice = int(input('''
    1 Moneytransfer
    2 checkBalance
    '''))
    if User_Choice ==1:
        app.Moneytransfer()
        
   
    
    elif User_Choice ==2:
        app.checkBalance()
        
        
    else:
        break 


