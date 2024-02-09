# db.py
from databases import Database

DATABASE_URL = 'mysql+aiomysql://账号:密码@域名:端口/form_to_project'


database = Database(DATABASE_URL)

async def connect_to_database():
    await database.connect()

async def disconnect_from_database():
    await database.disconnect()
