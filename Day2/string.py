#Basic os string
"""
name = "abhay"
print(name.upper())
print(name.title())
print(name.find('bh'))
print(name.find('f'))
"""



# f'string method is used to format the output in which we want

""" 
we have to take input from user as date and time, if the date is 1st of january
and the time is 12:00 am then we have to print "Happy New Year"
and the time is 12:00 am and date is match with stored date variable then
we have to print "Happy Birthday"
"""


# stored birthday date (DD-MM format)
birthday_date = "15-08"

# taking input
date = input(f"Enter date (DD-MM): ")
time = input(f"Enter time (HH:MM am/pm): ").lower()

if date == f"01-01" and time == f"12:00 am":
    print(f"Happy New Year")

elif date == f"{birthday_date}" and time == f"12:00 am":
    print(f"Happy Birthday")

else:
    print(f"No special occasion")

