from typing import Optional, Union
from datetime import date

from pydantic import BaseModel


class App:
    id: int
    _name: str
    _download_link: str
    price: int
    rating: float
    description: str
    img_url: str
    sha: str
    version: int
    publication_date: str
    creator: str

    def __init__(self, id: int, name: str, download_link: str, price: int, img_url: str, sha: str,
                 creator: str, desc: str = "", version: int = 1, rating: int = None) -> None:
        self.id = id
        self._name = name
        self._download_link = download_link
        self.price = price
        self.rating = rating
        self.description = desc
        self.img_url = img_url
        self.sha = sha
        self.version = version
        self.publication_date = str(date.today())
        self.creator = creator

    @property
    def download_link(self):
        return self._download_link

    @property
    def name(self):
        return self._name

    def __str__(self) -> str:
        return f"App {self._name} can be downloaded from {self._download_link}"

    def jsonify(self) -> dict:
        return {
            "id": self.id,
            "name": self._name,
            "download_link": self._download_link,
            "price": self.price,
            "rating": self.rating,
            "description": self.description,
            "img_url": self.img_url,
            "sha": self.sha,
            "version": self.version,
            "publication_date": self.publication_date,
            "creator": self.creator
        }


class AppCollection:
    apps = {} # name: App

    def __init__(self, apps: dict = None) -> None:
        if apps:
            self.apps = apps

    def insert_app(self, app) -> None:
        self.apps[app.name] = app

    def remove_app(self, app) -> None:
        del self.apps[app.name]

    def __getitem__(self, key) -> App:
        return self.apps.get(key)

    def __iter__(self) -> Union[str, App]:
        for k, v in self.apps.items():
            yield v



class AppRequestBody(BaseModel):
    id: str # creator id?
    filters: dict
    start: Optional[int] = -1
    end: Optional[int] = -1
    # order: dict
    



    
        
