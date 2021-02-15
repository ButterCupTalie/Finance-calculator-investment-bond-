# Finance-calculator-investment-bond-
Finance calculator to calculate the amount to be received from investment or amount to be repaid monthly on a bond

*Created in Python*

Program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
The user should is allowed to choose which calculation they want to do. The first output that the user sees when the program runs is a menu to choose an option of a calculator.
Capitalisation of the selection does not affect how the program proceeds. I.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc. all recognised as valid
entries. If the user doesn’t type in a valid input, appropriate error message is displayed.

If the user selects ‘investment’ user's input is required for:
1. The amount of money that they are depositing
2. The interest rate (as a percentage)
3. The number of years they plan on investing for
4. Whether they want “simple” or “compound” interest
Depending on whether they typed “simple” or “compound”, output is the amount that they will get after the given period at the interest rate. 
The total amount when simple interest is applied is calculated using formula: A = P*(1 + r * t).
The total amount when the compounded interest is applied is calculated using formula: A = P* math.pow((1+r),t).
The output is the result of the calculations which shows how much money the user will receive after the period of investment is over.

If the user selects ‘bond’, the user is asked to input:
1. The present value of the house
2. The interest rate
3. The number of months they plan to take to repay the bond
Bond repayment formula: repayment = x = (i.P)/(1 - (1+i)^(-n))

The output is the result of the calculations which shows how much money the user will have to repay each month.
