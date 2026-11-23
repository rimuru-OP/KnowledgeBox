from app.services.embeddings import generate_embeddings


def test_generate_embeddings():

    texts = [
        "I love machine learning",
        "Artificial intelligence is fascinating"
    ]

    embeddings = generate_embeddings(texts)

    assert len(embeddings) == 2
    assert len(embeddings[0]) == 384
    assert len(embeddings[1]) == 384
