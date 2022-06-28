# Import modules
import time
import sys

# Create countdown function
def countdown(t):
    while t > 0:
        sys.stdout.write('\rDuration : {}s'.format(t))
        t -= 1
        sys.stdout.flush()
        time.sleep(1)

countdown(10)

#Convert the 0 into a number so we can add scores
score = 0
score = int(score)

#Ask user for their name
name = input("Siapa nama kamu?")
name = name.title()
print("""Hai {}, Selamat Datang ke Kuiz Matematik! 
Kamu diberikan 5 soalan Matematik.
Kamu tidak dibenarkan menggunakan kalkulator. 
Sila masukkan huruf bagi jawapan yang kamu pilih.
Selamat mencuba dan semoga berjaya!""".format(name))

#Soalan1
print("""Berapa jumlah 30 + 40?
A. 60
B. 70 
C. 80 
D. 90""")

answer1 = "B"
response1 = input("Jawapan anda ialah:")

if (response1 != answer1):
    print("Maaf jawapan anda salah!")
else:
    print("Tahniah! " + response1 + " Jawapan anda betul!")
    score = score + 1

print("Skor kamu adalah " + str(score) + " daripada 5")

#Soalan2
print("""Berapakah hasil darab 15 * 6?
A. 60 
B. 70
C. 80 
D. 90""")

answer2 = "D"
response2 =  input("Jawapan anda ialah:")

if (response2 != answer2):
    print("Maaf jawapan anda salah!")
else:
    print("Tahniah! " + response2 + " Jawapan anda betul!")
    score = score + 1

print("Skor kamu adalah " + str(score) + " daripada 5")

#Soalan3
print("""Berapakah hasil tolak 220 - 120?
A. 80 
B. 90
C. 100 
D. 110""")

answer3 = "C"
response3 =  input("Jawapan anda ialah:")

if (response3 != answer3):
    print("Maaf jawapan anda salah!")
else:
    print("Tahniah! " + response3 + " Jawapan anda betul!")
    score = score + 1

print("Skor kamu adalah " + str(score) + " daripada 5")


#Soalan4
print("""Berapakah hasil bahagi 280 / 4?
A. 60 
B. 70
C. 80 
D. 90""")

answer4 = "B"
response4 =  input("Jawapan anda ialah:")

if (response4 != answer4):
    print("Maaf jawapan anda salah!")
else:
    print("Tahniah! " + response4 + " Jawapan anda betul!")
    score = score + 1

print("Skor kamu adalah " + str(score) + " daripada 5")

#Soalan5
print("""Berapakah hasil bahagi 1100 + 210?
A. 1300 
B. 1310
C. 1320 
D. 1330""")

answer5 = "B"
response5 =  input("Jawapan anda ialah:")

if (response5 != answer5):
    print("Maaf jawapan anda salah!")
else:
    print("Tahniah! " + response5 + " Jawapan anda betul!")
    score = score + 1

print("Skor kamu adalah " + str(score) + " daripada 5")

print("Jumlah keseluruhan anda adalah " + str(score) + " daripada 5")
print("Terima kasih kerana menyertai kuiz ini {}, Semoga berjumpa lagi!".format(name))