# Check if s given year is a leap year

def is_leap_year(year):
    """
    Returns:
    True if the year is a leap year, False otherwise.
    """
    print("Year", year)

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2020))
print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))

