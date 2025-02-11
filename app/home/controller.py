from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('/')
def home():
    return (
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">'
        '<body>'
        '<main class="container">'
        '<h1 style="text-align: center;">The BJJ API 🌐 🔌</h1>'
        '<ul><li></span><a href="/fighters">Fighters</a> 🥋</span></li></ul>'
        '<ul><li></span><a href="/teams">Teams</a> 🤼</span></li></ul>'
        '<ul><li></span><a href="/lineages">Lineages</a> 🌳</span></li></ul>'
        '<ul><li></span><a href="/achievements">Achievements</a> 🏅</span></li></ul>'
        '<ul><li></span><a href="/docs">API Docs</a> 📄💻</span></li></ul>'
        '</main>'
        '</body>'
    )