# Examples modified from https://www.sbert.net/

from glob import glob
from sentence_transformers import SentenceTransformer, util

# any of these models will work: https://huggingface.co/models?library=sentence-transformers
model = SentenceTransformer("all-MiniLM-L6-v2")

# search query
query = "food"

corpus = []

# open a text file and read lines into a list
# with open("mobydick_the_book.txt", "r") as f:
#     corpus = f.readlines()
#     corpus = [line.strip() for line in corpus if line.strip()]

# or open a series a of text files in a directory
# you could also read these one line at a time rather than the whole files
for f in glob("*.txt"):
    with open(f, "r") as f:
        content = f.read()
        corpus.append(content)


# create an embedding for the query
query_embedding = model.encode(query, convert_to_tensor=True)

# create an embedding for the corpus
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

# find the top 100 most similar sentences in the corpus to the query
search_hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=10)[0]

# print the results
for hit in search_hits:
    index = hit["corpus_id"]
    score = hit["score"]
    print(score, corpus[index])
