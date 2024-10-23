# Transaction Exercise

bill = float(input('Please pay your bill: '))
discount = bill*0.1
if bill >= 50: 
    discount = bill*0.1
    final_bill = bill - discount  
    print(f'You are eligible for a 10% discount! Your final bill is: £{final_bill}.')
else: print(f'Transaction complete! Your final bill is : £{bill}.')

# Age Verification Exercise

age = int(input('Please enter your age:'))
if age > 65: print('Your ticket price is £6')
elif age > 18 and age < 64: print('Your ticket price is £10')
elif age > 13 and age < 17: print ('Your ticket price is £7')
elif age > 0 and age < 12: print ('Yout ticket price is £5')

# Bank Withdrawal Exercise

bal = int(input('Input your balance'))
wd = int(input('Input how much you want to withdraw'))
remaining = bal - wd
if wd <= bal:
    print(f'You have withdrawn {wd}.')
    if remaining > 1000:
        print('You are now a VIP')
    if remaining < 100:
        print('You have a low-balance')
else: print('You must have more balance than withdrawal.')