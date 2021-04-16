from flask import Blueprint, jsonify

bp = Blueprint("api", __name__, url_prefix="/api/")

@bp.route("/")
def helloWorld():
    return jsonify(success=True, data=["one", "two", "three"])