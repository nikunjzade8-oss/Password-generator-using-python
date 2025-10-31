import random
import string

def generate_password(length):
    # Password ke liye characters define kar rahe hain
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly characters choose karke password banate hain
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
        
        password = generate_password(length)
        print("\nYour Generated Password is:", password)
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
