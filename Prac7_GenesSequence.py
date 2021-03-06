file=open("genes.txt","r")
r=file.read()
size=len(r)
score_A=0
score_C=0
score_T=0
score_G=0
for i in range(size):
    if(r[i]=='A'):
        score_A+=1
    elif (r[i]=='C'):
        score_C+=1
    elif (r[i]=='T'):
        score_T+=1
    elif (r[i]=='G'):
        score_G+=1
print("score of A is ",score_A)
print("score of C is ",score_C)
print("score of T is ",score_T)
print("score of G is ",score_G)


#OUTPUT

'''

input :: CAACTCCGGAGCCATGGCCTGGCTCTTGCTGAGAGCCGTGTTTGAAGGGACGGTTAGCT

output ::
score of A is  10
score of C is  16
score of T is  14
score of G is  20

'''
