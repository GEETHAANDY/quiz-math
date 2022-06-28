#Convert the 0 into a number so we can add scores
score = 0
score = int(score)

#Ask user for their name
name = input("Sila masukkan nama anda?")
name = name.title()
print("""Hai {}, Selamat Datang ke Kuiz Matematik! \n
!!ARAHAN!!
Anda diberikan 5 soalan Matematik mudah.
Anda tidak dibenarkan menggunakan kalkulator.
Anda dikehendaki untuk menjawab setiap mengikut masa yang diberikan.
Sila masukkan jawapan yang anda pilih dengan HURUF BESAR.
Selamat mencuba dan semoga berjaya!\n""".format(name))

#Soalan1
print("""SOALAN 1: Berapa jumlah 30 + 40?
A. 60
B. 70 
C. 80 
D. 90\n""")

answer1 = "B"

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

countdown(5)

response1 = input("Jawapan anda ialah:")

if (response1 != answer1):
    print("Maaf jawapan anda salah!\n")
else:
    print("Tahniah! " + response1 + " Jawapan anda betul!\n")
    score = score + 1

print("Skor anda adalah " + str(score) + " daripada 5")
print("Terus ke soalan seterusnya\n")

#Soalan2
print("""SOALAN 2: Berapakah hasil darab 15 * 6?
A. 60 
B. 70
C. 80 
D. 90\n""")

answer2 = "D"

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    
countdown(5)

response2 =  input("Jawapan anda ialah:")

if (response2 != answer2):
    print("Maaf jawapan anda salah!\n")
else:
    print("Tahniah! " + response2 + " Jawapan anda betul!\n")
    score = score + 1

print("Skor anda adalah " + str(score) + " daripada 5")
print("Terus ke soalan seterusnya\n")

#Soalan3
print("""SOALAN 3: Berapakah hasil tolak 220 - 120?
A. 80 
B. 90
C. 100 
D. 110\n""")

answer3 = "C"

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    
countdown(5)

response3 =  input("Jawapan anda ialah:")

if (response3 != answer3):
    print("Maaf jawapan anda salah!\n")
else:
    print("Tahniah! " + response3 + " Jawapan anda betul!\n")
    score = score + 1

print("Skor anda adalah " + str(score) + " daripada 5")
print("Terus ke soalan seterusnya\n")

#Soalan4
print("""SOALAN 4: Berapakah hasil bahagi 280 / 4?
A. 60 
B. 70
C. 80 
D. 90\n""")

answer4 = "B"

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    
countdown(5)

response4 =  input("Jawapan anda ialah:")

if (response4 != answer4):
    print("Maaf jawapan anda salah!\n")
else:
    print("Tahniah! " + response4 + " Jawapan anda betul!\n")
    score = score + 1

print("Skor anda adalah " + str(score) + " daripada 5")
print("Terus ke soalan seterusnya\n")

#Soalan5
print("""SOALAN 5: Berapakah hasil tolak 2400 - 1100?
A. 1300 
B. 1310
C. 1320 
D. 1330\n""")

answer5 = "A"

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    
countdown(5)

response5 =  input("Jawapan anda ialah:")

if (response5 != answer5):
    print("Maaf jawapan anda salah!\n")
else:
    print("Tahniah! " + response5 + " Jawapan anda betul!\n")
    score = score + 1

print("Skor anda adalah " + str(score) + " daripada 5")
print("Jumlah keseluruhan anda adalah " + str(score) + " daripada 5\n")
print("-Soalan tamat-\n")
print("Terima kasih kerana menyertai kuiz ini {}, Semoga berjumpa lagi!".format(name))
# grinning face
print("\U0001f600")