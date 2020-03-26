import subprocess, random, os

calls = {
    "python multiplication.py 12 15 15 19": 10,
    "python multiplication.py 11 11 20 99": 10,
    "python multiplication.py 11 11 200 500": 10,
}

command = random.choices(list(calls.keys()), list(calls.values()), k=1)
print(command)
os.system(command[0])
