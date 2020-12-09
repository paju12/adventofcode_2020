f = open("inputD4.txt","r")

passports = []

i = 0
nuevo = True
for row in f:
    if (row.strip() == "") : 
        i+=1
        nuevo = True
        continue
    if nuevo:
        passports.append([])
        nuevo = False
    args = row.split()
    for arg in args:
        passports[i].append(arg.strip())

f.close()

valid=0
for passport in passports:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    cid = False #no obligatorio
    for param in passport:
        val = param.split(':')[0]
        if val == "byr" :
            byr = True
        elif val == "iyr" :
            iyr = True
        elif val == "eyr" :
            eyr = True
        elif val == "hgt" :
            hgt = True
        elif val == "hcl" :
            hcl = True
        elif val == "ecl" :
            ecl = True
        elif val == "pid" :
            pid = True
        elif val == "cid" :
            cid = True
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid+=1

print(valid)
