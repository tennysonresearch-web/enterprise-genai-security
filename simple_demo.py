"""
Simple PII Detection Demo
A minimal example of multi-layer PII detection
"""

import re

def detect_pii_simple(text):
    """
    Simple PII detection for demo purposes
    """
    
    # Pattern definitions
    patterns = {
        'SSN': r'\b\d{3}-\d{2}-\d{4}\b',
        'Phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'Email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'Credit Card': r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'
    }
    
    results = []
    
    # Check each pattern
    for pii_type, pattern in patterns.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            results.append({
                'type': pii_type,
                'value': match.group(),
                'position': (match.start(), match.end())
            })
    
    return results

# Test the function
if __name__ == "__main__":
    test_text = "Call me at 555-123-4567 or email john@example.com. My SSN is 123-45-6789."
    
    print("Testing PII Detection")
    print("-" * 40)
    print(f"Input: {test_text}")
    print("-" * 40)
    
    detections = detect_pii_simple(test_text)
    
    print(f"Found {len(detections)} PII elements:")
    for item in detections:
        print(f"  - {item['type']}: {item['value']}")
