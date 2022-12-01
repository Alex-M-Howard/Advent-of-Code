def part_one():
    with open('day2_data.txt') as data:
        data = data.readlines()

    i = 0

    x_coord = 0
    y_coord = 0


    while i < len(data):
        if '\n' in data[i]: data[i] = data[i].split('\n')[0]
        
        if 'forward' in data[i]:
            x = data[i].split('forward ')[1]
            x_coord += int(x)
            
        elif 'up' in data[i]:
            y = data[i].split('up ')[1]
            y_coord -= int(y)
            
        else:
            y = data[i].split('down ')[1]
            y_coord += int(y)
        
        i += 1

    return x_coord * y_coord, data


def part_two():
    data = part_one()[1]
    
    i = 0

    x_coord = 0
    y_coord = 0
    aim = 0

    while i < len(data):
        
        if 'forward' in data[i]:
            x = data[i].split('forward ')[1]
            x_coord += int(x)
            y_coord += int(x) * aim
            
        elif 'up' in data[i]:
            y = data[i].split('up ')[1]
            aim -= int(y)
            
        else:
            y = data[i].split('down ')[1]
            aim += int(y)
        
        i += 1

    return x_coord * y_coord
    

answer_one = part_one()[0]
answer_two = part_two()

print(answer_one, answer_two)
