word = input("Input qwerty")
print(word,"has",len(word) - word.count(" "),"letters") 
word = word.upper()
for chars in word:
    print (chars) 
print()
word = word.lower()
word = word[::-1]
for chars in word:
    print(chars)
print()
print()
print("We finished 3rd in the Counter Strike competition, unfortunatly.") 
