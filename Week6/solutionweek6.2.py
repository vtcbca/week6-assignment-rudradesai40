with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    print(file_data[::-1])




with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    total_no_lines = len(file_data.split('.'))
    print(f"Total No Of Lines :: {total_no_lines}")
    print("Total No Of Words :: {}".format(len(file_data.split())))


with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    file_data_list = file_data.split()
    for i in set(file_data_list):
        print(i,end="\t")
    print("\nTotal No Of Unique Word :: {}".format(len(set(file_data_list))))


with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    data_list = []
    for i in file_data.split():
        data_list.append([len(i),i])
    sorted_list = sorted(data_list,reverse=True)
    largest_word_no = sorted_list[0][0]
    smallest_word_no = sorted_list[len(sorted_list)-1][0]
    for i in sorted_list:
        if i[0] == largest_word_no:
            print('Largest Word  :: {}'.format(i[1]))
        elif i[0] == smallest_word_no:
            print("Smallest Word :: {}".format(i[1]))
    

with open('Python.txt','r') as file_read,\
     open('Python_upper.txt','w+') as file_write:
    file_data = file_read.read()
    file_write_data = file_data.upper()
    file_write.writelines(file_write_data)

with open('Python_upper.txt','r') as file_read:
    file_data = file_read.read()
    print(file_data)
