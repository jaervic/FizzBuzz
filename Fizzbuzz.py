#The idea is to print each number from 1 to 100 but each number that is divisible by 3 will print "Fizz", each number divisible by 5 will print "Buzz" and the ones that are divisibles by both 3 and 5 will print "FizzBuzz"

for all in range(1, 101):
  if all % 3 == 0 and all % 5 == 0: #Divisibles by 3 and 5 at the same time first
    print("FizzBuzz")
  elif all % 5 == 0: #Divisibles by 5
    print("Buzz")
  elif all % 3 == 0: #Divisibles by 3
    print("Fizz")
  else:
    print(all)