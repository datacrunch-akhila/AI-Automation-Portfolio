from groq import Groq
from pypdf import PdfReader

client = Groq(api_key="your-groq-key")

def read_cv(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def tailor_cv(cv_text, job_description):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """You are Akhila Varakil's personal CV editor.
                Edit her CV summary to match the job description.
                Keep it ATS friendly, under 4 sentences."""
            },
            {
                "role": "user",
                "content": f"""
                My CV: {cv_text[:2000]}
                Job Description: {job_description}
                Write tailored summary only.
                """
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

# Test
cv = read_cv(r"C:\Users\Abhitha\Desktop\Akhila_Varakil_CV.pdf")
jd = "Looking for n8n developer with AI automation experience in Dubai"
print("Tailored Summary:")
print(tailor_cv(cv, jd))
