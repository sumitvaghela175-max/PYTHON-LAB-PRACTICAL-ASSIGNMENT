# List Operations Program
# Initial Lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("=" * 55)
print("         INITIAL LISTS")
print("=" * 55)
print("list1 =", list1)
print("list2 =", list2)

# i. List Concatenation
print("\n" + "=" * 55)
print("i. LIST CONCATENATION")
print("=" * 55)
concatenated = list1 + list2
print("list1 + list2 =", concatenated)

# ii. Remove list1[3]
print("\n" + "=" * 55)
print("ii. REMOVE list1[3]")
print("=" * 55)
print("Before:", list1)
del list1[3]
print("After removing list1[3]:", list1)

# iii. Add "Java" in List1
print("\n" + "=" * 55)
print('iii. ADD "Java" IN list1')
print("=" * 55)
print("Before:", list1)
list1.append("Java")
print('After appending "Java":', list1)

# iv. Update list2[3] = 11
print("\n" + "=" * 55)
print("iv. UPDATE list2[3] = 11")
print("=" * 55)
print("Before:", list2)
list2[3] = 11
print("After list2[3] = 11:", list2)

# v. del list2[2]
print("\n" + "=" * 55)
print("v. del list2[2]")
print("=" * 55)
print("Before:", list2)
del list2[2]
print("After del list2[2]:", list2)

# vi. Print "Welcome to Marwadi University" 4 times
print("\n" + "=" * 55)
print('vi. PRINT "Welcome to Marwadi University" 4 TIMES')
print("=" * 55)
for i in range(4):
    print("Welcome to Marwadi University")

# vii. Slicing Operations
print("\n" + "=" * 55)
print("vii. SLICING OPERATIONS")
print("=" * 55)
print("Current list1:", list1)
print("Current list2:", list2)
print("list1[-2]      =", list1[-2])
print("list2[1:3]     =", list2[1:3])
print("list1[-1:-3]   =", list1[-1:-3],  "  (empty: step goes wrong direction)")

# viii. Length of list2
print("\n" + "=" * 55)
print("viii. LENGTH OF list2")
print("=" * 55)
print("len(list2) =", len(list2))

# ix. Maximum element in list1 (only string or only numeric)
print("\n" + "=" * 55)
print("ix. MAXIMUM ELEMENT IN list1")
print("=" * 55)
print("list1:", list1)
# list1 has mixed types; find max among strings and numerics separately
str_elements  = [x for x in list1 if isinstance(x, str)]
int_elements  = [x for x in list1 if isinstance(x, (int, float))]
print("String elements:", str_elements, "→ max =", max(str_elements))
if int_elements:
    print("Numeric elements:", int_elements, "→ max =", max(int_elements))

# x. Minimum element in list2
print("\n" + "=" * 55)
print("x. MINIMUM ELEMENT IN list2")
print("=" * 55)
print("list2:", list2)
print("min(list2) =", min(list2))

# xi. list2.append(100)  [note: append(2)=100 means appending value 100]
print("\n" + "=" * 55)
print("xi. list2.append(100)")
print("=" * 55)
print("Before:", list2)
list2.append(100)
print("After list2.append(100):", list2)

# xii. Extend operation
print("\n" + "=" * 55)
print("xii. EXTEND OPERATION")
print("=" * 55)
extra = [200, 300, 400]
print("list2 before extend:", list2)
print("Extending with:", extra)
list2.extend(extra)
print("list2 after extend:", list2)

# xiv. Difference between POP and REMOVE
print("\n" + "=" * 55)
print("xiv. POP vs REMOVE")
print("=" * 55)
demo_list = [10, 20, 30, 40, 50]
print("Demo list:", demo_list)

# POP - removes by index, returns the removed element
popped_value = demo_list.pop(2)          # removes element at index 2
print(f"\nAfter demo_list.pop(2)  → removed value = {popped_value}")
print("List after pop:", demo_list)

demo_list2 = [10, 20, 30, 40, 50]
print("\nDemo list2:", demo_list2)
demo_list2.remove(30)                    # removes first occurrence of value 30
print("After demo_list2.remove(30)  → removes by VALUE (no return)")
print("List after remove:", demo_list2)

print("\n--- KEY DIFFERENCE ---")
print("pop(index)   → removes by INDEX, RETURNS the removed element")
print("remove(val)  → removes by VALUE, returns None")

# xv. reverse() on list1
print("\n" + "=" * 55)
print("xv. REVERSE list1")
print("=" * 55)
print("Before:", list1)
list1.reverse()
print("After list1.reverse():", list1)

# xvi. Arrange list2 in descending order
print("\n" + "=" * 55)
print("xvi. SORT list2 IN DESCENDING ORDER")
print("=" * 55)
print("Before:", list2)
list2.sort(reverse=True)
print("After list2.sort(reverse=True):", list2)

print("\n" + "=" * 55)
print("         PROGRAM COMPLETE")
print("=" * 55)