def getdistinctchars(mapper, arr):
    sz = len(arr)
    for i in range(0, sz):
        if arr[i] not in mapper.keys():
            mapper[arr[i]] = 1

def maxdistinct(arr):
    mapper = {}
    getdistinctchars(mapper, arr)
    numchars = len(mapper)

    sz = len(arr)
    left_ptr = 0
    right_ptr = 0
    max_d = sz
    window_chars = 0

    char_in_window = {}

    while right_ptr < sz:
        
        while (right_ptr < sz and window_chars != numchars):
            if mapper[arr[right_ptr]] > 0:
                mapper[arr[right_ptr]] = 0
                window_chars = window_chars + 1
            if arr[right_ptr] not in char_in_window.keys():
                char_in_window[arr[right_ptr]] = 0
            char_in_window[arr[right_ptr]] += 1
            right_ptr += 1

        while (window_chars == numchars):
            char_in_window[arr[left_ptr]] -= 1
            if char_in_window[arr[left_ptr]] == 0:
                mapper[arr[left_ptr]] = 1
                window_chars -= 1
            left_ptr += 1

        min_len = right_ptr - left_ptr + 1
        if (max_d > min_len):
            max_d = min_len

    return max_d

if __name__ == "__main__":
    input0 = "jiujitsu"
    input1 = "jjjj"
    input2 = "qwerty"
    input3 = "a"
    input4 = "abcddddbbbbccca"
    input5 = "AABBBCBB"

    print("Smallest window for {} is {}".format(input0, maxdistinct(input0)))
    print("Smallest window for {} is {}".format(input1, maxdistinct(input1)))
    print("Smallest window for {} is {}".format(input2, maxdistinct(input2)))
    print("Smallest window for {} is {}".format(input3, maxdistinct(input3)))
    print("Smallest window for {} is {}".format(input4, maxdistinct(input4)))
    print("Smallest window for {} is {}".format(input5, maxdistinct(input5)))