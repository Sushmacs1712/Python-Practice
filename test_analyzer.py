text = input("Enter a sentence: ")

words = text.split()

print("Characters:", len(text))
print("Words:", len(words))
print("Uppercase letters:", sum(1 for ch in text if ch.isupper()))
print("Lowercase letters:", sum(1 for ch in text if ch.islower()))
print("Digits:", sum(1 for ch in text if ch.isdigit()))
print("Spaces:", text.count(" "))