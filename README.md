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
  &nbsp;
- Modern web frameworks use routes or endpoints as a part of URL instead of file-based URLs. This helps the user to remember the application URLs more effectively.
  &nbsp;
- In FastAPI, it is termed a path. A path or route is the part of the URL trailing after the first /. In http://localhost:8000/hello/, /hello would be the path or the route.
  &nbsp;
- In FastAPI, such a path string is given as a parameter to the operation decorator. The operation here refers to the HTTP verb used by the browser to send the data. These operations include GET, PUT, etc. The operation decorator (for example, @app.get("/")) is immediately followed by a function that is executed when the specified URL is visited.
  &nbsp;
  ```
  from fastapi import FastAPI
  app = FastAPI()
  @app.get("/")
  async def index():
    return {"message": "Hello World"}
  ```
  &nbsp;
- **Here, ("/") is the path, get is the operation, @app.get("/") is the path operation decorator, and the index() function just below it is termed as path operation function.**
  &nbsp;
- Any of the following HTTP verbs can be used as operations: GET, HEAD, POST, PUT, DELETE.
  &nbsp;
- The async keyword in the functions definition tells FastAPI that it is to be run asynchronously i.e. without blocking the current thread of execution. However, a path operation function can be defined without the async prefix also.
  &nbsp;
- The decorated function returns a JSON response. Although it can return almost any of Pythons objects, it will be automatically converted to JSON.
  &nbsp;
- The URLs endpoint or path can have one or more variable parameters. They can be accepted by using Pythons string formatting notation.
  &nbsp;
- This variable parameter can be accepted in a variable as defined in the path and passed to the formal parameters defined in the function bound to the operation decorator.
  &nbsp;
- A classical method of passing the request data to the server is to append a query string to the URL. Assuming that a Python script on a server is executed as CGI, a list of key-value pairs concatenated by the ampersand (&) forms the query string, which is appended to the URL by putting a question mark (?) as a separator.
  &nbsp;
- The trailing part of the URL, after (?), is the query string, which is then parsed by the server-side script for further processing. FastAPI automatically treats the part of the endpoint which is not a path parameter as a query string and parses it into parameters and its values.
