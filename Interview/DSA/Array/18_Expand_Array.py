import itertools

my_list = ["a2b10"]

my_list = ["".join(x) for _, x in itertools.groupby(my_list[0], key=str.isdigit)]
print type(my_list)

for i in range(0,len(my_list)):
    if i != len(my_list):
        my_list[i] = my_list[i] * int(my_list[i+1])
        del my_list[i+1]
    else:
        break

print ''.join(my_list)