import math,string
user_data = input().split(' ')
avg_word = []
for calculate in user_data:
    for check in calculate:
        if check in string.punctuation:
            continue
        else:
            avg_word.append(len(check))

print(math.ceil(sum(avg_word)/len(user_data)))