import random
def main():
    name = "Abhay Mittal" 
    admission_number = "21JE0014" 

    print(f"\nWelcome to {name}'s Fortune Teller ({admission_number}) \n")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed/excited): ").strip().lower()

    fortunes = {
        "happy": [
            "You're on a roll — don’t stop now!",
            "Good vibes ahead. Keep riding that wave, dear!"
        ],
        "sad": [
            "It's okay to not be okay. Brighter days are coming.",
            "The clouds will clear soon. Hang in there."
        ],
        "neutral": [
            "Still waters run deep. Something surprising is coming.",
            "No chaos = more clarity. Use this moment."
        ],
        "stressed": [
            "Breathe in. Breathe out. You've got this.",
            "Stress means you care. Don’t forget to care for yourself too, dear."
        ],
        "excited": [
            "Your enthusiasm is contagious!",
            "Excitement is the first step to success."
        ],
    }

    if mood in fortunes:
        message = random.choice(fortunes[mood])
        print(f"\nYour fortune: {message} \n")
    else:
        print("\nHmm, I don’t know that mood. Try happy/sad/neutral/stressed/excited.\n")


if __name__ == "__main__":
    main()