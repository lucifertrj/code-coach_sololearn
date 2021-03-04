def numeral(num,n):
    nonum=dict()
    for i in n:
        nonum[str(i)]=num[i]
    return(nonum)
num=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
n=range(0,11)
nonumeral=numeral(num,n) #dict is returned and assigned to nonumeral
data=input('').split()
new_data=[]
for word in data:
    if word in nonumeral.keys():
        word=nonumeral[word]
    new_data.append(word)
print(' '.join(new_data))

