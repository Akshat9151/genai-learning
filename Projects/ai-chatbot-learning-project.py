import json
import pandas as pd              # import libraries



data = pd.read_csv("data.csv")   # load csv file 
# variable use --> data 


class ChatBot:   # oops -> class -- chatbot design (Class = blueprint)

    def __init__(self):  # constructor --> As soon as the object is created, it runs automatically
        # self --> represent the current object of the class



        # List for chat history
        self.chat_history = []   # --> store the conversation history between user and bot

        # Dictionary from CSV
        self.responses = {}    # --> store the question-answer pairs from the CSV file



        # Convert CSV into dictionary
        for index, row in data.iterrows():  #--> Loop (This will run on every row of the CSV.)

            self.responses[row["question"]] = row["answer"]

    # Function
    def reply(self, message):  # --> This function will take user input and return bot response

        message = message.lower() # --> Convert user message to lowercase (HELLO --> hello) 

        # Dictionary response check
        if message in self.responses:  #--> Check -- Is the user's message in the dictionary?

            bot_reply = self.responses[message]  #--> If yes, take the answer from the dictionary

        else:

            bot_reply = "Sorry bro, I don't understand 😅"  # --> if message are not matching so answer are defalut

        # Save history using dictionary
        self.chat_history.append({

            "user": message,
            "bot": bot_reply
        })

        return bot_reply

    # File Handling + JSON
    def save_chat(self):

        with open("chat_history.json", "w") as file:

            json.dump(self.chat_history, file, indent=4)


# Create object
bot = ChatBot()


# Loop
while True:

    user = input("You: ")

    # Exit condition
    if user.lower() == "exit":

        bot.save_chat()

        print("Bot: Chat saved successfully ✅")
        print("Bot: Goodbye 👋")

        break

    response = bot.reply(user)

    print("Bot:", response)







    