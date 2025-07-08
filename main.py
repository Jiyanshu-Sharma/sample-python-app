from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# In-memory list for now
todos = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add")
async def add_todo(task: str = Form(...)):
    todos.append(task)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete")
async def delete_todo(index: int = Form(...)):
    if 0 <= index < len(todos):
        todos.pop(index)
    return RedirectResponse(url="/", status_code=303)
