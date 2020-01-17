a = int(input("enter the year"))

if a % 4 == 0 or a % 400 == 0 and a % 100 != 0:
    print("the given year {} is leap year".format(a))
else:
    print('the given year is not leap year')
