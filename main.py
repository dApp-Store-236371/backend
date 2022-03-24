from email.policy import HTTP
from turtle import down
from fastapi import FastAPI, status
from models.app_model import App, AppCollection
from fastapi.responses import JSONResponse

api_app = FastAPI()

sandbox_db = AppCollection({
    "A": App("A", "d1"),
    "B": App("B", "d2")
    })


@api_app.get("/")
def root():
    return "Goodbye Moon"


@api_app.get("/download/{app_name}")
async def fetch_download_link(app_name: str) -> str:
    app_obj = sandbox_db[app_name]
    
    if not app_obj:
        return JSONResponse(content={"link": None},
                            status_code=status.HTTP_404_NOT_FOUND)
    download_link = app_obj.download_link

    if not download_link:
        return JSONResponse(content={"link": None},
                            status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content={"link": download_link},
                        status_code=status.HTTP_200_OK)
