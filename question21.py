salary_data = int(input("Enter your Salary:\n"))
credit_data= int(input("Enter your credit score: \n"))
if salary_data >= 50000 and credit_data >= 700:
    print("Eligible")
else:
    print("Not eligible")