import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
responses = {
        'hi': [
            'Hey 👋 how’s it going?',
            'Hey there! 😄 How are you doing?',
            'Yo! ✌️ What’s up?',
            'Hiya 👋 how’ve you been?',
            'Hello 🙂 how are things with you?',
            'Hey buddy 👋 what’s new?',
            'Sup 😎 how’s everything?',
            'Hey 👋 what’s happening?',
            'Hi 👋 how are you feeling today?',
            'Hey mate 🙂 how’s life treating you?',
            'Hey 👋 been up to anything fun?',
            'What’s up 👋 how’s your day?',
            'Hey there 😄 how’s everything going?',
            'Hello 👋 what’s going on?',
            'Yo 😎 how’s life?',
            'Hi 👋 what are you up to?',
            'Hey friend 🙂 how’s your day been?',
            'Sup 👋 how are you today?',
            'Hey 👋 what’s new with you?',
            'Hi there 😄 how have you been?',
        ],         
    'Hello': ['Hello 🙂 what are you up to?'],
    'Hey': ['Hey there! 😄'],
    'Yo': ['Yo! What’s up?'],
    'Good morning': ['Good morning ☀️ have a great day ahead!'],
    'Good afternoon': ['Good afternoon 🌞 how’s your day?'],
    'Good evening': ['Good evening 🌇 how are you doing?'],
    'Good night': ['Good night 🌙 sweet dreams!'],
    'How are you': ['I’m doing great, thanks for asking 😊 how about you?'],
    'What’s up': ['Not much 🤗 just here to chat with you!'],
    'How’s it going': ['It’s going well 🙌 how’s it going for you?'],
    'Hey buddy': ['Hey buddy 👋 good to see you!'],
    'Hi there': ['Hi there 😃'],
    'Hello friend': ['Hello friend 👋'],
    'Howdy': ['Howdy 🤠'],
    'Heya': ['Heya 🙋‍♂️'],
    'Greetings': ['Greetings 👋 how’s everything?'],
    'Sup': ['Sup 😎'],
    'Yo yo': ['Yo yo 🙌'],
    'Hey man': ['Hey man ✌️'],
    'Hey bro': ['Hey bro 👊'],
    'Hey sis': ['Hey sis 💖'],
    'Long time no see': ['Yeah, long time! 😃 what’s new?'],
    'Hi friend': ['Hi friend 🫶'],
    'Hey there': ['Hey there 👋'],
    'Hola': ['Hola! 🇪🇸'],
    'Namaste': ['Namaste 🙏', 'नमस्ते  🙏'],
    'Bonjour': ['Bonjour 🇫🇷'],
    'Ciao': ['Ciao 🇮🇹'],
    'Konnichiwa': ['Konnichiwa 🇯🇵'],
    'Annyeong': ['Annyeong 🇰🇷'],
    'Salaam': ['Salaam 🤝'],
    'Shalom': ['Shalom ✡️'],
    'Good to see you': ['Good to see you too 😄'],
    'How have you been': ['I’ve been great! Thanks for asking 🌟'],
    'Hiya': ['Hiya 👋'],
    'Ello': ['Ello mate 🇬🇧'],
    'Wassup': ['Wassup 😁'],
    'Hi bro': ['Hi bro 👋'],
    'Hi sis': ['Hi sis 🌸'],
    'Hello buddy': ['Hello buddy 🙌'],
    'Peace': ['Peace ✌️'],
    'Hey dude': ['Hey dude 😎'],
    'Hey girl': ['Hey girl 💃'],
    'Hey boy': ['Hey boy 🕺'],
    'Yo buddy': ['Yo buddy 🙌'],
    'Hey mate': ['Hey mate 🇦🇺'],
    'Hi buddy': ['Hi buddy 🥳'],
    'Hi mate': ['Hi mate 👋'],
    'Hey pal': ['Hey pal 😃'],
    'Pranaam': ['प्रणाम 🙏', 'Pranaam 🙏'],
    'Who are you': ['I’m Alex 🤖 your friendly chatbot assistant!']

}

while True:
    user = input('You: ').lower().strip()  # remove extra spaces
    # convert all keys to lowercase dynamically
    responses = {
        k.lower(): v 
        if isinstance(v, list) 
        else [v] 
        for k, v in responses.items()
        }
    match, score =  process.extractOne(user, responses.keys())
    if score > 70:
        print('Bot:', random.choice(responses[match]))
    elif user in ['bye', 'exit']:
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Can't respond due to server load. Try again later!")


