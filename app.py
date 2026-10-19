from flask import Flask, render_template_string

app = Flask(__name__)

PSYKERS = [
    "Лорд-псайкер Аврелий Каст",
    "Сестра Мириам Вейл",
    "Библиарий Теомар Скарн",
    "Астропат Йоссек Ренн",
    "Сангвиний-Дар, санкционированный псайкер",
    "Брат-литейщик Харкон Бэйл",
    "Безымянная, душа №4 127 090",
]

PAGE = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Золотой Трон: список жертв</title>
  <style>
    body { background:#0b0b0b; color:#d4af37; font-family:Georgia,serif;
           max-width:640px; margin:40px auto; padding:0 16px; }
    h1 { text-align:center; letter-spacing:2px; }
    li { padding:6px 0; border-bottom:1px solid #3a2f0b; }
    footer { margin-top:30px; text-align:center; opacity:.7; }
  </style>
</head>
<body>
  <h1>☩ Золотой Трон питается ☩</h1>
  <p>Души, отданные на поддержание жизни Императора ({{ names|length }}):</p>
  <ol>
    {% for n in names %}<li>{{ n }}</li>{% endfor %}
  </ol>
  <footer>Император защищает.</footer>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(PAGE, names=PSYKERS)

if __name__ == "__main__":
    app.run(debug=True)