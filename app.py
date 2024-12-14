from flask import Flask, render_template, request, jsonify
from models.grammar_model import correct_grammar
from models.suggestion_model import get_suggestions
from models.enhancement_model import enhance_content
from models.plagiarism_model import check_plagiarism_with_longformer  # Import the Longformer function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():
    text = request.json['text']
    corrected_text = correct_grammar(text)
    return jsonify({'corrected_text': corrected_text})

@app.route('/suggest', methods=['POST'])
def suggest():
    text = request.json['text']
    suggestions = get_suggestions(text)
    return jsonify({'suggestions': suggestions})

@app.route('/enhance', methods=['POST'])
def enhance():
    text = request.json['text']
    enhanced_text = enhance_content(text)
    return jsonify({'enhanced_text': enhanced_text})

@app.route('/plagiarism', methods=['POST'])
def plagiarism():
    text = request.json['text']
    
    # Define or retrieve your reference text
    reference_text = """This is an example of a reference text that will be used for comparison."""
    
    # Call the updated plagiarism check function using Longformer
    result = check_plagiarism_with_longformer(text, reference_text)
    
    return jsonify({'is_plagiarized': result})

if __name__ == '__main__':
    app.run(debug=True)
