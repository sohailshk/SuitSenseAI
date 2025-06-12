# SuitSense AI

**SuitSense AI** is an intelligent assistant designed to revolutionize how real estate agents and investors analyze condominium data in Miami. Using the power of **Natural Language Processing (NLP)**, SuitSense AI allows non-technical users to perform deep data queries, generate insights, and visualize market trends without writing a single line of code.

---

## 🌟 Key Features

* 🔍 **Natural Language Interface**: Ask questions like "What condos had the most sales in 2023 in South Beach?" and get intelligent, actionable answers.
* 🌐 **Google Maps Integration**: Visualize condo locations, nearby schools, and driving distances using Maps.
* ⚖️ **Dynamic SQL Generation**: Converts your natural language queries into accurate SQL to fetch insights.
* 🌍 **Interactive Maps & Charts**: View trends and analytics in dynamic, visual formats.
* 📄 **PDF Report Generation**: Export data-driven reports with charts and maps for offline access.

---

## ⚙️ Tech Stack

* **Python 3.x**
* **Flask** (web framework)
* **PostgreSQL** (condo database)
* **LangChain & LangGraph** (NLP agents)
* **OpenAI GPT Models** (NLP backend)
* **Google Maps API** (location services)
* **Chart.js** (visualizations)
* **ReportLab** (PDF report generation)

---

## 🚀 Quickstart

### 1. 🔹 Clone the Repository

```bash
git clone https://github.com/sohailshk/suitsense-ai.git
cd suitsense-ai
```

### 2. 🪖 Setup Environment & DB

```bash
virtualenv gpt_env
source gpt_env/bin/activate
```

```sql
-- From PostgreSQL shell
CREATE DATABASE condo_gpt;
CREATE USER readonly_user WITH PASSWORD 'password';
GRANT CONNECT ON DATABASE suitsense_AI TO readonly_user;
GRANT USAGE ON SCHEMA public TO readonly_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly_user;
```

### 3. 🔍 Configure Environment Variables

Edit `gpt_env/bin/activate` and add:

```bash
export GPLACES_API_KEY="your_google_places_key"
export OPENAI_API_KEY="your_openai_key"
export FLASK_SECRET="your_secret"
export PG_USER="readonly_user"
export PG_PASSWORD="password"
export PG_PORT=5432
export PG_DB="suitsense_AI"
```

### 4. 📃 Load Sample Data

```bash
psql -d condo_gpt < sample_db.sql
```

### 5. ⚖️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. 🚦 Run the Server

```bash
python server.py
```

Navigate to [http://localhost:5000](http://localhost:5000)

---

## ⚖️ Usage

* Ask natural language questions about condo buildings and sales.
* Visualize results via charts, graphs, and Google Maps.
* Generate detailed PDF reports.
* Use the **"Clear Memory"** button to start a fresh session.

---

## ✨ Example Prompt Sequence

```text
1. What buildings on Collins had the most sales in 2023?
2. Generate a graph of this data.
3. Put the data in an HTML table.
4. Add a third column with total sales volume per building.
5. Add a fourth column with median sales price.
6. Replace third column with closest school, fourth with driving distance to that school.
```

---
![image](https://github.com/user-attachments/assets/c5308b96-7832-49b7-8e42-39d684f9941a)
![image](https://github.com/user-attachments/assets/964185b1-21d4-4dc7-a414-c36f216a8d02)
![image](https://github.com/user-attachments/assets/4d8ce226-89bc-4b30-92d2-26995dcbff46)


## 📁 Project Structure

```
suitsense-ai/
├── server.py         # Flask server
├── main.py           # Query processing logic
├── tools.py          # Database & API tools
├── prefix.py         # Agent system prompt
├── boilerplate.py    # Map/chart generation code
├── sample_db.sql     # Sample data for Miami condos
├── requirements.txt  # Python dependencies
```

---

## 🏆 Contributing

SuitSense AI was built as a portfolio project to demonstrate AI engineering skills. Contributions are welcome to enhance features, optimize performance, or expand market coverage.

* 📊 Check open issues for improvements
* 📄 Submit PRs for new ideas
* ✨ Showcase your work in your AI resume or portfolio

---

## 🚀 Why This Matters

Real estate firms pay analysts thousands monthly to generate insights. SuitSense AI automates this with AI, making data-driven decision-making accessible, instant, and cost-effective.

Be a part of this AI-driven revolution in real estate.

**✨ Star the repo. Fork it. Build on it. ✨**
