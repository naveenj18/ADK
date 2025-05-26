from . import agent
import pandas as pd

# Load HSN master data once
df = pd.read_excel("D:\hsn_validator_aagent\HSN_SAC.xlsx", dtype=str)
hsn_dict = dict(zip(df["HSNCode"], df["Description"]))

def validate_hsn_code(code: str) -> dict:
    """Validates a single HSN code against the master dataset."""
    if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
        return {
            "code": code,
            "status": "Invalid",
            "reason": "Invalid format (must be numeric and 2, 4, 6, or 8 digits long)"
        }
    if code not in hsn_dict:
        return {
            "code": code,
            "status": "Invalid",
            "reason": "Code not found in master dataset"
        }
    return {
        "code": code,
        "status": "Valid",
        "description": hsn_dict[code]
    }
