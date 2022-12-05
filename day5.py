def part_one():
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

    for each in test_data:
        each = each.split('move ')[1]
        
        num_to_move = int(each.split(' from')[0])
        
        from_column = each.split('from ')[1]
        from_column = int(from_column.split(' to')[0])
        
        to_column = each.split('from ')[1]
        to_column = int(to_column.split(' to ')[1])

        print(num_to_move, from_column, to_column)


def part_two():
    pass

print(part_one())
print(part_two())