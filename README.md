# Instructions.

## A. Set up API
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
<br><br>
## B. Requirements file
   - Create: `pip freeze > requirements.txt`
   - Install: `pip install -r requirements.txt`
<br><br>
## C. GIT Versioning
### C.1 Push to the Stage branch
Pycharm can handle the pushing to the repository.
1. Initialize a Git Repository (if not already done)
```bash
git init
```
2. Create and change to the stage branch.
```bash
git checkout -b stage
```
3. Add the Remote Repository.
```bash
git remote add origin <repository-url>
```
4. Stage all the files for Commit.
```bash
git add .
```
5. Commit Your Changes.
```bash
git commit -m "Initial commit"
```
6. Push the Changes to the Remote Repository in the `stage` branch.
```bash
git push -u origin stage
```

<br><br>
### C.2 Merge into `main`/`master`
This part can be done directly from GitHub to make it easier to visualize conflicts and changes.
1. Switch to `main` branch
```bash
git checkout main
```
2. Pull the latest changes form the Remote Repository. (if collaborating)
```bash
git pull origin main
```
3. Merge the `stage`  branch into the `main`
```bash
git merge stage
```
4. Resolve Conflicts (if any)
```bash
git add <conflicting-file>
git commit
```
5. Resolve Conflicts (if any)
```bash
git add <conflicting-file>
git commit
```
6. Push the updated `main` branch to the repository.
```bash
git push origin main
```