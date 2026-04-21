#print("Hello, World!")
Int_list = [5, 10, 20, 25, 30]
print("Original list:", Int_list)
del Int_list[1] # Deletes the element at index 1 (10)
print("After del:", Int_list) # Output: [5, 20, 25, 30]
Int_list.remove(25) # Removes the value 25
print("After remove:", Int_list) # Output: [5, 20, 30]
last_item = Int_list.pop() # Removes the last element (30)
print("After pop:", Int_list) # Output: [5, 20]
print("Popped item:", last_item) # Output: 30
