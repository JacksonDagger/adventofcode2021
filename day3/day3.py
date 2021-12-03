with open('input.txt', 'r') as f:
    strlines = f.readlines()

def parse_bin_str(strnum):
    ret = 0
    for c in strnum:
        if c != "1" and c != "0":
            break
        ret = ret << 1
        if c == "1":
            ret += 1
    return ret

def getbits(testlines):
    numbits = 0
    for c in testlines[0]:
        if c == '1' or c == '0':
            numbits += 1
        else:
            break
    bits = [0] * numbits

    for line in testlines:
        for i in range(len(line)):
            c = line[i]
            if c == '1':
                bits[i] += 1
    return bits

def getbit(testlines, i):
    bit = 0

    for line in testlines:
        c = line[i]
        if c == '1':
            bit += 1
    return bit

bits = getbits(strlines)

g_bits = [bits[i] >= len(strlines) / 2 for i in range(len(bits))]
gamma = 0
epsilon = 0

for j in range(len(g_bits)):
    gamma = gamma << 1
    epsilon = epsilon << 1
    if g_bits[j]:
        gamma += 1
    else:
        epsilon += 1

print(epsilon*gamma)

testlines = strlines
for i in range(12):
    bit = getbit(testlines, i)
    mcb = "1" if bit >= len(testlines) / 2 else "0"
    testlines = list(filter(lambda x: x[i] == mcb, testlines))
    if len(testlines) <= 1:
        break

ox_bits = testlines[0]
oxygen = parse_bin_str(ox_bits)

testlines = strlines
for i in range(12):
    bit = getbit(testlines, i)
    mcb = "1" if bit >= len(testlines) / 2 else "0"
    testlines = list(filter(lambda x: x[i] != mcb, testlines))
    if len(testlines) <= 1:
        break

co2_bits = testlines[0]
co2 = parse_bin_str(co2_bits)

print(oxygen*co2)