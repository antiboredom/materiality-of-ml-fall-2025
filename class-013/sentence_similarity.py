# Examples modified from https://www.sbert.net/

from sentence_transformers import SentenceTransformer

# any of these models will work: https://huggingface.co/models?library=sentence-transformers
model = SentenceTransformer("all-MiniLM-L6-v2")

# query
query = "Hello this is a test."

# sentences to compare
sentences = [
    "The dog plays in the garden",
    "This is an exam.",
    "We are doing an experiement",
]

# compute the query embeddings
embeddings1 = model.encode(query)

# compute the sentence embeddings
embeddings2 = model.encode(sentences)

# Compute cosine similarities
similarities = model.similarity(embeddings1, embeddings2)

# sort by most similar
similarities = sorted(zip(sentences, similarities[0]), key=lambda x: x[1], reverse=True)

# print the results
for sentence, score in similarities:
    print(float(score), sentence)
