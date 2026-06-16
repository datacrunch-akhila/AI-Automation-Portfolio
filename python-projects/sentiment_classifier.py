from groq import Groq

client = Groq(api_key="REDACTED")

# TOOL 1
def classify_sentiment(text):
    """Classify sentiment of customer feedback"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Return ONLY: SENTIMENT: [POSITIVE/NEGATIVE/NEUTRAL], PRIORITY: [URGENT/NORMAL/LOW], REASON: [one sentence]"},
            {"role": "user", "content": f"Analyze: {text}"}
        ]
    )
    return response.choices[0].message.content

# TOOL 2
def decide_action(sentiment_result):
    """Decide what action to take based on sentiment"""
    if "URGENT" in sentiment_result:
        return "🚨 ACTION: Escalate to manager immediately"
    elif "NEGATIVE" in sentiment_result:
        return "📧 ACTION: Send apology email to customer"
    elif "POSITIVE" in sentiment_result:
        return "⭐ ACTION: Request Google review from customer"
    else:
        return "📝 ACTION: Log for weekly review"

# AGENT LOOP — this is what makes it an agent!
def run_sentiment_agent(feedbacks):
    print("🤖 Sentiment Analysis Agent Running...")
    print("=" * 50)
    
    for feedback in feedbacks:
        print(f"\n📝 Processing: {feedback[:50]}...")
        
        # Agent decides to use classify tool
        sentiment = classify_sentiment(feedback)
        print(f"Analysis: {sentiment}")
        
        # Agent decides next action
        action = decide_action(sentiment)
        print(f"Decision: {action}")
        print("-" * 40)

# Run the agent
feedbacks = [
    "Absolutely terrible experience! Court double booked!",
    "Great facility, loved playing here today!",
    "Booking was fine, nothing special.",
    "App crashed 3 times, lost my booking money!"
]

run_sentiment_agent(feedbacks)
