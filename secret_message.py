import string
user_data = input().lower()
backwards = string.ascii_lowercase[::-1]
back_alpha = ''
for alpha in user_data:
    if alpha == ' ':
        back_alpha+=' '
    else:
        index = string.ascii_lowercase.index(alpha)
        back_alpha+=backwards[index]
print(back_alpha)