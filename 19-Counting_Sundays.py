# This problem is only as complicated as one wants.
# You can predefine arrays that contain numbers of 
# days per month and so forth, or use a built in 
# time/calendar library. Here, only the rules
# that were given in the original problem were
# used.

day = 1      # Start on Tues so new month/year check isn't triggered
cycle = 1    # The day of the week
month = 0
days = 31
year = 1900
leapYear = False
sundayFirstCount = 0

while year != 2001:

    if day == 0:
        month = (month + 1) % 12

        if cycle == 6 and year != 1900:
            sundayFirstCount += 1

        if month == 0:
            days = 31
            year += 1
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        leapYear = True
                    else:
                        leapYear = False
                else:
                    leapYear = True   
            else:
                leapYear = False

        elif month == 1:
            if leapYear:
                days = 29
            else:
                days = 28

        elif month in (3,5,8,10): 
            days = 30
        else:
            days = 31
    
    day = (day + 1) % days
    cycle = (cycle + 1) % 7

print sundayFirstCount
