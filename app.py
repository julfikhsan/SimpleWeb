import os
from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

# Initialize the Gemini client (it automatically picks up GEMINI_API_KEY from environment variables)
client = genai.Client()

@app.route("/", methods=["GET", "POST"])
def index():
    ai_response = ""
    user_prompt = ""
    
    if request.method == "POST":
        user_prompt = request.form.get("prompt", "")
        if user_prompt:
            try:
                # Call Gemini API
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt,
                )
                ai_response = response.text
            except Exception as e:
                ai_response = f"Error generating AI response: {str(e)}"
                
    return render_template("index.html", user_prompt=user_prompt, ai_response=ai_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)