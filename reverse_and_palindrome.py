word = input("Enter a word: ")

reversed_word = word[::-1]

print("Original word:", word)
print("Reversed word:", reversed_word)

if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")