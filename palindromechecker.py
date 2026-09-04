text = input("Enter a word: ")

if text.lower() == text.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
