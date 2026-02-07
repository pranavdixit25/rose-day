from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# ---------- PASSWORD PAGE ----------
password_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Secret Entry 🤫</title>
    <style>
        body {
            font-family: Arial;
            background: #fff0f5;
            text-align: center;
            padding-top: 80px;
        }
        input, button {
            padding: 10px;
            font-size: 16px;
            margin-top: 10px;
        }
        .hint {
            margin-top: 15px;
            font-style: italic;
            color: #555;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h2>🔐 Enter Password</h2>
    <form method="post">
        <input type="text" name="password" placeholder="Answer here" required><br>
        <button type="submit">Enter</button>
    </form>
    <div class="hint">"aap dudu ki kya ho?" 😏</div>
    {% if error %}
        <div class="error">Galat jawab 😌 phir se try karo</div>
    {% endif %}
</body>
</html>
"""

# ---------- FLOWER PAGE ----------
flower_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Choose a Flower 🌸</title>
    <style>
        body {
            font-family: Arial;
            background: #fff;
            text-align: center;
            padding-top: 80px;
        }
        .flower {
            display: block;
            margin: 10px auto;
            padding: 12px;
            width: 200px;
            font-size: 18px;
            border: none;
            cursor: pointer;
        }
        .red { color: red; }
        .orange { color: orange; }
        .pink { color: hotpink; }
        .yellow { color: goldenrod; }
        .white { color: gray; }
    </style>
</head>
<body>
    <h2>🌹 Choose a Flower 🌹</h2>

    <form action="/flower" method="post">
        <button class="flower red" name="choice" value="red">Red Rose</button>
        <button class="flower orange" name="choice" value="orange">Orange Rose</button>
        <button class="flower pink" name="choice" value="pink">Pink Rose</button>
        <button class="flower yellow" name="choice" value="yellow">Yellow Rose</button>
        <button class="flower white" name="choice" value="white">White Rose</button>
    </form>

    {% if error %}
        <p style="color:red;">😌 Nahi… phir se choose karo</p>
    {% endif %}
</body>
</html>
"""

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def password():
    error = False
    if request.method == "POST":
        pwd = request.form.get("password")
        if pwd.lower() == "bubu":
            return redirect(url_for("flower"))
        else:
            error = True
    return render_template_string(password_page, error=error)


@app.route("/flower", methods=["GET", "POST"])
def flower():
    error = False
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice == "red":
            return "<h1 style='text-align:center;'>RED selected ❤️ (Next step coming soon)</h1>"
        else:
            error = True
    return render_template_string(flower_page, error=error)


if __name__ == "__main__":
    app.run(debug=True)
