import random
from util import *
import time

# Variabel Global
final_seq = []
final_points = 0
final_l_loc = []
done = False

# Mengatur format koordinat
def print_final_l_loc():
    global final_l_loc
    for i in range (len(final_l_loc)):
        final_l_loc[i][0] += 1
        final_l_loc[i][1] += 1

        temp = final_l_loc[i][0]
        final_l_loc[i][0] = final_l_loc[i][1]
        final_l_loc[i][1] = temp

        print("%d," % final_l_loc[i][0], end=" ")
        print("%d" % final_l_loc[i][1], end="\n")

# Menghitung point
def hitung(l_seq, string_seq, l_points):
    sum = 0
    string_l_seq = arrtostring(l_seq)
    for i in range(len(string_seq)):
        if(string_seq[i] in string_l_seq):
            sum += l_points[i]
    return sum

# Fungsi Bruteforce
def solver(matrix, h, w, temp_seq, max_buffer, temp_l_loc, string_seq, l_points, curr_loc, nowvertical):
    global final_seq # List penampung sekuens final
    global final_points # Point maksimal 
    global final_l_loc # Koordinat dari tiap sekuens final
    global done # Ketika setiap sekuens sudah ditemukan dalam satu rangkaian buffer sehingga diraih point maksimum, program berhenti

    max_points = 0 
    for i in range(len(l_points)):
        max_points += l_points[i]

    if not done:
        if(len(temp_seq) == max_buffer): #Basis rekursi. Jika buffer penuh maka stop, hitung point, atau backtracking
        # Ketika panjang temp_seq == max buffer
            temp_point = hitung(temp_seq, string_seq, l_points)
            if(temp_point>final_points):
                final_points = temp_point
                final_seq.clear()
                final_seq.extend(temp_seq)
                final_l_loc.clear()
                final_l_loc.extend(temp_l_loc)
                #print("points: ",final_points)
                #print("final seq", final_seq)
                if (final_points == max_points):
                    done = True
        else:
            if(nowvertical == False):
                for i in range (w):
                    new_loc = [0,0]
                    new_loc[0] = curr_loc[0]
                    new_loc[1] = curr_loc[1]
                    new_loc[1] = i
                    if(matrix[new_loc[0]][new_loc[1]] == '??'):
                        continue
                    temp_l_loc.append(new_loc)
                    temp_seq.append(matrix[new_loc[0]][new_loc[1]])
                    matrix[new_loc[0]][new_loc[1]] = '??'
                    #print("Matriks: ", matrix)
                    #print("Temp seq: ", temp_seq)
                    #print("Temp l loc", temp_l_loc)
                    solver(matrix, h, w, temp_seq, max_buffer, temp_l_loc, string_seq, l_points, new_loc, True)
                    matrix[temp_l_loc[len(temp_l_loc)-1][0]][temp_l_loc[len(temp_l_loc)-1][1]]= temp_seq[len(temp_seq)-1]
                    temp_seq.pop(len(temp_seq) - 1)
                    temp_l_loc.pop(len(temp_l_loc) - 1)
                    #print("Matriks: ", matrix)
                    #print("Temp seq: ", temp_seq)
                    #print("Temp l loc", temp_l_loc)
            else:
                for i in range (h):
                    new_loc = [0,0]
                    new_loc[0] = curr_loc[0]
                    new_loc[1] = curr_loc[1]                    
                    new_loc[0] = i
                    #print("New loc", new_loc)
                    if(matrix[new_loc[0]][new_loc[1]] == '??'):
                        continue
                    temp_l_loc.append(new_loc)
                    temp_seq.append(matrix[new_loc[0]][new_loc[1]])
                    matrix[new_loc[0]][new_loc[1]] = '??'
                    #print("Matriks: ", matrix)
                    #print("Temp seq: ", temp_seq)
                    #print("Temp l loc", temp_l_loc)
                    solver(matrix, h, w, temp_seq, max_buffer, temp_l_loc, string_seq, l_points, new_loc, False)
                    #print("Matriks: ", matrix)
                    #print("Temp seq: ", temp_seq)
                    #print("Temp l loc", temp_l_loc)
                    matrix[temp_l_loc[len(temp_l_loc)-1][0]][temp_l_loc[len(temp_l_loc)-1][1]]= temp_seq[len(temp_seq)-1]
                    temp_seq.pop(len(temp_seq) - 1)
                    temp_l_loc.pop(len(temp_l_loc) - 1)

# Membaca file dari path
def bacafile(pathfile):
    file = open(pathfile, "r")

    #Bilangan pertama adalah buffer size
    buffer_size = int(next(file).split()[0])

    #Bilangan kedua dan ketiga adalah kolom dan baris
    kolom, baris = [int(x) for x in next(file).split()]

    #Matrix
    array = []
    for i in range(baris):
        line = file.readline()
        temp = []
        for x in line.split():
            temp.append(str(x))
        array.append(temp)

    #Number of sequences
    n_seq = int(next(file).split()[0])

    #Seq and points
    l_points = []
    seq = []
    for i in range(n_seq):
        line = file.readline()
        temp = []
        for x in line.split():
            temp.append(str(x))
        seq.append(temp)
        l_points.append(int(next(file).split()[0]))
    
    #Menjadikan string 
    stringseq = []
    for i in range(n_seq):
        stringseq.append(arrtostring(seq[i]))

    return buffer_size, kolom, baris, array, stringseq, l_points


# Program Utama
print('Selamat datang di game Saiberpang 2045 Breach Protokol!')
opsi = int(input('Kamu mau upload file txt atau atau generate otomatis nih?\nKetik 1 untuk upload file\nKetik 2 untuk otomatis\nPilihanmu: '))
while ((opsi != 1) and (opsi!=2)):
    opsi = int(input('Ketik 1 untuk upload file\nKetik 2 untuk otomatis\nPilihanmu: '))

if (opsi == 1):
    print('\nYuk masukkan path filemu!')
    print("Contoh path: C:/Users/ACER/Downloads/input.txt")
    path = input("Path file mu: ")

    buffer_size, w, h, m, stringseq, l_points = bacafile(path)

    start = time.process_time()
    solver(m, h, w, [], buffer_size, [], stringseq, l_points, [0,0], False)
    duration = time.process_time() - start

    if(final_points == 0):
        print("Maaf ya ternyata gaada solusinya hehe")
        print("\nDurasi: %s s" %str(duration))

    else:
        print("Point maksimum:", final_points)
        print("Buffer optimum:", arr_to_string(final_seq))
        print("Jalur: ")
        print_final_l_loc() 
        print("\nDurasi: %s s" %str(duration))
    
    tulistxt(final_points, final_seq, final_l_loc, duration)

    
elif (opsi == 2):
    n_token = int(input("Masukkan jumlah token unik: "))
    token = input("Masukkan token: ")
    ukuran_buffer = int(input("Masukkan ukuran buffer: "))
    w = int(input("Masukkan jumlah kolom matriks: "))
    h = int(input("Masukkan jumlah baris matriks: "))
    n_seq = int(input("Masukkan jumlah sekuens: "))
    n_max_seq = int(input("Masukkan ukuran maksimal sekuens: "))

    l_token = []
    for x in token.split():
        l_token.append(str(x))
    print(l_token)

    # Membuat matriks
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

    print("Oke! Saatnya memulai permainan!\n")    
    
    mulai = time.process_time()
    solver(matrix, h, w, [], ukuran_buffer, [], stringseq, l_points, [0,0], False)
    durasi = time.process_time() - mulai

    if(final_points == 0):
        print("Maaf ya ternyata gaada solusinya hehe")
        print("\nDurasi: %s s" %str(durasi))
    else:
        print("Point maksimum:", final_points)
        print("Buffer optimum:", arr_to_string(final_seq))
        print("Jalur: ")
        print_final_l_loc() 
        print("\nDurasi: %s s" %str(durasi))

    tulistxt(final_points, final_seq, final_l_loc, durasi)





   