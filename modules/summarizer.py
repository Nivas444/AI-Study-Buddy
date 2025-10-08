from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")  # force PyTorch


def summarize_text(text, max_length=130, min_length=30):
    """Summarize given text"""
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Example usage
if __name__ == "__main__":
    sample_text = "Your long text here..."
    print(summarize_text(sample_text))
