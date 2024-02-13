import sys

def printmatrix(matrix):
    for i in matrix:
        print(' '.join(map(str, i)))

def arrtostring(arr):
    return (''.join(map(str, arr)))

def arr_to_string(arr):
    return (' '.join(map(str, arr)))

def steptoparagraph(step):
    text = ""
    for i in range (len(step)):
        text += str(step[i][0])
        text += ", "
        text += str(step[i][1])
        text += "\n"
    return text

def tulistxt(point, seq, step, duration):
    simpan = input("Apakah ingin menyimpan solusi? (y/n): ")
    if (simpan == "Y") or (simpan == "y"):
        print("\nYuk masukkan nama file!\nContoh: solusi.txt")
        nama_file = input("Ketik nama file: ")
        with open(nama_file, "w") as file:
            if(point== 0):
                file.write(str(point) + "\n" + str(duration) + " s")
            else:
                file.write(str(point) + "\n" + arr_to_string(seq) + "\n" + steptoparagraph(step) + "\n" + str(duration) + " s")

        print("\nFile berhasil dibuat!")
    else:
        print("Sip! Sampai jumpa!")
        sys.exit()
