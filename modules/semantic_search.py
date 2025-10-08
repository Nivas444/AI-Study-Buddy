from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_search(query, documents, top_k=3):
    """Search documents semantically"""
    doc_embeddings = model.encode(documents, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, doc_embeddings, top_k=top_k)
    return [documents[i['corpus_id']] for i in hits[0]]

# Example usage
if __name__ == "__main__":
    docs = ["Python is a programming language.", "AI Study Buddy helps in learning."]
    print(semantic_search("learning with AI", docs))
