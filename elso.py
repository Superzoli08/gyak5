elso = int(input("Add meg az első oldal hosszát: "))
maso = int(input("Add meg a második oldal hosszát: "))
harm = int(input("Add meg a harmadik oldal hosszát: "))
# 3! = 1*2*3
if elso + maso > harm and elso + harm > maso and maso + harm > elso:
    print("A megadott szakaszok alkothatnak háromszöget.")
else:
    print("A megadott szakaszok nem alkothatnak háromszöget.")

