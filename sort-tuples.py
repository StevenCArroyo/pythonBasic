list_of_tuples = [(1, 'z'), (2, 'a'), (3, 'b'), (4, 'b', 'c')]

# Sort by the first element of each tuple
sorted_list_by_first = sorted(list_of_tuples)
print(sorted_list_by_first)
# Expected output: [(1, 'z'), (2, 'a'), (3, 'b')]

# Sort by the second element of each tuple
sorted_list_by_second = sorted(list_of_tuples, key=lambda x: x[1])
print(sorted_list_by_second)
# Expected output: [(2, 'a'), (3, 'b'), (1, 'z')]