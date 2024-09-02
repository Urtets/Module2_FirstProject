def find_num():
    for k in range(3, 21):
        result = str(k) + " - "
        for i in range(1, k):
            for j in range(i + 1, k):
                if k % (i + j) == 0:
                    result = result + str(i) + str(k)

        print(result)

find_num()