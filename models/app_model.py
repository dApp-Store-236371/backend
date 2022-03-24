class App():
    _name: str
    _download_link: str
    ...
    # category, price

    def __init__(self, name: str, download_link: str) -> None:
        self._name = name
        self._download_link = download_link

    @property
    def download_link(self):
        return self._download_link

    @property
    def name(self):
        return self._name

    def __str__(self) -> str:
        return f"App {self._name} can be downloaded from {self._download_link}"


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

    



    
        
