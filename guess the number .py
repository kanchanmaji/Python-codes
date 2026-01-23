import random

num = random.randint(1, 20)   # secret number between 1 and 50
attempts = 0
max_attempts = 5
user_num = None

while attempts < max_attempts:
    attempts += 1
    user_num = int(input(f"Attempt {attempts}/{max_attempts} - Guess the number: "))

    if user_num == num:
        print("\n🎉 You Crack the code!")
        break
    elif user_num > num + 5:
        print("\nToo High")
    elif user_num < num - 5:
        print("\nToo Low")
    else:
        print("\nSo closer!")

# Only runs if the loop finished without a correct guess
if user_num != num:
    print(f"\n❌ You Have no Try. The number was {num}")