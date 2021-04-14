import datetime
import random
import validations


allowedUsers = {}
availableBalance = 9000000


print("Welcome to JavaScript Bank")


def initialization():
    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no): "))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        initialization()



def withdrawalOperation():
    withdrawal_successful = False
    global availableBalance

    while withdrawal_successful == False:
        print(f'Your current balance is: N{availableBalance}')
        amountWithdraw = input('How much would you like to withdraw: ')
        is_valid_amount = validations.validate_withdrawal(amountWithdraw)
        if is_valid_amount:
            if(int(is_valid_amount) < availableBalance):
                withdrawal_successful = True
                print(f'Take your cash N{int(is_valid_amount)}')
                availableBalance -= int(is_valid_amount)
                print(f'Your available balance is: N{availableBalance}')
                print('Thank you for banking with us')
            else:
                print(f'You can not withdraw more than N{availableBalance}, try again')
                withdrawalOperation()



def cashDepositOperation():
    global availableBalance
    cash_deposit_successful = False

    while cash_deposit_successful == False:
        print(f'Your current balance is: N{availableBalance}')
        deposit = input('How much would you like to deposit?: ')
        is_valid_amount = validations.validate_deposit(deposit)
        if is_valid_amount:
            cash_deposit_successful = True
            availableBalance += int(is_valid_amount)
            print(f'Your current balance is: N{availableBalance}')
            print('Thank you for banking with us')


def handleCompliat():
    complait_successful = False

    while complait_successful == False:
        complait = input("What issue will you like to report? \n")
        is_valid_complait = validations.validate_complait(complait)
        if is_valid_complait:
            complait_successful = True
            print("Thank you for contacting us")



def bankOperations():
    print('These are the available options')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Exit')

    selectedOption = int(input('Please select an option: '))
    isSelectOption = False
    while isSelectOption == False:        
        if(selectedOption == 1):
            isSelectOption = True
            withdrawalOperation()
        elif(selectedOption == 2):
            isSelectOption = True
            cashDepositOperation()
        elif(selectedOption == 3):
            isSelectOption = True
            handleCompliat()
        elif(selectedOption == 4):
            isSelectOption = True
            exit()
        else:
            print('Invalid Option selected, please try again')
            bankOperations()
    

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def register():
    print("Create your account")
    email = input("Enter your email address: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Create your password: ")

    accountNumber = generateAccountNumber()
    allowedUsers[accountNumber] = [first_name, last_name, email, password]
    print(f"Your account has been created. \nYour Account Number is:  {str(accountNumber)} \nkindly keep your account number safe." )
    login()




def login():
    print("*** Login ***")
    isLoginSuccessful = False
    
    while isLoginSuccessful == False:
        accountNumberFromUser = input("Enter your account number: ")
        is_valid_account_number = validations.account_number_validation(accountNumberFromUser)

        if is_valid_account_number:
            passwordFromUser = input("Enter your password: ")
            accountNumber = next(iter(allowedUsers))
            user = allowedUsers[accountNumber]
            if(accountNumber == int(accountNumberFromUser)):
                print("Account Number is Correct")
                if(user[3] == passwordFromUser):
                    isLoginSuccessful = True
                    loginTime = datetime.datetime.now()
                    print(f'Welcome {user[0]}')
                    print(f'Today: {loginTime.strftime("%a")}, {loginTime.strftime("%B")} {loginTime.strftime("%d")} {loginTime.strftime("%Y")} - {loginTime.strftime("%H")}:{loginTime.strftime("%M")}:{loginTime.strftime("%S")}')
                    bankOperations()
                else:
                    print("Invalid account or password")
            else:
                print("Invalid account or password")
                print("Account Number is Never Correct")
        else:
            initialization()

### ATM System ###
initialization()











