from datetime import date
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

DAILY_CACHE = {"date": None, "psykers": []}


def get_daily_psykers(count=1000):
    today_str = date.today().isoformat()

    if DAILY_CACHE["date"] == today_str:
        return DAILY_CACHE["psykers"], today_str

    rng = random.Random(today_str)
    psykers = []

    for _ in range(count):
        roll = rng.random()
        if roll < 0.25:
            num = f"{rng.randint(1, 999)} {rng.randint(100, 999)} {rng.randint(100, 999)}"
            grade = rng.choice(["Каппа", "Йота", "Тета", "Эта", "Дзета"])
            psykers.append(
                f"Безымянная душа №{num} [Уровень псайканы: {grade}]"
            )
        elif roll < 0.65:
            psykers.append(
                f"{rng.choice(TITLES)} {rng.choice(FIRST_NAMES)} {rng.choice(LAST_NAMES)}"
            )
        else:
            psykers.append(
                f"{rng.choice(TITLES)} {rng.choice(FIRST_NAMES)} {rng.choice(LAST_NAMES)} ({rng.choice(ORIGINS)})"
            )

    DAILY_CACHE["date"] = today_str
    DAILY_CACHE["psykers"] = psykers
    return psykers, today_str


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
    h1 { text-align:center; letter-spacing:2px; margin-bottom: 5px; }
    .subtitle { text-align:center; margin-bottom: 5px; opacity: 0.85; }
    .timer { text-align:center; margin-bottom: 20px; font-size: 0.9rem; color: #a68523; }
    
    .scroll-box {
      max-height: 65vh;
      overflow-y: auto;
      border: 1px solid #5a460c;
      background: #110f0a;
      padding: 10px 20px 10px 45px;
      box-shadow: inset 0 0 25px #000;
    }
    
    .scroll-box::-webkit-scrollbar { width: 10px; }
    .scroll-box::-webkit-scrollbar-track { background: #0b0b0b; border-left: 1px solid #3a2f0b; }
    .scroll-box::-webkit-scrollbar-thumb { background: #5a460c; }
    .scroll-box::-webkit-scrollbar-thumb:hover { background: #d4af37; }

    ol { margin: 0; padding: 0; }
    li { padding: 8px 4px; border-bottom: 1px solid #2a2208; font-size: 0.95rem; }
    li:hover { background: #1c180d; }
    
    footer { margin-top:20px; text-align:center; opacity:.7; font-size: 0.9rem; }
  </style>
</head>
<body>
  <h1>☩ Золотой Трон питается ☩</h1>
  <p class="subtitle">Суточная квота душ от <b>{{ current_date }}</b> ({{ names|length }}):</p>
  <div class="timer">Следующая подача душ через: <span id="countdown">--:--:--</span></div>
  
  <div class="scroll-box">
    <ol>
      {% for n in names %}<li>{{ n }}</li>{% endfor %}
    </ol>
  </div>

  <footer>Император защищает.</footer>

  <script>
    function updateCountdown() {
      const now = new Date();
      const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, 0, 0, 0);
      const diff = tomorrow - now;

      // Если наступила полночь (00:00:00) — перезагружаем страницу за новым списком
      if (diff <= 0) {
        window.location.reload();
        return;
      }

      const hours = String(Math.floor((diff / (1000 * 60 * 60)) % 24)).padStart(2, '0');
      const minutes = String(Math.floor((diff / 1000 / 60) % 60)).padStart(2, '0');
      const seconds = String(Math.floor((diff / 1000) % 60)).padStart(2, '0');

      document.getElementById('countdown').textContent = `${hours}:${minutes}:${seconds}`;
    }

    setInterval(updateCountdown, 1000);
    updateCountdown();
  </script>
</body>
</html>
"""


@app.route("/")
def index():
    psykers_list, today_str = get_daily_psykers(1000)
    return render_template_string(
        PAGE, names=psykers_list, current_date=today_str
    )


if __name__ == "__main__":
    app.run(debug=True)