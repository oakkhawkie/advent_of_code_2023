with open("input.txt", 'r') as f:
    file = f.read()
    
# print(file)

lines = file.split("\n")

position_symbol_dict = {i: [] for i in range(1, len(lines)+1)}
position_number_dict = {i: [] for i in range(1, len(lines)+1)}
for row, line_string in enumerate(lines):
    for position, item in enumerate(line_string):
        if item == ".":
            continue
        if item.isdigit():
            position_number_dict[row+1].append(position)
            continue
        
        position_symbol_dict[row+1].append(position)

adjecent_symbol_positions = {i: [] for i in range(0, 141)}
for row, positions in position_symbol_dict.items():
    for position in positions:
        adjecent_symbol_positions[row-1].append(position - 1)
        adjecent_symbol_positions[row-1].append(position)
        adjecent_symbol_positions[row-1].append(position + 1)
        adjecent_symbol_positions[row].append(position - 1)
        adjecent_symbol_positions[row].append(position + 1)
        adjecent_symbol_positions[row+1].append(position - 1)
        adjecent_symbol_positions[row+1].append(position)
        adjecent_symbol_positions[row+1].append(position + 1)
        
for row, positions in position_number_dict.items():
    for position in positions:
        
            


print(position_number_dict)
