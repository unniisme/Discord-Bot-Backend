# LeetCodeScraper
Scrapes data by using selenium
## To setup
* Install all the requirements from requirements.txt
* Replace the URL in the code with the Question's URL you need for scraping
* Run the ```LeetScraper.py``` file
## How the code works
* It logs into the account whose details have been given in the ```settings.py``` file
* It goes to the URL given in the code and scrapes all the URL of the questions from the group
* It iterates through the url's obtained from scraping the questions stored in cleaned_title list
* After entering each question's site it scrapes the questions after which it writes it onto the "Questions.txt" file
* It clicks onto the solution tab and then scrapes the solution and writes it onto a "Answers.txt" file

### Issues
* Sometimes CloudFlare gets triggered while logging in, in which case you have to try again