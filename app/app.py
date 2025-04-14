from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# A simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


# A simple GET endpoint to check the health of the app
@app.get("/health")
def health_check():
    return {"status": "healthy"}
