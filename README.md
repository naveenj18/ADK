🧠 HSN Code Validator Agent
This project implements an intelligent agent using Google's ADK (Agent Developer Kit) that validates HSN (Harmonized System of Nomenclature) codes based on a master Excel dataset.

🔍 Features
✅ Validates if a given HSN code is properly formatted.

📄 Checks the HSN code against a master dataset (Excel file).

🧠 Built using Google's adk with support from Gemini 2.0 Pro model.

📦 Easy to plug into larger AI workflows or systems.

📁 Project Structure
bash
Copy
Edit
hsn_validator_agent/
│
├── agent.py             # Sets up the root agent using ADK
├── _init_.py            # Logic to validate HSN code from Excel
├── HSN_SAC.xlsx         # Master dataset of HSN codes and descriptions
└── README.md            # Project documentation
⚙️ Installation & Setup
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/hsn_validator_agent.git
cd hsn_validator_agent
Install Dependencies

bash
Copy
Edit
pip install pandas google-adk openpyxl
Update the Excel File Path

Make sure the Excel file path in _init_.py is correct:

python
Copy
Edit
df = pd.read_excel("D:/hsn_validator_agent/HSN_SAC.xlsx", dtype=str)
Update it if needed.

🚀 Usage
You can use the agent to validate HSN codes:

python
Copy
Edit
from google.adk.agents import run_agent
from agent import root_agent

response = run_agent(root_agent, input="Validate HSN code 6101")
print(response)
Or call the validation function directly:

python
Copy
Edit
from _init_ import validate_hsn_code

print(validate_hsn_code("6101"))
✅ HSN Validation Logic
Code must be numeric.

Length must be 2, 4, 6, or 8 digits.

Code must be present in the master Excel dataset.

📜 Example Output
json
Copy
Edit
{
  "code": "6101",
  "status": "Valid",
  "description": "Men’s or boys’ overcoats, car-coats, capes, cloaks..."
}
📌 Requirements
Python 3.8+

Google ADK

pandas, openpyxl

👨‍💻 Author
Naveen – LinkedIn (Add your link)

# ADK
