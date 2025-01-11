month = int(input("Enter a month (1-12): "))
if 1 <= month <= 12:
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    print(f"The month is: {months[month - 1]}")
else:
    print("Please enter a number between 1 and 12.")
