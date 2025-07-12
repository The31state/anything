import random

def get_restaurants():
    return [
        "Pasty Kitchen",
        "Adalberto's Mexican Food",
        "Pho 99 Plus (Best Meal Plus)",
        "Mustard's Chicago Style Eatery",
        "Maderas Steak & Ribs",
        "Ameci Pizza & Pasta",
        "Paul's Place",
        "Chick-fil-A",
        "Uroko Poke",
        "Volcano Burgers",
        "In-N-Out Burger",
        "Xtreme Sushi Restaurant",
        "Nick's Deli II"
    ]

restaurant_meta = {
    "Pasty Kitchen": {"cuisine":"british","dish":"pies"},
    "Adalberto's Mexican Food": {"cuisine":"mexican","dish":"tacos"},
    "Pho 99 Plus (Best Meal Plus)": {"cuisine":"vietnamese","dish":"soup"},
    "Mustard's Chicago Style Eatery": {"cuisine":"american","dish":"hotdogs"},
    "Maderas Steak & Ribs": {"cuisine":"american","dish":"steak"},
    "Ameci Pizza & Pasta": {"cuisine":"italian","dish":"pizza"},
    "Paul's Place": {"cuisine":"american","dish":"burgers"},
    "Chick-fil-A": {"cuisine":"american","dish":"sandwiches"},
    "Uroko Poke": {"cuisine":"hawaiian","dish":"poke"},
    "Volcano Burgers": {"cuisine":"american","dish":"burgers"},
    "In-N-Out Burger": {"cuisine":"american","dish":"burgers"},
    "Xtreme Sushi Restaurant": {"cuisine":"japanese","dish":"sushi"},
    "Nick's Deli II": {"cuisine":"american","dish":"sandwiches"}
}

cuisine_options = {
    "a":"mexican","b":"american","c":"japanese","d":"italian",
    "e":"hawaiian","f":"vietnamese","g":"british"
}

dish_options = {
    "a":"tacos","b":"burgers","c":"sushi","d":"pizza",
    "e":"salad","f":"sandwiches","g":"steak"
}

def ask_questions():
    print("\nSoldier, take a breath. You've fought hard. Now, it's time to indulge.")

    # Question 1
    print("\n1. Is today that sacred Tuesday when the thought of soft, steamy tacos wrapping around your craving makes you weak with desire?")
    print("1) Yes, I'm surrendering to Taco Tuesday.")
    print("2) No, tempt me further.")
    while True:
        t = input("Enter 1 or 2: ").strip()
        if t in ["1","2"]:
            if t == "1":
                return {
                    "cuisine": "mexican",
                    "dish": "tacos",
                    "reason": "It's Taco Tuesday. Let the seduction begin.",
                    "force_restaurant": "Adalberto's Mexican Food"
                }
            break

    # Question 2
    print("\n2. Is it Wing Wednesday, a day to lose yourself in something messy and irresistible?")
    print("1) Yes, I crave that satisfaction.")
    print("2) No, take me deeper.")
    while True:
        w = input("Enter 1 or 2: ").strip()
        if w in ["1","2"]:
            if w == "1":
                return {
                    "cuisine": "american",
                    "dish": "hotdogs",
                    "reason": "It's Wing Wednesday. Indulgence is your only mission.",
                    "force_restaurant": random.choice([
                        "Mustard's Chicago Style Eatery",
                        "Paul's Place"
                    ])
                }
            break

    # Question 3
    print("\n3. Tell me... which territory of pleasure do you yearn to invade?")
    for k,v in cuisine_options.items():
        print(f"{k.upper()}) {v.capitalize()}")
    while True:
        c = input("Select your desire (letter): ").strip().lower()
        if c in cuisine_options:
            cuisine = cuisine_options[c]
            break

    # Question 4
    print("\n4. Which indulgence is calling your name, whispering promises you can barely resist?")
    for k,v in dish_options.items():
        print(f"{k.upper()}) {v.capitalize()}")
    while True:
        d = input("Choose your craving (letter): ").strip().lower()
        if d in dish_options:
            dish = dish_options[d]
            break

    # Question 5
    print("\n5. Describe the sensation you long to feel on your lips.")
    mouth_moods = {
        "a":"fiery and unforgettable",
        "b":"creamy and slow-melting",
        "c":"fresh and awakening",
        "d":"crispy and forbidden",
        "e":"hearty and primal",
        "f":"delicate and refined"
    }
    for k,v in mouth_moods.items():
        print(f"{k.upper()}) Something {v}")
    while True:
        m = input("Select your fantasy (letter): ").strip().lower()
        if m in mouth_moods:
            mood = mouth_moods[m]
            break

    # Question 6
    print("\n6. How far are you willing to go... to taste satisfaction?")
    print("1) All the way. No regrets.")
    print("2) Just enough to feel alive.")
    print("3) I'll keep some discipline.")
    while True:
        g = input("Enter 1, 2, or 3: ").strip()
        if g in ["1","2","3"]:
            guilt = g
            break

    return {
        "cuisine": cuisine,
        "dish": dish,
        "mood": mood,
        "guilt": guilt,
        "reason": f"You crave {cuisine} wrapped in something {mood}, embracing {'total surrender' if guilt=='1' else 'a teasing indulgence' if guilt=='2' else 'a disciplined delight'}."
    }

def pick_restaurant(answer, restaurants):
    if "force_restaurant" in answer:
        return answer["force_restaurant"]

    matches = [r for r in restaurants if restaurant_meta[r]["cuisine"] == answer["cuisine"]]
    if not matches:
        matches = restaurants
    return random.choice(matches)

def main():
    print("=== Welcome to Operation Temptation ===")
    restaurants = get_restaurants()
    answer = ask_questions()
    chosen = pick_restaurant(answer, restaurants)
    print("\nYour craving has spoken.")
    print(answer['reason'])
    print(f"\nYour orders are clear: proceed to {chosen} and surrender to satisfaction.")

if __name__=="__main__":
    main()
