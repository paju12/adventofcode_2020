data = [line.strip() for line in open("inputD5.txt", 'r')]

max_id = 0

for row in data:
    fila_min = 0
    fila_max = 127
    resta = 128
    for i in row[:7]:
        resta = resta/2
        if i == "F":
            fila_max-=resta
        else:
            fila_min+=resta
    
    col_min = 0
    col_max = 7
    resta = 8
    for i in row[7:]:
        resta = resta/2
        if i == "L":
            col_max-=resta
        else:
            col_min+=resta

    id = fila_max*8+col_max
    if (id>max_id): 
        max_id = id

print(int(max_id))
