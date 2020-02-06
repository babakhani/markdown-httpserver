from bddrest import Given, status, response, when


def test_markdownserver(app):
    with Given(app, '/foo.md'):
        assert status == 200
        assert response.text.strip() == \
            '<doctype><html><header></header><body><h1>Foo</h1>\n</body>' \
            '</html>'

        when('/notexists')
        assert status == 404
