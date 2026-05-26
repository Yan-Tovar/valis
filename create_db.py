from database.connection import engine
from database.base import Base

import database.models


Base.metadata.create_all(bind=engine)

print("Base de datos creada correctamente")