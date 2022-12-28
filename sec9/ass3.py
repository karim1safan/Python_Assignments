age = float(input("What's your age? "))
age_months = age * 12
age_weeks = age_months * 4
age_days = age * 365
age_houres = age_days * 24
age_minutes = age_houres * 60
age_seconds = age_minutes * 60

if age > 10 and age < 100:
    print(f"Your age with months: {age_months} M")
    print(f"Your age with weeks: {age_weeks} W")
    print(f"Your age with days: {age_days} D")
    print(f"Your age with houres: {age_houres} H")
    print(f"Your age with minutes: {age_minutes} M")
    print(f"Your age with seconds: {age_seconds} S")
else:
    print("your age out of range")
