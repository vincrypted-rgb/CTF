message = input("What is your original/final message?")
keyword = input("Keyword? ")

result = ""
key_index = 0

for letter in message:
  if letter.isalpha():
    key_letter =  keyword[key_index % len(keyword)]
    shift = ord(key_letter) - ord("a")
    
    base = ord("a")
    new_number = (ord(letter) - base + shift) % 26 + base
    result = result + chr(new_number)
    
    key_index = key_index + 1
  else:
    result = result + letter

print(result)
