import datetime 
now = datetime.datetime.now ()


time = [now.day, now.month, now.year]
time_new = [now.day, now.month, now.year]
i=0

while True:
     time_new[0] += 7
     if (time_new[1] == 1 or time_new[1] == 3 or time_new[1] == 5 or time_new[1] == 7 or time_new[1] == 8 or time_new[1] == 10 or time_new[1] == 12) and time_new[0] > 31:
      time_new[0] -= 31
      time_new[1] += 1
     if (time_new[1] == 4 or time_new[1] == 6 or time_new[1] == 9 or time_new[1] == 11) and  time_new[0]  > 30:
      time_new[0] -= 30
      time_new[1] += 1
     if time_new[1] == 2 and time_new[2] % 4 != 0 and time_new[0] > 28:
      time_new[0] -= 28
      time_new[1] += 1
     if time_new[1] == 2 and time_new[2] % 4 == 0 and time_new[0] > 29:
      time_new[0] -= 29
      time_new[1] += 1
     if  time_new[1] > 12:
      time_new[1]  -= 12
      time_new[2]  += 1
     if time_new[2] == time[2] + 10:
       break
     if time_new[0] == time[0]:
        i += 1
        
print "The total times will be", i 
 
     
   