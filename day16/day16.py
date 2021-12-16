import statistics
import binascii

def main():
    test = False
    if test:
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]

    hexinput = lines[0]

    i = 0
    version_sum = 0
    while i < len(hexinput):
        val, i = packet_version_sum(hexinput, i)
        version_sum += val
    print(version_sum)

    i = 0
    print(packet_evaluate(hexinput, i)[0])

def read_bit(hexinput, i):
    return (int(hexinput[i//4], 16)) >> (3 - i%4) & 1

def read_bits(hexinput, i, n):
    val = 0
    for j in range(n):
        val = val << 1
        val = val | read_bit(hexinput, i+j)
    return val

def read_packet_header(hexinput, i):
    version = read_bits(hexinput, i, 3)
    type_ID = read_bits(hexinput, i+3, 3)
    return(version, type_ID)

def read_literal_packet(hexinput, i):
    val = 0
    block = read_bits(hexinput, i, 5)
    val = block & 15

    while block >= 16:
        i += 5
        val = val << 4
        block = read_bits(hexinput, i, 5)
        val += block & 15
    
    return(val, i+5)

def packet_evaluate(hexinput, i):
    header = read_packet_header(hexinput, i)
    version, type_ID = header
    i += 6

    if type_ID == 4:
        val, i = read_literal_packet(hexinput, i)
    else:
        subpackets = []
        lentype = read_bit(hexinput, i)
        i += 1
        if lentype:
            numpackets = read_bits(hexinput, i, 11)
            i += 11
            for j in range(numpackets):
                spval, i = packet_evaluate(hexinput, i)
                subpackets += [spval]
        else:
            packetlen = read_bits(hexinput, i, 15)
            i += 15
            packetend = i + packetlen
            while i < packetend:
                spval, i = packet_evaluate(hexinput, i)
                subpackets += [spval]
        if type_ID == 0:
            val = sum(subpackets)
        elif type_ID == 1:
            val = subpackets[0]
            for sp in subpackets[1:]:
                val = val * sp
        elif type_ID == 2:
            val = min(subpackets)
        elif type_ID == 3:
            val = max(subpackets)
        elif type_ID == 5:
            val = 1 if subpackets[0] > subpackets[1] else 0
        elif type_ID == 6:
            val = 1 if subpackets[0] < subpackets[1] else 0
        elif type_ID == 7:
            val = 1 if subpackets[0] == subpackets[1] else 0
        else:
            print("oh no")

    return (val, i)

def packet_version_sum(hexinput, i):
    header = read_packet_header(hexinput, i)
    version, type_ID = header
    i += 6

    version_sum = version
    if type_ID == 4:
        val, i = read_literal_packet(hexinput, i)
    else:
        lentype = read_bit(hexinput, i)
        i += 1
        if lentype:
            numpackets = read_bits(hexinput, i, 11)
            i += 11
            for j in range(numpackets):
                val, i = packet_version_sum(hexinput, i)
                version_sum += val
        else:
            packetlen = read_bits(hexinput, i, 15)
            i += 15
            packetend = i + packetlen
            while i < packetend:
                val, i = packet_version_sum(hexinput, i)
                version_sum += val
    return (version_sum, i)

if __name__ == '__main__':
    main()