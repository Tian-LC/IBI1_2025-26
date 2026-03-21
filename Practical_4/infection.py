#initial infectors = 5 (or inputted data)
#infect rate = 0.4 (or inputted data)
#days = 0
#while infectors < 91:
#    days plus one
#    new infectors = infectors one day ago * infect rate
#    print(new infectors)
#    infectors = new infectors + infectors one day ago
#print(days)


infect_rate = float(input("Please enter the infect_rate:"))
total_infector = int(input("Please enter the initial infectors number:"))
count = 0
while total_infector < 91:  
    count+=1 
    new_infectors = total_infector * infect_rate
    total_infector = new_infectors + total_infector
    if total_infector >=91:
        total_infector = 91 #if total_infector number is more than the students' number of the whole class, let it equals 91(the students' number of the shole class)
        print("day", count, ":", total_infector, "students are totally infected")
        break
    else:
        print("day", count, ":", total_infector, "students are totally infected")
print(count,"days")
