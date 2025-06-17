import pandas as pd
import random

def themed_quiz(csv_file, num_questions=3):
    df = pd.read_csv(csv_file)
    df = df.sample(frac=1).reset_index(drop=True)  # Shuffle the rows

    score = 0

    for i in range(min(num_questions, len(df))):
        q = df.iloc[i]
        print(f"\nQuestion {i+1}: {q['Question']}")
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == str(q['Answer']).strip().lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Nope. Correct answer: {q['Answer']}")

    print(f"\n🏁 You got {score} out of {min(num_questions, len(df))} correct!\n")

def start_quiz():
    while True:
        print("🎉 Welcome to Jeopardy: Carmen's Edition 🎉")
        print("Choose a category:\n1. Bob's Burgers\n2. Zodiac Signs")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            print("\n🍔 You chose Bob's Burgers!")
            themed_quiz("bobs_burgers_quiz.csv", num_questions=7)
        elif choice == "2":
            print("\n🔮 You chose Zodiac Signs!")
            themed_quiz("zodiac_quiz.csv", num_questions=7)
        else:
            print("\n❌ Invalid choice. Try again.")
            continue

        # 🔁 Ask if user wants to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing! Come back soon!")
            break

start_quiz()