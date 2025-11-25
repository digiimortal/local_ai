from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/transcript")
def read_transcription():
    return {"transcription": "This is a sample transcription page."}

# API Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

