# Method 1: Using a for loop
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)


# Method 2: Using a for loop and lower()
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)


# Method 3: Using a function
def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))