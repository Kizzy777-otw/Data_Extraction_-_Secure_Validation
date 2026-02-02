# RenewEnergy Regex Data Extraction & Secure Validation

We collects our customer feedback to check if renewable energy systems (like solar panels or biogas) are properly functioning.  
WE use regex to identify structured data such as emails, URLs, phone numbers, credit card numbers, times, hashtags, and currency amounts.

**Context:**
- Customers are **the users of the systems we installed**. They do not install the systems themselves so they need help with maintenance.
- If they meet any isuues, they **either call in to report problems or share feedback**.
- This feedback is processed by the system to extract useful information safely.



## Data Types Extracted
The program looks for:
- **Emails** : `super.mane@customer.com`
- **URLs** eg: `https://renewenergyreviews.org/my-story`
- **Phone numbers** only commonly used formats in Rwanda `+250785774712`, `+250 785774712`, `0785774712`
- **Credit cards** : `9876-5432-1098-****` (last 4 digits masked)
- **Times** : `14:30`, `2:30 PM`
- **Hashtags** : `#RenewEnergy`, `#SolarPower`
- **Currency (RWF)** : `RWF 1,234` (whole amounts only, no decimals)



## Security
1. Unsafe links as `javascript:alert('hack')` are ignored.
2. Credit card numbers are hidden with **** at the end.
3. Only well-written and formatted input is accepted.



## Project Files
main.py: for Python code
feedback_input.txt:for Sample feedback text  
README.md : for Documentation
## How to Run
run python main.py
it will run the information in feedback_input.txt
if you want to change the information, use the nano or vim text editors to test the program.