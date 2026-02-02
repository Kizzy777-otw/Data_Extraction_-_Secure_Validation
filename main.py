import re

#code reads user input (  from feedback_input.txt as a sample, you can edit it and test.)
with open("feedback_input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# the regex pattterns
patterns = {
    "emails found": re.compile(r"\S+@\S+\.\S+"),
    # checking email adress
    "urls found": re.compile(r"https?://\S+"),

    # Only accepting http/https URL links

    "phone numbers found (Rwanda)": re.compile(r"(?:\+250\d{9}|0\d{9})"),
    # Checking Rwanda phone numbers: +250785774712 and 0785774712 common formats

    "credit_cards found" : re.compile(r"(?:\d{4}[- ]?){3}\d{4}"),
    # Card numbers with spaces or dashes

    "times found": re.compile(r"\d{1,2}:\d{2}(?:\s?[APMapm]{2})?"),
    #checking fir both 24-hour and 12-hour times

    "hashtags found": re.compile(r"#\w+"),
    # Checking for hashtags

    "currency found": re.compile(r"RWF\s\d{1,3}(?:,\d{3})*"),

    # RWF currency amounts with no decimals
}

# Extracting  and print results

for key, pattern in patterns.items():
    matches = pattern.findall(text)

    # we hide the last 4 digits for security
    if "credit_cards" in key:
        matches = [re.sub(r"\d{4}$", "****", m) for m in matches]

    print(f"{key.capitalize()}:")
    if matches:
        for m in matches:
            print(f"- {m}")
    else:
        print("- None found")
    print()
