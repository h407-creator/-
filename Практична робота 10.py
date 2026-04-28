a=[]
fin=open('Книга1.txt','r')
for line in fin:
    a.append(int(line.strip()))
mini=a[0]
maxi=a[0]
for i in range(len(a)):
    if a[i]>maxi:
        maxi=a[i]
    if a[i]<mini:
        mini=a[i]
print(mini,"- найменше значення")
print(maxi,"- найбільше значення")
