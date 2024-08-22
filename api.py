from fastapi import FastAPI  # type: ignore
from fastapi.middleware.cors import CORSMiddleware  # type: ignore

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    """
    Default route to welcome users and direct them to documentation.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Hi, add /docs to the URL to use the API."}


@app.post("/recover_data")
async def recover_data():
    """
    Endpoint to recover data from
    player and store them in database.

    Args:
        str (text): The tweet.

    Returns:
        Response: The response containing the predicted sentiment.
    """
    return
