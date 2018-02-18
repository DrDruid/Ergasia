import datetime
now = datetime.datetime.now ()
a = input("Give month in number")
b = input("Give year in number")
time = [now.day, now.month, now.year]
time_new = [1, a, b]
i = input("Give number from 1 to 7 for days of the week starting from Sunday to Saturday for today")
if (time_new[1] > time[1] or time_new[2] > time[2]  or (time_new[1] > time[1] and time_new[2] == time[2] ) or (time_new[1] > time[1] and time_new[2] == time[2])):
 while True:   
    time[0] += 1
    i += 1
    if (i == 8):
     i = 1 
    if ((time[1] == 1 or time[1] == 3 or time[1] == 5 or time[1] == 7 or time[1] == 8 or time[1] == 10 or time[1] == 12) and time[0] == 31) :
      time[0] -= 31
      time[1] += 1
    if ((time[1] == 4 or time[1] == 6 or time[1] == 9 or time[1] == 11) and  time[0]  == 30):
      time[0] -= 30
      time[1] += 1
    if (time[1] == 2 and time[2] % 4 != 0 and time[0] == 28 ):
      time[0] -= 28
      time[1] += 1
    if (time[1] == 2 and time[2] % 4 == 0 and time[0] == 29) :
      time[0] -= 29
      time[1] += 1
    if  (time[1] == 12):
      time[1]  -= 12
      time[2]  += 1
    if (time[0] == time_new[0] and time[1] == time_new[1] and time[2] == time_new[2]):
      break
else:
 while True:   
    time[0] -= 1
    i -= 1
    if (i == 0):
     i = 7 
    if ((time[1] == 1 or time[1] == 3 or time[1] == 5 or time[1] == 7 or time[1] == 8 or time[1] == 10 or time[1] == 12) and time[0] == 0):
      time[0] += 31
      time[1] -= 1
    if ((time[1] == 4 or time[1] == 6 or time[1] == 9 or time[1] == 11) and  time[0]  == 0):
      time[0] += 30
      time[1] -= 1
    if (time[1] == 2 and time[2] % 4 != 0 and time[0] == 0) :
      time[0] += 28
      time[1] -= 1
    if (time[1] == 2 and time[2] % 4 == 0 and time[0] == 0 ):
      time[0] += 29
      time[1] -= 1
    if  (time[1] ==0):
      time[1]  += 12
      time[2]  -= 1
    if (time[0] == time_new[0] and time[1] == time_new[1] and time[2] == time_new[2]):
      break
if (time_new[1] == 1):
 print "  ""January", time_new[2]
if (time_new[1] == 2):
 print "  ""February", time_new[2] 
if (time_new[1] == 3):
 print "  ""March", time_new[2]
if (time_new[1] == 4):
 print "  ""April", time_new[2]
if (time_new[1] == 5):
 print "  ""May", time_new[2]
if (time_new[1] == 6):
 print "  ""June", time_new[2]
if (time_new[1] == 7):
 print "  ""Jule", time_new[2]
if (time_new[1] == 8):
 print "  ""August", time_new[2]
if (time_new[1] == 9):
 print "  ""September", time_new[2]
if (time_new[1] == 10):
 print "  ""Octomber", time_new[2]
if (time_new[1] == 11):
 print "  ""November", time_new[2]
if (time_new[1] == 12):
 print "  ""December", time_new[2]
print "S\tM\tT\tW\tT\tF\tS"
if (time[1] == 1 or time[1] == 3 or time[1] == 5 or time[1] == 7 or time[1] == 8 or time[1] == 10 or time[1] == 12):
 n = 31
elif (time[1] == 4 or time[1] == 6 or time[1] == 9 or time[1] == 11):
 n = 30
elif (time[1] == 2 and time[2] % 4 != 0 ):
 n = 28
else:
 n = 29
if (n == 31):
 if (i == 1):
  print "1\t2\t\t4\t5\t6\t7"
  print "8\t9\t10\t11\t12\t13\t14"
  print "15\t16\t17\t18\t19\t20\t21"
  print "22\t23\t24\t25\t26\t27\t28"
  print "29\t30\t31"
 elif ( i == 2):
  print "\t1\t2\t3\t4\t5\t6"
  print "7\t8\t9\t10\t11\t12\t13"
  print "14\t15\t16\t17\t18\t19\t20"
  print "21\t22\t23\t24\t25\t26\t27"
  print  "28\t29\t30\t31" 
 elif ( i == 3):
  print  "\t\t1\t2\t3\t4\t5"
  print   "6\t7\t8\t9\t10\t11t\t12"
  print  "13\t14\t15\t16\t17\t18\t19"
  print  "20\t21\t22\t23\t24\t25\t26"
  print  "27\t28\t29\t30\t31"         
 elif ( i == 4):
  print  "\t\t\t1\t2\t3\t4"
  print  "5\t6\t7\t8\t9\t10\11"
  print  "12\t13\t14\t15\t16\t17\t18"
  print  "19\t20\t21\t22\t23\t24\t25"
  print  "26\t27\t28\t29\t30\t31"
 elif ( i == 5):
  print  "\t\t\t\t1\t2\t3"
  print  "4\t5\t6\t7\t8\t9\t10"
  print  "11\t12\t13\t14\t15\t16\t17"
  print  "18\t19\t20\t21\t22\t23\t24"
  print  "25\t26\t27\t28\t29\t30\t31"
 elif ( i == 6):
  print  "\t\t\t\t\t1\t2"
  print  "3\t4\t5\t6\t7\t8\t9"
  print  "10\t11\t12\t13\t14\t15\t16"
  print  "17\t18\t19\t20\t21\t22\t23"
  print  "24\t25\t26\t27\t28\t29\t30"
  print  31
 elif ( i == 7):
  print  "\t\t\t\t\t\t1"
  print  "2\t3\t4\t5\t6\t7\t8"
  print  "9\t10\t11\t12\t13\t14t\15"
  print  "16\t17\t18\t19\t20\t21\t22"
  print  "23\t24\t25\t26\t27\t28\t29"
  print  "30\t31"
elif (n == 30):
 if (i == 1):
  print "1\t2\t\t4\t5\t6\t7"
  print "8\t9\t10\t11\t12\t13\t14"
  print "15\t16\t17\t18\t19\t20\t21"
  print "22\t23\t24\t25\t26\t27\t28"
  print "29\t30"
 elif ( i == 2):
  print "\t1\t2\t3\t4\t5\t6"
  print "7\t8\t9\t10\t11\t12\t13"
  print "14\t15\t16\t17\t18\t19\t20"
  print "21\t22\t23\t24\t25\t26\t27"
  print  "28\t29\t30" 
 elif ( i == 3):
  print  "\t\t1\t2\t3\t4\t5"
  print   "6\t7\t8\t9\t10\t11t\t12"
  print  "13\t14\t15\t16\t17\t18\t19"
  print  "20\t21\t22\t23\t24\t25\t26"
  print  "27\t28\t29\t30"         
 elif ( i == 4):
  print  "\t\t\t1\t2\t3\t4"
  print  "5\t6\t7\t8\t9\t10\11"
  print  "12\t13\t14\t15\t16\t17\t18"
  print  "19\t20\t21\t22\t23\t24\t25"
  print  "26\t27\t28\t29\t30"
 elif ( i == 5):
  print  "\t\t\t\t1\t2\t3"
  print  "4\t5\t6\t7\t8\t9\t10"
  print  "11\t12\t13\t14\t15\t16\t17"
  print  "18\t19\t20\t21\t22\t23\t24"
  print  "25\t26\t27\t28\t29\t30"
 elif ( i == 6):
  print  "\t\t\t\t\t1\t2"
  print  "3\t4\t5\t6\t7\t8\t9"
  print  "10\t11\t12\t13\t14\t15\t16"
  print  "17\t18\t19\t20\t21\t22\t23"
  print  "24\t25\t26\t27\t28\t29\t30"
 elif ( i == 7):
  print  "\t\t\t\t\t\t1"
  print  "2\t3\t4\t5\t6\t7\t8"
  print  "9\t10\t11\t12\t13\t14t\15"
  print  "16\t17\t18\t19\t20\t21\t22"
  print  "23\t24\t25\t26\t27\t28\t29"
  print  30
elif (n == 28):
 if (i == 1):
  print "1\t2\t\t4\t5\t6\t7"
  print "8\t9\t10\t11\t12\t13\t14"
  print "15\t16\t17\t18\t19\t20\t21"
  print "22\t23\t24\t25\t26\t27\t28"
 elif ( i == 2):
  print "\t1\t2\t3\t4\t5\t6"
  print "7\t8\t9\t10\t11\t12\t13"
  print "14\t15\t16\t17\t18\t19\t20"
  print "21\t22\t23\t24\t25\t26\t27"
  print  28 
 elif ( i == 3):
  print  "\t\t1\t2\t3\t4\t5"
  print   "6\t7\t8\t9\t10\t11t\t12"
  print  "13\t14\t15\t16\t17\t18\t19"
  print  "20\t21\t22\t23\t24\t25\t26"
  print  "27\t28"         
 elif ( i == 4):
  print  "\t\t\t1\t2\t3\t4"
  print  "5\t6\t7\t8\t9\t10\11"
  print  "12\t13\t14\t15\t16\t17\t18"
  print  "19\t20\t21\t22\t23\t24\t25"
  print  "26\t27\t28"
 elif ( i == 5):
  print  "\t\t\t\t1\t2\t3"
  print  "4\t5\t6\t7\t8\t9\t10"
  print  "11\t12\t13\t14\t15\t16\t17"
  print  "18\t19\t20\t21\t22\t23\t24"
  print  "25\t26\t27\t28"
 elif ( i == 6):
  print  "\t\t\t\t\t1\t2"
  print  "3\t4\t5\t6\t7\t8\t9"
  print  "10\t11\t12\t13\t14\t15\t16"
  print  "17\t18\t19\t20\t21\t22\t23"
  print  "24\t25\t26\t27\t28"
  print  31
 elif ( i == 7):
  print  "\t\t\t\t\t\t1"
  print  "2\t3\t4\t5\t6\t7\t8"
  print  "9\t10\t11\t12\t13\t14t\15"
  print  "16\t17\t18\t19\t20\t21\t22"
  print  "23\t24\t25\t26\t27\t28"
else:
 if (i == 1):
  print "1\t2\t\t4\t5\t6\t7"
  print "8\t9\t10\t11\t12\t13\t14"
  print "15\t16\t17\t18\t19\t20\t21"
  print "22\t23\t24\t25\t26\t27\t28"
  print 29
 elif ( i == 2):
  print "\t1\t2\t3\t4\t5\t6"
  print "7\t8\t9\t10\t11\t12\t13"
  print "14\t15\t16\t17\t18\t19\t20"
  print "21\t22\t23\t24\t25\t26\t27"
  print  "28\t29" 
 elif ( i == 3):
  print  "\t\t1\t2\t3\t4\t5"
  print   "6\t7\t8\t9\t10\t11t\t12"
  print  "13\t14\t15\t16\t17\t18\t19"
  print  "20\t21\t22\t23\t24\t25\t26"
  print  "27\t28\t29"         
 elif ( i == 4):
  print  "\t\t\t1\t2\t3\t4"
  print  "5\t6\t7\t8\t9\t10\11"
  print  "12\t13\t14\t15\t16\t17\t18"
  print  "19\t20\t21\t22\t23\t24\t25"
  print  "26\t27\t28\t29"
 elif ( i == 5):
  print  "\t\t\t\t1\t2\t3"
  print  "4\t5\t6\t7\t8\t9\t10"
  print  "11\t12\t13\t14\t15\t16\t17"
  print  "18\t19\t20\t21\t22\t23\t24"
  print  "25\t26\t27\t28\t29"
 elif ( i == 6):
  print  "\t\t\t\t\t1\t2"
  print  "3\t4\t5\t6\t7\t8\t9"
  print  "10\t11\t12\t13\t14\t15\t16"
  print  "17\t18\t19\t20\t21\t22\t23"
  print  "24\t25\t26\t27\t28\t29"
  print  31
 elif ( i == 7):
  print  "\t\t\t\t\t\t1"
  print  "2\t3\t4\t5\t6\t7\t8"
  print  "9\t10\t11\t12\t13\t14t\15"
  print  "16\t17\t18\t19\t20\t21\t22"
  print  "23\t24\t25\t26\t27\t28\t29"  