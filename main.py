# Import FastAPI class from the fastapi module
# FastAPI is the framework we use to build APIs
from fastapi import FastAPI

# Create an instance of the FastAPI application
# This 'app' object is what runs our API
app = FastAPI()

# -----------------------------
# 1. Root Endpoint ("/")
# -----------------------------

# @app.get("/") means:
# - This function will run when a client sends a GET request
# - The URL path is "/"
@app.get("/")
def read_root():
    # This function returns a Python dictionary
    # FastAPI automatically converts it to JSON
    return {"Hello": "World"}


# -----------------------------
# 2. Path + Query Parameters
# -----------------------------

# {item_id} is a PATH PARAMETER
# → It is part of the URL itself (e.g., /items/5)

# q is a QUERY PARAMETER
# → It is optional and comes after ? in the URL (e.g., ?q=search)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    # item_id: int  → FastAPI converts the URL string to an integer automatically
    #                  if someone visits /items/abc, FastAPI rejects it before this runs
    #
    # q: str | None = None  → q is an optional query parameter
    #                          Example: /items/42?q=hello  sets q = "hello"
    #                          Example: /items/42          sets q = None
    # Return both values as a JSON response
    return {
        "item_id": item_id,
        "q": q
    }