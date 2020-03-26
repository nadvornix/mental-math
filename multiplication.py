import sys, random, time

start_time = time.time()
amin, amax, bmin, bmax = [int(x) for x in sys.argv[1:5]]

a = random.randint(amin, amax)
b = random.randint(bmin, bmax)

print(a, b)

user_input = int(input())
end_time = time.time()

if a * b == user_input:
    print("Correct")
else:
    print("Wrong. %s x %s = %s" % (a, b, a * b))

print("{:.2f}s".format(end_time - start_time), file=sys.stderr)
