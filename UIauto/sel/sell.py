import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select,WebDriverWait


class FistUntest(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Chrome()
        self.d.get("http://www.python.org")

    def test_pyFing(self):
        d = self.d
        # self.assertIn("Python",d.title)
        so = d.find_element_by_name("q")
        so.send_keys("pycon")
        so.send_keys(Keys.RETURN)
        assert "Python" in d.title
        assert "No results found" not in d.page_source

    # def test_sel(self):
    #     s = Select(self.d.find_element_by_id("id"))  # choice
    #
    # def test_window(self):           # about windows moving
    #     for x in self.d.window_handles:
    #         self.d.switch_to_frame()
    #
    # def test_el(self):                       # choice element
    #     self.d.find_element(By.CLASS_NAME,'kkkk')
    #
    # def test_wait(self):               # wait until
    #     element = WebDriverWait(self.d, 10).until(
    #         ec.presence_of_element_located((By.ID, "myDynamicElement"))
    #     )
    #
    #     wait = WebDriverWait(self.d,20)
    #     el = wait.until(ec.element_to_be_clickable((By.ID,'id')))   # be careful '()'

    def tearDown(self):
        self.d.close()


if __name__ == "__main__":
    unittest.main()


