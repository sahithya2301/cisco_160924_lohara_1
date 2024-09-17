n = input("Enter the words: ")
lis=n.split()
print('List:',lis)
t=tuple(lis)
print('tuple:',t)
with open('qn01_data.txt','w') as data_file:
    data_file.write(f'List: {lis}\n')
    data_file.write(f'tuple: {t}')
with open('qn01_data.txt','r') as data_file:
    line_list = data_file.readline()
    line_tuple = data_file.readline()
    print(line_list)
    print(line_tuple)    
    
