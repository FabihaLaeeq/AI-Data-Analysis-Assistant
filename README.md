# 🤖 AI Data Analysis Assistant

An AI-powered data analysis application that helps users explore and understand datasets through an interactive interface.

The project combines **Python-based data analysis** with **Generative AI** to make dataset exploration easier for users, especially those who may not want to manually write code for every analysis task.

Users can provide their dataset, explore the available data, and receive AI-assisted explanations of the analysis and insights.

---

## ✨ Features

* 📂 Dataset upload and analysis
* 🔍 Dataset exploration and inspection
* 🧹 Data cleaning support
* 📊 Exploratory Data Analysis (EDA)
* 📈 Data visualization
* 🤖 AI-powered explanations
* 💬 Natural-language interaction with dataset insights
* 📋 Automatic interpretation of analysis results
* ⚡ Interactive web interface

---

## 🧠 How It Works

The application combines traditional data-analysis libraries with Generative AI.

```text
                 User
                  │
                  ▼
             Upload Dataset
                  │
                  ▼
          Data Loading & Inspection
                  │
                  ▼
          Data Cleaning / Analysis
                  │
                  ▼
             EDA & Visualization
                  │
                  ▼
             AI Explanation
                  │
                  ▼
          Insights & Understanding
```

The data-analysis layer handles operations such as inspecting, processing, and analyzing the dataset, while the AI component helps convert analytical results into understandable explanations.

---

## 🛠️ Technologies Used

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| **Python**        | Core programming language         |
| **Pandas**        | Data manipulation and analysis    |
| **NumPy**         | Numerical operations              |
| **Matplotlib**    | Data visualization                |
| **Seaborn**       | Statistical visualization         |
| **Google Gemini** | AI-powered explanations           |
| **Streamlit**     | Interactive application interface |
| **python-dotenv** | Environment variable management   |

---

## 📁 Project Structure

```text
AI Data Analysis Assistant/
│
├── ai/
│   ├── __init__.py
│   ├── _explanation.py
│   └── ...
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> The exact contents of the `ai/` directory may change as the project is developed further.

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/https://github.com/FabihaLaeeq/AI-Data-Analysis-Assistant.git
```

Then move into the project directory:

```bash
cd AI-Data-Analysis-Assistant
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Command Prompt

```cmd
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

The application uses the **Google Gemini API** for AI-powered explanations.

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace:

```text
your_api_key_here
```

with your actual API key.

### 🔐 Security

**Do not upload your `.env` file to GitHub.**

Your `.gitignore` should contain:

```text
.env
venv/
__pycache__/
*.pyc
```

This prevents sensitive information and unnecessary environment files from being committed to the repository.

---

# ▶️ Running the Application

After activating the virtual environment and installing the dependencies, run:

```bash
streamlit run app.py
```

The application should then open in your browser.

If it does not open automatically, Streamlit will display a local URL in the terminal.

---

# 📊 Data Analysis Workflow

The project follows a typical data-analysis workflow:

### 1. Data Loading

The application accepts a dataset and loads it for analysis.

### 2. Data Inspection

The dataset can be explored to understand:

* Number of rows and columns
* Column names
* Data types
* Missing values
* Basic dataset characteristics

### 3. Data Analysis

Python data-analysis libraries are used to process and analyze the dataset.

### 4. Visualization

Charts and visualizations can be used to identify patterns and relationships within the data.

### 5. AI Explanation

The AI component helps explain analytical findings in natural language, making the results easier to understand.

---

# 💬 Example Questions

The assistant can be used to ask questions such as:

```text
What columns are present in this dataset?

Are there any missing values?

What are the data types of the columns?

Give me a summary of this dataset.

What are the important patterns in this data?

Explain the analysis results.

Which variables appear to be related?
```

---

# 🎯 Project Objective

The main objective of this project is to combine **Data Analysis and Generative AI** into a single application.

Traditional data analysis often requires users to write Python code for tasks such as:

* Inspecting datasets
* Cleaning data
* Performing exploratory analysis
* Creating visualizations
* Interpreting results

This project aims to make that process more accessible by providing an interactive interface together with AI-assisted explanations.

---

# 🖼️ Screenshots

Screenshots of the working application will be added here.

### Application Interface

![Application Interface](screenshots/home.png)

### Dataset Analysis

![Dataset Analysis](screenshots/analysis.png)

### AI-Generated Insights

![AI Insights](screenshots/insights.png)

> Create a `screenshots` folder inside the project directory and place your actual screenshots there.

---

# 🚀 Future Improvements

The project can be extended with:

* 📑 Automatic analysis report generation
* 📊 Automatic dashboard creation
* 📈 More advanced visualizations
* 🧠 Improved natural-language data querying
* 🔎 Automated anomaly detection
* 📉 Statistical analysis automation
* 💾 Exportable analysis reports
* 📁 Support for additional dataset formats
* ☁️ Cloud deployment
* 🤖 More advanced AI agents for specialized analysis tasks

---

# 🔐 Security Notes

* API keys should always be stored in environment variables.
* `.env` should never be committed to GitHub.
* The virtual environment should not be uploaded to the repository.
* Sensitive credentials should never be included in source code.

---

# 📚 Learning Outcomes

Through this project, I worked with:

* Python programming
* Pandas and NumPy
* Exploratory Data Analysis
* Data visualization
* Generative AI
* API integration
* Environment variables
* Streamlit application development
* Git and GitHub
* Building an AI-powered data application

---

# 👩‍💻 Author

## Fabiha Laeeq

**Data Analysis & AI Enthusiast**

📍 Pakistan

🔗 **GitHub:**
https://github.com/FabihaLaeeq

🔗 **LinkedIn:**
https://www.linkedin.com/in/fabihalaeeq/

---

# ⭐ Acknowledgement

This project was developed as part of my learning journey in **Data Analysis, Python, Generative AI, and AI-powered application development**.

---

⭐ **If you find this project useful, consider giving the repository a star!**
