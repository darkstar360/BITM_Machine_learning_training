# list1 = [1991, 1994, 1992]
# list2 = [1991, 1994, 2000, 1992]
#
# print("list1: ", list1)
# print("list2: ", list2)
#
# # Return element count.
# print("len(list1): ", len(list1))
# print("len(list2): ", len(list2))
#
# # Maxinum value in the list.
# maxValue = max(list1)
#
# print("Max value of list1: ", maxValue)
# # Minimum value in the list
# minValue = min(list1)
# print("Min value of list1: ", minValue)
#
# print("Max value of list2: ", max(list2))
# print("Min value of list2: ", min(list2))


years = [1990, 1991, 1992, 1993, 1993, 1993, 1994]
print("Years: ", years)
print("\n - Reverse the list")
# Reverse the list.
years.reverse()
print("Years (After reverse): ", years)
aTuple = (2001, 2002, 2003)
print("\n - Extend: ", aTuple)
years.extend(aTuple)
print("Years (After extends): ", years)
print("\n - Append 3000")
years.append(3000)
print("Years (After appends): ", years)
print("\n - Remove 1993")
years.remove(1993)
print("Years (After remove): ", years)
print("\n - years.pop()")
# Remove last element of list.
lastElement = years.pop()
print("last element: ", lastElement)
print("\n")
# Count
print("years.count(1993): ", years.count(1993))
