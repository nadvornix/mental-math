import random

nums_to_days = {
    0: "Noneday",
    1: "Mon",
    2: "Tue",
    3: "Wed",
    4: "Thu",
    5: "Fri",
    6: "Sat",
}

days_to_nums = {
    "sun": 0,
    "mon": 1,
    "tue": 2,
    "wed": 3,
    "thu": 4,
    "fri": 5,
    "sat": 6,
}

year = random.randint(1900, 2000)
# Zvýšení pravděpodobnosti speciálního případu:
if random.random() < 0.1:
    year = random.choice([1900, 2000])

print(year)
user_input = input()

if 1900 <= year < 2000:
    anchor = 3
if 2000 <= year < 2100:
    anchor = 2

y = year % 100
doomsday = ((y // 12 + (y % 12) + ((y % 12) // 4)) % 7 + anchor) % 7

if days_to_nums.get(user_input, None) == doomsday:
    print("Correct!")
else:
    print("Wrong!. Century's anchor day: ", end="")

    print("Doomsday: {}, ({})".format(nums_to_days[doomsday], doomsday))
