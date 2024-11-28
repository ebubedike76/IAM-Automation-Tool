#!/usr/bin/env python3
import random

def send_mfa_code(username):
    # Simulate sending a code (e.g., via email/SMS)
    mfa_code = str(random.randint(100000, 999999))
    print(f"MFA Code for {username}: {mfa_code}")
    return mfa_code

def verify_mfa_code(input_code):
    # Example verification logic, store sent code securely
    return input_code == '123456'
