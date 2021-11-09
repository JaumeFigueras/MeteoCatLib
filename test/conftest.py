import tempfile

from pytest_postgresql import factories
from pathlib import Path

test_folder = Path(__file__).parent
socket_dir = tempfile.TemporaryDirectory()
postgresql_session = factories.postgresql_proc(port=None, unixsocketdir=socket_dir.name)
postgresql_schema = factories.postgresql('postgresql_proc', dbname='test', load=[
    str(test_folder) + '/database_init.sql',
    str(test_folder.parent) + '/src/gisfire_meteocat_lib/database/meteocat_xdde.sql',
    str(test_folder.parent) + '/src/gisfire_meteocat_lib/database/meteocat_xema.sql',
    str(test_folder) + '/database_populate.sql'])

pytest_plugins = [
   'test.fixtures.sqlalchemy',
   'test.fixtures.meteocat.meteocat',
   'test.fixtures.meteocat.xema',
]
