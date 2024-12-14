from transformers import LongformerTokenizer, LongformerForSequenceClassification
import torch

tokenizer = LongformerTokenizer.from_pretrained('allenai/longformer-base-4096')
model = LongformerForSequenceClassification.from_pretrained('allenai/longformer-base-4096', num_labels=6)


def check_plagiarism_with_longformer(text1, text2):
    inputs = tokenizer([text1, text2], return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    return torch.argmax(logits).item()  # Returns class label (0 or 1)
