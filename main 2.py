print('plz enter the month of the year')
m = int(input('take 1 for january 2 for february etc . : '))
print('if u face any errors plz rerun  the program')
if m == 1 or 3 or 5 or 7 or 8 or 10 or 12:
     # one is a 31-day month
     d=int( input('enter the day of the month '))
     if d > 31 : print('error ')
     elif d <= 0 :print('error ')
     else: print(31-d , 'days are left tell the end of the month '  )
elif m == 2:
    s = int(input('if its a leap year plz enter 1 if not enter 0 '))
    if s == 1 :
        d=int( input('enter the day of the month '))
        if d > 29 : print('error ')
        elif d <= 0 :print('error ')
        else: print(29-d , 'days are left tell the end of the month '  )

    elif s == 0 :   d=int( input('enter the day of the month '))
     if d > 28 :
     print('error')
     elif d <= 0 :\
     print('error ')
     else:
         print(28-d , 'days are left tell the end of the month '  )
elif m == 4 or 6 or 9 or 11 :   \
      d=int( input('enter the day of the month '))
      if d > 30 : print('error ')
      elif d <= 0 :print('error ')
      else: print(30-d , 'days are left tell the end of the month '  )

else: print("error ")
