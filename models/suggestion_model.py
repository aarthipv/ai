from transformers import pipeline

# Load a pre-trained model for contextual suggestions (e.g., GPT-2)
suggestion_model = pipeline('text-generation', model='gpt2')

def get_suggestions(text):
    suggestions = suggestion_model(text, max_length=50, num_return_sequences=3)
    return [s['generated_text'] for s in suggestions]
