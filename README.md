# backend

"Install" via clone  
Run with  `uvicorn main:api_app --reload`

Endpoints:

* `/` - non relevant, prints random stuff
* `/download/{app_name}` - to get the download link of app called `app_name`
* `/apps/` - given a criteria body fetches all apps that match the criteria.
This is a post request which requires a specific body that includes the fields: id (int), filter(dict), start(Optional int), end(Optional int)  
Request example - `curl -X 'POST' \
  'http://127.0.0.1:8000/apps/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "creator1",
  "filters": {},
  "start": 2,
  "end": 3

}'`

* `/my_apps/{creator_id}` - fetches all apps created by creator_id
