l=input('Enter a text:').lower().split()
new=[]
for i in l:
    k=i[1:]+i[0]+'ay'
    new.append(k)
print(' '.join(new))