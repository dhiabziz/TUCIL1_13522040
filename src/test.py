from util import *
def hitung(l_seq, string_seq, l_points):
    sum = 0
    string_l_seq = arrtostring(l_seq)
    for i in range(len(string_seq)):
        if(string_seq[i] in string_l_seq):
            sum += l_points[i]
    return sum

print(arrtostring(["A", 'B', 'C', 'A']))

print(hitung(["A", 'B', 'C', 'A'], ["ABC", "BBB"],[10, 20] ))