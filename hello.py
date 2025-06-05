# Simple Personalized Greeting Script
name = input("What's your name? ")
age = int(input("How old are you? "))
mood = input("How are you feeling today? (happy/sad/excited/tired) ").lower()

# Greeting based on mood
greetings = {
    "happy": "🌟 Awesome! Keep shining!",
    "sad": "☔️ Hope your day gets better!",
    "excited": "🚀 Woohoo! Let's go!",
    "tired": "😴 Get some rest, champ!"
}

# Age-based comment
if age < 18:
    age_comment = "Young and brilliant!"
elif 18 <= age <= 30:
    age_comment = "Prime time of life!"
else:
    age_comment = "Wisdom comes with age!"

# Print personalized message
print(f"\nHello, {name}! ({age_comment})")
print(greetings.get(mood, "Nice to meet you!"))