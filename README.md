# ODISHA AI ONE — Build AI for the World
> **Tagline:** *Local Intelligence. Global Impact.*

A unified open-source AI innovation platform engineered for students, researchers, grassroots innovators, and startups in Odisha to learn artificial intelligence, discover verified resources, develop impactful local solutions, and showcase prototypes to a global audience.

---

## 🌐 Quick Access URL

Your application is currently running live:

* **Local URL:** [http://localhost:8501](http://localhost:8501)
* **Network URL:** `http://10.20.3.129:8501`

---

## 📁 Project Architecture & File Purpose

```
odisha_ai_one/
├── app.py                      # Main entry point; initializes DB, session state, routing & footer
├── requirements.txt            # Python dependencies (streamlit, pandas, plotly)
├── .streamlit/
│   └── config.toml             # Custom color theme (Deep Navy #101B33, Emerald #10B981, Teal #0F766E)
├── assets/
│   └── styles.css              # Custom styling: typography, KPI boxes, status badges, hero container
├── components/
│   ├── __init__.py             # Component package exports
│   ├── header.py               # Top persistent header with branding and session tags
│   ├── sidebar.py              # Persistent 9-page navigation sidebar with active indicator
│   ├── cards.py                # Reusable KPI metric card, Project card, and Resource card
│   ├── footer.py               # Platform footer with disclosures, copyright, and pillars
│   └── ui_utils.py             # CSS loader, status pill formatters, empty-state containers
├── database/
│   ├── __init__.py             # Database package exports
│   ├── db_connection.py        # Safe SQLite connection context manager with dict factory
│   ├── schema.py               # SQLite tables: projects, resources, chat_history, activity_logs
│   └── seed_data.py            # Verified AI resources and labeled demo projects (is_sample=1)
├── services/
│   ├── __init__.py             # Services package exports
│   ├── project_service.py      # Project CRUD, validation, search, filter, and authorization
│   ├── metrics_service.py      # Real DB aggregations, Plotly datasets, and target comparisons
│   ├── resource_service.py     # Search and filter for verified open-source AI assets
│   ├── ai_assistant_service.py # Bilingual (Odia & English) domain knowledge reasoning engine
│   └── innovation_service.py   # 4 Innovation Lab interactive demos (NLP, Agri, Health, Artisan)
└── views/
    ├── __init__.py             # Views package exports
    ├── home_view.py            # Page 1: Hero, workflow ribbon, 5 modules, featured projects
    ├── dashboard_view.py       # Page 2: Real DB KPIs, category donut, stage chart, activity log
    ├── assistant_view.py       # Page 3: Odia & English conversational chat interface
    ├── project_hub_view.py     # Page 4: Project discovery, multi-filter search, validated submit form
    ├── innovation_lab_view.py  # Page 5: 4 interactive AI testbeds with disclaimers
    ├── resource_hub_view.py    # Page 6: Verified models, datasets, tutorials, courses
    ├── global_impact_view.py   # Page 7: Live DB vs Sample Data vs 2026-2027 future targets
    ├── about_view.py           # Page 8: Vision, mission, student guide, ethics manifesto, roadmap
    └── settings_view.py        # Page 9: Language, accessibility, session profile, DB utilities
```

---

## 🛠️ How Frontend Connects to Backend

1. **Decoupled Architecture**: None of the UI page views in `views/` write raw SQL queries or handle raw database cursors.
2. **Service Gateway**: Page views call pure Python service functions in `services/`:
   * `project_service.py` handles business logic and input validation before saving to SQLite.
   * `metrics_service.py` computes real-time database counts directly from tables.
   * `ai_assistant_service.py` matches user intents and persists chat dialogues.
   * `innovation_service.py` drives the interactive testbeds.
3. **Database Integrity**: The `database/` layer manages schema migrations, connection pooling, and strict separation between user-created records and sample demonstration records (`is_sample = 1`).

---

## 💻 How to Run Locally

If the server is ever stopped, you can restart it from PowerShell or Command Prompt:

```powershell
python -m streamlit run app.py
```

Then open your browser at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🧪 How to Test Every Module

1. **Home (`Page 1`)**:
   * Click **"Explore AI Projects"** → automatically switches to Project Hub.
   * Click **"Open AI Assistant"** → navigates to Odia AI Assistant.
   * Click **"Start an AI Project"** → opens the project submission form.
2. **AI Dashboard (`Page 2`)**:
   * Inspect the 5 KPI metric cards (derived from SQLite).
   * Hover over the Plotly donut chart to see category breakdowns.
   * Toggle sample data from the sidebar or click **"Load Demo Sample Data"** to verify empty-state handling.
3. **Odia AI Assistant (`Page 3`)**:
   * Switch between **English** and **Odia** using the language toggle.
   * Click any suggested chip (e.g., *"How can AI help farmers in Odisha?"*).
   * Type a custom query in the chat input and click **Send 🚀**.
   * Click **"Clear Chat"** to test history reset.
4. **AI Project Hub (`Page 4`)**:
   * Under **"Browse Projects"**, search by title or filter by category (e.g. *Agriculture*).
   * Click **"Details 🔍"** on any project to open the inspection panel.
   * Under **"Submit New Project"**, submit a test project with validation (try submitting with an empty title to see validation errors).
   * Under **"Manage My Submissions"**, edit or delete projects owned by your session.
5. **AI Innovation Lab (`Page 5`)**:
   * **Demo A (Odia Text Helper):** Select a sample text, choose *Translate to Odia* or *Summarize*, and click **Run Text Helper ⚡**.
   * **Demo B (Agriculture AI):** Select a field scenario (e.g., *Paddy - Leaf Blast Disease*) and verify IPM advice and KVK disclaimers.
   * **Demo C (Rural Healthcare AI):** Enter symptoms and verify the structured doctor question checklist and red-flag emergency notice.
   * **Demo D (Artisan AI):** Select *Sambalpuri Ikat* or *Pattachitra* and generate an export brand narrative with SEO tags.
6. **AI Resource Hub (`Page 6`)**:
   * Search for *"IndicBERT"* or filter by *"AI Models"*.
   * Click *"Visit Official Resource ↗"* to verify authentic external links.
7. **Global Impact Dashboard (`Page 7`)**:
   * Switch between the three tabs: *Live Database Metrics*, *Sample Demonstration Data*, and *Proposed Future Targets*.
8. **About the Initiative (`Page 8`)**:
   * Review the ethical AI guidelines, roadmap, and student participation paths.
9. **Settings (`Page 9`)**:
   * Update your contributor name and affiliation.
   * Toggle High Contrast mode or Compact layout.
   * Use Database Utilities to reset or load sample data.

---

## ☁️ How to Deploy on Streamlit Community Cloud

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of Odisha AI One platform"
   git remote add origin https://github.com/<your-username>/odisha-ai-one.git
   git branch -M main
   git push -u origin main
   ```
2. **Deploy on Streamlit Cloud**:
   * Go to [share.streamlit.io](https://share.streamlit.io) and log in with GitHub.
   * Click **"New app"**.
   * Select your repository: `<your-username>/odisha-ai-one`.
   * Set Branch to `main`.
   * Set Main file path to `app.py`.
   * Click **"Deploy!"**.
3. **Persistence**:
   * The application uses SQLite which writes to `data/odisha_ai.db` in the container.
   * Pre-seeded verified resources and demonstration data load automatically on first startup.
