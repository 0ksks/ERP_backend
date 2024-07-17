def register_routes(app):
    from .apis import Controller, UserController
    env = "test"

    app.register_blueprint(UserController.register_entity(env=env))
    app.register_blueprint(Controller.register_entity(entityName="GoodsReceipt", env=env))
    app.register_blueprint(Controller.register_entity(entityName="Material", env=env))
    app.register_blueprint(Controller.register_entity(entityName="PurchaseOrder", env=env))
    app.register_blueprint(Controller.register_entity(entityName="Stock", env=env))
    app.register_blueprint(Controller.register_entity(entityName="Supplier", env=env))
