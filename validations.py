def account_number_validation(accountNumber):
    # check if accountNumber is not empty
    # if the accountNumber is 10 digits
    # if the accountNumber is an integer
    if accountNumber:
        try:
            int(accountNumber)
            if len(str(accountNumber)) == 10:
                return True
            else:
                print("Account Number must be exactly 10 digits")
                return False
        except ValueError:
            print("Invalid Account number, account number should be an integer")
            return False
        except TypeError:
                print("Invalid account type")
                return False      
    else:
        print("Account number is a required field")
        return False




def validate_withdrawal(amountWithdraw):
	if amountWithdraw:
		try:
			int(amountWithdraw)
			return amountWithdraw
		except ValueError:
			print("Invalid Amount, Amount should be an integer")
			return False            
	else:
		print("Please specify the amount you want to withdraw")
		return False



def validate_deposit(amountDeposited):
	if amountDeposited:
		try:
			int(amountDeposited)
			return amountDeposited
		except ValueError:
			print("Invalid Amount, Amount should be an integer")
			return False
	else:
		print("Please specify the amount you want to deposit")
		return False



def validate_complait(issue):
	if issue:
		return issue
	else:
		return False