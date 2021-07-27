from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

class Browser:
    def __init__(self, email, number, expiry, thisMonth, nextMonth, test):
        self.url = 'https://drivetest.ca/book-a-road-test/booking.html#/validate-driver-email'
        self.email = email
        self.number = number
        self.expiry = expiry
        self.error = 'https://drivetest.ca/book-a-road-test/booking.html#/error'
        self.alert = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
        self.licence = 'https://drivetest.ca/book-a-road-test/booking.html#/licence'
        self.chedule = 'https://drivetest.ca/book-a-road-test/booking.html#/schedule'
        self.home = 'https://drivetest.ca/book-a-road-test/'
        self.thisMonth = thisMonth
        self.nextMonth = nextMonth
        if test == 'G':
            self.gTest = True
        else:
            self.gTest = False
        self.g2Test = not self.gTest
    
    def open(self):
        """
        op = webdriver.ChromeOptions()
        op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        op.add_argument("--headless")
        op.add_argument("--no-sandbox")
        op.add_argument("--disable-dev-sh-usage")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
        """
        options = webdriver.ChromeOptions()
        options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"
        self.driver = webdriver.Chrome(chrome_options=options)
        #self.driver = webdriver.Chrome(ChromeDriverManager.install())

    def login(self):
        # Load Website
        self.driver.get(self.url)
        time.sleep(2)
        # Enter Email
        while True:
            try:
                self.driver.find_element_by_id("emailAddress").clear()
                break
            except:
                time.sleep(7)
        self.driver.find_element_by_id("emailAddress").send_keys(self.email)
        time.sleep(2)
        # Enter Email again
        self.driver.find_element_by_id("confirmEmailAddress").clear()
        self.driver.find_element_by_id("confirmEmailAddress").send_keys(self.email)
        time.sleep(2)
        # Enter Licence Number
        self.driver.find_element_by_id("licenceNumber").clear()
        self.driver.find_element_by_id("licenceNumber").send_keys(self.number)
        time.sleep(2)
        # Enter Expiry Date
        self.driver.find_element_by_id("licenceExpiryDate").clear()
        self.driver.find_element_by_id("licenceExpiryDate").send_keys(self.expiry)
        time.sleep(2)
        # Click Submit Button
        self.driver.find_element_by_id("regSubmitBtn").click()
        time.sleep(2)
        
        # Sleep until the browswer changes
        while self.url == self.driver.current_url:
            time.sleep(5)

        # Login again if error
        if self.driver.current_url == self.error:
            login()

        
    def gtest(self):
        time.sleep(5)
        # Select License
        if self.gTest:
            self.driver.find_element_by_id("Gbtn").click()
        else:
            self.driver.find_element_by_id("G2btn").click()
        
        time.sleep(2)
        # Click Continue
        self.driver.find_element_by_class_name("booking-submit").click()
        time.sleep(2)

        # Wait for Browser to change
        while self.driver.current_url == "https://drivetest.ca/book-a-road-test/booking.html#/licence":
            time.sleep(2)
            
            if self.driver.current_url == error:
                login()
        
        time.sleep(5)


    def checkPage(self):
        tried = False
        date = 0
        try:
            date = self.driver.find_element_by_xpath("//a[@class='date-link']").click().text
            tried = True
            
            # Second tab
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(alert)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            
            buttons = self.driver.find_elements_by_css_selector(".booking-submit")
            buttons[2].click()
            self.driver.find_element_by_class_name("timeslot_label").click()
            buttons[2].click()
            
            return date
        except:
            return date
    
    
    def search(self):
        notBooked = True;
        barrie = ["9554", "Barrie"]
        burlington = ["9559", "Burlington"]
        guelph = ["9567", "Guelph"]
        hamilton = ["9597", "Hamilton"]
        kingston = ["9572", "Kingston"]
        kitchener = ["9574", "Kitchener"]
        london = ["9576", "London"]
        sauga = ["12448", "Mississauga"]
        newMarket = ["9552", "Newmarket"]
        oakville = ["9580", "Oakville"]
        oshawa = ["9583", "Oshawa"]
        peter = ["9588", "Peterborough"]
        simcoe = ["9593", "Simcoe"]
        catherine = ["9596", "St Catharines"]
        stratford = ["9598", "Stratford"]
        tdown = ["9602", "Toronto Downsview"]
        etobi = ["9565", "Toronto Etobicoke"]
        metro = ["9579", "Toronto Metro East"]
        port = ["9592", "Toronto Port Union"]

        places = [newMarket, oshawa, peter, metro, port]
        index = 0

        while notBooked:
            index = 0
            while index < 5:
                time.sleep(2)
                #driver.find_element_by_id(places[index][0]).click()
                self.driver.execute_script("window.scrollTo(0, 10)") 
                time.sleep(2)
                #driver.find_element_by_class_name("dtc_listings").click()
                time.sleep(2)
                
                if self.driver.current_url == self.home:
                    login()
                    gtest()
                    continue
                    
                self.driver.find_element_by_xpath("//a[@title='" + places[index][1] + "']").click()
                self.driver.find_element_by_class_name("booking-submit").click()
                time.sleep(3)

                # July Check
                if self.thisMonth and checkPage():
                    notBooked = False
                    print("FOUND")
                    break

                if self.driver.current_url == licence:
                    gtest()
                    continue
                
                time.sleep(2)
                
                # Click Next Month
                self.driver.find_element_by_xpath("//a[@title='next month']").click()
                time.sleep(4)

                # August Check
                if self.nextMonth and checkPage():
                    notBooked = False
                    print("FOUND")
                    break

                index += 1
                time.sleep(2)
                
                if self.driver.current_url == error:
                    login()
                    gtest()
                    search()

        