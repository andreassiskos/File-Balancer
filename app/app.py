from fileinput import filename
from itertools import count
from pickle import TRUE
from tokenize import String
from typing import List
from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import HTMLResponse, FileResponse
import os.path 
from datetime import date

app = FastAPI()
FILE_DIRECTORY = "saved_files/"
EXTENTION_OF_DIR = ""
ACCEPTED_FILENAMES = ["txt", "yaml", "pdf"]
ACCEPTED_VALUE = True

def add_date():
    today = date.today()
    d3 = today.strftime("%m-%Y")
    return d3 + "/"

def distribute_file_based_on_filename(filename):
    splited_name = filename.split(".")
    if(len(splited_name) == 1 and "" in ACCEPTED_FILENAMES):
        return "General/", True
    if(len(splited_name) == 1 and "" not in ACCEPTED_FILENAMES):
        return splited_name[0] , False
    
    if(splited_name[-1] not in ACCEPTED_FILENAMES):
        return splited_name[0] , False

    return str(splited_name[-1]) + "/" , True

def check_and_create_directory(dirname):

    dir_components = dirname.split("/")
    curr_dir = ""

    for i in range(len(dir_components) - 1 ):
        
        curr_dir += dir_components[i] + "/"
        isdir = os.path.exists(curr_dir)
        
        if(not isdir):
            os.mkdir(curr_dir)

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    not_accepted_files = []
    accepted_files = []
    for file in files:
        string = file.file.read()
        EXTENTION_OF_DIR, ACCEPTED_VALUE  = distribute_file_based_on_filename(file.filename)
        
        if(not ACCEPTED_VALUE):
            not_accepted_files.append(file)
            continue
            #return {"Error": "Not Accepted Type of file " + EXTENTION_OF_DIR + ". Please try again."}
        accepted_files.append(file)

        new_dir_name = FILE_DIRECTORY + EXTENTION_OF_DIR 
        new_dir_name_plus_date = new_dir_name + add_date()
        
        check_and_create_directory(new_dir_name_plus_date)
        
        with open(new_dir_name_plus_date + file.filename, "wb") as binary_file:
            binary_file.write(string)
        print(new_dir_name_plus_date)
    return {"Accepted_filenames": [file.filename for file in accepted_files],
            "Rejected_filenames": [file.filename for file in not_accepted_files]}


@app.get("/getfiles/", response_class=FileResponse)
async def get_files(q: list = Query(default=[])):
    return "saved_files/txt/07-2022/hello.txt"

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
