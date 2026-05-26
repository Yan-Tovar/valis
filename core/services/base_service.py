from database.connection import SessionLocal


class BaseService:


    def __init__(self):

        self.session = SessionLocal()


    def close(self):

        if self.session is not None:
            self.session.close()
            self.session = None


    def __del__(self):

        try:
            self.close()
        except Exception:
            pass

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def search(
        self,
        query_text,
        columns=None,
        include_inactive=False,
        filters=None
    ):

        # Expected that concrete services set `self.repository`
        if not hasattr(self, "repository"):

            raise AttributeError(
                "Service has no repository to perform search"
            )

        return self.repository.search(
            query_text,
            columns,
            include_inactive,
            filters
        )