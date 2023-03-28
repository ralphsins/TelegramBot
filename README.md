# TelegramBot using ChatGPT API

This is a simple Telegram bot project that uses the ChatGPT API to generate responses to messages sent to the bot. The project consists of 3 files: `.env`, `main.py`, and `api.py`.

## Installation

To run this project, you will need to have Python 3 installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/

1. Clone the repository to your local machine using the following command:
git clone https://github.com/yourusername/telegrambot.git

2. Navigate to the project directory:
cd telegrambot

3. Install the required libraries by running:
pip install -r requirements.txt


4. Create a `.env` file in the project directory with the following content:
TELEGRAM_TOKEN=<your telegram bot token>
OPENAI_API_KEY=<your openai api key>

Make sure to replace `<your telegram bot token>` and `<your openai api key>` with your own tokens.

## Usage

To run the bot, simply run the following command in your terminal or command prompt:
python main.py

The bot should now be up and running, and you can start sending messages to it on Telegram.

## Deployment on PythonAnywhere

To deploy this project on PythonAnywhere, follow these steps:

1. Create a new account on PythonAnywhere: https://www.pythonanywhere.com/registration/register/beginner/

2. Once you've created an account, go to the dashboard and click on the "Consoles" tab.

3. Click on the "Bash" console and enter the following command to clone your repository:
git clone https://github.com/yourusername/telegrambot.git

4. Navigate to the project directory:
cd telegrambot

5. Install the required libraries by running:
pip install -r requirements.txt --user

6. Create a new Telegram bot by following the instructions here: https://core.telegram.org/bots#6-botfather

7. Create a new file on PythonAnywhere called `.env` and add the following content:
TELEGRAM_TOKEN=<your telegram bot token>
OPENAI_API_KEY=<your openai api key>


8. Go back to the dashboard and click on the "Web" tab.

9. Click on the "Add a new web app" button and follow the instructions to set up a new web app.

10. Once you've set up the web app, go to the "Code" tab and enter the following command in the "Source code" section:
/home/yourusername/telegrambot/main.py

Make sure to replace `yourusername` with your own username.

11. Click on the "Save" button and your bot should now be up and running on PythonAnywhere.

12. To keep your bot running continuously, you can set up a task that runs the following command every minute:
python /home/yourusername/telegrambot/main.py


Again, make sure to replace `yourusername` with your own username.

