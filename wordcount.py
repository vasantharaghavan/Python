f =open("/home/vasanth/open1.txt")
counts={}
for line in f:
    words=line.split()
    print words
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print counts
