#Program that allows the user to access two different financial calculators:
#an investment calculator and a home loan repayment calculator

import math


#First message for the user to see what is the calculator for: to calculate investment payout or bond monthly repayment 

print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment      - to calculate the amount of interest you'll earn on investment")
print("bond            - to calculate the amount you'll have to pay on a home loan \n")



#Asking input from the user to determine with which calculator to proceed
#.casefold function is used to make user's input case insensitive

inv_bond = input("Enter your choice: ")

inv_bond = inv_bond.casefold()



#if user types invalid input program shows error message and asking to enter choice again

if inv_bond != "investment" and inv_bond != "bond":

    print("\nError. Please make appropriate selection: ")

    inv_bond = input("\nEnter your choice: ")

    inv_bond = inv_bond.casefold()

  

#if investment is choisen for the calculator further questions are asked to gather information
#to execute calculations    
    

if inv_bond == "investment":

    deposit = int(input("\nWhat is the amount of money you would like to deposit?: R "))

    int_rate = float(input("\nWhat is the interest rate (as a percentage): "))

    years = int(input("\nWhat is the number of years you would like to invest for: "))

    interest = input("\nWould you like to calculate with simple or compound interest: ")


#calculations differs based on which interest is chosen simple or compound, different formulas
#are used. For simple interest: A =P*(1+r*t), for compound interest: A = P* math.pow((1+r),t)  


    if interest == "simple":

        amount = deposit * (1 + (int_rate / 100) * years)

        amount = round(amount, 2)

    
    else:

        amount = deposit * math.pow ((1 + (int_rate / 100)),years)

        amount = round(amount, 2)


#message containing outcome of the calculations is printed out for the user

    print("\nAfter {} years with {}% interest rate you will recieve R {}.".format(years, int_rate, amount))



#if bond calculator is chosen further questions are asked to gather information to
#execute calculations. Formula is used: x = (i.P)/(1 - (1+i)^(-n)) to calculate monthly repayments
#Message with outcome of the calculations is printed out for the user    


elif inv_bond == "bond":

    pr_value = int(input("\nWhat is the present value of the house?: "))

    int_rate = float(input("\nWhat is the interest rate (as a percentage)?: "))

    int_rate = (int_rate / 100) / 12

    months = int(input("\nWhat is the number of months you are planing to take to repay the bond?: "))

    amount = (int_rate * pr_value) / (1 - (1 + int_rate) ** -months)

    amount = round(amount, 2)

    print("\nMonthly repayment is R {}.".format(amount))
    




#******References******

#Python - How to make user input not case sensitive?. Retrieved 18 January 2021, from
#https://stackoverflow.com/questions/50192965/python-how-to-make-user-input-not-case-sensitive
