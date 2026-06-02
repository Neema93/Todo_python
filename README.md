# Todo_python
# Backend
# FastAPI Project

A REST API built with FastAPI.

## Prerequisites

- Python 3.9+
- pip

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create a virtual environment

**macOS/Linux**

```bash
python3 -m venv venv
```

**Windows**

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows PowerShell**

```powershell
venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```cmd
venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Replace `main:app` if your application entry point is different:

```bash
uvicorn <filename>:<app_instance> --reload
```

Example:

```bash
uvicorn app:app --reload
```

---

## API Documentation

Once the server is running:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Project Structure

```text
project/
├── app/
│   ├── routers/
│   ├── services/
│   ├── models/
│   └── main.py
├── requirements.txt
├── README.md
└── venv/
```

---

## Development

Run the server with auto-reload:

```bash
uvicorn main:app --reload
```

Run on a custom host and port:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Generate Requirements File

If new packages are installed:

```bash
pip freeze > requirements.txt
```

---

## Deactivate Virtual Environment

```bash
deactivate
```

## License

This project is licensed under the MIT License.