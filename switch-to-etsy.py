"""
Repoe o site para vender pelo Etsy em vez do Paddle.

Duas mudancas mecanicas:
  1. Preco $29 -> $19  (o Etsy tem taxa maior e o mercado da categoria vive
     entre US$ 12 e US$ 14; $29 era o preco de venda direta)
  2. Botoes de compra -> a loja do Etsy, no lugar de buy.paddle.com/REPLACE-ME

O texto juridico (terms / privacy / refund) NAO e tocado aqui. Trocar quem e o
vendedor oficial e reescrita, nao busca-e-substitui, e esta feito a mao.

Uso:
    python switch-to-etsy.py              # aplica
    python switch-to-etsy.py --check      # so relata, nao escreve
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = "--check" in sys.argv

# URL previsivel da loja. Quando o anuncio existir, troque pela URL do listing
# (converte melhor: cai no produto, nao na vitrine) rodando set-etsy-link.py.
ETSY = "https://www.etsy.com/shop/TutorLedger"
OLD_LINK = "https://buy.paddle.com/REPLACE-ME"

TARGETS = [
    "index.html",
    "tutoring-profit-calculator/index.html",
    "blog/build_blog.py",
    "blog/index.html",
    "blog/client-wont-pay-tutoring/index.html",
    "blog/track-tutoring-payments-google-sheets/index.html",
    "blog/tutoring-business-profit-margin/index.html",
    "blog/tutoring-cancellation-no-show-policy/index.html",
]

# Ordem importa: as regras mais especificas primeiro.
RULES = [
    (OLD_LINK, ETSY),
    ('"price":"29.00"', '"price":"19.00"'),
    ("$29", "$19"),
    # Ficou desatualizado: a pasta tem 12 abas desde que Health Check e
    # Chart Data entraram. Vendia menos do que entrega.
    ("Nine connected sheets", "Twelve connected sheets"),
    ("nine connected sheets", "twelve connected sheets"),
]

total, touched = 0, []
for rel in TARGETS:
    p = os.path.join(HERE, rel)
    if not os.path.exists(p):
        print(f"  ausente: {rel}")
        continue
    src = open(p, encoding="utf-8").read()
    out, hits = src, 0
    for a, b in RULES:
        n = out.count(a)
        if n:
            out = out.replace(a, b)
            hits += n
    if hits:
        touched.append((rel, hits))
        total += hits
        if not CHECK:
            open(p, "w", encoding="utf-8").write(out)

for rel, n in touched:
    print(f"  {n:>3}  {rel}")
print(f"\n{'(check) ' if CHECK else ''}{total} substituicoes em {len(touched)} arquivos")

# Sobrou algum vestigio nos arquivos que o cliente ve?
leftovers = []
for rel in TARGETS:
    p = os.path.join(HERE, rel)
    if not os.path.exists(p):
        continue
    txt = open(p, encoding="utf-8").read()
    for pat in (r"\$29\b", r"buy\.paddle\.com", r"REPLACE-ME"):
        for m in re.finditer(pat, txt):
            leftovers.append(f"{rel}: {m.group(0)}")
if leftovers:
    print("\nAINDA PRESENTE:")
    for l in leftovers[:20]:
        print("   -", l)
else:
    print("Nenhum $29, buy.paddle.com ou REPLACE-ME restante nos alvos.")
