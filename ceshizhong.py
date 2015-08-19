listty = [ 0 for n in range(100)]
n = input("jigeshuju: ")
for i in range(n):
    y = "shuru di" + str(i+1) + "geshu:"
    numty = input(y)
    listty[i] = numty

head = 0
tail = n
listjiemi = []
while head != tail:
    listjiemi.append(listty[head])
    head += 1
    listty[tail]=listty[head]
    tail += 1
    head += 1
print listty
print listjiemi
