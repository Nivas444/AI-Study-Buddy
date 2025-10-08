
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
print(summarizer("Hello world!"))
