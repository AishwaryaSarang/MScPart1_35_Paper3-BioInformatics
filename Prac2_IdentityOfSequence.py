# take 2 sequences from user to calculate identity of sequences

input1 = input("Enter first sequence :: ")
input2 = input("Enter second sequence :: ")

seq1 = list(input1)
seq2 = list(input2)

def gap(a,b):
    if(len(a) == len(b)):
        print()
    else:
        gap_position = int(input("Enter position for gap :: "))
        if(len(a) < len(b)):
            a.insert(gap_position, "-")
            if(len(a) != len(b)):
                gap(a,b)
        else:
            b.insert(gap_position, "-")
            if(len(a) != len(b)):
                gap(a,b)

    return(a,b)

def Calculate_identity(a,b):
    gap(a,b)
    print(a)
    print(b)
    score = 0
    length = len(a)
    total_elements = len(a) * len(b)
    for i in range(0, length):
        for j in range(0, length):
            if(a[i] == b[j]):
                score += 1
    identity = (score/total_elements) * 100
    print("Matching elements score :: ", score)
    print("Identity of teh sequence :: ", identity)

Calculate_identity(seq1, seq2)


#output

''' >>>>>>>    Enter first sequence :: asdfghhh
Enter second sequence :: asdfgh
Enter position for gap :: 3
Enter position for gap :: 4
['a', 's', 'd', 'f', 'g', 'h', 'h', 'h']
['a', 's', 'd', '-', '-', 'f', 'g', 'h']
Matching elements score ::  8
Identity of teh sequence ::  12.5     <<<<<<<< '''
