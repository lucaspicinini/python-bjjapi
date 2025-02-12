
home_html = (b'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/cs'
 b's/pico.min.css"><body><main class="container"><h1 style="text-align: center;'
 b'">The BJJ API \xf0\x9f\x8c\x90 \xf0\x9f\x94\x8c</h1><ul><li></span><a href="'
 b'/fighters">Fighters</a> \xf0\x9f\xa5\x8b</span></li></ul><ul><li></span><a h'
 b'ref="/teams">Teams</a> \xf0\x9f\xa4\xbc</span></li></ul><ul><li></span><a hr'
 b'ef="/lineages">Lineages</a> \xf0\x9f\x8c\xb3</span></li></ul><ul><li></span>'
 b'<a href="/achievements">Achievements</a> \xf0\x9f\x8f\x85</span></li></ul><u'
 b'l><li></span><a href="/docs">API Docs</a> \xf0\x9f\x93\x84\xf0\x9f\x92\xbb</'
 b'span></li></ul></main></body>')

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == home_html