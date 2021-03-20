def multiple_seq_alignment(list_of_sequences, no_of_columns):
    final_output = []
    
    for col in range(no_of_columns):
        temp = []
        for seq in list_of_sequences:
            temp.append(seq[col])
        
        final_output.append(check_column_values(temp))
    display_output(final_output)


def check_column_values(col_of_seqs):
    d = dict()
    result = 'aS'
    for c in col_of_seqs:
        if  c != '-':
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
    #print(d)
    sorted_d = dict(sorted(d.items(), key = lambda x: (-x[1], x[0])))
    print(sorted_d)
    
    if len(sorted_d) == 1:
        return list(d.keys())[0]
    else:
        first = list(sorted_d.values())[0]
        second = list(sorted_d.values())[1]
        if first > second:
            return (list(sorted_d.keys())[0]).lower()
        elif first == second:
            str = ''
            i = 0
            for element in d.values():
                if first == element:
                    str = str + (list(sorted_d.keys())[(list(sorted_d.values()).index(element))+i]) + '/'
                    i = i + 1
            print('val :: ', str)
            return str[0:-1]

        
def display_output(final_list):
    print(*final_list, sep=' ')

no_of_seq=int(input("Enter the number of sequence :: "))
print("Enter all the sequences below :: ")
seq_list=[]
for _ in range(no_of_seq):
    seq_list.append(list(map(str, input("").split())))
multiple_seq_alignment(seq_list, len(seq_list[0]))


'''

output
Enter the number of sequence :: 6
Enter all the sequences below ::
Y D G A Y - E A L
Y D G - - - E A L
F E G I L V F A L
F D - I L V F A L
F D - I L V Q A L
Y E G A V V Q A L

output >> F/Y d G i l V E/F/Q A L

'''

