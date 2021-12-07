def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()

    crabs = strlines[0].split(',')

    for i in range(len(crabs)):
        crabs[i] = int(crabs[i])

    minfuel = 1000000000

    for i in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - i)
        minfuel = min(minfuel, fuel)
    print(minfuel)

    minfuel = 10000000000000

    for i in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            mf = abs(crab - i)
            while mf > 0: # this is rather slow but it finished while I was working on my solution using memoization
                fuel += mf
                mf -= 1
        minfuel = min(minfuel, fuel)
    print(minfuel)

if __name__ == '__main__':
    main()