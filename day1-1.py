with open("input1.txt") as f:
    file = f.read()
    
lines = file.split("\n")

total = 0
for line in lines:
    numbers = {}
    for position, symbol in enumerate(line):
        if not symbol.isdigit():
            continue
        numbers[position] = symbol
        
    keys = list(numbers)
    if len(keys) == 1:
        total += int(numbers[keys[0]]) * 11
        continue
    if not keys:
        continue
    
    start_key = min(keys)
    end_key = max(keys)
    total += int(numbers[start_key]) * 10 + int(numbers[end_key])
print(total)
