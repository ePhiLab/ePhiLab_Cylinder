eΦLab: Cilindro
Base visual del nuevo repositorio de la aplicación educativa.
Estructura inicial
```text
ephi-lab-cilindro/
├── app.py
├── assets/
├── modules/
├── pages/
├── ui/
│   ├── __init__.py
│   ├── theme.py
│   └── components.py
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── .gitignore
```
Primera ejecución
```bash
pip install -r requirements.txt
streamlit run app.py
```
Logo
Coloque el archivo:
```text
assets/EphiCiencia_Logo.png
```
Si todavía no está disponible, la aplicación funciona sin mostrar el logo.
