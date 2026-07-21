years = int(input("enter number of years:"))

choice = input("""enter your choice:
1 - days
2 - weeks
3 - hours
""")

if choice == "1":
    print(years*365)
elif choice == "2":
    print(years*52)
elif choice == "3":
    print(years*365*24)
else:
    print("invalid choice")
