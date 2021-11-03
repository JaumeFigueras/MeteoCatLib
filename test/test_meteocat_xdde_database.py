#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..src.gisfire_meteocat_lib.database.lightnings import Lightning
from ..src.gisfire_meteocat_lib.database.lightnings import LightningAPIRequest
import datetime
import pytz


def test_add_lightning_01(db_session, postgresql_schema):
    light = Lightning(1, '2021-02-24T21:45:05Z', 23.4, 1.23, 700, 300, 0.56, 2, False, 23456, 42.356578, 2.1244578)
    db_session.add(light)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_lightning')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_lightning')
    record = cursor.fetchone()
    assert record[1] == 1
    assert record[2] == datetime.datetime(2021, 2, 24, 21, 45, 5, tzinfo=pytz.UTC)
    assert record[3] == 23.4
    assert record[4] == 1.23
    assert record[5] == 700
    assert record[6] == 300
    assert record[7] == 0.56
    assert record[8] == 2
    assert not record[9]
    assert record[10] == 23456
    assert record[11] == 42.356578
    assert record[12] == 2.1244578


def test_add_lightning_api_request_01(db_session, postgresql_schema):
    req = LightningAPIRequest(2021, 11, 3, 14, 200, 57)
    db_session.add(req)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_xdde_request')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_xdde_request')
    record = cursor.fetchone()
    assert record[0] == 2021
    assert record[1] == 11
    assert record[2] == 3
    assert record[3] == 14
    assert record[4] == 200
    assert record[5] == 57
