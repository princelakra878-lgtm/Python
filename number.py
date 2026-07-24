mood = input("How are you feeling today? ").lower()

if mood == "happy":
    print("😊 That's great! Keep smiling and enjoy your day!")

elif mood == "sad":
    print("💙 Don't worry. Better days are coming. Stay strong!")

elif mood == "angry":
    print("😌 Take a deep breath and try to relax.")

elif mood == "tired":
    print("😴 Get some rest and drink plenty of water.")

elif mood == "excited":
    print("🎉 Awesome! Make the most of your energy today!")

else:
    print("🙂 Have a wonderful day and take care of yourself!")

advice = {
    "happy": "😊 Keep smiling and spread positivity!",
    "sad": "💙 Stay strong. Tomorrow is a new day!",
    "angry": "😌 Take a deep breath and stay calm.",
    "tired": "😴 Get enough sleep and relax.",
    "excited": "🎉 Enjoy every moment!"
}

mood = input("Enter your mood: ").lower()

print(advice.get(mood, "🙂 Have a great day!"))