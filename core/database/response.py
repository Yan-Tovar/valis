class Response:


    def __init__(
        self,
        success,
        message="",
        data=None
    ):

        self.success = success

        self.message = message

        self.data = data


    # ---------------------------------------------------------
    # SUCCESS
    # ---------------------------------------------------------

    @classmethod
    def success(
        cls,
        message="Operación exitosa",
        data=None
    ):

        return cls(
            success=True,
            message=message,
            data=data
        )


    # ---------------------------------------------------------
    # ERROR
    # ---------------------------------------------------------

    @classmethod
    def error(
        cls,
        message
    ):

        return cls(
            success=False,
            message=message,
            data=None
        )