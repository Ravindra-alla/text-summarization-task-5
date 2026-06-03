import time
import re
import numpy as np
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

print("Starting the summarization app...")
print("Loading the Transformers summarization model. This may take a few minutes the first time.")

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

print("Model loaded successfully.")


def extract_metrics(text):
    words = [w for w in re.findall(r"\w+", text)]
    word_count = len(words)
    char_count = len(text)
    avg_word_len = round(np.mean([len(word) for word in words]) if words else 0, 1)
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentence_count = len([s for s in sentences if s.strip()])

    return {
        "word_count": word_count,
        "char_count": char_count,
        "avg_word_length": avg_word_len,
        "sentence_count": sentence_count,
    }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json(silent=True) or {}
    text = data.get('text', '').strip()

    if not text:
        return jsonify({"error": "Please enter some text to summarize."}), 400

    if len(text) < 20:
        return jsonify({"error": "Please enter at least 20 characters."}), 400

    # Restrict the text length to avoid very long model inputs.
    words = text.split()
    if len(words) > 800:
        text = " ".join(words[:800])

    inputs = tokenizer(text, max_length=1024, truncation=True, return_tensors="pt")
    start = time.time()
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=130,
        min_length=30,
        num_beams=4,
        early_stopping=True,
    )
    duration = round(time.time() - start, 3)

    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()

    return jsonify({
        "summary": summary_text,
        "time_taken": duration,
        "input_metrics": extract_metrics(data.get('text', '').strip()),
        "summary_metrics": extract_metrics(summary_text),
    })


if __name__ == '__main__':
    app.run(debug=True)
