city= input("Enter the city name;")
temp= float(input("Enter the temperature in C;"))

print("City:", city)
print("Temperature:", temp, "C")

# Part-2
if temp > 35:
    print("It's a hot day in")


#part-3

    if temp < 25:
        print("Great day to go outside!")
    else:
        print("Grab a jacket before you go outside!")


#part-4

if temp < 35:
   print("Weather: scorching Hot")
elif temp < 25:
   print("Weather: Warm and Sunny")

elif temp < 15:
    
  print("Weather: Cool and Breezy")

else:

 print("Weather: Cold - stay warm!")

#part-5
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))

number = int(input("Enter number to check: "))
print("Number to be checked:", number)

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")