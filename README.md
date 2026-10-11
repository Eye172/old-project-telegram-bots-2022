# Old Project: Telegram Bots (2022)

A collection of Telegram bots built during the **Kodland** programming course in 2022.
Each bot was a standalone project to practice Python, the Telegram Bot API, and various libraries.

---

## Bots

### 🖼 Image Filters Bot — `Main_Image_Filters_Bot.py`
Applies image filters to photos sent by the user via PIL (Pillow).

**Commands:** `/blur` `/sharpen` `/smooth` `/emboss` `/contour` `/white_black` `/negativ` `/brightness` `/sunset` `/aliy` `/custom_filter` `/random_filter`

---

### 😂 Meme Bot — `Main_Mem_Bot.py`
Meme generator. The user sends a photo, then types top and bottom text — the bot draws the text onto the image and returns a finished meme.

---

### 📚 Eye of Knowledge Bot — `Main_Oko_Znaniy_Bot.py` / `Main_Oko_Znaniy_Bot_2.py`
Searches Wikipedia in any language and returns article summaries. Also has a yes/no oracle for questions about the future.

**Commands:** `/language` `/vechnoe_znanie` `/vechnoe_znanie_file` `/future`

---

### 🔐 Validator Bot — `Main_Validator_Bot.py`
Checks password strength (minimum length, must contain digits). Also includes a countdown timer and a character/word counter.

**Commands:** `/check_password` `/timer` `count <text>`

---

### 🧠 Quiz Bot — `Main_Victorina_Bot.py`
Sends random math addition problems as native Telegram polls (Quiz mode) so the user answers directly in the chat.

**Commands:** `/quiz`

---

### 🤖 Voithos Bot — `Main_Voithos_Bot.py` / `Main_Voithos_Bot_COPY.py`
General-purpose utility bot: arithmetic, word counter, echo, yes/no oracle, random number generator, and a countdown timer.

**Commands:** `/sum` `/min` `/umn` `/del` `/count` `/eho` `/vopros` `/random_ot_0_do_10` `/timer`

---

### 💻 Console Prototype — `43dadax.py`
A terminal version of the Voithos bot (no Telegram) used to test logic before adding the bot API layer. Also draws a flower with Python's `turtle` module.

---

## Tech Stack

- Python 3
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v13
- [Pillow](https://python-pillow.org/) (PIL) — image processing
- [wikipedia](https://pypi.org/project/wikipedia/) — Wikipedia search
- `turtle` (stdlib) — console prototype drawing

## Setup

1. Install dependencies:
   ```bash
   pip install python-telegram-bot==13.* Pillow wikipedia easygui
   ```

2. Create a `*_token.py` file for the bot you want to run, e.g. `Voithos_Bots_token.py`:
   ```python
   bot_token = "YOUR_TOKEN_HERE"
   ```
   Get a token from [@BotFather](https://t.me/BotFather) on Telegram.

3. Run the bot:
   ```bash
   python Main_Voithos_Bot.py
   ```

> Token files (`*_token.py`) are excluded from this repository via `.gitignore`.


---

<sub>Account history: Magitcian172 → Eye172 (same developer). [Authorship note](AUTHORSHIP.md).</sub>
