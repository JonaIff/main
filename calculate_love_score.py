def calculate_love_score(name1,name2):
    name = [name1,name2]
    count_true = 0
    total_true = 0
    count_while = 0

    while count_while <= 1:

        for letter in name[count_while]:
            count_true = 0
            if letter in "True":
                count_true += 1
                print(f"{letter} occurs{count_true} times")
                total_true += 1

            else:
                print(f"{letter} occurs{0} times")
            print(f"Total {total_true}")      
    
             


calculate_love_score("True","Love")
        
        
    
    