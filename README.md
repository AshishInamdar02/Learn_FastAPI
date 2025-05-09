# Learn Fast API

- To install FastAPI, use pip installer. FastAPI depends on Starlette and Pydantic libraries, hence they also get installed.
  &nbsp;
  `pip3 install fastapi`
  &nbsp;
- FastAPI doesnt come with any built-in server application. To run FastAPI app, you need an ASGI server called **uvicorn**.
  &nbsp;  
   `pip3 install uvicorn`
  &nbsp;
- First step is to declare application object of FastAPI Class. This app object is the main point of interaction of the application with the client browser. The uvicorn server uses this object to listen to clients request.
  &nbsp;
  ```
  from fastapi import FastAPI
  app = FastAPI()
  ```
  &nbsp;
- Next step is to create path operation. Path is a URL which when visited by the client invokes, visits a mapped URL to one of the HTTP methods, an associated function is to be executed.
  &nbsp;
- We need to bind a view function to a URL and the corresponding HTTP method. For example, the index() function corresponds to / path with get operation.
  &nbsp;
  ```
  @app.get("/")
  async def index():
    return {"message": "Hello World"}
  ```
- The function returns a JSON response, however, it can return **dict, list, str, int, etc.** It can also return Pydantic models.
  &nbsp;
- Start the uvicorn server by mentioning the file in which the FastAPI application object is instantiated.
  &nbsp;
  ```
  uvicorn main:app --reload
  ```
  &nbsp;
- Open the browser and visit http://localhost:/8000. You will see the JSON response in the browser window.
  &nbsp;
- Opening the URl (http://127.0.0.1:8000/docs) in browser will automatically generate interactive documentation.FastAPI uses Swagger UI to produce this documentation.
  &nbsp;
- This shows **Curl** command internally executed, the request URL, the response headers, and the JSON format of the servers response.
  &nbsp;
- FastAPI generates a schema using OpenAPI specifications. The specification determines how to define API paths, path parameters, etc.
  &nbsp;
- The API schema defined by the OpenAPI standard decides how the data is sent using JSON Schema. Visit http://127.0.0.1:8000/openapi.json from your browser.
  &nbsp;
- FastAPI also supports another automatic documentation method provided by Redoc ( https://github.com/Redocly/redoc).Enter the URL (http://localhost:8000/redoc)
  &nbsp;
- FastAPI doesnt contain any built-in development server, It implements ASGI standards and is lightning fast. ASGI stands for **Asynchronous Server Gateway Interface.**
  &nbsp;
- The WSGI (Web Server Gateway Interface the (older standard)) compliant web servers are not suitable for asyncio applications. Uvicorn uses uvloop and httptools libraries. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.
  &nbsp;
- uvloop id is similar to the built-in asyncio event loop and httptools library handles the http protocols.
  &nbsp;
- Relational State Transfer (REST) is a software architectural style. REST defines how the architecture of a web application should behave. It is a resource based architecture where everything that the REST server hosts, (a file, an image, or a row in a table of a database), is a resource, having many representations.
  &nbsp;
- REST uses HTTP verbs or methods for the operation on the resources. The POST, GET, PUT and DELETE methods perform CREATE, READ, UPDATE and DELETE operations respectively.
