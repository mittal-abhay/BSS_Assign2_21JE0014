def main():
    name = "Abhay Mittal" 
    admission_number = "21JE0014" 

    print(f"\nWelcome to {name}'s Fortune Teller ({admission_number}) \n")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print(f"\nYour fortune: Happiness is contagious, {name.split()[0]}! Spread it around.")
    elif mood == "sad":
        print("\nYour fortune: Tough times never last, but tough people do. Stay strong!")
    elif mood == "neutral":
        print("\nYour fortune: Life is full of surprises—embrace the unexpected!")
    else:
        print("\nSorry, I can only interpret happy/sad/neutral moods at the moment.")

if __name__ == "__main__":
    main()