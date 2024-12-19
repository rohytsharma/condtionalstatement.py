data_month = int(input("Enter the month number: "))
if data_month == 1 or data_month == 2 or data_month == 12:
    print("Winter")
elif data_month == 3 or data_month == 4 or data_month == 5:
    print("Spring")
elif data_month == 6 or data_month == 7 or data_month == 8:
    print("Summer")
elif data_month == 9 or data_month == 10 or data_month == 11:
    print("Autumn")
else:
    print("\nEnter valid month number")