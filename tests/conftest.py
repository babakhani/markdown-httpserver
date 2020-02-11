from os.path import dirname, join

import pytest


HERE = dirname(__file__)


@pytest.fixture
def app():
    from markdownserver import app
    here = dirname(__file__)
    templatefilename = join(here, 'dummy.mako')
    app.settings.template.filename=templatefilename
    app.settings.root = join(HERE, 'root')
    app.ready()
    yield app
    app.shutdown()

