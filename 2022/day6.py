test_data_one = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'   # Answer is 7

def part_one():
    with open('2022/day6_data.txt') as data:
        data = data.read()
    
    i = 3               # Since 4 characters need to be checked, start here
    
    while i < len(data):
        sequence = set([data[i], data[i-1], data[i-2], data[i-3]])
        if len(sequence) < 4:
            i += 1
        else:
            return i+1  # Because of indexing, make sure to add 1 back in
    

def part_two():
    with open('2022/day6_data.txt') as data:
        data = data.read()
    
    i = 13               # Since 4 characters need to be checked, start here
    
    while i < len(data):
        
        x = i            # Setting new counter variable so we don't affect other
        sequence = []
        for each in range(14):
            sequence.append(data[x])
            x -= 1
        
        sequence = set(sequence)     # Sets remove duplicates
        
        
        if len(sequence) < 14:
            i += 1
        else:
            return i+1  # Because of indexing, make sure to add 1 back in
    
    
print(part_one())
print(part_two())
