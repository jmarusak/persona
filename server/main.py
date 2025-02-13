from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on App Engine!"}

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
