email = input("email: ").strip().lower() # Osama@Nn.Sa

print(f"Your Name Is {email[:-6].title()}") # Osama
print(f"Email Service Provider Is {email[-5:-3]}") # nn
print(f"Top Level Domain Is {email[-2:]}") # sa
