
rows = 5 

# Loop for each row
for i in range(1, rows + 1):
    
    for j in range(rows - i):
        print(" ", end="")
    
    num=1
    for j in range(2*i-1):
        print(num, end="")
        num=num+1
    #  Move to the next line
    print()

for i in range(rows-1,0,-1):
    
    for j in range(rows - i):
        print(" ", end="")
    
    num=1
    for j in range(2*i-1):
        print(num, end="")
        num=num+1
    
    print()
