# Gen-prompt-server-nineteen

## Cách chạy server gen prompt (nên chạy bằng tmux)
```bash
git clone https://github.com/TuanNT-ZenAI/Gen-prompt-server-nineteen.git
cd Gen-prompt-server-nineteen
pip install -r requirements.txt
uvicorn --lifespan on --reload --host 0.0.0.0 --port 8000 app.asgi:app
```

Thay thế URL_SYNTHETIC_DATA = "http://20.29.36.33:8000/get-synthetic-data" trong test_image_server.py thành URL_SYNTHETIC_DATA = "http://localhost:8000/get-synthetic-data"

```python
python test_image_server.py   #chatgpt để hiểu file này làm gì
```



