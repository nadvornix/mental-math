import random, sys, time

start_time = time.time()

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

if len(sys.argv) == 1:
    year = random.randint(1900, 2060)

    # increasing probability of exceptions:
    if random.random() < 0.1:
        year = random.choice([1900, 2000])
elif len(sys.argv) == 2:
    year = int(sys.argv[1])
elif len(sys.argv) == 3:
    start_year = int(sys.argv[1])
    end_year = int(sys.argv[2])
    year = random.randint(start_year, end_year)
else:
    print("Wrong number of parameters", file=sys.stderr)

print(year)
user_input = input()
end_time = time.time()

if 1900 <= year < 2000:
    anchor = 3
if 2000 <= year < 2100:
    anchor = 2

y = year % 100
doomsday = ((y // 12 + (y % 12) + ((y % 12) // 4)) % 7 + anchor) % 7

if days_to_nums.get(user_input, None) == doomsday:
    print("Correct!")
else:
    print("Wrong!. ", end="")

    print("Doomsday: {}, ({})".format(nums_to_days[doomsday], doomsday))

print("{:.2f}s".format(end_time - start_time))
