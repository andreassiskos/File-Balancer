from itertools import count
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()
FILE_DIRECTORY = "./saved_files/"
EXTENTION_OF_DIR = ""

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):

    for file in files:
        string = file.file.read()

        with open(FILE_DIRECTORY + EXTENTION_OF_DIR + file.filename, "wb") as binary_file:
            binary_file.write(string)

    return {"submitted_filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
