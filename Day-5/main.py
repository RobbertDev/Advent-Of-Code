# Created with the help of https://www.youtube.com/watch?v=LvH2DU1bARk

# Getting input
with open(r'C:\Users\Robbert\Documents\Development\Advent of Code\Day-5\input.in') as file:
    stack_strings, instructions = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))

# Create dictionary
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}

# Create array of indexes that contain values
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]

# Added crate to correct stack
def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

# Return all top crates
def getAnswer():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

loadStacks()

# Loop through instructions
for instruction in instructions:

    # Convert instructions to usable data
    instruction = instruction.replace("move","").replace("from ","").replace("to ","").strip().split(" ")
    instruction = [int(i) for i in instruction]

    # Set parameters
    crates = instruction[0]
    origin = instruction[1]
    destination = instruction[2]

    crates_to_remove = stacks[origin][-crates:]
    stacks[origin] = stacks[origin][:-crates]

    for crate in crates_to_remove:
        stacks[destination].append(crate)

# Print out the answer string
print(getAnswer())