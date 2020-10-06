from flask import url_for


class TestLearn(object):
    def test_learn_page(self, client):
        response = client.get(url_for('test.index'))
        assert response.status_code == 200
