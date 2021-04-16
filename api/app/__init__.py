from flask import Flask, jsonify

from .blueprints import blueprints

def createApp():
    app = Flask(__name__)

    for i in blueprints:
        app.register_blueprint(i)

    @app.errorhandler(404)
    async def not_found(err):
        return jsonify(success=False, error=str(err)), 404

    return app