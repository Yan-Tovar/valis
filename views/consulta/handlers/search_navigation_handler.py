class SearchNavigationHandler:

    def __init__(self, page, state, ui):

        self.page = page
        self.state = state
        self.ui = ui

    def handle(
        self,
        e,
        results,
        selected_index_key,
        render_results,
        select_by_index
    ):

        key = getattr(e, "key", None)

        if not key or not results:
            return

        index = getattr(
            self.state,
            selected_index_key,
            0
        )

        if key in ("ArrowDown", "Down"):

            index = (
                index + 1
            ) % len(results)

            setattr(
                self.state,
                selected_index_key,
                index
            )

            render_results()

            self.page.update()

        elif key in ("ArrowUp", "Up"):

            index = (
                index - 1
            ) % len(results)

            setattr(
                self.state,
                selected_index_key,
                index
            )

            render_results()

            self.page.update()

        elif key == "Enter":

            select_by_index(index)

        elif key == "Escape":

            self.state.estudio_results_visible = False
            self.state.entidad_results_visible = False

            self.page.update()