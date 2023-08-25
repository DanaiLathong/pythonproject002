#1 ใช้ ,
print ("Hello...",456,'Hi...',True,10+20,"Hey...")
#2 ใช้ + มีข้อแม้ว่าทุกกตัวที่เอามาต่อกันต้องเป็น String
print ("Hello... "+str(456)+' Hi... '+str(True)+' '+str(10+20)+" Hey...")
#3 ใช้เมธอด format
print ("Hello... {} Hi... {} {} Hey...".format(456,True,20+10))
print ("Hello... {0} Hi... {1} {2} Hey...".format(456,True,20+10)) # index number ในทางโปรแกรมเริ่มจาก 0
#4 ใช้ f-string
print (f"Hello... {456} Hi... {True} {10+20} Hey...")
#5 ใช้ modulo/modulas operator (%) -> %d, %f, %c, %s, ......
print ("Hello... %d Hi... %s %d Hey..." %(456,True,20+10))