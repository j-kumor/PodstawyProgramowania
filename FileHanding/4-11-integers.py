def calculate_powers():
    with open('powers.txt', 'w') as file:
        for i in range(1, 101):
            second_power = i ** 2
            third_power = i ** 3 
            
            result = f"{i},{second_power},{third_power}"
            
            print(result)
            
            file.write(result + '\n')

calculate_powers()