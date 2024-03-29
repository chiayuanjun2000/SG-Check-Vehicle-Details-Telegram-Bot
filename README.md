# SG-Check-Vehicle-Details-Telegram-Bot
A telegram bot that returns vehicle details of Singapore registered vehicles



## Contents
- [About](#about)
- [Set-Up](#set-up)
  - [Direct Message](#direct-message)
  - [Groups](#groups)
- [Usage](#usage)
  - [Commands](#commands)
- [Development](#development)
  - [Requirements](#requirements)
  - [File Structure](#file-structure)
  - [Build](#build)
  - [Deployment](#deployment)
- [Community](#community)
  - [Contribution](#contribution)
- [FAQ](#faq)
- [Credits/Acknowledgement](#creditsacknowledgement)
- [License](#license)



## About
SG Check Vehicle Details Telegram Bot is a telegram bot that uses [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot/) and [Selenium](https://selenium-python.readthedocs.io/) to scrape the LTA website in order to retrieve the vehicle's model and road tax expiry date of Singapore registered vehicles.



## Set-Up
This bot can be called from direct messages or from within a group. <br>
(Do note that the bot currently requires admin rights to work in a group chat.)

### Direct Message
1. Search for the bot by typing "@check_vehicle_bot" in the search bar from within telegram.
2. Select "@check_vehicle_bot" and click "START".

### Groups
1. Within the group you would like the bot to be added to, click on "Add Members".
2. Search for the bot by typing "@check_vehicle_bot" in the search bar.
3. Add "@check_vehicle_bot" to the group and promote it to admin.
4. Click on "/start" from the bot commands menu.



## Usage
To call the bot in direct message, enter the vehicle plate directly into the chat.
- "ABC0000A"

To call the bot in a group, make sure to tag the bot, followed by the vehicle plate.
- "@check_vehicle_bot ABC0000A"

### Commands
/start
- Starts the bot

/help
- Displays help menu



## Development
### Requirements
This bot was created using:
- Python (3.12.1)

This bot was created using the following python packages:
- Selenium (4.18.1)
- python-telegram-bot (21.0.1)

This bot uses:
- Chromedriver (123.0.6312.86)

Chrome driver can be obtained from [this link](https://chromedriver.chromium.org/home). <br>
(Make sure that your current chrome version matches your chrome driver version)

### File Structure
### Build
### Deployment



## Community
### Contribution
Please feel free to contribute to this project by:

1. Reporting a bug
2. Request a feature



## FAQ



## Gallery



## Credits/Acknowledgement




## License
