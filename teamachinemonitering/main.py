from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from database import check_login

app = FastAPI(title="Tea Machine Monitoring Dashboard")


# Static Folder
app.mount("/static", StaticFiles(directory="static"), name="static")


# Templates
templates = Jinja2Templates(directory="templates")


# Machine Data
machine_data = {
    "machine_status": "OFF",
    "blade_status": "STOPPED",
    "machine_on_time": "--:--:--",
    "machine_off_time": "--:--:--",
    "running_time": "00:00:00",
    "wifi_status": "Disconnected",
    "last_sync": "--:--:--"
}



# =========================
# LOGIN PAGE
# =========================

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "error": ""
        }
    )



# =========================
# LOGIN CHECK
# =========================

@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    user = check_login(username, password)

    if user:

        response = RedirectResponse(
            url="/dashboard",
            status_code=302
        )

        return response


    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "error": "Invalid Username or Password"
        }
    )



# =========================
# DASHBOARD
# =========================

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "data": machine_data
        }
    )



# =========================
# ANALYTICS
# =========================

@app.get("/analytics", response_class=HTMLResponse)
async def analytics(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="analytics.html",
        context={
            "data": machine_data
        }
    )



# =========================
# HISTORY
# =========================

@app.get("/history", response_class=HTMLResponse)
async def history(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "data": machine_data
        }
    )



# =========================
# REPORTS
# =========================

@app.get("/reports", response_class=HTMLResponse)
async def reports(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="reports.html",
        context={
            "data": machine_data
        }
    )



# =========================
# SETTINGS
# =========================

@app.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={
            "data": machine_data
        }
    )



# =========================
# API GET DATA
# =========================

@app.get("/api/data")
async def get_data():

    return JSONResponse(machine_data)



# =========================
# API UPDATE DATA
# =========================

@app.post("/api/update")
async def update_data(data: dict):

    global machine_data

    for key, value in data.items():

        if key in machine_data:
            machine_data[key] = value


    return {
        "status": "success",
        "message": "Machine Data Updated Successfully"
    }



# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
async def health():

    return {
        "status": "Server Running Successfully"
    }



# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )