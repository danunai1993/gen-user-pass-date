import names, random, string

words = [
            "manste","noxze","ssad","medsw","lovex","loxsz","meyous","amsazte","sdrsd","opesee",
            "gorsd","messer","lnwst","tomsa","goodstr","saddss","eieisa","kuyria","noiza","newop",
            "suppua","appeal","apply","argument","artist","assistant","attempt","beat","beach","behavior",
            "capability","career","ceiling","chance","characterize","chief","chapter","clinic","colleague",
            "concentrate","course","darkness","desert","devote","device"
        ]
months = [ "January","Fabruary","March","April","May","June","July","August","September","October","November","December"]
passwords = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(14))
        
word = random.choice(words)             #สุ่มคำ
getname = names.get_first_name()+"xz"   #สร้างชื่อ
getlast = names.get_last_name()+"er"
day = random.randint(0,28)              #สุ่มวันเกิด
month = random.choice(months) 
year = random.randint(1990,2000)        #สุ่มปีเกิด
password = passwords                    #สุ่มรหัส
format = getname+word+str(day)


print(getname)
print(getlast)
print(day)

print(format)
print(password)

txt = open("user.txt","a")
user = format + " || " + password + " || " + str(day) + "/" + month + "/" + str(year) + "\n"
txt.write(user)
print(user)
txt.close()


