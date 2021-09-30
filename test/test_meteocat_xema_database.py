import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from database.variable import Variable


def test_add_variable_01(db_session, postgresql_schema):
    var = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    db_session.add(var)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_metadata_variables')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_metadata_variables')
    record = cursor.fetchone()
    assert record[1] == 1
    assert record[2] == 'Pressió atmosfèrica màxima'
    assert record[3] == 'hPa'
    assert record[4] == 'Px'
    assert record[5] == 'DAT'
    assert record[6] == 1
