def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()

    inputl = [line.split(" | ")[0] for line in strlines]
    output = [line.split(" | ")[1] for line in strlines]
    output_wrds = []

    for line in output:
        words = line.split()
        output_wrds += words

    numsum = 0
    for word in output_wrds:
        numlen = len(word)
        if numlen == 2 or numlen == 4 or numlen == 3 or numlen == 7:
            numsum += 1

    print(numsum)

    # what I know, one with len=2 is 1, len=4 is 4, len=3 is 7, len=7 is 8
    # len=5 could be 2, 3, 5 and len=6 could be 0, 6, 9
    # 9 will have 4 in it
    # 0 will have 7 in it (and won't be 9)
    # 6 will be only of len 6 without 7 in it
    # 3 will have 7 in it
    # 6 will be in 5 but not 2
    # 2 will be the last of len=5

    numsum = 0
    
    insets = []
    outsets = []

    for i in range(len(inputl)):
        inwrds = inputl[i].split()
        inwrds = [set(wrd) for wrd in inwrds]
        outwrds = output[i].split()
        outwrds = [set(wrd) for wrd in outwrds]
        insets.append(inwrds)
        outsets.append(outwrds)

    for i in range(len(insets)):
        x = insets[i]
        y = outsets[i]

        nums = [None] * 10
        nums[1] = list(filter(lambda x: len(x) == 2, x))[0]
        nums[4] = list(filter(lambda x: len(x) == 4, x))[0]
        nums[7] = list(filter(lambda x: len(x) == 3, x))[0]
        nums[8] = list(filter(lambda x: len(x) == 7, x))[0]
        nums[9] = list(filter(lambda x: len(x) == 6 and nums[4].issubset(x), x))[0]
        nums[0] = list(filter(lambda x: len(x) == 6 and nums[7].issubset(x) and x != nums[9], x))[0]
        nums[6] = list(filter(lambda x: len(x) == 6 and not nums[7].issubset(x), x))[0]
        nums[3] = list(filter(lambda x: len(x) == 5 and nums[7].issubset(x), x))[0]
        nums[5] = list(filter(lambda x: len(x) == 5 and x.issubset(nums[6]), x))[0]
        nums[2] = list(filter(lambda x: len(x) == 5 and x != nums[3] and x != nums[5], x))[0]

        mult = 1000
        for s in y:
            numsum += nums.index(s) * mult
            mult = mult / 10

    print(numsum)


        

if __name__ == '__main__':
    main()