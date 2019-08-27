def getNregularnumbers(N):
    counter2 = 0
    counter3 = 0
    counter5 = 0

    result = [1] * N

    count = 1

    while count < N:
        values = [ result[counter2]*2, result[counter3]*3, result[counter5]*5]

        min_value = min(values)

        result[count] = min_value

        if min_value % 2 == 0:
            counter2 = counter2 + 1
        if min_value % 3 == 0:
            counter3 = counter3 + 1
        if min_value % 5 == 0:
            counter5 = counter5 + 1

        count = count + 1

    return result

if __name__ == "__main__":
    result = getNregularnumbers(20)
    print(result)