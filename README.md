## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/esteveslean/fastapi-powered-sudoku-solver.git
cd fastapi-powered-sudoku-solver
```

### **2️⃣ Install Dependencies**
Make sure you have Python 3.8+ installed.

```sh
pip install -r requirements.txt
```

### **3️⃣ Run the API**
```sh
uvicorn main:app --reload
```
*(Replace `main.py` with your actual script name if different.)*

- The API will be available at:  
  📌 **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 

---

## 🎯 API Usage

### **Solve Sudoku Puzzle**
- **Endpoint:** `POST /solve`
- **Request Body (JSON format):**
```json
{
  "board": [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
  ]
}
```

## 🐳 Running with Docker

### **1️⃣ Build the Docker Image**
```sh
docker build -t fastapi-sudoku-solver .
```

### **2️⃣ Run the Docker Container**
```sh
docker run -p 8000:8000 fastapi-sudoku-solver
```

The API will be available at:  
📌 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---
