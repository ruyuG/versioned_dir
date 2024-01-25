
this_year = 2022

start_year = 2010
end_year = 2026

for year in range(start_year, end_year):
    
    if year%4 == 0 and year%400 == 0:
        leap_year = "Yes"
    elif year%4 == 0 and year%100 == 0:
        leap_year = "No"
    elif year%4 == 0:
        leap_year = "Yes"
    else:
        leap_year = "No"
    
    if year == this_year:
        print(f"Is this year a leap year? {leap_year}")
    else:
        print(f"Is {year} a leap year? {leap_year}")
