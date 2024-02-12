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


    print(buffer_size)
    print(kolom)
    print(baris)
    print(array)
    print(n_seq)
    print(l_points)
    print(seq)
