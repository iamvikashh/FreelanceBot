# FreelanceBot

Freelance Jobs Notifier is a Python script designed to periodically fetch new projects from popular freelance platform [Upwork.com](https://upwork.com)) and notify a Telegram group about them. It uses the API, RSS Feed to retrieve project details and sends notifications to a specified Telegram group.



---

## 🍰 Features
- Fetches new [project/job]s based on specified categories.
- Sends project notifications to a Telegram group.
- Uses the Apscheduler library for job scheduling.
- Stores project IDs in an SQLite database to avoid duplicate notifications.

---

## ⚙️ Requirements

- Python 3.11 or higher
- Dependencies listed in `requirements.txt`
- A Telegram Bot Token (obtain one from @BotFather on Telegram)
- For [Upwork.com](https://upwork.com) - log in to your account and create a search query for jobs by following this [link](https://www.upwork.com/nx/jobs/search) and get the credentials from the query parameters in the rss feed url that was generated for you. (see `.env` file)
- Configuration via environment variables (see `.env` file)

---

## 💽 Installation

1. Clone this repository:

   ```shell
   git clone https://github.com/hoosnick/freelance-job-notifier.git
   ```

   ```shell
   cd freelance-job-notifier
   ```

2. Install the required dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your environment variables from [.sample.env](.sample.env) file.

4. Run the script:
   ```shell
   python -m app
   ```

---


## 📃 License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

