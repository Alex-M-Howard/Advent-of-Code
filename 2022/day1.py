def part_one():
    with open('data.txt') as data:
        data = data.read()

    data = data.split('\n')  

    elves = []
    sum = 0
    i = 0

    while i < len(data):
        if data[i] != '':
            sum += int(data[i])
        else:
            elves.append(sum)
            sum = 0
        
        i += 1

    return max(elves), elves

def part_two():
    elves = part_one()[1]

    total = 0
    for num in range(3):
        total += max(elves)
        index = elves.index(max(elves))
        elves.pop(index)
    
    return total

part_one_answer = part_one()[0]
part_two_answer = part_two()

print(part_one_answer, part_two_answer)
