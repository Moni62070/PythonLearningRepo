sentence=(input("Enter a sentence :"))
words=sentence.split()
for i in words:
    average=sum(map(len,words))/float(len(words))
    print(average)
