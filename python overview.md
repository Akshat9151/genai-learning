Python — Complete Overview for AI/ML 🐍
Tera base strong karte hain — har topic ka practical overview!

1️⃣ Variables & Data Types
python# Variables — data store karna
name = "Akshat"          # String
age = 20                 # Integer  
cgpa = 8.5               # Float
is_student = True        # Boolean

# Type check
print(type(name))        # <class 'str'>

# Type conversion
age_str = str(age)       # "20"
num = int("42")          # 42
pi = float("3.14")       # 3.14

# String formatting (f-string — sabse useful!)
print(f"Name: {name}, Age: {age}")
# Output: Name: Akshat, Age: 20

# Multiple assignment
x, y, z = 1, 2, 3

# Constants (convention — CAPS mein likho)
MAX_TOKENS = 1000
API_KEY = "sk-xxxx"
AI mein use: Model ka naam, API keys, scores store karna

2️⃣ Loops
python# FOR loop — list pe iterate karna
fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print(fruit)

# Range — numbers ke liye
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(1, 6):     # 1,2,3,4,5
    print(i)

# WHILE loop — condition true ho tab tak
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue    # skip 3
    if i == 7:
        break       # 7 pe rok do
    print(i)

# Enumerate — index bhi chahiye
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")
# 0: apple
# 1: mango

# List comprehension — powerful shortcut!
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# AI mein use:
responses = [model.predict(text) for text in texts]
AI mein use: Dataset ke har row pe loop, batch processing

3️⃣ Functions
python# Basic function
def greet(name):
    return f"Hello {name}!"

print(greet("Akshat"))   # Hello Akshat!

# Default parameters
def chat(message, temperature=0.7):
    return f"Processing: {message} at temp {temperature}"

chat("Hello")              # temperature=0.7 default
chat("Hello", 0.9)         # temperature=0.9

# *args — multiple arguments
def add(*numbers):
    return sum(numbers)

add(1, 2, 3, 4)    # 10

# **kwargs — keyword arguments (VERY important in AI!)
def create_model(**settings):
    print(settings)

create_model(model="gpt-4", temperature=0.7, max_tokens=500)
# {'model': 'gpt-4', 'temperature': 0.7, 'max_tokens': 500}

# Lambda — ek line function
double = lambda x: x * 2
double(5)    # 10

# Nested functions
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
add5(3)    # 8
AI mein use: API call karna, data preprocess karna, model run karna

4️⃣ Lists, Dicts, Tuples, Sets
python# ── LIST — ordered, changeable ──
messages = ["Hello", "How are you", "Bye"]

messages.append("New message")   # add at end
messages.insert(0, "First")      # add at position
messages.remove("Bye")           # remove by value
messages.pop()                   # remove last
messages[0]                      # access by index
messages[-1]                     # last element
messages[1:3]                    # slicing

# Sort
messages.sort()
messages.sort(reverse=True)

# AI mein use:
chat_history = []
chat_history.append({"role": "user", "content": "Hello"})
chat_history.append({"role": "assistant", "content": "Hi!"})

# ── DICT — key-value pairs (MOST used in AI!) ──
person = {
    "name": "Akshat",
    "age": 20,
    "skills": ["Python", "AI", "ML"]
}

person["name"]              # "Akshat"
person.get("email", "N/A")  # safe access — "N/A" if not found
person["city"] = "Jaipur"   # add new key
del person["age"]           # delete key

# Loop through dict
for key, value in person.items():
    print(f"{key}: {value}")

# Check key exists
if "name" in person:
    print("Found!")

# Dict comprehension
scores = {name: score for name, score in zip(names, scores)}

# AI mein use — API request body:
payload = {
    "model": "gpt-4",
    "messages": chat_history,
    "temperature": 0.7,
    "max_tokens": 1000
}

# ── TUPLE — ordered, NOT changeable ──
coordinates = (28.6, 77.2)   # lat, long
rgb = (255, 128, 0)

# Use karo jab data change nahi hona chahiye
# Model configurations, constants ke liye

# ── SET — unique values only ──
tags = {"python", "ai", "ml", "python"}  # duplicate remove!
print(tags)    # {'python', 'ai', 'ml'}

tags.add("nlp")
tags.remove("ml")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1 & set2    # intersection: {3, 4}
set1 | set2    # union: {1,2,3,4,5,6}
set1 - set2    # difference: {1, 2}

5️⃣ OOP — Classes & Objects
python# Class banana
class ChatBot:
    # Constructor — object bante waqt run hota hai
    def __init__(self, name, model="gpt-3.5"):
        self.name = name          # instance variable
        self.model = model
        self.history = []         # conversation history

    # Method
    def chat(self, message):
        self.history.append(message)
        return f"{self.name}: Processing '{message}'"

    def clear_history(self):
        self.history = []
        return "History cleared!"

    # String representation
    def __str__(self):
        return f"ChatBot({self.name}, model={self.model})"


# Object create karna
bot = ChatBot("MyBot", "gpt-4")
bot.chat("Hello!")
print(bot)      # ChatBot(MyBot, model=gpt-4)

# ── INHERITANCE — existing class se extend karna ──
class AdvancedBot(ChatBot):
    def __init__(self, name, model, temperature=0.7):
        super().__init__(name, model)   # parent init
        self.temperature = temperature

    # Override method
    def chat(self, message):
        response = super().chat(message)
        return f"{response} [temp={self.temperature}]"

    # New method
    def set_temperature(self, temp):
        self.temperature = temp


adv_bot = AdvancedBot("AdvBot", "gpt-4", 0.9)
adv_bot.chat("What is AI?")
AI mein use: LangChain, FastAPI, HuggingFace — sab OOP pe based hain!

6️⃣ File I/O
python# ── TEXT FILE ──
# Write
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Second line\n")

# Read
with open("output.txt", "r") as f:
    content = f.read()         # poora file
    # ya
    lines = f.readlines()      # list of lines

# Append (existing file mein add karo)
with open("output.txt", "a") as f:
    f.write("New line added\n")

# ── JSON FILE — AI mein sabse zyada use! ──
import json

# Save data
data = {
    "model": "gpt-4",
    "responses": ["Hello!", "How can I help?"],
    "tokens_used": 150
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Load data
with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded["model"])    # gpt-4

# ── CSV FILE ──
import csv

# Write CSV
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Akshat", 95])

# Read CSV
with open("results.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ── .ENV FILE — API keys store karna ──
# .env file mein:
# API_KEY=sk-xxxx
# MODEL=gpt-4

from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")
AI mein use: Results save karna, dataset load karna, API keys store karna

7️⃣ APIs — requests library
pythonimport requests
import json

# ── GET request ──
response = requests.get("https://api.github.com/users/Akshat9151")
print(response.status_code)   # 200 = success
data = response.json()
print(data["name"])

# ── POST request — AI APIs yahi use karte hain! ──
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "What is RAG?"}
    ]
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()
print(result["choices"][0]["message"]["content"])

# ── Error handling ──
try:
    response = requests.get("https://api.example.com", timeout=10)
    response.raise_for_status()   # 4xx/5xx error throw karo
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out!")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"Error: {e}")
AI mein use: OpenAI, Gemini, HuggingFace API calls — sab yahi pattern!

8️⃣ Pandas & NumPy
pythonimport pandas as pd
import numpy as np

# ── NUMPY — numbers & arrays ──
arr = np.array([1, 2, 3, 4, 5])
arr * 2           # [2,4,6,8,10]
arr.mean()        # 3.0
arr.max()         # 5
arr.reshape(5,1)  # shape change

# 2D array (matrix)
matrix = np.array([[1,2,3],[4,5,6]])
matrix.shape      # (2, 3)

# Random numbers
np.random.seed(42)
random_arr = np.random.rand(5)     # 0-1 ke beech

# ── PANDAS — data tables ──
# DataFrame banana
df = pd.DataFrame({
    "name": ["Akshat", "Rahul", "Priya"],
    "score": [95, 87, 92],
    "city": ["Jaipur", "Delhi", "Mumbai"]
})

# Basic operations
df.head()              # pehli 5 rows
df.shape               # (3, 3)
df.info()              # column types
df.describe()          # statistics

# Column access
df["name"]             # ek column
df[["name", "score"]]  # multiple columns

# Filter
df[df["score"] > 90]   # score > 90 wale

# New column
df["grade"] = df["score"].apply(
    lambda x: "A" if x >= 90 else "B"
)

# Load CSV (dataset)
df = pd.read_csv("dataset.csv")

# Missing values
df.isnull().sum()          # count missing
df.dropna()                # remove rows with missing
df.fillna(0)               # fill with 0

# Group by
df.groupby("city")["score"].mean()

# Save
df.to_csv("output.csv", index=False)
AI mein use: Dataset load karna, clean karna, features banana — ML ka base!

9️⃣ Virtual Environment & pip
bash# Virtual env banana — ALWAYS karo har project mein!
python -m venv myenv

# Activate karo
# Windows:
myenv\Scripts\activate
# Mac/Linux:
source myenv/bin/activate

# Install packages
pip install langchain openai pandas numpy

# requirements.txt banana
pip freeze > requirements.txt

# Kisi aur ke project mein install karna
pip install -r requirements.txt

# Deactivate
deactivate
AI mein use: Har AI project ka apna environment hona chahiye!

🔟 Git & GitHub
bash# ── Setup ──
git config --global user.name "Akshat Jain"
git config --global user.email "bakshiakshat05@gmail.com"

# ── Naya project ──
git init                        # start tracking
git add .                       # sab files stage karo
git commit -m "First commit"    # save snapshot

# ── GitHub pe push ──
git remote add origin https://github.com/Akshat9151/project
git push -u origin main

# ── Roz ka workflow ──
git status                      # kya badla?
git add filename.py             # specific file
git add .                       # sab files
git commit -m "Added RAG pipeline"
git push                        # GitHub pe bhejo

# ── .gitignore — important! ──
# .gitignore file mein likho:
# .env          (API keys mat bhejo!)
# __pycache__/
# myenv/
# *.pyc
