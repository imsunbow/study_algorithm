limit = int(input())
my_speed = int(input())

diff = my_speed - limit

if diff >= 31:
    print("You are speeding and your fine is $500.")
elif 21 <= diff <= 30:
    print("You are speeding and your fine is $270.")
elif 1 <= diff <= 20:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")    