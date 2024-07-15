def register_routes(app):
    from .DocumentFlow import documentFlowBP

    app.register_blueprint(documentFlowBP)
