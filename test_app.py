import unittest
import apps
import os 
class PlatformTesting(unittest.TestCase):
    def setUp(self):
        self.app = apps.app.test_client()
        self.app.testing = True
        apps.app.config.from_object("config.Development")
        apps.app.config["SECRET_KEY"] = "plnUptSBY2020"
        apps.db.create_all()

    def tearDown(self):
        apps.db.session.remove()
        apps.db.drop_all()

    def test_index(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

    def test_index_404(self):
        result = self.app.get("/index")
        self.assertEqual(result.status_code, 404)

    
if __name__ == "__main__":
    unittest.main()

        


