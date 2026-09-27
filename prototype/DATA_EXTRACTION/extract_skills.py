import ollama

# 1. The Raw, Messy Job Description (Hardcoded for the video demo)
job_description = """
We are looking for a Full-Stack Developer to join our fast-paced team. 
The ideal candidate will have 2+ years of experience building UIs with React and Next.js. 
You must have strong backend experience designing APIs with Node.js and FastAPI. 
Experience with relational databases, specifically PostgreSQL, is required. 
Strong communication skills and agile methodology experience are a huge plus.
"""

# 2. The Strict Prompt 
prompt = f"""
Analyze the following job description and extract all technical and soft skills.
You must return the output STRICTLY as a valid JSON object with a single key "skills" containing a list of strings.
Do not include any introductory text, markdown, or explanations.

Job Description:
{job_description}
"""

print("Processing Job Description via Llama 3...\n")

# 3. Call the Local LLM (Enforcing JSON format)
response = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': prompt}],
    format='json'
)

# 4. Output the Result
print("--- EXTRACTED SKILLS (JSON) ---")
print(response['message']['content'])