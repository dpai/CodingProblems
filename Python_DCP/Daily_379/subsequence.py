""" Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:


x
y
z
xy
xz
yz
xyz

Note that zx is not a valid subsequence since it is not in the order of the given string. """

def helper(input_string, i, output_string):
    if i == len(input_string):
        print(''.join(output_string))
        return

    helper(input_string, i+1, output_string)
    output_string.append(input_string[i])
    helper(input_string, i+1, output_string)
    del output_string[-1]

def subsequence(input_string):
    output_string = []
    helper(input_string, 0, output_string)

if __name__ == "__main__":
    input_string = "xyz"
    subsequence(input_string)