import re

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
    for param in passport:
        par = param.split(':')[0]
        val = param.split(':')[1]
        if par == "byr" and 1920<=int(val)<=2002 :
            byr = True
        elif par == "iyr" and 2010<=int(val)<=2020 :
            iyr = True
        elif par == "eyr" and 2020<=int(val)<=2030 :
            eyr = True
        elif par == "hgt" :
            if (val[-2]+val[-1] == "cm" and 150<=int(val[:len(val)-2])<=193) or (val[-2]+val[-1] == "in" and 59<=int(val[:len(val)-2])<=76) :
                hgt = True
        elif par == "hcl" and re.search("^#[0-9a-fA-F]{6}$", val) :
            hcl = True
        elif par == "ecl" and val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] :
            ecl = True
        elif par == "pid" and re.search("^[0-9]{9}$", val):
            pid = True
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid+=1
            

print(valid)
