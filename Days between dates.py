#(c) Alexander Peat, 2025
#All rights reserved

year1 = 0
year2 = 0
month1 = ""
no_month1 = 0
month2 = ""
no_month2 = 0
day1 = 0
day2 = 0

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

lowest_year = 0
lowest_month = ""
lowest_month_number = 0
lowest_day = 0

highest_year = 0
highest_month = ""
highest_month_number = 0
highest_day = 0

day_counter = 0
is_leap_year = ""

leapy_ness = ""

def is_light_year(year):
    if year % 100 == 0 and year % 400 == 0:
        #print("That year is a leap year")
        return "Y"
    
    elif year % 100 == 0:
        #print("That year is not a leap year")
        return "N"
    
    elif year % 4 == 0:
        #print("That year is a leap year")
        return "Y"
    
    elif year % 4 != 0:
        #print("That year is not a leap year")
        return "N"

def month_number_getter(mo):
    if mo == "January":
        return int(1)
    if mo == "February":
        return int(2)
    if mo == "March":
        return int(3)
    if mo == "April":
        return int(4)
    if mo == "May":
        return int(5)
    if mo == "June":
        return int(6)
    if mo == "July":
        return int(7)
    if mo == "August":
        return int(8)
    if mo == "September":
        return int(9)
    if mo == "October":
        return int(10)
    if mo == "November":
        return int(11)
    if mo == "December":
        return int(12)

year1 = int(input("Enter year one "))
month1 = str(input("Enter year one's month "))
day1 = int(input("Enter the day of year one's month "))

no_month1 = month_number_getter(month1)
int(no_month1)

year2 = int(input("Enter year two "))
month2 = str(input("Enter year two's month "))
day2 = int(input("Enter the day of year two's month "))

no_month2 = month_number_getter(month2)
int(no_month2)

if year1 < year2:
    lowest_year = year1
    snapshot = year1
    lowest_month = month1
    lowest_day = day1
    lowest_month_number = no_month1
    
    highest_year = year2
    highest_month = month2
    highest_day = day2
    highest_month_number = no_month2
else:
    lowest_year = year2
    snapshot = year2
    lowest_month = month2
    lowest_day = day2
    lowest_month_number = no_month2
    
    highest_year = year1
    highest_month = month1
    highest_day = day1
    highest_month_number = no_month1

lowest_year += 1
    
while lowest_year != highest_year:
    is_leap_year = is_light_year(lowest_year)
    if is_leap_year == "Y":
        day_counter += 366
        print(str(lowest_year) + " is leap year - Y - add 366 days - total day count - " + str(day_counter))
    elif is_leap_year == "N":
        day_counter += 365
        print(str(lowest_year) + " is leap year - N - add 365 days - total day count - " + str(day_counter))
        
    lowest_year += 1
    
else:
    for loop in range((lowest_month_number - 1)):
        day_counter += month_days_list[loop + 1]
    if is_light_year(snapshot) == "Y":
        remaining_days = 366 - lowest_day
    else:
        remaining_days = 365 - lowest_day
    day_counter += remaining_days
    
    for loop in range((highest_month_number - 1)):
        day_counter += month_days_list[loop + 1]
    day_counter += highest_day
    
    day_counter += 1
    
    print("Total days = " + str(day_counter))
