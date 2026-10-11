# how many times character repated in string
s="anjali"
for i in set(s):
    if s.count(i)>1:
        print(f"{i} is repeated {s.count(i)} times")



# max repeated character in string
from collections import Counter
s="anjali"
counts=Counter(s)
max_count=max(counts.values())
for char,count in counts.items():
    if count==max_count:
        print(f"{char} is the most repeated character and it is repeated {count} times")


# particular letter repeated
s="anjali"
letter=input("Enter a letter to check how many times it is repeated: ")
print(f"{letter} is repeated {s.count(letter)} times")
