# Determine whether there exists a one-to-one character mapping from one string s1 to another s2

# Idea - Bijective map of a set.  
# Have 2 dictonaries, one has a forward mapping and other has a reverse mapping
# As we iterate through the string, that if any of the current characters are present as keys in the 
# dictionary, we have to check whether it is the same mapping. If not return False.
# If everything passes return True

def characterMap(s1, s2):
    sz1 = len(s1)
    if (sz1 != len(s2)):
        return False

    map1 = dict()
    map2 = dict()

    for i in range(0, sz1):
        if s1[i] in map1.keys() and map1[s1[i]] != s2[i]:
            return False
        if s2[i] in map2.keys() and map2[s2[i]] != s1[i]:
            return False

        map1[s1[i]] = s2[i]
        map2[s2[i]] = s1[i]

    return True

if __name__ == "__main__":
    s1 = "abc"
    s2 = "bcd"

    print("This is " + str(characterMap(s1,s2)))

    s3 = "foo"
    s4 = "bar"

    print("This is " + str(characterMap(s3,s4)))

    s5 = "abc"
    s6 = "ahh"

    print("This is " + str(characterMap(s5, s6)))