def part_one():
    with open('2022/day2_data.txt') as data:
        data = data.read()
        data = data.split('\n')
    
    shapes = {
        'X': 1,  # Rock
        'Y': 2,  # Paper
        'Z': 3   # Scissors
    }
    
    my_score = 0
    
    for round in data:
        round_score = 0
        game = round.split(' ')
        
        round_score += shapes[game[1]]
        
        if game[0] == 'A' and game[1] == 'X': round_score += 3
        elif game[0] == 'A' and game[1] == 'Y': round_score += 6
        elif game[0] == 'B' and game[1] == 'Y': round_score += 3
        elif game[0] == 'B' and game[1] == 'Z': round_score += 6
        elif game[0] == 'C' and game[1] == 'Z': round_score += 3
        elif game[0] == 'C' and game[1] == 'X': round_score += 6
        
        my_score += round_score
        
    return my_score


def part_two():
    with open('2022/day2_data.txt') as data:
        data = data.read()
        data = data.split('\n')
    
    shapes = {
        'A': 1,  # Rock
        'B': 2,  # Paper
        'C': 3,  # Scissors
    }
    
    my_score = 0
    
    for round in data:
        round_score = 0
        game = round.split(' ')
        
        if game[1] == 'X':
            if game[0] == 'A': round_score += shapes['C']
            if game[0] == 'B': round_score += shapes['A']
            if game[0] == 'C': round_score += shapes['B']
            
        if game[1] == 'Y':
            round_score += shapes[game[0]] + 3

        if game[1] == 'Z':
            if game[0] == 'A': round_score += shapes['B'] + 6
            if game[0] == 'B': round_score += shapes['C'] + 6
            if game[0] == 'C': round_score += shapes['A'] + 6
        
        my_score += round_score
        
    return my_score

print(part_one())
print(part_two())