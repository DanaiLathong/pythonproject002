#รับค่า/ป้อนทางแป้นพิมพ์ *** ใช้ฟังก์ชั่น input() โดยสิ่งที่ป้อนทั้งหมดเป็น string ***

#ตัวแปร variable เป็น identifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม ข้อมูลที่เก็บอยู่ใน RAM
#identifier คือ  ชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ')
print('-------------------------------------')
stdAge =2023 - int(stdYearBorn) #ต้องแปลง string เป็น number -> int( ), float6519410022( ) 
print(f"ยินดีต้อนรับ {std_id} ชือ {std_name}")
print (f'ปีเกิด {stdYearBorn} อายุ {stdAge}')

print('-------------------------------------')
print("ยินดีต้อนรับ ",(std_id),'ชื่อ ',(std_name) )
print('ปีเกิด ' ,(stdYearBorn) ,'อายุ ', (stdAge))
print('-------------------------------------')
print('ยินดีต้อนรับ '+str(std_id)+'ชื่อ '+str(std_name))
print('ปีเกิด '+str(stdYearBorn)+'อายุ '+str(stdAge))
print('-------------------------------------')
print("ยินดีต้อนรับ {0} ชื่อ {1} ".format(std_id,std_name))
print("ปีเกิด {0} อายุ {1}".format(stdYearBorn,stdAge))
print('-------------------------------------')
print("ยินดีต้อนรับ %s ชื่อ %s"%(std_id,std_name))
print("ปีเกิด %s อายุ %s"%(stdYearBorn,stdAge))