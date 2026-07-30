"""
Alterna o site entre "pre-lancamento" e "a venda".

Enquanto a loja do Etsy nao existe, os botoes de compra apontariam para um 404.
Isso e pior que nao ter trafego: queima a primeira impressao de quem ja estava
interessado. No modo "soon" eles viram captura de e-mail, e o trafego adiantado
dos pins vira lista para o dia do lancamento.

Uso:
    python launch-mode.py soon
    python launch-mode.py live https://www.etsy.com/listing/123456/...
"""

import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "index.html")
FORMSPREE = "https://formspree.io/f/mjgnlzzq"

MODE = sys.argv[1] if len(sys.argv) > 1 else ""
URL = sys.argv[2] if len(sys.argv) > 2 else ""
if MODE not in ("soon", "live") or (MODE == "live" and not URL):
    raise SystemExit(__doc__)

s = io.open(PAGE, encoding="utf-8", newline="").read()

NAV_LIVE = '<a class="btn glow" href="{u}" rel="noopener">Get it — $19</a>'
NAV_SOON = '<a class="btn glow" href="#notify">Notify me</a>'

HERO_LIVE = """      <p style="margin-bottom:22px">
        <a class="btn lg glow" href="{u}" rel="noopener">Get TutorLedger</a>
      </p>
"""
HERO_SOON = """      <div id="notify" style="margin-bottom:22px">
        <form class="notify" action="{f}" method="POST">
          <input type="email" name="email" placeholder="you@yourbusiness.com" required aria-label="Your email address">
          <input type="hidden" name="source" value="prelaunch-hero">
          <button class="btn lg glow" type="submit">Tell me when it's ready</button>
        </form>
        <p class="tiny faint" style="margin:9px 0 0">Launching shortly on Etsy at $19. One email when it goes live — nothing else, unsubscribe any time.</p>
      </div>
"""

CTA_LIVE = """    <div class="btnrow">
      <a class="btn lg onnavy glow" href="{u}" rel="noopener">Get TutorLedger</a>
      <a class="btn lg ghost" href="tutoring-profit-calculator/" style="color:#c3cddb; border-color:#2c3d5c">Try the free calculator</a>
    </div>
    <p class="tiny" style="color:#8496af; margin:0">Secure checkout on Etsy · Instant download · 30-day refund · One-time payment</p>
"""
CTA_SOON = """    <form class="notify onnavy" action="{f}" method="POST" style="margin-bottom:14px">
      <input type="email" name="email" placeholder="you@yourbusiness.com" required aria-label="Your email address">
      <input type="hidden" name="source" value="prelaunch-cta">
      <button class="btn lg onnavy glow" type="submit">Tell me when it's ready</button>
    </form>
    <div class="btnrow" style="margin-bottom:14px">
      <a class="btn lg ghost" href="tutoring-profit-calculator/" style="color:#c3cddb; border-color:#2c3d5c">Try the free calculator</a>
    </div>
    <p class="tiny" style="color:#8496af; margin:0">Launching shortly on Etsy · $19 one-time · Instant download · 30-day refund</p>
"""

def swap(old, new, label):
    global s
    if old not in s:
        print(f"  ja estava no formato pedido: {label}")
        return
    s = s.replace(old, new, 1)
    print(f"  trocado: {label}")


if MODE == "soon":
    m = re.search(r'<a class="btn glow" href="(https://[^"]+)" rel="noopener">Get it — \$19</a>', s)
    if m:
        swap(NAV_LIVE.format(u=m.group(1)), NAV_SOON, "botao do topo")
    m = re.search(r'<a class="btn lg glow" href="(https://[^"]+)" rel="noopener">Get TutorLedger</a>', s)
    if m:
        swap(HERO_LIVE.format(u=m.group(1)), HERO_SOON.format(f=FORMSPREE), "CTA do hero")
    m = re.search(r'<a class="btn lg onnavy glow" href="(https://[^"]+)" rel="noopener">Get TutorLedger</a>', s)
    if m:
        swap(CTA_LIVE.format(u=m.group(1)), CTA_SOON.format(f=FORMSPREE), "CTA final")
else:
    swap(NAV_SOON, NAV_LIVE.format(u=URL), "botao do topo")
    swap(HERO_SOON.format(f=FORMSPREE), HERO_LIVE.format(u=URL), "CTA do hero")
    swap(CTA_SOON.format(f=FORMSPREE), CTA_LIVE.format(u=URL), "CTA final")

io.open(PAGE, "w", encoding="utf-8", newline="").write(s)

forms = s.count('class="notify')
links = len(re.findall(r'href="https://www\.etsy\.com/[^"]*"', s))
print(f"\n  formularios de captura: {forms}   links para o Etsy: {links}")
if MODE == "soon" and links:
    print("  ATENCAO: ainda ha link para o Etsy na pagina")
if MODE == "live" and forms:
    print("  ATENCAO: ainda ha formulario de captura na pagina")
