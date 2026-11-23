
from app.services.embeddings import generate_embeddings
import numpy as np

sentences = [
    "How do I learn Python?",
    "What is the best way to study Python?",
    "I enjoy playing football."
]

vectors = generate_embeddings(sentences)

similarity = np.dot(
    vectors,
    np.array(vectors).T
)

print(similarity)
