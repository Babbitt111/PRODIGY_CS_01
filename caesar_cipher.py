def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

# Input
mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
text = input("Enter your message: ")

try:
    shift = int(input("Enter shift value (0–25): "))
    if not (0 <= shift <= 25):
        print("Shift must be between 0 and 25.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

# Output
output = caesar_cipher(text, shift, mode)
print(f"\nYour {mode}ed message:\n{output}")