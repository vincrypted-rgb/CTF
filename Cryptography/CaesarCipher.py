def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            offset = (ord(ch) - base + shift) % 26
            result += chr(base + offset)
        else:
            result += ch
    return result
