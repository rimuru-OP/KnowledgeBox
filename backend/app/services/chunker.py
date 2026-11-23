def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be non-negative and smaller than chunk size")

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_document(pages: list[dict], chunk_size=500, overlap=100):

    document_chunks = []

    for page in pages:

        chunks = chunk_text(
            page["text"],
            chunk_size,
            overlap
        )

        for index, chunk in enumerate(chunks):

            document_chunks.append({
                "text": chunk,
                "page": page["page"],
                "chunk_index": index
            })

    return document_chunks
