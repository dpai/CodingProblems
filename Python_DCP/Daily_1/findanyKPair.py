def findanyKpair(input, k):
    sz = len(input)

    normal_set = set()

    for i in range(sz):
        if input[i] in normal_set:
            return True

        normal_set.add(k - input[i])
        
    return False

if __name__ == "__main__":
    input = [ 3, 18, 7, 55, 125, 37, 28, 25, 9]

    print("For 16 it is " + str(findanyKpair(input, 16)))
    print("For 125 it is " + str(findanyKpair(input, 125)))