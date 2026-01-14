
# UITAP — Clique Físico no Botão (Playwright + Python) — POM

Automação da página **http://uitestingplayground.com/click** para clicar, via **mouse físico**, no botão `#badButton` ("Button That Ignores DOM Click Event") e validar que o botão fica **verde**.

## Stack
- Python 3.10+
- Playwright (sync API)
- Pytest
- Page Object Model (POM)
- GitHub Actions (CI) opcional

## Estrutura
```
uitap_click_pom/
├── README.md
├── LICENSE
├── requirements.txt
├── pytest.ini
├── .gitignore
├── run.py
├── screenshots/
├── .github/
│   └── workflows/
│       └── ci.yml
└── src/
    ├── pages/
    │   └── uitap_click_page.py
    ├── tests/
    │   └── test_uitap_click.py
    └── utils/
        └── __init__.py
```

## Como rodar localmente
```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# ou .venv\Scripts\activate  # Windows
pip install -r requirements.txt
python -m playwright install
python run.py
```
- O script salva um screenshot em `screenshots/btn_green.png`.

### Rodar testes
```bash
pytest
```

## Publicar no GitHub
```bash
git init
git add .
git commit -m "feat: UITAP clique físico com POM (Playwright)"
git branch -M main
git remote add origin https://github.com/<seu-usuario>/<nome-repo>.git
git push -u origin main
```

## CI (GitHub Actions)
O workflow `ci.yml` instala Playwright, baixa os browsers e executa os testes em **Ubuntu**.

## Notas técnicas
- A página foi criada para ignorar cliques DOM. Por isso usamos `bounding_box()` + `page.mouse.click(x,y)`.
- A cor "verde" do Bootstrap é `rgb(40, 167, 69)`. Validamos via `getComputedStyle` e `expect(...).to_have_css(...)`.
