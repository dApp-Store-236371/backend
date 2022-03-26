from email.policy import HTTP
from turtle import down
from fastapi import FastAPI, status
from models.app_model import App, AppCollection, AppRequestBody
from fastapi.responses import JSONResponse

api_app = FastAPI()

sandbox_db = AppCollection({
    "A": App(1, "A", "d1", 10, "img1", "sha1", "creator1"),
    "B": App(2, "B", "d2", 20, "img2", "sha2", "creator2"),
    "C": App(3, "C", "d3", 30, "img3", "sha3", "creator1"),
    "D": App(4, "D", "d4", 20, "img2", "sha2", "creator3"),
    "E": App(5, "E", "d5", 20, "img2", "sha2", "creator4")
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


@api_app.post("/apps/")
async def fetch_apps(req: AppRequestBody):
    contains = req.filters.get("name", "")

    start = req.start
    end = req.end
    use_bounds = start != -1 and end != -1

    creator = req.id
    response = {}

    for idx, app in enumerate(sandbox_db):
        if app.creator == creator and contains in app.name:
            if use_bounds:
                if start <= app.id <= end:
                    response[idx] = app.jsonify()
            else:
                response[idx] = app.jsonify()

    return JSONResponse(content=response,
                        status_code=status.HTTP_200_OK)


