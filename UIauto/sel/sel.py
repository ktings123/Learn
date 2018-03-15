import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class FistUntest(unittest.TestCase):

    def setUp(self):
        self.d = webdriver.Chrome()

    def test_pyFing(self):
        d = self.d
        d.get("http://www.python.org")
        # self.assertIn("Python",d.title)
        so = d.find_element_by_name("q")
        so.send_keys("pycon")
        so.send_keys(Keys.RETURN)
        assert "Python" in d.title
        assert "No results found" not in d.page_source

    def tearDown(self):
        self.d.close()


if __name__ == "__main__":
    unittest.main()
