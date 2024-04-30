from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from transformers import pipeline

# Initialize the FastAPI app
app = FastAPI()

# Load the sentiment analysis pipeline
sentiment_model = pipeline("text-classification", model="MarieAngeA13/Sentiment-Analysis-BERT")


# Define a Pydantic model for the input data
class Text(BaseModel):
    text: str

    @validator('text')
    def must_not_be_blank(cls, value):
        if not value.strip():  # Check if the text is not just whitespace
            raise ValueError('Text must not be empty or just whitespace')
        return value

@app.get("/")
def read_root():
    return {"Hello": "Welcome to our Sentiment Analysis API, type '/docs' after the <URL> to access the Swagger UI"}

@app.post("/analyze")
def analyze(text: Text):
    try:
        # Process the text through the sentiment analysis model
        result = sentiment_model(text.text)
        return {"result": result}
    except ValueError as ve:
        # Handle validation errors, which occur when text is empty or just whitespace
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # Handle all other kinds of unexpected errors
        raise HTTPException(status_code=500, detail="An error occurred during the analysis.")
