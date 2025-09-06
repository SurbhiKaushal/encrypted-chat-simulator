# Simple Encrypted Chat Simulator
def send_message():
    message = input("You: ")
    encrypted = encrypt_message(message)
    print("Encrypted message:", encrypted)
    decrypted = decrypt_message(encrypted)
    print("Decrypted message:", decrypted)

def encrypt_message(msg):
    # Caesar Cipher example: shift letters by 3
    encrypted = ""
    for char in msg:
        if char.isalpha():
            shift = 3
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt_message(msg):
    # Reverse Caesar Cipher
    decrypted = ""
    for char in msg:
        if char.isalpha():
            shift = 3
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

# Main loop
while True:
    send_message()
    again = input("Send another message? (y/n): ")
    if again.lower() != 'y':
        break

print("Chat ended. Goodbye!")
