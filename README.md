# Minimal Flask site for Azure App Service

This repo contains a single-file Flask application that serves a static greeting page. The page welcomes the visitor and shows the name of the Azure App Service instance via the `WEBSITE_SITE_NAME` environment variable that App Service sets automatically.

## Local run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:8000`.

## Deploy to Azure App Service

1. Create a new Web App (Linux, Python 3.11 or similar) from the Azure portal.
2. Under **Deployment Center**, connect the Web App directly to the GitHub repo that contains this project.
3. Set **Startup Command** to `python app.py` to skip any build steps.
4. Save the configuration. After deployment finishes, navigate to the app URL; you should see the greeting along with the Web App name.

No build pipeline is required; App Service simply installs `requirements.txt` and runs the Flask app.

