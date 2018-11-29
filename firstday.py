start_year = eval(input("Enter the first year: "))
end_year = eval(input("Enter the second year: "))
for i in range(start_year, end_year + 1):
    year = i - 1
    day = ((1+5*(year%4)+4*(year%100)+6*(year%400))%7)
    if day == 0:
        day = "Sunday"
    elif day == 1:
        day = "Monday"
    elif day == 2:
        day = "Tuesday"
    elif day == 3:
        day = "Wednesday"
    elif day == 4:
        day = "Thursday"
    elif day == 5:
        day = "Friday"
    else:
        day = "Saturday"
    print("The 1st of January " + str(i) + " falls on a " + day + ".")