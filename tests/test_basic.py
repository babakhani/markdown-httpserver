from bddrest import Given, status, response, when

EXPECTED_HEADER = '<doctype><html><header></header><body>'
EXPECTED_FOOTER = '</body></html>'
EXPECTED_TOC = '''<ul>
  <li><a href="/bar#bar-bar">Bar bar</a>
    <ul>
      <li><a href="/bar#baz">Baz</a>
        <ul>
          <li><a href="/bar#qux">Qux</a>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li><a href="/foo#foo-bar-baz">Foo Bar Baz</a>
  </li>
</ul>
'''


def assertbody(b):
    assert response.text == (EXPECTED_HEADER + b + EXPECTED_FOOTER)


def test_markdownserver(app):
    with Given(app):
        assert status == 200
        assertbody(EXPECTED_TOC)

        when('/foo.md')
        assert status == 200
        assertbody('<h1 id="foo-bar-baz">Foo Bar Baz</h1>\n')

        when('/notexists')
        assert status == 404

