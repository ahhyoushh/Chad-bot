# 🤖 Discord Moderator & Fun Bot

A multipurpose Discord bot built for **moderation** and **fun features**.  
It identifies phrases or triggers in messages using **vectorization** (collections module) and **cosine similarity** to respond intelligently.

---

## 🧩 Overview

- Monitors Discord messages for predefined patterns.
- Detects abusive or specific phrases using vector-based comparison.
- Provides fun commands and automated replies for server engagement.

---

## ⚙️ Features

- **Phrase Detection**: Detects similar phrases using vector-based text comparison.  
- **Moderation**: Warns or reacts based on context.  
- **Fun Commands**: Offers automated replies or interactions to make the server lively.

---

## 🧠 How It Works

1. Messages are converted into **token frequency vectors**.  
2. Each message vector is compared with pre-defined pattern vectors using **cosine similarity**.  
3. If a message matches a pattern above a certain threshold, the bot triggers the corresponding response.

---

## 🛠️ Tech Stack

- Python  
- discord.py  
- Collections, Numpy  

---

