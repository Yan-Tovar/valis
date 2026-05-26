class SessionManager:


    _current_user = None


    # ---------------------------------------------------------
    # LOGIN
    # ---------------------------------------------------------

    @classmethod
    def login(
        cls,
        user
    ):

        cls._current_user = {

            "id": user.id,

            "nombre_usuario": (
                user.nombre_usuario
            ),

            "nombre_completo": (
                user.nombre_completo
            ),

            "rol": (
                user.rol.strip().upper()
                if user.rol
                else None
            ),

            "estado": user.estado
        }


    # ---------------------------------------------------------
    # LOGOUT
    # ---------------------------------------------------------

    @classmethod
    def logout(cls):

        cls._current_user = None


    # ---------------------------------------------------------
    # CURRENT USER
    # ---------------------------------------------------------

    @classmethod
    def current_user(cls):

        return cls._current_user


    # ---------------------------------------------------------
    # AUTH
    # ---------------------------------------------------------

    @classmethod
    def is_authenticated(cls):

        return cls._current_user is not None