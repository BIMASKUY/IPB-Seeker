import os

#Input User Bebas Uppercase/Lowercase Karena Akan Diconvert Ke Lowercase
target = input("Masukkan Nama atau NIM = ").lower()

candidate = []

for root, dirs, files in os.walk("C:\My Apps\Database\FMIPA 59"):
    for nama in files:
        if target in nama.lower():
            candidate.append(os.path.join(root, nama))

if(len(candidate) == 0):
    print("\033[91mError! Not Found\033[0m")
    exit()

print(f'\033[92m{len(candidate)}\033[0m Files Found. Open It? \033[92mY/N/L\033[0m')

# L = List Of Candidate 
user = input("Your Decision = ").lower()

while 'l' in user and user != 'clear':
    if 'l' in user:
        for nama in candidate:
            count = 0
            start = 0
            for idx, huruf in enumerate(nama):
                if count == 4 : start = idx+1
                if huruf == '\\' : count += 1           
            if nama[start:-6][-1] == '_' : print(nama[start:-7]) #jpeg
            else : print(nama[start:-6]) #jpg

    user = input("Your Decision = ").lower()

if('n' not in user and 'y' in user):
    for foto in candidate:
        os.system(f'start "" "{foto}"')

else:
    print("GoodBye!")
