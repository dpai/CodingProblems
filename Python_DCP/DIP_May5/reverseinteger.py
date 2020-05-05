# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

# Here's some examples and some starter code.
#Insight - Use mod and div to work with digits and accumalate the result . O(n)

def reverse_integer(num):
  # Fill this in.
  result = 0
  val = num

  while(val != 0):
      val1 = ((val % 10) + 10) % 10  ## Bug 1 : Forgot this -- Though I think Python does not need this
      val = int(val / 10)
      if (num < 0 and val1 != 0): ## Bug 2 : This is edge case for negative numbers.
          result = result * 10 + (10 - val1)
      else:
          result = result * 10 + val1
  
  if (num < 0):
      result = result * -1

  return result

if __name__ == "__main__":
    for i in range(-150, 151):
        print("FLip of " + str(i) + " is " + str(reverse_integer(i)))

print(reverse_integer(-9))
#-9

print(reverse_integer(-10000))
# -1

print(reverse_integer(-10))
# -1

print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123