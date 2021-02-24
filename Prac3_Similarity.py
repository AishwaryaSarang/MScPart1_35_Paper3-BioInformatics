# take 2 sequences from user to calculate similarity of sequences

input1 = input("Enter first sequence :: ")
input2 = input("Enter second sequence :: ")

seq1 = list(input1)
seq2 = list(input2)

count_of_similar_elements = int(input("How many elements to pass for similarity condition?"))

similarities = []
for i in range(0, count_of_similar_elements):
    element = input("Enter an element :: ")
    count_of_similar_to = int(input("How many elements it is similar to?"))
    similarities.append([])
    similarities[i].append(element)

    for j in range(0, count_of_similar_to):
        similar_to = input("What is it similar to?")
        similarities[i].append(similar_to)

def Calculate_similarity(a,b,c):
    print(a)
    print(b)
    print(c)
    
    score = 0
    length = len(a)
    for i in range(0, length):
        for j in range(0, len(c)):
            if(a[i] in c[j] and b[i] in c[j] and a[i] != b[i]):
                score += 1
    similarity = (score/length) * 100
    print("Matching elements score :: ", score)
    print("Similarity of the sequence :: ", similarity, "%")

Calculate_similarity(seq1, seq2, similarities)


#output

""" >>>

Enter first sequence :: asdfgggh
Enter second sequence :: assdfghh
How many elements to pass for similarity condition?3
Enter an element :: a
How many elements it is similar to?1
What is it similar to?f
Enter an element :: h
How many elements it is similar to?1
What is it similar to?g
Enter an element :: s
How many elements it is similar to?1
What is it similar to?d
['a', 's', 'd', 'f', 'g', 'g', 'g', 'h']
['a', 's', 's', 'd', 'f', 'g', 'h', 'h']
[['a', 'f'], ['h', 'g'], ['s', 'd']]
Matching elements score ::  2
Similarity of the sequence ::  25.0 %

<<< """
