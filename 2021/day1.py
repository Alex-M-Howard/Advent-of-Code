def part_one():
    with open('day1_data.txt') as data:
        data = data.readlines()
        
    for each in data:
        if '\n' in each:
            each = each.split('\n')[0]

    i = 0
    is_larger = 0

    while i < len(data):
        if '\n' in data[i]: data[i] = data[i].split('\n')[0]
        
        try:
            if '\n' in data[i+1]: data[i+1] = data[i+1].split('\n')[0]
        except:
            pass
        
        try:
            if int(data[i]) < int(data[i+1]):
                is_larger += 1
        except:
            pass
        
        i += 1
        
    return is_larger, data

def part_two():
    data = part_one()[1]
    
    i = 0
    is_larger = 0
    
    while i < len(data):
        
        try:
            if int(data[i]) + int(data[i+1]) + int(data[i+2]) < int(data[i+1]) + int(data[i+2]) + int(data[i+3]) :
                is_larger += 1
        except:
            break  
        i += 1
        
    return is_larger

answer_one = part_one()[0]
answer_two = part_two()

print(answer_one)
print(answer_two)
