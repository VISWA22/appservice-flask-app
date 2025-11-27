from flask import Flask, render_template_string
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        :root {
            color-scheme: light dark;
        }
        body {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            margin: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle at top, #f5f5f5, #e0e0e0);
        }
        main {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 18px;
            padding: 3rem 4rem;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.12);
            text-align: center;
        }
        h1 {
            margin-bottom: 0.5rem;
            font-size: clamp(2rem, 4vw, 3rem);
            color: #0f172a;
        }
        p {
            margin: 0.4rem 0;
            font-size: 1.15rem;
            color: #444;
        }
        .app-name {
            font-weight: 600;
            color: #2563eb;
        }
    </style>
</head>
<body>
<main>
    <h1>Hello from Azure!</h1>
    <p>Welcome to this demo Flask site.</p>
    <p>Currently running on: <span class="app-name">{{ app_name }}</span></p>
</main>
</body>
</html>
"""


@app.route("/")
def home():
    app_name = os.environ.get("WEBSITE_SITE_NAME", "Azure App Service")
    return render_template_string(TEMPLATE, title="Azure Flask Greeting", app_name=app_name)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)

