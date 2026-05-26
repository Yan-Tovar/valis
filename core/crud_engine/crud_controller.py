class CrudController:


    def __init__(
        self,
        service
    ):

        self.service = service


    # =================================================
    # GET ALL
    # =================================================

    def get_all(self):

        return self.service.get_all()


    # =================================================
    # CREATE
    # =================================================

    def create(
        self,
        data
    ):

        return self.service.create(
            data
        )


    # =================================================
    # UPDATE
    # =================================================

    def update(
        self,
        record_id,
        data
    ):

        return self.service.update(
            record_id,
            data
        )


    # =================================================
    # SOFT DELETE
    # =================================================

    def soft_delete(
        self,
        record_id
    ):

        return self.service.soft_delete(
            record_id
        )


    # =================================================
    # RESTORE
    # =================================================

    def restore(
        self,
        record_id
    ):

        return self.service.restore(
            record_id
        )


    # =================================================
    # HARD DELETE
    # =================================================

    def hard_delete(
        self,
        record_id
    ):

        return self.service.hard_delete(
            record_id
        )


    # =================================================
    # SEARCH
    # =================================================

    def search(
        self,
        query_text,
        columns=None,
        filters=None,
        include_inactive=False
    ):

        return self.service.search(
            query_text,
            columns,
            include_inactive,
            filters
        )