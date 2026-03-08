from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.services.document_ingestion_service import process_document

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    filename = file.filename or "uploaded_file"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("File saved:", file_path)

    process_document(file_path)

    return {"message": "Document uploaded and processing started"}