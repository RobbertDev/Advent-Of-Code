# Getting input
with open(r'C:\Users\Robbert\Documents\Development\Advent of Code\Day-6\input.txt') as file:
    input = file.read()

for i in range(14, len(input)):
    s = set(input[(i-14):i])
    if len(s) == 14:
        print("Answer for part 2 is: ", i)
        break