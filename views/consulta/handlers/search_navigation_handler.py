class SearchNavigationHandler:

    def __init__(
        self,
        page,
        state,
        ui
    ):

        self.page = page
        self.state = state
        self.ui = ui

    def handle(
        self,
        e,
        results,
        selected_attr,
        on_select
    ):

        if not results:
            return

        current = getattr(
            self.state,
            selected_attr
        )

        if e.key == "Arrow Down":

            current = min(
                current + 1,
                len(results) - 1
            )

        elif e.key == "Arrow Up":

            current = max(
                current - 1,
                0
            )

        elif e.key == "Enter":

            on_select(current)

            return

        setattr(
            self.state,
            selected_attr,
            current
        )

        self.page.update()