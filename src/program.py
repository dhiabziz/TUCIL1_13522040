from inputtxt import *
import random
from util import *
import numpy

print('Selamat datang di game Saiberpang 2045 Breach Protokol!')
opsi = int(input('Kamu mau upload file txt atau atau generate otomatis nih?\nKetik 1 untuk upload file\nKetik 2 untuk otomatis\nPilihanmu: '))
while ((opsi != 1) and (opsi!=2)):
    opsi = int(input('Ketik 1 untuk upload file\nKetik 2 untuk otomatis\nPilihanmu: '))

if (opsi == 1):
    path = input('Masukkan path filemu: ')
    bacafile("C:/Users/ACER/Downloads/input.txt")
    
elif (opsi == 2):
    n_token = int(input("Masukkan jumlah token unik: "))
    token = input("Masukkan token: ")
    #ukuran_buffer = int(input("Masukkan ukuran buffer: "))
    #w = int(input("Masukkan jumlah kolom matriks: "))
    #h = int(input("Masukkan jumlah baris matriks: "))
    #n_seq = int(input("Masukkan jumlah sekuens: "))
    #n_max_seq = int(input("Masukkan ukuran maksimal sekuens: "))

    l_token = []
    for x in token.split():
        l_token.append(str(x))
    print(l_token)

    # Membuat matriks
    w = 5
    h = 4
    k = 0
    matrix = []
    for i in range(h):
        temp = []
        for j in range(w):
            x = random.randint(0,n_token-1)
            temp.append(l_token[x])
            k = x
        matrix.append(temp)
    
    print("\n[MATRIKS PERMAINAN]")
    printmatrix(matrix)

    #Membuat sekuens sebanyak n_seq
    #Minimal dua token, maksimal nmaxseq token
    #Hapus
    n_seq = 3
    n_max_seq = 4
    
    isUnique = False
    while (not isUnique): 
        seq = []
        l_points = []
        for i in range(n_seq):
            temp = []
            sum = 0
            # Merandom banyaknya token dalam satu sequence
            x = random.randint(2,n_max_seq)
            for j in range(x):
                y = random.randint(0, n_token-1)
                temp.append(l_token[y])
                sum += y
            seq.append(temp)

            #Merandom poin
            z = random.randint(0,1)
            l_points.append(((x-1)**2)*10 + ((sum//x + z)*5))

        #Menjadikan string
        stringseq = []
        for i in range(n_seq):
            stringseq.append(arrtostring(seq[i]))
        
        #Mengecek apakah sequence sudah unique atau tidak
        isUnique = True
        i = 0
        while(isUnique and i<n_seq):
            j = i+1
            while(isUnique and j<n_seq):
                if(stringseq[i] == stringseq[j]):
                    #Kalau ada yang sama maka ulang loop
                    isUnique = False
                else:
                    j += 1
            i += 1

    #Mengeprint
    print("\n[SEQUENCE PERMAINAN]")
    for i in range(n_seq):
        print("Sequence ke-%d: " %(i+1), end='')
        print(arr_to_string(seq[i]))
        print("Dengan point sebesar: %d\n" %l_points[i])
    
    printmatrix(seq)
    print(stringseq)
    print(l_points)

    print("\nOke! Saatnya memulai permainan!\n")
    
   


   