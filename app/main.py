from .routers import item
from app import app

app.include_router(item.router)

if __name__ == '__main__':
    pass
