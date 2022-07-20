# File-Balancer
A File Balancer written in FastAPI

## Create and Activate Virtual Environment:
1. Open Terminal
2. Type:
  python3 -m venv venv
  source venv/bin/activate

## Install requirements
1. Type:
  pip3 install -r requirements.txt

## How to run:

1. Go to folder app:
  cd app
2. Type:
  python -m uvicorn app:app --reload
3. Open a Browser and go to:
  http://127.0.0.1:8000 or go to http://127.0.0.1:8000/docs to use it through the swagger UI
  
## TODO:

1. Make a Docker Container
2. Make a nice web interface
3. Test it in cloud
4. Use database instead of directories
5. Use kubernetes
