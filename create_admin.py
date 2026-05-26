from database.connection import SessionLocal
from database.models import Usuario

from core.security.password_hasher import (
    PasswordHasher
)


session = SessionLocal()

exists = session.query(Usuario).filter(
    Usuario.nombre_usuario == "admin"
).first()


if not exists:

    admin = Usuario(

        nombre_usuario="admin",

        nombre_completo="Administrador",

        rol="ADMIN",

        password=PasswordHasher.hash_password(
            "admin123"
        ),

        estado="ACTIVO"
    )

    session.add(admin)

    session.commit()

    print("Admin creado correctamente")


else:

    print("El admin ya existe")


session.close()