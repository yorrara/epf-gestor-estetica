from .user_controller import user_routes

def init_controllers(app):
    app.mount("/usuarios", user_routes)
