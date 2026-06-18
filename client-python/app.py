from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "bilingual-flask-secret")
API_URL = os.getenv("API_URL", "http://localhost:5000/api")

LANGUAGES = [
    {"code": "hi", "name": "Hindi"},
    {"code": "ta", "name": "Tamil"},
    {"code": "ml", "name": "Malayalam"},
    {"code": "te", "name": "Telugu"},
    {"code": "kn", "name": "Kannada"},
]
CATEGORIES = ["JavaScript", "Python", "React", "Node.js", "Databases"]
LANG_NAMES = {l["code"]: l["name"] for l in LANGUAGES}
VALID_LANG_CODES = {l["code"] for l in LANGUAGES}

def get_headers():
    token = session.get("token")
    return {"Authorization": f"Bearer {token}"} if token else {}

def get_language():
    return session.get("language", "hi")

@app.route("/")
def home():
    counts = {cat: 0 for cat in CATEGORIES}
    last_studied = None
    try:
        res = requests.get(f"{API_URL}/units/", headers=get_headers(), timeout=5)
        units = res.json() if res.ok else []
    except Exception:
        units = []
    for u in units:
        cat = u.get("category", "").lower()
        for c in CATEGORIES:
            if CAT_SLUG.get(c.lower(), c.lower()) == cat:
                counts[c] += 1
    if session.get("token"):
        try:
            res_user = requests.get(f"{API_URL}/auth/me", headers=get_headers(), timeout=5)
            if res_user.ok:
                ls = res_user.json().get("lastStudied")
                if ls:
                    last_studied = {
                        "title": ls.get("title", ""),
                        "category": ls.get("category", ""),
                        "unit_id": ls.get("unit_id", ""),
                        "at": ls.get("at", "")
                    }
        except Exception:
            pass
    return render_template("home.html", counts=counts, categories=CATEGORIES, last_studied=last_studied)

CAT_SLUG = {"node.js": "nodejs", "databases": "databases"}

@app.route("/courses/<category>")
def courses(category):
    try:
        res = requests.get(f"{API_URL}/units/", headers=get_headers(), timeout=5)
        all_units = res.json() if res.ok else []
    except Exception:
        all_units = []
    slug = CAT_SLUG.get(category.lower(), category.lower())
    units = [u for u in all_units if u.get("category", "").lower() == slug]
    return render_template("courses.html", units=units, category=category, categories=CATEGORIES)

@app.route("/articles/<article_id>")
def article(article_id):
    try:
        res = requests.get(f"{API_URL}/articles/{article_id}", headers=get_headers(), timeout=5)
    except Exception:
        return render_template("error.html", message="Could not reach server"), 503
    if not res.ok:
        return render_template("error.html", message="Article not found"), 404
    art = res.json()
    art.setdefault("sections", [])
    language = get_language()
    return render_template("article.html", article=art, language=language,
                           lang_name=LANG_NAMES.get(language, language), languages=LANGUAGES)

@app.route("/unit/<unit_id>")
def unit(unit_id):
    try:
        res = requests.get(f"{API_URL}/units/{unit_id}", headers=get_headers(), timeout=5)
    except Exception:
        return render_template("error.html", message="Could not reach server"), 503
    if not res.ok:
        return render_template("error.html", message="Unit not found"), 404
    u = res.json()
    u.setdefault("sections", [])
    language = get_language()
    # track last studied
    if session.get("token"):
        try:
            requests.post(f"{API_URL}/units/track",
                json={"token": session["token"], "unit_id": unit_id}, timeout=3)
        except Exception:
            pass
    return render_template("article.html", article=u, language=language,
                           lang_name=LANG_NAMES.get(language, language), languages=LANGUAGES)

@app.route("/api/translate", methods=["POST"])
@app.route("/api/translate/", methods=["POST"])
def translate():
    data = request.json or {}
    try:
        res = requests.post(f"{API_URL}/translate/", json=data, timeout=60)
        return jsonify(res.json() if res.ok else {"translated": data.get("text", "")})
    except Exception:
        return jsonify({"translated": data.get("text", "")})

@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        try:
            res = requests.post(f"{API_URL}/auth/login", json={
                "email": request.form.get("email", ""),
                "password": request.form.get("password", "")
            }, timeout=5)
            if res.ok:
                session["token"] = res.json()["token"]
                session["user"]  = res.json()["user"]
                return redirect(url_for("home"))
            error = res.json().get("detail", "Login failed")
        except Exception:
            error = "Server error. Please try again."
    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""
    if request.method == "POST":
        try:
            res = requests.post(f"{API_URL}/auth/register", json={
                "name":              request.form.get("name", ""),
                "email":             request.form.get("email", ""),
                "password":          request.form.get("password", ""),
                "preferredLanguage": "hi"
            }, timeout=5)
            if res.ok:
                session["token"] = res.json()["token"]
                session["user"]  = res.json()["user"]
                return redirect(url_for("home"))
            error = res.json().get("detail", "Registration failed")
        except Exception:
            error = "Server error. Please try again."
    return render_template("register.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/set-language", methods=["POST"])
def set_language():
    lang = request.form.get("language", "hi")
    if lang in VALID_LANG_CODES:
        session["language"] = lang
    return ("", 204)   # JS fetch — no redirect needed

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true", port=3000)
