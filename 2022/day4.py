def part_one():
    with open('2022/day4_data.txt') as data:
        data = data.read()
        data = data.split('\n')
            
    contained_pairs = 0
    
    for each in data:
        each = each.split(',')
        
        range_a = each[0].split('-')
        range_b = each[1].split('-')
        
        if int(range_b[0]) >= int(range_a[0]) and int(range_b[1]) <= int(range_a[1]):
            contained_pairs += 1
        
        elif int(range_a[0]) >= int(range_b[0]) and int(range_a[1]) <= int(range_b[1]):
            contained_pairs += 1
            
            
    return contained_pairs

    
def part_two():
    with open('2022/day4_data.txt') as data:
        data = data.read()
        data = data.split('\n')
            
   
    contained_pairs = 0
    
    for each in data:
        each = each.split(',')
        
        range_a = each[0].split('-')
        range_b = each[1].split('-')
        
        if (int(range_b[0]) >= int(range_a[0]) and int(range_b[0]) <= int(range_a[1])) or (int(range_b[1]) >= int(range_a[0]) and int(range_b[1]) <= int(range_a[1])):
            contained_pairs += 1
        
        elif (int(range_a[0]) >= int(range_b[0]) and int(range_a[0]) <= int(range_b[1])) or (int(range_a[1]) >= int(range_b[0]) and int(range_a[1]) <= int(range_b[1])):
            contained_pairs += 1
            
            
    return contained_pairs

    
print(part_one())
print(part_two())