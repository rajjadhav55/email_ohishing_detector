import pandas as pd

def load_dataset():
    return pd.read_csv('C:/Users/asus/projectcyber/datasets/sample_emails.csv')

def is_phishing(email_text):
    # Rule 1: Suspicious keywords
    red_flags = ["click", "verify", "urgent", "password", "suspended", 
                 "account", "prize", "winner", "login", "update"]
    
    # Rule 2: Suspicious domains
    suspicious_domains = [".xyz", ".top", ".gq", ".tk", ".rest"]
    
    # Rule 3: Excessive punctuation
    has_excessive_punctuation = sum(email_text.count(c) for c in ['!', '?', '$']) > 3
    
    # Check all rules
    return (
        any(flag in email_text.lower() for flag in red_flags) or
        any(domain in email_text.lower() for domain in suspicious_domains) or
        has_excessive_punctuation
    )

# Test
if __name__ == "__main__":
    emails = load_dataset()
    for _, row in emails.iterrows():
        print(f"Email: {row['text']}")
        print(f"Prediction: {'Phishing' if is_phishing(row['text']) else 'Legitimate'}")
        print("---")