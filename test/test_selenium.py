import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
        return HomePage(self.driver)

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.ID, 'error')))
        return self.driver.find_element(By.ID, 'error').text

class HomePage(BasePage):
    def get_title_message(self):
        return self.driver.find_element(By.CLASS_NAME, 'post-title').text

class SeleniumExampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_python_search(self):
        self.driver.get("http://www.python.org")
        self.assertTrue("Python" in self.driver.title)
        elem = self.driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertTrue("No results found." not in self.driver.page_source)

    def test_positive_login(self):
        # Acessando a página que será testada
        self.driver.get('https://practicetestautomation.com/practice-test-login/')

        # Selecionando os elementos que serão utilizados
        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.NAME, 'password')
        submit = self.driver.find_element(By.ID, "submit")

        # Realizando ações nos elementos
        username.send_keys('student')
        password.send_keys('Password123')
        submit.click()

        # Verificando os efeitos após as ações
        self.assertEqual('https://practicetestautomation.com/logged-in-successfully/', self.driver.current_url)
        self.assertIn('Logged In Successfully', self.driver.find_element(By.CLASS_NAME, 'post-title').text)
        self.assertTrue(len(self.driver.find_elements(By.LINK_TEXT, 'Log out')) == 1)

    def test_invalid_username_login(self):
        self.driver.get('https://practicetestautomation.com/practice-test-login/')
        self.driver.find_element(By.ID, 'username').send_keys('incorrectUser')
        self.driver.find_element(By.NAME, 'password').send_keys('Password123')
        self.driver.find_element(By.ID, "submit").click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.ID, 'error')))
        self.assertTrue(self.driver.find_element(By.ID, 'error').is_displayed())
        self.assertIn('Your username is invalid!', self.driver.find_element(By.ID, 'error').text)

    def test_invalid_password_login_using_page_object(self):
        self.driver.get('https://practicetestautomation.com/practice-test-login/')
        login_page = LoginPage(self.driver)
        login_page.login('student', 'incorrectPassword')
        self.assertIn('Your password is invalid!', login_page.get_error_message())