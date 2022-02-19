# Twitter Bot
Python app to look for specific keywords in tweets and to give like and retweet them.

## Twitter Account Setup
- Create a new account or use an existing twitter account for the bot.
- Sign up for a [developer account](https://developer.twitter.com/) using bot's account.
- Create an Application, We need an app to get credentials.
- From the Projects & Apps menu select the app that you created.
- Select the Keys & tokens tab.
- Generate consumer keys. Copy it and update it in the config.py file.
- Generate Access Token and Secret. Copy it and update it in the config.py file.

## Project Setup
- Python 3.6 or grater.
- Install requirements `pip install -r requirements.txt`.
- Twitter developer account is required to generate the tokens that are required in `config.py`.
- Update list of key words in `config.py` line number [7](https://github.com/iharshgor/twitter-bot/blob/main/config.py#L7).
