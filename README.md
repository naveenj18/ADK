# 🧠 HSN Code Validator Agent

This project implements an intelligent agent using **Google ADK** that validates HSN (Harmonized System of Nomenclature) codes against a master Excel dataset. It uses `pandas` for data processing and `gemini-2.0-pro` as the underlying model.

---

## 🚀 Features

- ✅ Validates HSN codes based on format and existence
- 📄 Returns HSN description from Excel master file
- 🧠 Powered by Gemini model using Google's Agent Developer Kit (ADK)

---

## 🗂️ Project Structure

hsn_validator_agent/
├── agent.py # Defines the ADK agent
├── init.py # Contains the validation logic
├── HSN_SAC.xlsx # Master Excel file with HSN codes & descriptions
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/hsn_validator_agent.git
cd hsn_validator_agent

##. Create and activate a virtual environment
python -m venv env
source env/bin/activate 


##Get an API key from Google AI Studio.
When using Python, open the .env file located inside (multi_tool_agent/) and copy-paste the following code.

multi_tool_agent/.env

GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
###When using Java, define environment variables:

terminal

export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE

#Run the following command to launch the dev UI.


adk web
Step 1: Open the URL provided (usually http://localhost:8000 or http://127.0.0.1:8000) directly in your browser.

Step 2. In the top-left corner of the UI, you can select your agent in the dropdown. Select "multi_tool_agent".
