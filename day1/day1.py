with open('input', 'r') as f:
    strlines = f.readlines()

vals = [int(x) for x in strlines]

sum  = 0
prev = vals[0]

for val in vals[1:]:
    if val > prev:
        sum += 1
    prev = val

print(sum)

sum = 0
windows = [vals[i-2] + vals[i-1] + vals[i] for i in range(2, len(vals))]
prev=windows[0]
for window in windows[1:]:
    if window > prev:
        sum += 1
    prev = window
print(sum)