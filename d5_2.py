data = [line.strip() for line in open("inputD5.txt", 'r')]

avion = []

for i in range(128):
    avion.append(["#","#","#","#","#","#","#","#"])

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

    avion[int(fila_max)][int(col_max)] = "X"

for i, fila in enumerate(avion):
    for x, plaza in enumerate(fila):
        if (0 == x == 7):
            continue
        if (plaza == "#" and fila[x-1] == "X" and fila[x+1] == "X") :
            print(f"fila {i} columna {x}")
            print(i*8+x)
            break

    