from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.parser import extract_text_from_pdf

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    file_bytes = await file.read()

    if not file_bytes:
        raise HTTPException(
            status_code=400,
            detail="Empty file"
        )

    try:
        pages = extract_text_from_pdf(file_bytes)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Could not process PDF"
        )

    return {
        "filename": file.filename,
        "total_pages": len(pages),
        "pages": pages
    }
