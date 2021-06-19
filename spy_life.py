import stringnaruto

def spy_text(text):
    data=[]
    for filter in text:
        if filter not in string.punctuation and filter not in string.digits:
            data.append(filter)
        else:
            continue
    return(''.join(data))
    
data=input('')
result = spy_text(data)
print(result[::-1])