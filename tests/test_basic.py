from bddrest import Given, status, response, when

EXPECTED_HEADER = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Markdownserver</title>
  </head>
  <body>
'''
EXPECTED_FOOTER = '''
  </body>
</html>
'''
EXPECTED_TOC = '''<ul>
  <li><a href="/bar#bar-bar">Bar bar</a>
    <ul>
      <li><a href="/bar#baz">Baz</a>
      </li>
    </ul>
  </li>
  <li><a href="/foo#foo-bar-baz">Foo Bar Baz</a>
  </li>
  <li><a href="/grault#grault">Grault</a>
    <ul>
      <li><a href="/grault#garply">Garply</a>
      </li>
      <li><a href="/grault#waldo-fred-30-plugh-xyzzy">Waldo fred (> 30 plugh) xyzzy</a>
      </li>
    </ul>
  </li>
</ul>
'''


def assertbody(b):
    assert response.text == (EXPECTED_HEADER + b + EXPECTED_FOOTER)


def test_markdownserver(app):
    with Given(app):
        assert status == 200
        assertbody(EXPECTED_TOC)

        when('/foo')
        assert status == 200
        assertbody('<h2 id="foo-bar-baz">Foo Bar Baz</h2>\n')

        when('/notexists')
        assert status == 404

