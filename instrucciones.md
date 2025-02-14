### Initial Steps
1. Create the "app" object from the FastAPI class.
2. Define parameters.
3. Create a POST (or the required method) using the *@app* decorator.
    - Create the function.
    - In this case, it receives a dictionary because the POST method gets information from the client.
    - Configure the behavior.
4. Use uvicorn in the terminal.
   - `uvicorn $python_file$:$app_name$ --reload`
   - Example: `uvicorn main:app --reload`
5. To better visualize the methods, access [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
6. Exceptions can be implemented.
7. Requirements file:
   - Create: `pip freeze > requirements.txt`
   - Install: `pip install -r requirements.txt`
