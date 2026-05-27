import threading
import time

from database.init import (
    init_database,
    create_admin
)

from core.router.navigation_service import (
    NavigationService
)

from core.router.routes import (
    Routes
)


class SplashController:


    def __init__(self, page):

        self.page = page


    # =================================================
    # START
    # =================================================

    def start(self):

        threading.Thread(

            target=self._initialize_app,

            daemon=True

        ).start()

    # =================================================
    # INITIALIZE APP
    # =================================================

    def _initialize_app(self):

        start_time = time.time()

        # =============================================
        # INIT DATABASE
        # =============================================

        init_database()

        create_admin()

        # =============================================
        # MIN SPLASH TIME
        # =============================================

        elapsed = time.time() - start_time

        minimum_splash_time = 5

        if elapsed < minimum_splash_time:

            time.sleep(
                minimum_splash_time - elapsed
            )

        # =============================================
        # NAVIGATE SAFELY
        # =============================================

        self.page.run_task(
            self._go_to_login
        )

    # =================================================
    # GO LOGIN
    # =================================================

    async def _go_to_login(self):

        NavigationService.navigate(
            Routes.LOGIN
        )