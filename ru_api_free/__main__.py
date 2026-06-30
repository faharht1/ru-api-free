import uvicorn
from .main import app


def main():
    uvicorn.run("ru_api_free.main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
