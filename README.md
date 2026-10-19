# Conversor de Bases Numéricas (Python + Flask)

Atividade prática de Redes de Computadores 1. Converte entre decimal, binário,
hexadecimal e octal (extra). A lógica está em `conversor.py` e não usa
`bin()`, `hex()`, `oct()`, `int(x, base)` nem bibliotecas de conversão.

## Infraestrutura necessária
- Python 3.9 ou superior
- Flask (listado em `requirements.txt`)

## Como rodar
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Abra http://127.0.0.1:5000

## Estrutura
- `app.py`: rotas (`/`, `/conversor`, `/grupo`, `/api/converter`)
- `conversor.py`: algoritmos de conversão (método posicional e divisões sucessivas)
- `templates/` e `static/`: páginas, modal e CSS

## Antes de entregar
Troque os nomes em `INTEGRANTES` no `app.py` pelos dos integrantes reais e
ajuste o que cada um desenvolveu.
