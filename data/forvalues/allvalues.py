from ..models import Calendar

n = 20000

dayno=1
monthno=1
yearnoo=1995

for i in range(0,n):
    if dayno>9 :
        d = str(dayno)
    else :
        d = '0'+ str(dayno)
    if monthno>9 :
        m = str(monthno)
    else :
        m = '0' + str(monthno)
    y = str(yearnoo)
    b = Calendar()
    b.year = y
    b.month = m
    b.day = d
    b.date = y+'-'+m+'-'d
    b.save()

    #year = int(input("Input a year: "))

    if yearnoo % 400 == 0 :
        leap_year = True
    elif yearnoo % 100 == 0:
        leap_year = False
    elif yearnoo % 4 == 0 :
        leap_year = True
    else:
        leap_year = False


    if monthno in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif monthno == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30

    if dayno < month_length:
        dayno += 1
    else:
        dayno = 1
        if monthno == 12:
            monthno = 1
            yearnoo += 1
        else:
            monthno += 1
   # print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
