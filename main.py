from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "fastapi-backend"
    }

num1 = 10
num2 = 20

sum = num1 + num2

print("The sum is:", sum)
print("Done!")
if sum > 0:
    print("Positive sum")
