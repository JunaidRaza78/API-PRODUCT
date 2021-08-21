#  REST API 
http://127.0.0.1:8000/api/products/
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
id = []
Code: 200 
Content: { id : 1, name : "shirt", Color: "black", size:large }
HTTP 404 Not Found
Content: { Code: 404 NOT FOUND }
Vary: Accept

{
    "id": 1,
    "name": "shirts",
    "Color": "black",
    "size": "large"
}