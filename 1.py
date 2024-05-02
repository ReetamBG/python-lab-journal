def string_operations(s):
    capitalized = s.capitalize()  # Capitalize the string
    uppercased = s.upper()         # Convert to uppercase
    count_a = s.count('a')         # Count occurrences of a character
    replaced = s.replace('a', 'x') # Replace characters
    splitted = s.split()           # Split the string

    print("Original String:", s)
    print("Capitalized String:", capitalized)
    print("Uppercase String:", uppercased)
    print("Occurrences of 'a':", count_a)
    print("String after replacing 'a' with 'x':", replaced)
    print("Split String:", splitted)

def tuple_operations(t):
    length = len(t)              # Length of the tuple
    concatenated = t + (6, 7, 8) # Concatenation
    first_element = t[0]         # Indexing

    print("Original Tuple:", t)
    print("Length of Tuple:", length)
    print("Concatenated Tuple:", concatenated)
    print("First Element of Tuple:", first_element)

def array_operations(lst):
    length = len(lst)                  # Length of the list
    concatenated = lst + [6, 7, 8]     # Concatenation
    first_element = lst[0]             # Indexing

    print("Original List:", lst)
    print("Length of List:", length)
    print("Concatenated List:", concatenated)
    print("First Element of List:", first_element)

def dictionary_operations(d):
    length = len(d)             # Length of the dictionary
    d['age'] = 30               # Adding a new key-value pair
    d.pop('city')               # Removing a key
    city = d.get('city', 'Not Found')  # Accessing value by key

    print("Original Dictionary:", d)
    print("Length of Dictionary:", length)
    print("Dictionary after adding 'age':", d)
    print("City:", city)

# Example
string_operations("apple is a fruit")
print()
tuple_operations((1, 2, 3, 4, 5))
print()
dictionary_operations({'name': 'Alice', 'city': 'New York'})
print()
array_operations([1, 2, 3, 4, 5])
