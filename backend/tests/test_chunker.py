from app.services.chunker import chunk_text, chunk_document


def test_chunk_text():
    text = "A" * 1000

    chunks = chunk_text(text, 500, 100)

    assert len(chunks) == 3
    assert len(chunks[0]) == 500
    assert chunks[0][-100:] == chunks[1][:100]


def test_chunk_document():
    pages = [
        {"page": 1, "text": "Hello " * 100}
    ]

    chunks = chunk_document(pages)

    assert len(chunks) > 0
    assert chunks[0]["page"] == 1
    assert "text" in chunks[0]
