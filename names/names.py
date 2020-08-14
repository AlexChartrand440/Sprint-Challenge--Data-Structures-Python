import time

from binary_search_tree import BSTNode;

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# 64 duplicates in 17.6 seconds

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

aaa = BSTNode(names_1[0]);

for name_1 in names_1:
    aaa.insert(name_1);

for name_2 in names_2:
    if aaa.contains(name_2):
        duplicates.append(name_2);

end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"BST runtime: {end_time - start_time} seconds. {len(duplicates)} duplicates.")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time_2 = time.time()

duplicates_2 = [];

f = open('names_1.txt', 'r')
names_3 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_4 = f.read().split("\n")  # List containing 10000 names
f.close()

for name in names_3:
    if name in names_4:
        duplicates_2.append(name);

end_time_2 = time.time()

# print (f"{len(duplicates_2)} duplicates:\n\n{', '.join(duplicates_2)}\n\n")
print (f"List runtime: {end_time_2 - start_time_2} seconds. {len(duplicates_2)} duplicates.")