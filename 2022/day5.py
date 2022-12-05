test_data = [
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2'
    ]

test_crate_config = [
    ['N', 'Z'],
    ['D', 'C', 'M'],
    ['P'],
    ]


def part_one():
    with open('2022/day5_data.txt') as data:
        data = data.read()
        data = data.split('\n')
            
    crate_config = [
        ['T','Z','B'],
        ['N','D','T','H','V'],
        ['D','M','F','B'],
        ['L','Q','V','W','G','J','T'],
        ['M','Q','F','V','P','G','D','W',],
        ['S','F','H','G','Q','Z','V'],
        ['W','C','T','L','R','N','S','Z'],
        ['M','R','N','J','D','W','H','Z'],
        ['S','D','F','L','Q','M']
    ]

    for each in data:
        try:
            each = each.split('move ')[1]
            
            num_to_move = int(each.split(' from')[0])
            
            from_column = each.split('from ')[1]
            from_column = int(from_column.split(' to')[0]) - 1 # Minus 1 because list starts at 0, not 1
            
            to_column = each.split('from ')[1]
            to_column = int(to_column.split(' to ')[1]) - 1    # Minus 1 because list starts at 0, not 1
            
            for move in range(num_to_move):
                item_to_move = crate_config[from_column].pop(0)
                crate_config[to_column].insert(0, item_to_move)
        except:
            pass
    
    top_string = ''
    
    for each in crate_config:
        top_string += each[0]                
    
    return top_string


def part_two():
    with open('2022/day5_data.txt') as data:
        data = data.read()
        data = data.split('\n')
            
    crate_config = [
        ['T','Z','B'],
        ['N','D','T','H','V'],
        ['D','M','F','B'],
        ['L','Q','V','W','G','J','T'],
        ['M','Q','F','V','P','G','D','W',],
        ['S','F','H','G','Q','Z','V'],
        ['W','C','T','L','R','N','S','Z'],
        ['M','R','N','J','D','W','H','Z'],
        ['S','D','F','L','Q','M']
    ]

    for each in data:
        try:
            each = each.split('move ')[1]
            
            num_to_move = int(each.split(' from')[0])
            
            from_column = each.split('from ')[1]
            from_column = int(from_column.split(' to')[0]) - 1 # Minus 1 because list starts at 0, not 1
            
            to_column = each.split('from ')[1]
            to_column = int(to_column.split(' to ')[1]) - 1    # Minus 1 because list starts at 0, not 1

            location_of_move = num_to_move - 1
            
            for move in range(num_to_move):
                item_to_move = crate_config[from_column].pop(location_of_move)
                crate_config[to_column].insert(0, item_to_move)
                
                location_of_move -= 1
                
        except:
            pass
                
    top_string = ''
    for each in crate_config:
        top_string += each[0]                
    
    return top_string

print(part_one())
print(part_two())
