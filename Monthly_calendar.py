import calendar

year = int(input("Enter year: "))
month_input = input("Enter month (Name or Number): ")

# Try to convert to number, if it fails, it's a name
try:
    month_num = int(month_input)
except ValueError:
    # Convert name to number (e.g., "January" -> 1)
    months = list(calendar.month_name)
    month_num = months.index(month_input.capitalize())

print("\n", calendar.month(year, month_num))