x = input('Please enter a number:')
theMainList = []
primeList = [2,3]
wasAdded = False
for i in range(4,int(x)):
    for j in primeList:
        if i%j==0:
            theMainList.append(i)
            wasAdded = True
    if wasAdded == False:
        primeList.append(i)
    wasAdded = False

print('************** The Prime numbers List ******************')    
print(primeList)
print('************** The Main numbers List ******************') 
print(theMainList)