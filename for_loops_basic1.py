for i in range(151):
    print(i)

for i in range(1000):
    if i % 5 == 0:
        print(i)

def coding_dojo():
    for i in range(1,101,1):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

coding_dojo()

odd_total = 0 

for i in range(0, 500001, 2):
    odd_total += i
print(odd_total)

for i in range(2018,0,-4):
    print(i)

lowNum = 2
highNum = 9
mult = 3 
for i in range(2,10):
    if i % 3 == 0:
        print(i)
