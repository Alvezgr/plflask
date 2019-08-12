from flask_testing import TestCase
from main import APP
from flask import current_app, url_for


class MainTest(TestCase):
    """main test class"""
    def create_app(self):
        """return an app to run tests on it"""
        APP.config['TESTING'] = True
        APP.config['WTF_CSRF_ENABLED'] = False

        return APP

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))

        self.assertRedirects(response, url_for('hello'))

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'Fake-pass'
        }
        response = self.client.post(url_for('hello'), data=fake_form)
        self.assertRedirects(response, url_for('index'))
