import pytest


@pytest.fixture(scope='session')
def meteocat_invalid_token():
    return {"message": "Forbidden"}


@pytest.fixture(scope='session')
def meteocat_invalid_query():
    return {"message": "L'estació 'UK' no mesura la variable '6'",
            "aws": {"logGroupName": "/aws/lambda/api-xema-pro-getDades",
                    "logStreamName":"2021/11/09/[$LATEST]74661f40b3874bfc8c519ae29e45f0e1",
                    "functionName":"api-xema-pro-getDades",
                    "awsRequestId":"37d2c9f5-24fa-4f3c-a7ad-ecba5e284ef3"
                    }
            }


@pytest.fixture(scope='session')
def meteocat_empty_query():
    return list()
