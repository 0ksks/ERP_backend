def register_routes(app):
    from .apis import Controller

    app.register_blueprint(Controller.register("Supplier"))
