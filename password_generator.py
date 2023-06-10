import random
import string

def generate_password(length, include_numbers, include_special_chars):
    chars = string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    length = int(input("Milyen hosszú legyen a jelszó összesen (hány karakter): "))
    include_numbers = input("Legyenek-e benne számok? (igen/nem): ").lower() == "igen"
    include_special_chars = input("Legyenek-e benne speciális karakterek? (igen/nem): ").lower() == "igen"

    password = generate_password(length, include_numbers, include_special_chars)
    print("Generált jelszó:", password)

if __name__ == "__main__":
    main()