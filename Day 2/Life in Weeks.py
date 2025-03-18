#Life in Weeks

current_age = int(input("What is your current age? "))

total_days = 32_850
total_weeks = 4_680
total_months = 1_080

remaining_days = total_days - (current_age * 365)
remaining_weeks = total_weeks - (current_age * 52)
remaining_months = total_months - (current_age * 12)

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
