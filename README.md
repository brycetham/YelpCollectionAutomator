# YelpCollectionAutomator

This was a small project I did one night. Yelp wiped all of my restaurant check-ins, so I wanted to creat an automation tool that would add them all to a collection.

Unfortunately, I had to stop this project because some of the restaurants I have checked into have been permanently closed, and the Yelp API does not offer a way to search for permanently closed restaurants. Currently, all the script does is search for each checked-in restaurant by name, longitude, and latitude, and open the first result in Chrome.

If you still want to play with this, you can follow the instructions below.

### 1. Get a Yelp Fusion API key

Instructions are here: https://www.yelp.com/developers/documentation/v3/authentication. Set your key to `API_KEY` in `script.py`.

### 2. Install requirements

Simply run `pip install -r requirements.txt`.

### 3. Install Selenium

On macOS, run `sudo easy_install selenium`.

### 4. Download ChromeDriver

You can download it here: https://chromedriver.chromium.org. Copy `chromedriver` into this folder.

### 5. Download your Yelp data

Instructions are here: https://www.yelp-support.com/article/How-can-I-access-my-Yelp-data. Copy `check_in.html` into this folder.

### 6. Run script.py

Simply run `python script.py`.
