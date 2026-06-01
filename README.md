# 📊 Bidding Portal Automation Project (Python + Selenium)

## 🎯 Overview
This project aims to automate the monitoring and extraction of public tender opportunities from procurement portals. The solution replaces manual search workflows by simulating user behavior to look for specific business opportunities, filtering them based on strategic positive and negative keywords, and generating formatted, production-ready corporate reports.

The solution was built using **Python and Selenium WebDriver** for web automation and data extraction, combined with **OpenPyXL and Pandas** to handle advanced Excel styling and structure.

---

## 🛠️ Technologies Used
* **Python** – core programming language and logic
* **Selenium WebDriver** – web browser automation and dynamic element interaction
* **Pandas** – data structure and initial DataFrame manipulation
* **OpenPyXL** – advanced Excel styling, sheet formatting, and auto-filtering
* **Python-dotenv** – secure environment variable management (credentials isolation)

---

## 📊 Automation Structure
The robot executes a sequential multi-stage pipeline:
1. **Secure Authentication:** Logs into the target procurement portal using credentials safely loaded from an isolated `.env` file.
2. **Resilient UI Handling:** Automatically manages pop-ups, cookies, and floating elements using JavaScript injection to maintain stability even if the browser window is minimized or unfocused.
3. **Dynamic Filter Loop:** Iterates through predefined procurement statuses ("Recebendo Propostas" and "Em Andamento").
4. **Deep Keyword Analysis:** Opens each tender registry individually, reads the full descriptive object, and evaluates it against strategic lists of positive and negative keywords.
5. **Categorized Storage:** Classifies approved tenders and appends them to separate data sets depending on their current commercial stage.

---

## 📈 Spreadsheet Output
The spreadsheet is generated with a focus on corporate design, clarity, and immediate business decision-making. It includes:
* **Separated Worksheets:** Independent sheets for "Recebendo Propostas" and "Em Andamento".
* **Corporate Visual Identity:** Custom fonts (Segoe UI), hex-colored headers (#1B365D), and explicit grid lines.
* **Interactive Elements:** Auto-generated filters on all columns and functional hyperlinks pointing directly to each specific tender URL.
* **Smart Auto-Fit:** Columns dynamically resize based on string lengths to prevent layout truncation.

---

## 🧠 Key Features & Optimizations
* **Anti-Minimization Setup:** Configured with advanced Chrome arguments (`--window-size`, `--disable-gpu`) allowing the bot to run seamlessly in the background without throwing `ElementNotInteractable` exceptions.
* **Security Compliance:** Absolutely zero hardcoded credentials. All user names and passwords are isolated using environment variables.
* **Modular Codebase:** Clean segregation between automation logic (`bot.py`), parameters (`config.py`), and the main execution entry point (`main.py`).

---

## 📁 Project Structure

* **bidding-portal-automation**
  * **src/**
    * `__init__.py`
    * `bot.py` (Core scraping logic & spreadsheet styling)
    * `config.py` (Keywords and file path configurations)
  * `.env` (Local credentials - ignored by Git)
  * `.gitignore` (Repository exclusions)
  * `main.py` (Main execution script)
  * `requirements.txt` (Project dependencies)
  * `README.md` (Documentation)

---

## 🚀 Project Goal
This project was developed to practice end-to-end Robotic Process Automation (RPA), covering the full data engineering and automation pipeline:
Web UI Analysis ➔ Selenium Automation ➔ JavaScript Injection ➔ Data Filtering ➔ Corporate Excel Styling ➔ Secure Coding Practices

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📎 Author
Developed by **Victor Viapiana**

* **GitHub:** [https://github.com/VictorViapiana](https://github.com/VictorViapiana)
