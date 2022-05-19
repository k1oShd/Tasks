import os
import re
import tempfile
import shutil
from pathlib import Path
from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/readfile/")
async def main(in_file: UploadFile):
    content = await in_file.read()
    await in_file.close()
    return {"content": content}

@app.post("/writefile/")
async def main(in_file: UploadFile):
    content = bytes(input(),encoding='utf8')
    destination = f"files/{in_file.filename}"
    await in_file.write(content)
    try:
        with open(destination, "wb+") as buffer:
            shutil.copyfileobj(in_file.file, buffer)
    finally:
        in_file.file.close()
    return {"content": "New content is added!"}

@app.post("/updatefile/")
async def main(in_file: UploadFile):
    content = bytes(input(),encoding='utf8')
    destination = f"files/{in_file.filename}"
    await in_file.write(bytes('\n',encoding='utf8'))
    await in_file.write(content)
    try:
        with open(destination, "wb+") as buffer:
            shutil.copyfileobj(in_file.file, buffer)
    finally:
        in_file.file.close()
    return {"content": "The content is updated!"}

@app.post("/deletefile/")
async def main(in_file: UploadFile):
    destination = f"files/{in_file.filename}"
    try:
        os.remove(destination)
    finally:
        return {"content": "The file is deleted!"}