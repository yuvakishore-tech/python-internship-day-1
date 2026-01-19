import datetime

name = input("Enter your name: ")
role = input("Enter your internship role: ")

today_date = datetime.date.today()

print("\n------ Internship Details ------")
print("Name:", name)
print("Role:", role)
print("Date:", today_date)
print("--------------------------------")
