def part_one():
    with open('2022/day3_data.txt') as data:
        data = data.read()
        data = data.split('\n')

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priorities = {}
    priority_sum = 0
    
    for i in range(len(letters)):
        priorities[letters[i]] = i + 1
    
    for each in data:
        compartment_one = each[0:len(each)//2]
        compartment_two = each[len(each)//2:]
        
        unique = ''.join(
            set(compartment_one).intersection(compartment_two)
        )
        
        priority_sum += priorities[unique]
  
    return priority_sum    


def part_two():
    with open('2022/day3_data.txt') as data:
        data = data.read()
        data = data.split('\n')

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priorities = {}
    priority_sum = 0
    
    for i in range(len(letters)):
        priorities[letters[i]] = i + 1
    
    i = 0
    while i < len(data):
        rucksack_one = data[i]
        rucksack_two = data[i+1]
        rucksack_three = data[i+2]
        
        unique = ''.join(
            set(rucksack_one)
            .intersection(rucksack_two)
            .intersection(rucksack_three)
        )
        
        priority_sum += priorities[unique]
        i = i + 3
  
    return priority_sum    

print(part_one())
print(part_two())