from database.connection import engine, SessionLocal
from database.base import Base
import database.models

from database.models import Usuario

from sqlalchemy import inspect


# -------------------------------------------------
# CHECK IF TABLES EXIST
# -------------------------------------------------

def tables_exist():

    inspector = inspect(engine)

    return inspector.has_table("usuarios")


# -------------------------------------------------
# INIT DATABASE
# -------------------------------------------------

def init_database():

    existing_tables = tables_exist()

    # Si no hay tablas → crear todo
    if not existing_tables:

        Base.metadata.create_all(bind=engine)

        print("Tablas creadas correctamente")

    else:

        print("Las tablas ya existen")


# -------------------------------------------------
# CREATE ADMIN ONLY ON FIRST RUN
# -------------------------------------------------

def create_admin():

    session = SessionLocal()

    try:

        admin_exists = session.query(Usuario).filter_by(
            nombre_usuario="admin"
        ).first()

        if not admin_exists:

            from core.security.password_hasher import PasswordHasher

            admin = Usuario(

                nombre_usuario="admin",
                nombre_completo="Administrador",
                rol="ADMIN",
                password=PasswordHasher.hash_password("admin123"),
                estado="ACTIVO"
            )

            session.add(admin)
            session.commit()

            print("Admin creado")

        else:

            print("Admin ya existe")

    finally:
        session.close()