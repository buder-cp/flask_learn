from flask import Blueprint

bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route("/", methods=['GET', 'POST'])
def index():
    return "首页"
