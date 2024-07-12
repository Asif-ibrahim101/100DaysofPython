CheckYearTrue = True
CheckYearFalse = False

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return CheckYearTrue
      else:
        return CheckYearFalse
    else:
      return CheckYearTrue
  else:
    return CheckYearFalse

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if month == 2 and is_leap(year):
      return 29
  else :
      gotMonth = month_days[month - 1]
      return gotMonth
  

year = int(input()) # Enter a year
month = int(input()) # Enter a month
result = days_in_month(year, month)
print(result)
