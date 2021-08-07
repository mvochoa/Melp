import uvicorn
import os

from fastapi import FastAPI

from controllers import restaurant_controller

app = FastAPI(title="Melp", version=os.environ.get("VERSION", "local"))
app.include_router(restaurant_controller.router)


@app.get("/")
def main():
    return {
        "commit": os.environ.get('VERSION', ''),
        "github": "https://github.com/mvochoa/melp"
    }


if __name__ == "__main__":
    log_level = "info"
    reload = True
    if os.getenv("PYTHON_ENV") == "production":
        log_level = "error"
        reload = False
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", "8000")),
                log_level=log_level, reload=reload)
