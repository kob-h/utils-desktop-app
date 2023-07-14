while True:
    user_choice = input("Throw the coin and enter head or tail here: ?")
    with open('coins.txt', 'r') as file:
        flip_history = file.readlines()
        flip_history.append(f'{user_choice}\n')
        total = len(flip_history)
        head_count = flip_history.count('head\n')
    with open('coins.txt', 'w') as file:
        file.writelines(flip_history)
    print(f"{head_count / total * 100}%")
    
