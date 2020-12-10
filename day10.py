numbers = []
with open("day10.txt") as f:
    for cnt, l in enumerate(f):
        numbers.append(int(l))
        
numbers.sort()
diffs = [numbers[i+1] - numbers[i] for i in range(0, len(numbers)-1)]
print((diffs.count(1) + 1) * (diffs.count(3) + 1))
