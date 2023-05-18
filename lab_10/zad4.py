from datetime import datetime, timedelta

def calculate_age(date_of_birth):
    current_date = datetime.now()
    birth_date = datetime.strptime(date_of_birth, "%d.%m.%Y")

    age = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    if months < 0 or (months == 0 and days < 0):
        age -= 1
        months += 12

    if days < 0:
        months -= 1
        days += (current_date - timedelta(days=days)).day

    next_birthday = datetime(current_date.year, birth_date.month, birth_date.day)
    if next_birthday < current_date:
        next_birthday = datetime(current_date.year + 1, birth_date.month, birth_date.day)

    days_until_birthday = (next_birthday - current_date).days

    print(f"Your age is {age} years, {months} months, and {days} days.")
    print(f"Your next birthday will be in {days_until_birthday} days.")


calculate_age("24.05.1999")

# Your age is 23 years, 11 months, and 18 days. <- tu akurat całkiem zabawnie policzyło dni haha ale zakładam że to kwestia lat przestępnych
# Your next birthday will be in 5 days. 