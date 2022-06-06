import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
print("\n\n")
print("If we change some values of the original lists")
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)

print("\n\n")
print("If the old list is just a simple list:")
old_list = [1,2,3,4,5]
new_list = copy.copy(old_list)

old_list.append(7)
print("Old list:", old_list)
print("New list:", new_list)

print("\n\n")
print("If the change an element of the old list:")
old_list[4]=63
print("Old list:", old_list)
print("New list:", new_list)

