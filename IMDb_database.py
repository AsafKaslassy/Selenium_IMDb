import selenium
import tkinter as tk
from termcolor import colored
from selenium import webdriver
from tkinter import simpledialog
from selenium.common.exceptions import WebDriverException

# from PIL import Image
# from io import BytesIO



class IMDb_DataBase():
    """
    """


    def execute(self):
        """
        """
        # config
        Site_URL= "https://www.imdb.com/"
        IMDb_searchBar_Xpath = '//*[@id="navbar-query"]'
        IMDb_searchButton_Xpath = '//*[@id="navbar-submit-button"]/div'
        IMDb_firstOption_Xpath = '//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a'
        ChromeDriverPath = r"C:\utomationSelenium\chromedriver.exe"
        choose_movie_message = "Enter a movie name you'd like to get info about(Press enter at the end to continue): "
        Movie_Score = "//*[@id='title-overview-widget']/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span"
        release_year = '//*[@id="titleYear"]/a'
        length = '//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/time'
        Genre = '//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/a[1]'
        Director = '//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a'
        Writer = '//*[@id="title-overview-widget"]/div[2]/div[1]/div[3]/a[1]'
        Storyline = '//*[@id="titleStoryLine"]/div[1]/p/span'
        Language = '//*[@id="titleDetails"]/div[3]/a'
        Budget = '//*[@id="titleDetails"]/div[7]'
        No_results = '//*[@id="main"]/div/h1'


        Xpaths = {IMDb_firstOption_Xpath:'//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a',
                  Movie_Score:"//*[@id='title-overview-widget']/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span",
                  release_year:'//*[@id="titleYear"]/a',
                  length:'//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/time',
                  Genre:'//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/a[1]',
                  Director:'//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a',
                  Writer:'//*[@id="title-overview-widget"]/div[2]/div[1]/div[3]/a[1]',
                  Storyline:'//*[@id="titleStoryLine"]/div[1]/p/span',
                  Language:'//*[@id="titleDetails"]/div[3]/a',
                  Budget:'//*[@id="titleDetails"]/div[7]',
                  No_results:'//*[@id="main"]/div/h1'}
        #______________________________
        scores = []

        driver = webdriver.Chrome(ChromeDriverPath)
        driver.minimize_window()
        driver.maximize_window()
        driver.get(Site_URL)
        n=0
        while n<3:
            window = tk.Tk()
            window.withdraw()
            user_input = simpledialog.askstring(title="IMDb Database",
                                                prompt=choose_movie_message,
                                                initialvalue="what ever movie you want")
            n=n+1
            while user_input == "" or not user_input:
                print("ERROR! - Cannot continue without a user input.")
                window = tk.Tk()
                window.withdraw()
                user_input = simpledialog.askstring(title="IMDb Database",
                                                    prompt=choose_movie_message,
                                                    initialvalue="ERROR! - Cannot continue without a user input,Enter a movie name you'd like to get info about")

            print('\n')
            print("________________________")
            driver.find_element_by_xpath(IMDb_searchBar_Xpath).send_keys(user_input)
            driver.find_element_by_xpath(IMDb_searchButton_Xpath).click()
            driver.find_element_by_xpath(IMDb_firstOption_Xpath).click()
            # f = open("C:\SeleniumTests\results.txt")
            # f.write("URL: " + driver.current_url)
            print("URL: " + driver.current_url)
            try :
                print("Title: " + driver.title)

                print("Movie_Score: " + driver.find_element_by_xpath(Xpaths[Movie_Score]).text)
                scores.append(float(driver.find_element_by_xpath(Xpaths[Movie_Score]).text))
                print("release year: " + driver.find_element_by_xpath(Xpaths[release_year]).text)
                print("length: " + driver.find_element_by_xpath(Xpaths[length]).text)
                print("Genre: " + driver.find_element_by_xpath(Xpaths[Genre]).text)
                print("Director: " + driver.find_element_by_xpath(Xpaths[Director]).text)
                print("Writer: " + driver.find_element_by_xpath(Xpaths[Writer]).text)
                print("Storyline: " + driver.find_element_by_xpath(Xpaths[Storyline]).text)
                print("Language: " + driver.find_element_by_xpath(Xpaths[Language]).text)
                print("Budget: " + driver.find_element_by_xpath(Xpaths[Budget]).text)
            except selenium.common.exceptions.WebDriverException:
                print (colored('Oops!  one of the Fields for this movie is missing, try different movie','red'))
        driver.quit()
        print ("Highest score: " + str(max(scores)))

runner = IMDb_DataBase()
runner.execute()
