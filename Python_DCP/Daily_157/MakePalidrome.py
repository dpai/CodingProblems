## Given a word or string determine if we can make a palindrome.

# Check if the input string is a Palindrom
def CheckPalindrome(expr):
    l = 0
    r = len(expr)-1

    while l < r:
        if expr[l] != expr[r]:
            return False
        l = l + 1
        r = r - 1

    return True

# Recursive method to generate Palindrome of the input string
def rec_helper(expr, idx, output):

    # Base Case
    if idx+1 == len(expr):
        output[idx] = expr[idx]
        if CheckPalindrome(output):
            print("Palindrome word is " + "".join(output))
            return True
        else:
            return False
    
    # Recursion Case
    for i in range(idx, len(expr)):
        expr[idx], expr[i] = expr[i], expr[idx]
        output[idx] = expr[idx]
        if rec_helper(expr, idx+1, output):
            return True
        expr[i], expr[idx] = expr[idx], expr[i]

# Driver Call
def MakePalindrome(expr):
    print("Found for " + expr)
    output = expr
    rec_helper(list(expr), 0, list(output))

if __name__ == "__main__":
    input = "carrace"
    MakePalindrome(input)
    input = "faily"
    MakePalindrome(input)

