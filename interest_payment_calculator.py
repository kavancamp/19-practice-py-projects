#collect input principal, apr, years
#calculate monthly payment 
#print


def main():
  print("This is monthly payment loan calculator")
  print("")

  principal = float(input("input the loan amount: ")) 
  apr = float(input("Input the annual interest rate: "))
  years = int("Input amount of years: ")
  
  monthly_interest_rate = apr / 1200
  number_of_months = years * 12 

  monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))

  print("The monthly payment for this load is: " + str(monthly_payment))

main()
