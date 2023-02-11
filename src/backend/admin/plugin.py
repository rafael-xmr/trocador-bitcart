from api.plugins import BasePlugin

# If your module requires extra dependencies, create a file requirements.txt in this directory and list them here
# (we recommend pinning dependencies)
# If your module wants to add extra database tables, create a models.py file and define your models
# Then use scripts/pluginmigrate.py to create new database migrations in versions/ directory or to apply them

# Use BaseCoin in case you need to add custom payment methods
# Each object has metadata, interact with it via get_metadata/update_metadata/delete_metadata
# Create your own hooks/filters via run_hook/apply_filters
# Interact with the internal events system via register_event/register_event_handler/publish_event
# (usually for something like new websocket endpoints)


class Plugin(BasePlugin):
    name = "backend"

    def setup_app(self, app):
        # add new endpoints via app.include_router, or any other stuff
        pass

    async def startup(self):
        # run register_filter/register_hook here to hook into needed parts of the app
        # called both in web workers and background worker
        pass

    async def shutdown(self):
        # in case you need to clean up some resources
        # called both in web workers and background worker
        pass

    async def worker_setup(self):
        # called only in background worker, set up polling tasks here for example
        pass
