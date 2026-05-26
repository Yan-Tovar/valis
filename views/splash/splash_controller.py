import threading
import time

from core.router.navigation_service import (
    NavigationService
)

from core.router.routes import (
    Routes
)


class SplashController:


    def __init__(self, page):

        self.page = page


    # --------------------------------------------------
    # START
    # --------------------------------------------------

    def start(self):

        threading.Thread(

            target=self._navigate_to_login,

            daemon=True

        ).start()


    # --------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------

    def _navigate_to_login(self):

        time.sleep(5)

        NavigationService.navigate(
            Routes.LOGIN
        )