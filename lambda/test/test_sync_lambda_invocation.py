from aws_lambda import lambda_a
from aws_lambda import lambda_b
from nose.tools import assert_equals

#def test_a():
#    event = {
#            "commands": ["start(1, 2)", "info('aaa')"]
#            }
#    response = lambda_a.handle_request(event, None)
#    print(str(response))
#
#    assert_equals(1, 2)
#
#def test_b():
#    event = {
#            "cold_seconds": 30,
#            "hot_seconds": 0.1
#            }
#    response = lambda_b.handle_request(event, None)
#    print(str(response))
#
#    assert_equals(1, 2)
