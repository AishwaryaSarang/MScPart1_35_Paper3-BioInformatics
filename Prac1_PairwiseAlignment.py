# take 2 sequences from user to calculate score

input1 = input("Enter first sequence :: ")
input2 = input("Enter second sequence :: ")

seq1 = list(input1)
seq2 = list(input2)

score = []

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

def Pairwise_alignment(a,b):
    gap(a,b)
    print(a)
    print(b)
    value = 0
    length = len(a)
    for i in range(0, length):
        if(a[i] == b[i]):
            score.append(1)
            value += 1
        else:
            score.append(0)
    print(score)
    print(value)

Pairwise_alignment(seq1, seq2)


#output

#Enter first sequence :: abcvfc
#Enter second sequence :: abbcvf

#['a', 'b', 'c', 'v', 'f', 'c']
#['a', 'b', 'b', 'c', 'v', 'f']
#[1, 1, 0, 0, 0, 0]
#2
            
    
    
