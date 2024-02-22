import re
class bealeCodeIterator:

    def __init__(self, keysList, wordslist):
        self.keysList = keysList
        self.wordslist = wordslist

    def __iter__(self):
        self.n = 0
        self.i = self.keysList[self.n]
        return self
    
    def __next__(self):
        for x in range(len(self.wordslist)):
            if x == self.i - 1:
                self.n += 1
                if self.n == len(self.keysList):
                    # print(self.wordslist[x])
                    return self.wordslist[x][0]
                if self.n > len(self.keysList):
                    raise StopIteration
                while self.wordslist[x] == '':
                    # print(self.wordslist[x])
                    x += 1
                print(self.wordslist[x])
                self.i = self.keysList[self.n] 
                return self.wordslist[x][0]
        raise StopIteration

example = bealeCodeIterator([1,5,9],["my","name"
            ,"is"
            ,"yishai"
            ,"and"
            ,"I "
            ,"love"
            ,"to"
            ,"play "
            ,"chess"])


# str = 'I love\n you'
# x= list(re.split(' |\n',str))

# print(x)
keys = [4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100,
30, 10, 26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 633, 27, 70, 77,
45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]
with open('declaration.text', "r") as f:
    lines = ""
    for line in f.readlines():
        lines = lines + line
# input = list(lines.split(' '))
# print(input)
input= list(re.split(' |\n|, |;|:|\n\n',lines))
print(input)

for i in input:
    if i == '':
        input.remove(i)


example2 = bealeCodeIterator(keys, input)
result = ''
for i in example2:
    result += i

print(result.upper())

