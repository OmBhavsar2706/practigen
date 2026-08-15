import os  # Import operating system module for reading environment variables
from dotenv import load_dotenv  # Import load_dotenv function to parse .env file
from flask import Flask, jsonify, render_template, request  # Import Flask web framework utilities
from google import genai  # Import Google GenAI SDK package

load_dotenv()  # Load environment key-value pairs from .env file

api_key = os.getenv("GEMINI_API_KEY")  # Retrieve Gemini API key from environment
client = genai.Client(api_key=api_key) if api_key else None  # Initialize Google GenAI client if key exists
app = Flask(__name__)  # Initialize main Flask application instance (creates server)

PROMPT = (  # Define string template containing Gemini prompt
    "You are helping an MSBTE diploma student complete their practical file.\n\n"  # System persona statement
    "Subject: {subject}\nPractical Name: {practical}\nPractical Related Questions: {questions}\n\n"  # Dynamic placeholders
    "Generate exactly TWO sections:\n\n"  # Output section instruction
    "CONCLUSION:\n"  # Conclusion section header
    "Write 3-4 sentences concluding this practical. Mention what was done, what was learned, and that the practical was completed successfully. Keep it simple and suitable for a diploma student. Do not use complex English.\n\n"  # Conclusion instructions
    "ANSWERS TO PRACTICAL RELATED QUESTIONS:\n"  # Answers section header
    "Answer each question the student provided. Number each answer matching the question number. Write 3-5 simple lines per answer. Use plain, easy English.\n\n"  # Answers instructions
    "IMPORTANT RULES:\n"  # Important rules header
    "- Generate ONLY the above two sections\n"  # Rule 1 constraint
    "- Do NOT write Aim, Theory, Procedure, or anything else\n"  # Rule 2 constraint
    "- If a question asks for program output or screenshot, write the answer but add a note: '[Attach actual output]' at the end of that answer"  # Rule 3 constraint
)  # Close prompt template definition

@app.route("/")  # Register route handler for HTTP GET request on root endpoint
def index():  # Handler function for rendering homepage
    return render_template("index.html")  # Render and return index.html HTML document

@app.route("/generate", methods=["POST"])  # Register route handler for HTTP POST generation endpoint
def generate():  # Handler function processing form submissions
    try:  # Start error handling block for API execution
        current_api_key = os.getenv("GEMINI_API_KEY")  # Get current API key from environment
        if not current_api_key:  # Check if GEMINI_API_KEY is configured
            return jsonify({"error": "GEMINI_API_KEY is missing. Please set it in .env file."}), 500

        sub = request.form.get("subject", "").strip()  # Extract subject input parameter from request form
        prac = request.form.get("practical", "").strip()  # Extract practical name parameter from request form
        ques = request.form.get("questions", "").strip()  # Extract questions input parameter from request form

        if not sub or not prac or not ques:  # Validate that all required fields are provided
            return jsonify({"error": "Please fill out all fields (Subject, Practical Name, and Questions)."}), 400

        active_client = client if client else genai.Client(api_key=current_api_key)  # Ensure active client instance

        prompt_text = PROMPT.format(subject=sub, practical=prac, questions=ques)  # Format prompt template with user inputs
        res = active_client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt_text
        )  # Send populated prompt to Gemini API using google-genai SDK and get response
        
        if res.text:  # Check if model generated text output
            return jsonify({"result": res.text})  # Return generated response text as JSON object
        else:
            return jsonify({"error": "Failed to generate content. Please try again."}), 500
    except Exception as e:  # Handle runtime exceptions during API execution
        return jsonify({"error": str(e)}), 500  # Return error message as JSON response

if __name__ == "__main__":  # Verify script is executed directly from command line
    app.run(debug=True, port=5000)  # Launch Flask development application server on port 5000 in debug mode
