# AutomatedQuetionGeneration
# 🤖 Smart Aptitude Question Generator

An **AI-powered web app** that automatically generates aptitude questions using **Natural Language Processing (NLP)** and a **Transformer model (T5)**.  
This project combines **Flask**, **Hugging Face Transformers**, and **Pandas** to dynamically create new questions from an existing dataset.

---

## 🚀 Features

- 🧠 **AI-Generated Questions** – Uses a pretrained Transformer (T5) model to generate fresh questions from text.  
- 📚 **CSV Dataset Integration** – Reads existing aptitude questions, options, and answers from a CSV file.  
- ⚙️ **Flask Backend** – Provides an API endpoint (`/generate`) that dynamically returns a new AI question each time.  
- 💻 **Interactive Frontend** – Displays the generated question and options on a simple web page.  

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Flask** – Web framework  
- **Transformers (Hugging Face)** – For NLP model  
- **Torch** – Model backend  
- **Pandas** – For CSV handling  
- **SentencePiece** – Required by T5 tokenizer  

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/smart-aptitude-generator.git
cd smart-aptitude-generator
