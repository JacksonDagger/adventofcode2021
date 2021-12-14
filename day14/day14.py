import statistics

def main():
    test = False
    if test:
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]
    strpolymer = lines[0]
    polymer = list(strpolymer)

    pairs = [(list(line.split(' -> ')[0]), line.split(' -> ')[1]) for line in lines[2:]]
    strpairs = [(line.split(' -> ')[0], line.split(' -> ')[1]) for line in lines[2:]]

    pairmappings = []

    for pair, insertval in strpairs:
        pairmappings += [(pair, pair[0] + insertval, insertval + pair[1])]

    polymer_dict = {}

    for i in range(len(strpolymer)-1):
        if strpolymer[i:i+2] in polymer_dict:
            polymer_dict[strpolymer[i:i+2]] += 1
        else:
            polymer_dict[strpolymer[i:i+2]] = 1
    
    for i in range(10):
        polymer = polymer_insert(polymer, pairs)
    
    maxoccur = 0
    minoccur = len(polymer) + 1

    for item in set(polymer):
        occur = polymer.count(item)
        if occur > maxoccur:
            maxoccur = occur
        if occur < minoccur:
            minoccur = occur
    
    print(maxoccur-minoccur)

    for i in range(40):
        polymer_dict = pair_dict_polymer_insert(polymer_dict, pairmappings)

    cdict = {}

    for pair, count in polymer_dict.items():
        for c in pair:
            if c in cdict:
                cdict[c] += count
            else:
                cdict[c] = count

    cdict[strpolymer[0]] += 1
    cdict[strpolymer[-1]] += 1
    counts = cdict.values()            

    print(max(counts)/2-min(counts)/2)

    
    
def polymer_insert(polymer, pairs):
    inserts = []
    for i in range(len(polymer)-1):
        for pair, insertval in pairs:
            if polymer[i:i+2] == pair:
                inserts.insert(0, (i+1, insertval))
    for i, insertval in inserts:
        polymer.insert(i, insertval)
    return polymer

def pair_dict_polymer_insert(polymer, pairs):
    newpolymer = polymer.copy()
    for pair, newpair0, newpair1 in pairs:
        if pair in polymer:
            if newpair0 in newpolymer:
                newpolymer[newpair0] += polymer[pair]
            else:
                newpolymer[newpair0] = polymer[pair]
            if newpair1 in newpolymer:
                newpolymer[newpair1] += polymer[pair]
            else:
                newpolymer[newpair1] = polymer[pair]
            newpolymer[pair] -= polymer[pair]

    return newpolymer
    
if __name__ == '__main__':
    main()