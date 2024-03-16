#creating the empty list
my_list = []

#appending elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting the value 15 in the second position
my_list.insert(1, 15)

#extending the list
my_list.extend([50, 60, 70])

#removing the last element
my_list.pop()

#sorting the list in ascending order
list_sort = sorted(my_list)

#finding and printing the index of 30
index_30 = my_list.index(30)

print(index_30)