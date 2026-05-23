## 1)-->TRANSFORMER_ARCHITECTURE

Purana zamana — RNN (Recurrent Neural Network):

"Mujhe    kal    market    jaana    hai"
   ↓        ↓       ↓         ↓       ↓
 Word1 → Word2 → Word3 → Word4 → Word5
         (ek ek word process hota tha)

Problem:
❌ Slow — ek ek word process karna padta
❌ Long sentences mein pehle wale words bhool jaata
❌ Parallel processing nahi hoti


TRANSFORMER SOLVE ?

Transformer:

"Mujhe    kal    market    jaana    hai"
   ↓        ↓       ↓         ↓       ↓
 Word1   Word2   Word3    Word4   Word5
   ↕️       ↕️       ↕️        ↕️       ↕️
 SAARE WORDS EK SAATH DEKHO! (Parallel!)

✅ Fast — sab words ek saath
✅ Koi word nahi bhoolega
✅ GPU pe parallel run hota hai

2 MAIN PARTS OF TRANSFORMER

┌─────────────────────────────────────┐
│           TRANSFORMER               │
│                                     │
│  ┌──────────────┐ ┌──────────────┐  │
│  │   ENCODER    │ │   DECODER    │  │
│  │              │ │              │  │
│  │ Input samjho │ │ Output banao │  │
│  │              │ │              │  │
│  │ "Hello" →    │ │ → "Namaste"  │  │
│  └──────────────┘ └──────────────┘  │
└─────────────────────────────────────┘

Encoder = Samajhna (BERT yahi use karta hai)
Decoder = Generate karna (GPT yahi use karta hai)


INSIDE THE TRANSFORMER-->

INPUT TEXT
"I love AI"
     ↓
┌─────────────────────┐
│  1. TOKENIZATION    │  → Words ko numbers mein todna
│  "I"=1, "love"=2    │
└─────────────────────┘
     ↓
┌─────────────────────┐
│  2. EMBEDDING       │  → Numbers ko vectors mein
│  [0.2, 0.8, 0.1..] │    (meaning capture karna)
└─────────────────────┘
     ↓
┌─────────────────────┐
│  3. POSITIONAL      │  → Word ki position yaad rakhna
│     ENCODING        │    (1st, 2nd, 3rd word)
└─────────────────────┘
     ↓
┌─────────────────────┐
│  4. ATTENTION       │  → Har word doosre words se
│     MECHANISM       │    kitna related hai?  ⭐
└─────────────────────┘
     ↓
┌─────────────────────┐
│  5. FEED FORWARD    │  → Final processing
│     NETWORK         │
└─────────────────────┘
     ↓
OUTPUT

------------> Transformer Architecture is a deep learning architecture that uses self-attention to process relationships between words in parallel for better language understanding and generation.

# 2) Attention Mechanism  -->


Sentence: "The animal didn't cross the street 
           because IT was too tired"

IT = kisko refer kar raha hai?

Tumhara brain automatically "animal" pe 
focus karta hai — "street" pe nahi!

YAHI hai Attention!

Step 1: Har word ke 3 vectors banao

"I love AI" ke liye:

Word "love":
├── Query (Q)  = "Main kya dhundh raha hoon?"
├── Key   (K)  = "Meri identity kya hai?"
└── Value (V)  = "Meri actual information"

(Q, K, V — yeh sirf learned weights hain)

Step 2: Attention Score calculate karo

"love" ka har doosre word se score:

love → I    : Score = 0.1  (thoda related)
love → love : Score = 0.7  (khud se zyada)
love → AI   : Score = 0.2  (kuch related)

Formula: Score = Q × K / √(dimension)


Step 3: Softmax — scores ko 0-1 mein convert

love → I    : 0.1 → 0.14
love → love : 0.7 → 0.71
love → AI   : 0.2 → 0.15
              ────────────
              Total = 1.0  ✅


***Single Attention = ek perspective se dekho

Multi-Head = MULTIPLE perspectives ek saath!

Head 1: Grammar pe dhyan do
         ("love" = verb hai)

Head 2: Meaning pe dhyan do
         ("love" = positive emotion)

Head 3: Subject-Object relation
         ("I" love karta hai "AI" ko)

Sab heads combine → Rich understanding! 

# 3️)--> Tokens — What They Are & Cost 


Token = Text ka ek chhota piece

"Hello, how are you?"

Tokenize hoga:
["Hello", ",", " how", " are", " you", "?"]
= 6 tokens

Simple rule (English):
~1 token = ~4 characters
~1 token = ~0.75 words
100 tokens ≈ 75 words


# 4)--> Context Window — Limits 
Context Window = Model ek baar mein 
                 kitna text "yaad" rakh sakta hai

Jaise:
RAM = Computer ki working memory
Context Window = LLM ki working memory

Ek baar mein sirf itna hi process kar sakta hai!

--> different mopdels limit-->
Model              Context Window
──────────────────────────────────
GPT-3.5           4,096 tokens  (~3,000 words)
GPT-4             8,192 tokens  (~6,000 words)
GPT-4 Turbo       128,000 tokens (~96,000 words)
Claude 3.5        200,000 tokens (~150,000 words)
Gemini 1.5 Pro    1,000,000 tokens (1M!) 🤯
Llama 3 (local)   8,192 tokens


Turn 1: "Mera naam Akshat hai"          [50 tokens]
Turn 2: "Main Jaipur mein rehta hoon"   [50 tokens]
Turn 3: "Mujhe AI pasand hai"           [50 tokens]
...
Turn 50: "Mera naam kya hai?"

❌ Agar context window full ho gayi →
   Model bhool jaayega pehli baatein!

✅ Solution: 
   - Important info summarize karo
   - Vector DB mein store karo (RAG!)
   - Smart memory management

# 5)-->BERT vs GPT 

BERT = Pura book padh ke samjho
       (Bidirectional — dono taraf dekhta hai)

GPT  = Story likhte jao — ek ek word
       (Unidirectional — sirf left to right)


Sentence: "The cat sat on the [MASK]"

BERT ka approach:
"The" → "cat" → "sat" → "on" → "the" → ???
  ↑_______________________________________↑
  Dono directions se dekha → "mat" ✅

GPT ka approach:
"The" → "cat" → "sat" → "on" → "the" → "mat"
Sirf left se right → Next word predict kiya


┌─────────────────┬──────────────────┬──────────────────┐
│    Feature      │      BERT        │       GPT        │
├─────────────────┼──────────────────┼──────────────────┤
│ Direction       │ Bidirectional    │ Left to Right    │
│ Main Task       │ Understanding    │ Generation       │
│ Architecture    │ Encoder only     │ Decoder only     │
│ Training        │ Masked LM        │ Next token pred  │
│ Best For        │ Classification   │ Text generation  │
│                 │ NER, Q&A         │ Chatbots         │
│ Examples        │ BERT, RoBERTa    │ GPT-4, LLaMA     │
│                 │ DistilBERT       │ Mistral, Gemini  │
└─────────────────┴──────────────────┴──────────────────┘


# 5)-->Prompt Engineering

Same model, alag prompts → BILKUL alag results!

Bad prompt:   "Tell me about AI"
Good prompt:  "Explain Artificial Intelligence in 
               3 bullet points for a beginner, 
               using simple Hindi-English mix"

Prompt Engineering = AI se best output nikalna!




# Zero-shot = Koi example nahi diya
# Seedha kaam karne bolo

prompt = """
Classify the sentiment of this text as 
POSITIVE, NEGATIVE, or NEUTRAL.

Text: "The product quality is amazing!"
Sentiment:
"""
# Output: POSITIVE

# AI use case:
prompt = """
You are an expert AI engineer.
Explain what RAG (Retrieval Augmented Generation) is
in simple terms for a college student.
Keep it under 100 words.
"""

***Few-Shot Prompting:
# Few-shot = Kuch examples deke sikhao

prompt = """
Convert these sentences to formal English:

Informal: "gonna grab some food"
Formal: "I am going to get some food"

Informal: "wanna hang out tmrw?"
Formal: "Would you like to meet tomorrow?"

Informal: "btw the meeting is cancelled lol"
Formal:
"""
# Model samajh jaata hai pattern se!

# AI use case:
prompt = """
Extract the intent from user messages:

User: "What's the weather today?"
Intent: GET_WEATHER

User: "Order me a pizza"
Intent: ORDER_FOOD

User: "Play some music"
Intent: PLAY_MUSIC

User: "Remind me about my meeting at 5pm"
Intent:
"""

***prompt important elements-->

1. ROLE define karo
   "You are an expert data scientist..."

2. TASK clearly batao
   "Analyze this dataset and find..."

3. FORMAT specify karo
   "Respond in JSON format with keys: name, age, city"

4. CONSTRAINTS do
   "Keep response under 100 words"
   "Use bullet points"
   "No technical jargon"

5. EXAMPLES do (few-shot)
   "Here are some examples: ..."

6. CONTEXT do
   "Given this background information: ..."

# 7)-->Chain of Thought (CoT) Prompting

Without CoT:
Question: "Roger has 5 tennis balls. He buys 2 more 
cans of tennis balls. Each can has 3 balls. 
How many tennis balls does he have now?"

Without CoT:
Answer: "11"  ← Seedha answer, koi reasoning nahi
               (aur kabhi kabhi galat bhi hota hai!)


With CoT:

Same question + "Let's think step by step"

With CoT:
"Let me think step by step:
1. Roger starts with 5 tennis balls
2. He buys 2 cans of tennis balls
3. Each can has 3 balls
4. So 2 cans × 3 balls = 6 new balls
5. Total = 5 + 6 = 11 tennis balls
Answer: 11" ✅

Reasoning dikhta hai → More accurate!

# Template 1 — "Think step by step"
prompt = f"""
{question}

Let's think step by step:
"""

# Template 2 — Explicit steps maango
prompt = f"""
Solve this problem. Show your work:
1. First, identify what we know
2. Then, identify what we need to find
3. Show each calculation step
4. Give the final answer

Problem: {problem}
"""

# Template 3 — Self-check karo
prompt = f"""
Answer this question: {question}

Think through it carefully:
- What do I know?
- What approach should I take?
- Let me work through it...
- Let me verify my answer...

Final Answer:
"""

