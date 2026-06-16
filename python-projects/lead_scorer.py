from groq import Groq

client = Groq(api_key="REDACTED")

def score_lead(name, email, phone, property_type, budget):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a UAE real estate lead scoring expert. Score leads as HOT, WARM or COLD with one sentence reason."
            },
            {
                "role": "user",
                "content": f"""Score this lead:
                Name: {name}
                Email: {email}
                Phone: {phone}
                Property: {property_type}
                Budget: AED {budget}"""
            }
        ]
    )
    return response.choices[0].message.content

# Test
result = score_lead("Ahmed", "ahmed@gmail.com", 
                    "0501234567", "Villa", 2000000)
print("Lead Score:", result)
