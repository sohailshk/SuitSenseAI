# 🏢 SuitSenseAI - AI-Powered Real Estate Intelligence Platform

<div align="center">

![SuitSenseAI Logo](static/images/logo.webp)

**Conversational AI for Real Estate Analytics & Market Intelligence**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini%202.0-4285F4.svg)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://langchain.com)
[![Flask](https://img.shields.io/badge/Web-Flask-000000.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791.svg)](https://postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## 🌟 What is SuitSenseAI?

SuitSenseAI is a cutting-edge **conversational AI platform** that revolutionizes real estate analytics. Users can ask questions in plain English and receive sophisticated insights, interactive visualizations, and professional reports about condominium markets.

### ✨ Key Features

- 🤖 **Conversational Analytics** - Ask questions in natural language, get intelligent answers
- 📊 **Dynamic Visualizations** - Auto-generated charts, graphs, and interactive maps
- 📋 **AI-Generated Reports** - Professional PDF reports created on-demand
- 🗺️ **Location Intelligence** - Google Maps integration with proximity analysis
- 📈 **Market Analysis** - Holding periods, sales volumes, and trend predictions
- 🔒 **Secure Code Execution** - Safe AI-generated Python code execution
- 💬 **Memory-Aware** - Maintains conversation context for complex analysis

---

## 💡 Usage Examples

### Queries
```
"Which buildings has the highest sale in collins"
"can u put this into HTML Table"
"Can u please generate a graph of this for me to analyze"
"can u please add a third row with avergae median sale"
"can u also show me the closest school distance to each of this building"
"can u show me on map the nearby schools around this property"
"can u also add a new column with average holding period"
"provide me a pdf report of the whole table to download"
```
---

## 🏗️ Architecture & Technology Stack

### 🧠 AI & Machine Learning
- **Google Gemini 2.0 Flash Experimental** - Latest multimodal LLM
- **LangGraph ReAct Agent** - Advanced reasoning and acting framework
- **FAISS Vector Database** - Semantic search capabilities
- **Google Embeddings** - High-quality text embeddings

### 🗄️ Data & Backend
- **PostgreSQL** - Production-grade database with geographic data
- **LangChain SQL Toolkit** - Intelligent database interactions
- **Flask Web Framework** - Lightweight and scalable web server
- **Session Management** - Conversation history and user tracking

### 🌐 APIs & Integrations
- **Google Maps JavaScript API** - Interactive mapping
- **Google Places API** - Location search and discovery
- **Google Directions API** - Distance calculations
- **Google Geocoding API** - Address to coordinate conversion

### 📊 Visualization & Reporting
- **Chart.js** - Dynamic chart generation
- **ReportLab** - PDF report creation
- **Google Maps Advanced Markers** - Custom map visualizations
- **Markdown Processing** - Rich text formatting

---

## 🚀 Quickstart Guide

### 1. 🔹 Clone the Repository
```bash
git clone https://github.com/sohailshk/suitsense-ai.git
cd suitsense-ai
```

### 2. 🐍 Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. 🗄️ Setup PostgreSQL Database
```sql
-- From PostgreSQL shell (psql)
CREATE DATABASE suitsense_ai;
CREATE USER readonly_user WITH PASSWORD 'your_secure_password';
GRANT CONNECT ON DATABASE suitsense_ai TO readonly_user;
GRANT USAGE ON SCHEMA public TO readonly_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly_user;
```

### 4. 🔍 Configure Environment Variables

**Windows (PowerShell):**
```powershell
$env:GPLACES_API_KEY="your_google_places_api_key"
$env:GEMINI_API_KEY="your_gemini_api_key"
$env:FLASK_SECRET="your_flask_secret_key"
$env:PG_USER="readonly_user"
$env:PG_PASSWORD="your_secure_password"
$env:PG_PORT="5432"
$env:PG_DB="suitsense_ai"
```

**macOS/Linux (Bash):**
```bash
export GPLACES_API_KEY="your_google_places_api_key"
export GEMINI_API_KEY="your_gemini_api_key"
export FLASK_SECRET="your_flask_secret_key"
export PG_USER="readonly_user"
export PG_PASSWORD="your_secure_password"
export PG_PORT="5432"
export PG_DB="suitsense_ai"
```

### 5. 📃 Load Sample Data
```bash
psql -d suitsense_ai < sample_db.sql
```

### 6. ⚖️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 7. 🧪 Test Your Setup
```bash
python test_gemini.py
```
You should see all green checkmarks ✅

### 8. 🚦 Run the Application
```bash
python server.py
```

Visit `http://localhost:5000` and start asking questions! 🎉

---

## 🔑 API Keys Setup

### Google APIs (Required)
1. **Google Cloud Console**: https://console.cloud.google.com/
2. **Enable APIs**:
   - Google Places API
   - Google Maps JavaScript API
   - Google Geocoding API
   - Google Directions API
3. **Create API Key** and restrict it to your domains

### Google Gemini AI (Required)
1. **Google AI Studio**: https://aistudio.google.com/
2. **Get API Key** for Gemini 2.0
3. **Set Usage Limits** as needed

---



## 🏗️ Project Structure

```
SuitSenseAI/
├── 📄 main.py              # Core AI processing logic
├── 🌐 server.py            # Flask web application
├── 🛠️ tools.py             # AI tools and integrations
├── 📝 prefix.py            # AI system prompts and instructions
├── 🔧 boilerplate.py       # Code templates and snippets
├── 🧪 test_gemini.py       # Integration testing
├── 🗄️ init_db.py           # Database initialization
├── 📊 sample_db.sql        # Sample real estate data
├── 📋 requirements.txt     # Python dependencies
├── 📖 GEMINI_MIGRATION.md  # Migration guide from OpenAI
├── 📁 templates/           # HTML templates
│   └── 🏠 index.html       # Main web interface
├── 📁 static/              # Static assets
│   ├── 🖼️ images/          # Logo and images
│   └── 📄 README.md        # Static files documentation
└── 📁 __pycache__/         # Python cache files
```

---

## 🧠 How It Works

### 1. **Natural Language Processing**
User questions are processed by Google Gemini 2.0 Flash Experimental, which understands real estate terminology and context.

### 2. **Intelligent Tool Selection**
The AI agent autonomously selects appropriate tools:
- SQL queries for database analysis
- Google Maps for location services
- Vector search for semantic matching
- Code generation for reports

### 3. **Dynamic Content Generation**
Based on the analysis, the system generates:
- Interactive charts using Chart.js
- Google Maps with custom markers
- Professional PDF reports
- Rich markdown responses

### 4. **Security & Safety**
All AI-generated code is scanned for malicious patterns before execution, ensuring a secure environment.

---

## 🎯 Advanced Features

### 🔍 Semantic Search
Uses FAISS vector database with Google embeddings for intelligent property name and address matching.

### 📊 Complex Analytics
- **Holding Period Analysis**: Calculate investment holding periods
- **Market Segmentation**: Analyze by unit type, building, or location
- **Geographic Intelligence**: Distance calculations and proximity analysis
- **Trend Prediction**: Historical analysis and forecasting

### 🗺️ Interactive Mapping
- **Advanced Google Maps Integration**: Custom markers and clustering
- **School Proximity Analysis**: Find nearby educational institutions
- **Distance Calculations**: Multi-point route optimization
- **Boundary Visualization**: Market area definitions

### 📋 Report Generation
- **PDF Creation**: Executive-level reports with charts and analysis
- **Custom Layouts**: Professional formatting with ReportLab
- **Data Visualization**: Embedded charts and maps in reports

---

## 🔧 Configuration Options

### Database Settings
```python
# Modify in main.py for custom database connections
POSTGRES_USER = os.getenv("PG_USER")
POSTGRES_PASSWORD = os.getenv("PG_PASSWORD")
POSTGRES_PORT = os.getenv("PG_PORT")
POSTGRES_DB = os.getenv("PG_DB")
```

### AI Model Configuration
```python
# Modify in main.py for different Gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",  # or "gemini-pro", "gemini-2.0-flash"
    temperature=0.1,  # Adjust for creativity vs. consistency
)
```

### Conversation Memory
```python
# Modify in server.py for conversation history length
MAX_CONTEXT_LENGTH = 3  # Number of previous exchanges to remember
```

---

## 🧪 Testing & Development

### Run Tests
```bash
# Test database connection
python test_db.py

# Test Gemini integration
python test_gemini.py

# Test Google Places API
python sandbox.py
```

### Development Mode
```bash
# Run with debug mode
export FLASK_ENV=development
python server.py
```

---

## 🚀 Deployment

### Production Setup
1. **Use environment variables** for all sensitive configuration
2. **Set up proper database user permissions**
3. **Configure CORS** for your domain
4. **Use HTTPS** for secure communication
5. **Set up monitoring** and logging

### Docker Deployment (Optional)
```dockerfile
# Example Dockerfile structure
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]
```

---

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Ensure security best practices

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google AI** for Gemini 2.0 and embeddings
- **LangChain** for the agent framework
- **Google Maps Platform** for location services
- **PostgreSQL** for robust data storage
- **Open Source Community** for amazing tools and libraries

---

## 📞 Support & Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/sohailshk/suitsense-ai/issues)
- **Documentation**: [Read the full docs](https://github.com/sohailshk/suitsense-ai/wiki)
- **Email**: sohail@example.com

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

**🔄 Fork it to contribute or customize for your needs**

**📢 Share with others who might benefit from AI-powered real estate analytics**

---

*Made with ❤️ for the Real Estate & AI Community*

</div>
