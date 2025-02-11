from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('/')
def home():
    return (
        '<h1 style="text-align: center;">The BJJ API 🌐 🔌</h1>'
        '<ul><li></span><a href=\'/fighters\'>Fighters</a> 🥋</span></li></ul>'
        '<ul><li></span><a href=\'/teams\'>Teams</a> 🤼</span></li></ul>'
        '<ul><li></span><a href=\'/lineages\'>Lineages</a> 🌳</span></li></ul>'
        '<ul><li></span><a href=\'/achievements\'>Achievements</a> 🏅</span></li></ul>'
        '<ul><li></span><a href=\'/docs\'>API Docs</a> 📄💻</span></li></ul>'
    )