from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration de la base de données SQLite
DATABASE_URL = "sqlite:///./snake_game.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Modèle de base de données
class GameData(Base):
    __tablename__ = "game_data"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    game_time = Column(Float)
    snake_head_x = Column(Integer)
    snake_head_y = Column(Integer)
    current_food_position_x = Column(Integer)
    current_food_position_y = Column(Integer)
    previous_food_position_x = Column(Integer)
    previous_food_position_y = Column(Integer)


# Créer la table dans la base de données
Base.metadata.create_all(bind=engine)

# Initialisation de l'application FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


# Modèle Pydantic pour les données reçues
class GameDataRequest(BaseModel):
    score: int
    game_time: float
    snake_head_position: dict  # {"x": int, "y": int}
    current_food_position: dict  # {"x": int, "y": int}
    previous_food_position: dict  # {"x": int, "y": int}


@app.get("/")
def hello():
    """
    Default route to welcome users and direct them to documentation.

    Returns:
        dict: A welcome message.
    """

    return {"message": "Hi, add /docs to the URL to use the API."}


@app.post("/recover_data")
async def recover_data(data: GameDataRequest):
    """
    Endpoint to recover data from user and store it in a DB.

    Returns:
        dict: A successfull message with the data ID.
    """

    db = SessionLocal()
    try:
        # Créer un enregistrement de données de jeu
        game_data = GameData(
            score=data.score,
            game_time=data.game_time,
            snake_head_x=data.snake_head_position['x'],
            snake_head_y=data.snake_head_position['y'],
            current_food_position_x=data.current_food_position['x'],
            current_food_position_y=data.current_food_position['y'],
            previous_food_position_x=data.previous_food_position['x'],
            previous_food_position_y=data.previous_food_position['y']
        )
        db.add(game_data)
        db.commit()
        db.refresh(game_data)
        return {"message": "Data saved successfully", "data_id": game_data.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An error occurred while \
                            saving the data")
    finally:
        db.close()


@app.get("/game_data")
async def get_game_data():
    """
    Endpoint to consult data in the DB.
    """

    db = SessionLocal()
    try:
        game_data_list = db.query(GameData).all()
        return game_data_list
    finally:
        db.close()
