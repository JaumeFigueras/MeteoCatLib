#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..src.gisfire_meteocat_lib.database.lightnings import Lightning
from ..src.gisfire_meteocat_lib.database.lightnings import LightningAPIRequest
from ..src.gisfire_meteocat_lib.database.meteocat_xdde import get_lightning_api_requests
from ..src.gisfire_meteocat_lib.database.meteocat_xdde import get_lightnings
import datetime
import pytz
import dateutil.parser


def test_add_lightning_01(db_session, postgresql_schema):
    cursor = postgresql_schema.cursor()
    cursor.execute("SELECT count(*) FROM meteocat_lightning")
    record = cursor.fetchone()
    count = record[0]
    light = Lightning(1, '2021-02-24T21:45:05Z', 23.4, 1.23, 700, 300, 0.56, 2, False, 23456, 42.356578, 2.1244578)
    db_session.add(light)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute("SELECT count(*) FROM meteocat_lightning")
    record = cursor.fetchone()
    assert record[0] == count + 1
    cursor.execute("SELECT * FROM meteocat_lightning WHERE _id = 1")
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
    light = Lightning(2, datetime.datetime(2021, 2, 24, 21, 45, 5, tzinfo=pytz.UTC), 23.4, 1.23, 700, 300, 0.56, 2,
                      True, 23456, 42.356578, 2.1244578)
    db_session.add(light)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute("SELECT count(*) FROM meteocat_lightning")
    record = cursor.fetchone()
    assert record[0] == count + 2
    cursor.execute("SELECT * FROM meteocat_lightning WHERE _id = 2")
    record = cursor.fetchone()
    assert record[1] == 2
    assert record[2] == datetime.datetime(2021, 2, 24, 21, 45, 5, tzinfo=pytz.UTC)
    assert record[3] == 23.4
    assert record[4] == 1.23
    assert record[5] == 700
    assert record[6] == 300
    assert record[7] == 0.56
    assert record[8] == 2
    assert record[9] is True
    assert record[10] == 23456
    assert record[11] == 42.356578
    assert record[12] == 2.1244578


def test_add_lightning_api_request_01(db_session, postgresql_schema):
    cursor = postgresql_schema.cursor()
    cursor.execute("SELECT count(*) FROM meteocat_xdde_request")
    record = cursor.fetchone()
    count = record[0]
    req = LightningAPIRequest('2021-11-03 14:00:00Z', 200, 57)
    db_session.add(req)
    db_session.commit()
    requests = db_session.query(LightningAPIRequest).filter(LightningAPIRequest.date >= '2021-11-03 00:00:00Z').all()
    assert len(requests) == 1
    assert requests[0].date == dateutil.parser.isoparse('2021-11-03 14:00:00Z')
    cursor = postgresql_schema.cursor()
    cursor.execute("SELECT count(*) FROM meteocat_xdde_request")
    record = cursor.fetchone()
    assert record[0] == count + 1
    cursor.execute("SELECT request_date, result_code, number_of_lightnings "
                   "FROM meteocat_xdde_request WHERE request_date>='2021-11-03 00:00:00Z'")
    record = cursor.fetchone()
    assert record[0] == dateutil.parser.isoparse('2021-11-03 14:00:00Z')
    assert record[1] == 200
    assert record[2] == 57
    req = LightningAPIRequest(datetime.datetime(2021, 11, 3,  15, 0, 0, tzinfo=pytz.UTC), 404)
    db_session.add(req)
    db_session.commit()
    cursor.execute("SELECT request_date, result_code, number_of_lightnings "
                   "FROM meteocat_xdde_request WHERE request_date>='2021-11-03 15:00:00Z'")
    record = cursor.fetchone()
    assert record[0] == datetime.datetime(2021, 11, 3,  15, 0, 0, tzinfo=pytz.UTC)
    assert record[1] == 404
    assert record[2] is None


def test_get_lightning_api_requests_01(db_session):
    requests = get_lightning_api_requests(db_session, '2021-11-01 00:10:00Z')
    assert len(requests) == 0
    requests = get_lightning_api_requests(db_session, '2021-11-02 00:00:10Z')
    assert len(requests) == 1
    requests = get_lightning_api_requests(db_session, datetime.datetime(2021, 11, 1, 0, 59, 0, tzinfo=pytz.UTC))
    assert len(requests) == 0
    requests = get_lightning_api_requests(db_session, datetime.datetime(2021, 11, 2, 0, 0, 59, tzinfo=pytz.UTC))
    assert len(requests) == 1
    requests = get_lightning_api_requests(db_session, '2021-11-01 00:00:00Z', '2021-11-02 00:00:00Z')
    assert len(requests) == 2
    requests = get_lightning_api_requests(db_session, '2021-11-02 00:00:00Z', '2021-11-03 00:00:00Z')
    assert len(requests) == 3
    requests = get_lightning_api_requests(db_session, '2021-11-01 00:00:00Z', '2021-11-02 00:00:00Z')
    assert len(requests) == 2
    requests = get_lightning_api_requests(db_session, '2021-11-01 00:00:00Z', '2021-11-03 00:00:00Z')
    assert len(requests) == 5
    requests = get_lightning_api_requests(db_session, datetime.datetime(2021, 11, 1, 0, 0, 0, tzinfo=pytz.UTC),
                                          datetime.datetime(2021, 11, 2, 0, 0, 0, tzinfo=pytz.UTC))
    assert len(requests) == 2
    requests = get_lightning_api_requests(db_session, datetime.datetime(2021, 11, 2, 0, 0, 0, tzinfo=pytz.UTC),
                                          datetime.datetime(2021, 11, 3, 0, 0, 0, tzinfo=pytz.UTC))
    assert len(requests) == 3
    requests = get_lightning_api_requests(db_session, datetime.datetime(2021, 11, 1, 0, 0, 0, tzinfo=pytz.UTC),
                                          datetime.datetime(2021, 11, 2, 0, 0, 0, tzinfo=pytz.UTC))
    assert len(requests) == 2
    requests = get_lightning_api_requests(db_session, datetime.datetime(2021, 11, 1, 0, 0, 0, tzinfo=pytz.UTC),
                                          datetime.datetime(2021, 11, 3, 0, 0, 0, tzinfo=pytz.UTC))
    assert len(requests) == 5


def test_get_lightnings_01(db_session):
    lightnings = get_lightnings(db_session, '2021-11-01 00:00:00Z')
    assert len(lightnings) == 0
    lightnings = get_lightnings(db_session, datetime.datetime(2021, 11, 1, 0, 59, 0, tzinfo=pytz.UTC))
    assert len(lightnings) == 0
    lightnings = get_lightnings(db_session, '2021-11-01 00:00:00Z', '2021-11-03 00:00:00Z')
    assert len(lightnings) == 5
    lightnings = get_lightnings(db_session, datetime.datetime(2021, 11, 1, 0, 59, 0, tzinfo=pytz.UTC),
                                datetime.datetime(2021, 11, 3, 0, 59, 0, tzinfo=pytz.UTC))
    assert len(lightnings) == 5
    lightnings = get_lightnings(db_session, '2021-11-02 00:10:00Z', '2021-11-02 01:00:00Z')
    assert len(lightnings) == 3
    lightnings = get_lightnings(db_session, datetime.datetime(2021, 11, 2, 0, 59, 0, tzinfo=pytz.UTC),
                                datetime.datetime(2021, 11, 2, 1, 0, 0, tzinfo=pytz.UTC))
    assert len(lightnings) == 3


