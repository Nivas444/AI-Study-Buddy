from transformers import pipeline

# Load question generation & QA model
qa_model = pipeline("question-generation")

def generate_mcqs(text):
    """Generate MCQs or short questions from text"""
    questions = qa_model(text)
    mcqs = []
    for q in questions:
        mcqs.append({"question": q['question'], "answer": q['answer']})
    return mcqs

# Example usage
if __name__ == "__main__":
    sample_text = "Python is a popular programming language."
    print(generate_mcqs(sample_text))
