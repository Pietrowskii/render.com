import random
from flask import Flask, render_template_string

app = Flask(__name__)

TITLES = [
    "Лорд-псайкер",
    "Санкционированный псайкер",
    "Астропат-хорист",
    "Сестра",
    "Брат-аколит",
    "Библиарий-изгнанник",
    "Дикий псайкер",
    "Провидец душ",
    "Беглый ведьмак",
    "Мистик Адептус Астра Телепатика",
]

FIRST_NAMES = [
    "Аврелий",
    "Мириам",
    "Теомар",
    "Йоссек",
    "Харкон",
    "Валерий",
    "Кассия",
    "Мордекай",
    "Себастьян",
    "Игнатий",
    "Ливия",
    "Тиберий",
    "Ксавьер",
    "Геката",
    "Люций",
    "Корвус",
    "Селена",
    "Захария",
    "Агата",
    "Деметрий",
    "Соломон",
]

LAST_NAMES = [
    "Каст",
    "Вейл",
    "Скарн",
    "Ренн",
    "Бэйл",
    "Восс",
    "Кросс",
    "Морн",
    "Вэнс",
    "Торн",
    "Дрейк",
    "Стерн",
    "Кейн",
    "Фрост",
    "Грим",
    "Варлок",
    "Краун",
    "Шрайк",
    "Нокс",
    "Пейн",
]

ORIGINS = [
    "с Кадии",
    "из улья Некромунда",
    "с Терры",
    "с мира-кузницы Марс",
    "с Вальхаллы",
    "из сектора Каликсида",
    "с Мордии",
    "с Армагеддона",
    "с Чёрного Корабля «Безмолвный Конвой»",
    "с Чёрного Корабля «Оковы Веры»",
]


def generate_psykers(count=1000):
    psykers = []
    for _ in range(count):
        roll = random.random()
        if roll < 0.25:
            # 25% шанс на безымянного узника Чёрных Кораблей
            num = f"{random.randint(1, 999)} {random.randint(100, 999)} {random.randint(100, 999)}"
            grade = random.choice(["Каппа", "Йота", "Тета", "Эта", "Дзета"])
            psykers.append(
                f"Безымянная душа №{num} [Уровень псайканы: {grade}]"
            )
        elif roll < 0.65:
            # 40% шанс на имя + титул
            psykers.append(
                f"{random.choice(TITLES)} {random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
            )
        else:
            # 35% шанс на имя + титул + происхождение
            psykers.append(
                f"{random.choice(TITLES)} {random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)} ({random.choice(ORIGINS)})"
            )
    return psykers


PAGE = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Золотой Трон: список жертв</title>
  <style>
    body { background:#0b0b0b; color:#d4af37; font-family:Georgia,serif;
           max-width:700px; margin:30px auto; padding:0 16px; }
    h1 { text-align:center; letter-spacing:2px; margin-bottom: 10px; }
    .subtitle { text-align:center; margin-bottom: 20px; opacity: 0.85; }
    
    /* Контейнер с прокруткой */
    .scroll-box {
      max-height: 65vh;
      overflow-y: auto;
      border: 1px solid #5a460c;
      background: #110f0a;
      padding: 10px 20px 10px 45px;
      box-shadow: inset 0 0 25px #000;
    }
    
    /* Стилизация полосы прокрутки (WebKit) */
    .scroll-box::-webkit-scrollbar { width: 10px; }
    .scroll-box::-webkit-scrollbar-track { background: #0b0b0b; border-left: 1px solid #3a2f0b; }
    .scroll-box::-webkit-scrollbar-thumb { background: #5a460c; }
    .scroll-box::-webkit-scrollbar-thumb:hover { background: #d4af37; }

    ol { margin: 0; padding: 0; }
    li { padding: 8px 4px; border-bottom: 1px solid #2a2208; font-size: 0.95rem; }
    li:hover { background: #1c180d; }
    
    .btn {
      display: block; width: fit-content; margin: 15px auto;
      padding: 8px 20px; background: #1c180d; color: #d4af37;
      border: 1px solid #5a460c; text-decoration: none; cursor: pointer;
    }
    .btn:hover { background: #3a2f0b; }
    footer { margin-top:20px; text-align:center; opacity:.7; font-size: 0.9rem; }
  </style>
</head>
<body>
  <h1>☩ Золотой Трон питается ☩</h1>
  <p class="subtitle">Суточная квота душ на поддержание жизни Императора ({{ names|length }}):</p>
  
  <div class="scroll-box">
    <ol>
      {% for n in names %}<li>{{ n }}</li>{% endfor %}
    </ol>
  </div>

  <a href="/" class="btn">Загрузить следующую партию Чёрных Кораблей</a>
  <footer>Император защищает.</footer>
</body>
</html>
"""


@app.route("/")
def index():
    psykers_list = generate_psykers(1000)
    return render_template_string(PAGE, names=psykers_list)


if __name__ == "__main__":
    app.run(debug=True)