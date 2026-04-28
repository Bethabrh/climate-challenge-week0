📘 Climate Challenge Week 0
🌍 Project Overview

This project is part of the Climate Challenge Week 0 assignment.
It introduces a simple Streamlit-based application for exploring basic climate-related data and building foundational skills in Python data applications, Git workflow, and environment setup.

⚙️ Tech Stack
Python 3.10+
Streamlit
Pandas
Jupyter Notebook (if used)
Git & GitHub
📁 Project Structure
climate-challenge-week0/
│
├── app/
│   └── main.py
│
├── data/
├── notebooks/
├── .gitignore
├── README.md
└── requirements.txt
🚀 Environment Setup
1. Clone the repository
git clone https://github.com/Bethabrh/climate-challenge-week0.git
cd climate-challenge-week0
2. Create virtual environment
python -m venv .venv
3. Activate environment

Windows (PowerShell):

.venv\Scripts\activate
📦 Install dependencies
pip install -r requirements.txt

If Streamlit is not installed:

pip install streamlit
▶️ Run the application
python -m streamlit run app/main.py
📓 Running Notebooks (if applicable)

If Jupyter notebooks are included:

jupyter notebook

Then open files inside the notebooks/ folder.

📌 Features (Current)
Basic Streamlit interface
Climate data display structure
Clean project organization
Git-based workflow
🧭 Roadmap (Future Improvements)
Add interactive climate visualizations
Integrate real climate datasets (CSV/API)
Improve UI with Streamlit components
Add data analysis dashboard
Deploy app online (Streamlit Cloud)
---

## EDA Branching Strategy

To ensure modular and well-organized analysis, the Exploratory Data Analysis (EDA) was structured using separate Git branches for each country.

### Country-specific branches:
- eda-kenya  
- eda-sudan  
- eda-tanzania  
- eda-nigeria  
- eda-ethiopia  

Each branch contains independent analysis focusing on data cleaning, preprocessing, and exploratory insights for its respective country.

### Workflow Summary:
1. Created a separate branch for each country
2. Performed country-specific EDA
3. Committed and pushed changes per branch
4. Merged all branches into the `main` branch via Pull Requests
5. Resolved merge conflicts where necessary

This workflow ensures:
- Clear separation of analysis per country
- Better version control and collaboration practice
- Traceable development history through Git commits and PRs

---

## Streamlit App

The project includes a Streamlit dashboard for visualizing and exploring climate-related insights.

To run the app:

```bash
streamlit run app/main.py
👤 Author

Bethel

