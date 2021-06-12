age=int(input())
new=0
old=0
for val in data.values():
    if val<age:
        new+=5
    else:
        new+=20
        for val in data.values():
            if val<18:
                old+=5
            else:
                old+=20
                print(int((new-old)/old*100))
