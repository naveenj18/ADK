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
