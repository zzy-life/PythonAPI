# Python的web基础框架

Run the backend (I use Poetry for package management - `pip install poetry` if you don't have it):

```shell
cd backend
poetry install
poetry shell
poetry run uvicorn main:app --reload --port 7001
```

You can also run the backend (when you're in `backend`):

```python
poetry run pyright
```

