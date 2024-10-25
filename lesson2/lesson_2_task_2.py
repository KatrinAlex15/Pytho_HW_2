def is_year_leap(year):
    return True if year % 4 == 0 else False

year = int(input("Введите год: "))
result = is_year_leap(year)
print(f"Год  {year} - {result}")

year_to_check = 2008
result = is_year_leap(year_to_check)
print(f"Год  {year_to_check} - {result}")
