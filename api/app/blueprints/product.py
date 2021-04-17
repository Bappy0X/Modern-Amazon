from flask import Blueprint, jsonify

from ..models import Product

bp = Blueprint("api", __name__, url_prefix="/p")

@bp.route("/")
def many():
    thisProducts = [Product() for i in range(10)]
    return jsonify(success=True, data=[dict(i) for i in thisProducts])

@bp.route("/<asin>/")
def one(asin):
    thisProduct = Product()
    return jsonify(success=True, data=dict(thisProduct))
