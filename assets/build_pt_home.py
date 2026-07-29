"""
Builds assets/pt-home.json — the Portuguese innerHTML for each marked section of
the landing page.

Written as Python rather than hand-edited JSON: embedding HTML inside JSON by
hand is an escaping minefield, and this way the structure stays readable and
diffable. Rerun after any change to the English sections.
"""

import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PAY = "https://buy.paddle.com/REPLACE-ME"

TICK = ('<svg width="15" height="15" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">'
        '<path d="M8 14.2 4.3 10.5l1.4-1.4L8 11.4l6.3-6.3 1.4 1.4z"/></svg>')


def quote(t):
    return f'<blockquote class="card reveal" style="margin:0"><p style="margin:0; font-size:17px">{t}</p></blockquote>'


def card(h, p):
    return f'<div class="card reveal"><h3>{h}</h3><p class="muted" style="margin:10px 0 0">{p}</p></div>'


def faq(q, *paras):
    body = "".join(f"<p>{x}</p>" for x in paras)
    return (f'<details class="faq reveal"><summary>{q}</summary>'
            f'<div class="a">{body}</div></details>')


BLOCKS = {}

# ---------------------------------------------------------------- hero
BLOCKS["hero"] = f'''<div class="wrap"><div class="measure">
<p class="eyebrow">Para quem administra um negócio de tutoria</p>
<h1>Saiba exatamente quem está te devendo.</h1>
<p class="lede" style="margin-top:16px">Abra na segunda-feira e ele te entrega uma lista:
<strong>quais famílias contatar, em que ordem, e a mensagem exata para enviar.</strong> Por baixo,
controla mensalidades, classifica cada fatura vencida por 30/60/90 dias e mostra quanto cada aluno
vale depois do pagamento do tutor. Google&nbsp;Sheets e Excel. Configura uma vez, quinze minutos por
semana depois disso.</p>
<div class="price" style="margin:30px 0 18px"><span class="now num">US$ 29</span>
<span class="was num">US$ 39</span><span class="pill">Preço de lançamento</span></div>
<p style="margin-bottom:22px"><a class="btn lg glow" href="{PAY}" rel="noopener">Comprar o TutorLedger</a></p>
<div class="trustbar">
<span>{TICK} Reembolso em 30 dias, sem perguntas</span>
<span>{TICK} Pagamento único, não é assinatura</span>
<span>{TICK} Funciona no Google Sheets <em>e</em> no Excel</span>
<span>{TICK} Seu arquivo, seus dados — nada é enviado</span>
</div></div></div>'''

# ---------------------------------------------------------------- problem
BLOCKS["problem"] = f'''<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">O problema</p>
<h2>Seu faturamento está bem. Sua cobrança não.</h2>
<p class="lede" style="margin-top:14px">Quase ninguém que administra um negócio de tutoria tem falta
de alunos. Tem falta de faturas efetivamente pagas — e só descobre meses depois.</p></div>
<div class="grid g3">
{quote("“Não faço ideia de quem está me devendo agora.”")}
{quote("“Descobri que uma família não pagava havia três meses.”")}
{quote("“Passo os domingos à noite calculando quanto pagar aos tutores.”")}
{quote("“Estou cheio de trabalho, mas não sinto que estou ganhando dinheiro.”")}
{quote("“Sei que perco dinheiro com faltas. Só não sei quanto.”")}
<div class="card reveal" style="margin:0; background:var(--accent-soft); border-color:transparent">
<p style="margin:0; font-size:15.5px; color:var(--accent-ink); font-weight:600">
Não sabe quanto isso está custando? Passe seus números pela
<a href="tutoring-profit-calculator/" style="color:inherit">calculadora de lucro gratuita</a> primeiro.
Leva cerca de um minuto e você não precisa comprar nada.</p></div>
</div></div>'''

# ---------------------------------------------------------------- shows
BLOCKS["shows"] = f'''<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">O que você tira disso</p>
<h2>Quatro respostas que você hoje não tem.</h2></div>
<div class="grid g2">
{card("Quem te deve, separado por 30/60/90 dias",
      "Cada família, cada saldo em aberto, ordenado por quanto está atrasado. No momento em que uma "
      "fatura ultrapassa sua carência, ela muda de faixa e muda de cor. Sem garimpar extrato bancário "
      "para descobrir quem cobrar.")}
{card("Quanto cada aluno realmente vale",
      "Receita por aluno menos o que você paga ao tutor que dá aula para ele. Alguns alunos sustentam "
      "o negócio. Outros custam dinheiro. A maioria dos donos nunca viu essa lista ordenada.")}
{card("Quanto as faltas custam em dinheiro de verdade",
      "Cada falta e cancelamento tardio, precificado conforme a sua própria política — incluindo "
      "aqueles em que você pagou o tutor mesmo assim. É o número que faz as pessoas reescreverem a "
      "política de cancelamento.")}
{card("Quanto você vai receber no mês que vem",
      "Uma projeção de três meses montada a partir dos alunos ativos, dos planos e do ciclo de "
      "cobrança — para que um mês fraco seja algo que você vê chegando, e não algo que você atravessa.")}
</div></div>'''

# ---------------------------------------------------------------- inside
rows = [
    ("Comece Aqui", "Ordem de preenchimento, legenda de cores e a rotina semanal de quinze minutos.", False),
    ("Lista de Ação 🔒", "A aba que você abre na segunda. Cada família que te deve, ordenada por quanto a dívida está custando, com o que dizer e qual dos e-mails bônus enviar.", True),
    ("Configuração", "Seus planos e valores, seus tutores e o pagamento deles, seus prazos e sua política de faltas. Todo o resto lê daqui.", False),
    ("Alunos", "Cadastro com responsável, plano, desconto, tutor e status — agrupado por família, para que irmãos sejam cobrados juntos.", False),
    ("Aulas", "Cada aula registrada com status: realizada, falta, cancelamento tardio, cancelamento com aviso ou reposição. Cobrança e custo do tutor se aplicam sozinhos, a partir da sua política.", False),
    ("Faturas", "O que você cobrou, de qual família, referente a qual período e com que vencimento.", False),
    ("Pagamentos", "O que entrou, baixado na fatura certa.", False),
    ("Vencimentos 🔒", "O motor de cobrança. Saldo por família, dias de atraso e faixas de 30/60/90 com visão de semáforo.", True),
    ("Pagamento de Tutores 🔒", "Por tutor, por período: aulas dadas, horas, quanto você deve e a margem que ele gerou.", False),
    ("Painel 🔒", "Taxa de cobrança, valores em aberto por faixa, alunos ativos e perdidos, margem após pagamento de tutores, custo das faltas, melhores e piores alunos, projeção de três meses — e três gráficos.", False),
    ("Diagnóstico 🔒", "Dezessete verificações que pegam os erros de preenchimento que silenciosamente produzem números confiantes e errados — uma aula apontando para um aluno que não existe, um pagamento lançado numa família fora do cadastro, uma fatura sem vencimento.", True),
]
tbody = "".join(
    f'<tr{" class=\"hl\"" if hl else ""}><td><strong>{n}</strong></td><td>{d}</td></tr>'
    for n, d, hl in rows)
BLOCKS["inside"] = f'''<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">O que vem dentro</p>
<h2>Onze abas conectadas, não um monte de modelos.</h2>
<p class="lede" style="margin-top:14px">Você digita cada informação uma única vez. Tudo o que vem
depois se atualiza sozinho. As abas de cálculo são protegidas para que um clique errado não quebre
uma fórmula.</p></div>
<div class="tablewrap reveal"><table><thead><tr><th style="width:190px">Aba</th>
<th>O que faz</th></tr></thead><tbody>{tbody}</tbody></table></div>
<p class="tiny faint" style="margin-top:12px">🔒 Aba de cálculo protegida — somente leitura, de propósito.</p>
</div>'''

# ---------------------------------------------------------------- shots
BLOCKS["shots"] = '''<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Por dentro</p><h2>Veja antes de comprar.</h2></div>
<figure class="shot reveal" style="margin:0 0 18px"><div class="bar"><i></i><i></i><i></i></div>
<div class="body" style="overflow-x:auto"><img src="assets/shot-actionlist.png" width="2152" height="609" loading="lazy"
alt="A aba Lista de Ação classificando seis famílias por quanto devem e há quanto tempo."></div>
<figcaption>A Lista de Ação. Não é um relatório — é uma lista de tarefas, na ordem que custa menos ignorar por último.</figcaption></figure>
<figure class="shot reveal" style="margin:0 0 18px"><div class="bar"><i></i><i></i><i></i></div>
<div class="body" style="overflow-x:auto"><img src="assets/shot-dashboard.png" width="2152" height="1126" loading="lazy"
alt="O painel do TutorLedger com faturamento, recebimento, taxa de cobrança e margem."></div>
<figcaption>O Painel. Mude uma célula — o mês — e todos os números acompanham.</figcaption></figure>
<figure class="shot reveal" style="margin:0 0 18px"><div class="bar"><i></i><i></i><i></i></div>
<div class="body" style="overflow-x:auto"><img src="assets/shot-aging.png" width="2152" height="542" loading="lazy"
alt="A aba de vencimentos com saldo por família dividido em faixas de atraso."></div>
<figcaption>A aba de Vencimentos. Verde está seguro, âmbar pede e-mail, vermelho pede telefonema.</figcaption></figure>
<div class="grid g2">
<figure class="shot fit reveal" style="margin:0"><div class="body" style="padding:14px; background:var(--card)">
<img src="assets/chart-collections.png" width="908" height="409" loading="lazy"
alt="Gráfico comparando faturado e recebido nos últimos seis meses."></div>
<figcaption>Seis meses de faturado contra efetivamente recebido. A diferença é o problema.</figcaption></figure>
<figure class="shot fit reveal" style="margin:0"><div class="body" style="padding:14px; background:var(--card)">
<img src="assets/chart-aging.png" width="908" height="409" loading="lazy"
alt="Gráfico de valores em aberto por faixa de atraso."></div>
<figcaption>Valores em aberto por idade. Tudo à direita do verde é dinheiro que você já ganhou.</figcaption></figure>
</div></div>'''

# ---------------------------------------------------------------- compare
crows = [
    ("Registro de aulas e presença", "✓", "✓", "✓"),
    ("Planos de aula e progresso do aluno", "✓", "—", "✓"),
    ("Extrato e saldo por família", "—", "✓", "✓"),
    ("Faixas de 30/60/90 dias", "—", "✓", "✓"),
    ("Margem por aluno após pagamento do tutor", "—", "✓", "parcial"),
    ("Custo das faltas em dinheiro", "—", "✓", "—"),
    ("Projeção de recebimento de três meses", "—", "✓", "parcial"),
    ("<strong>Diz quem cobrar, em ordem</strong>", "—", "✓", "—"),
    ("<strong>Entrega a mensagem para enviar</strong>", "—", "✓", "—"),
    ("<strong>Verifica erros nos seus dados</strong>", "—", "✓", "—"),
    ("<strong>Custo em três anos</strong>", "<strong>US$ 3</strong>", "<strong>US$ 29</strong>", "<strong>US$ 1.800–3.600</strong>"),
    ("Migração e dependência", "nenhuma", "nenhuma — é seu arquivo", "alta"),
]


def cell(v, hl=False):
    cls = "c hl" if hl else "c"
    if v == "✓":
        return f'<td class="{cls} yes">✓</td>'
    if v == "—":
        return f'<td class="{cls} no">—</td>'
    return f'<td class="{cls}">{v}</td>'


ctbody = "".join(f"<tr><td>{n}</td>{cell(a)}{cell(b, True)}{cell(c)}</tr>"
                 for n, a, b, c in crows)
BLOCKS["compare"] = f'''<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Onde ele se encaixa</p>
<h2>Entre uma planilha de US$ 3 e uma plataforma de US$ 79/mês.</h2>
<p class="lede" style="margin-top:14px">Modelos baratos registram aulas. Plataformas de estúdio fazem
tudo, cobram todo mês e levam um fim de semana para migrar. O TutorLedger faz uma coisa só: o seu
dinheiro.</p></div>
<div class="tablewrap reveal"><table><thead><tr><th>&nbsp;</th>
<th class="c">Modelo de US$ 3</th><th class="c hl">TutorLedger</th>
<th class="c">Plataforma de estúdio</th></tr></thead><tbody>{ctbody}</tbody></table></div></div>'''

# ---------------------------------------------------------------- bonuses
BLOCKS["bonuses"] = '''<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Incluso sem custo adicional</p>
<h2>Duas coisas que impedem o problema de voltar.</h2></div>
<div class="grid g2">
<div class="card reveal"><span class="pill gain">Bônus 1</span>
<h3 style="margin:14px 0 8px">Contrato e Política de Pagamento</h3>
<p class="muted" style="margin:0">Um contrato de matrícula editável cobrindo vencimentos, multa por
atraso, faltas e prazo de cancelamento — em inglês simples. A maior parte das faturas não pagas nasce
de termos que nunca foram escritos.</p>
<p class="tiny faint" style="margin:12px 0 0">Modelo operacional, não aconselhamento jurídico. Peça a
um profissional local para revisar antes de usar com clientes.</p></div>
<div class="card reveal"><span class="pill gain">Bônus 2</span>
<h3 style="margin:14px 0 8px">Roteiros de E-mail de Cobrança</h3>
<p class="muted" style="margin:0">Cinco e-mails prontos para enviar, do lembrete gentil no primeiro
dia ao aviso firme de suspensão das aulas no sexagésimo — escritos para você cobrar sem se sentir um
agente de cobrança, que é o motivo pelo qual a maioria dos donos simplesmente não cobra.</p></div>
</div></div>'''

# ---------------------------------------------------------------- fit
BLOCKS["fit"] = '''<div class="wrap"><div class="grid g2">
<div class="card reveal"><h3>É para você se…</h3>
<ul class="ticks" style="margin-top:16px">
<li>Você administra um negócio de tutoria ou preparatório com aproximadamente 10 a 200 alunos</li>
<li>Você tem ao menos um tutor além de você, ou pretende ter</li>
<li>Você cobra mensalidade, por aula, ou uma mistura das duas</li>
<li>Você se vira digitando numa planilha — não precisa saber fórmula</li>
<li>Você prefere ser dono de um arquivo a alugar uma plataforma</li></ul></div>
<div class="card reveal"><h3><em>Não</em> é para você se…</h3>
<ul class="crosses" style="margin-top:16px">
<li>Você é tutor autônomo com um punhado de alunos — um caderno resolve, sinceramente</li>
<li>Você quer planejamento de aula, currículo ou acompanhamento pedagógico</li>
<li>Você quer integração bancária automática, cobrança no cartão ou portal para os pais</li>
<li>Você quer um software que envie e-mail pelas famílias por você — este mostra a quem escrever, o envio é seu</li></ul>
<p class="tiny faint" style="margin:16px 0 0">Preferimos perder a venda a processar um reembolso. Se
você se encaixa nesta coluna, por favor não compre.</p></div>
</div></div>'''

# ---------------------------------------------------------------- guarantee
BLOCKS["guarantee"] = '''<div class="wrap"><div class="guarantee reveal">
<h3>Use por 30 dias. Se não mostrar dinheiro que você estava perdendo, receba cada centavo de volta.</h3>
<p class="muted" style="margin:0">Envie um e-mail em até 30 dias da compra e devolvemos o valor
integral. Você não precisa se explicar, devolver nada, nem ouvir uma tentativa de retenção. Se uma
planilha não conseguir te mostrar mais de US$ 29 de receita vazando em um mês, ela não merece o preço
que custa.</p></div></div>'''

# ---------------------------------------------------------------- faq
BLOCKS["faq"] = f'''<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Dúvidas</p><h2>Antes de comprar.</h2></div>
<div class="measure">
{faq("Preciso ter Excel, ou o Google Sheets funciona?",
     "Os dois, e os dois foram testados. Você recebe um arquivo <code>.xlsx</code> que abre direto no "
     "Excel e importa no Google Sheets com todas as fórmulas, a formatação condicional e os três "
     "gráficos intactos.",
     "Toda fórmula foi deliberadamente restrita ao conjunto que as duas aplicações suportam — nada "
     "mais novo que o Excel 2007, sem arrays dinâmicos, sem funções exclusivas do Sheets. Essa "
     "contenção é exatamente o motivo de ele sobreviver à importação em vez de chegar cheio de "
     "<code>#NOME?</code>.")}
{faq("Isso é uma assinatura?",
     "Não. Você paga US$ 29 uma vez e o arquivo é seu para sempre. Não há nada para cancelar nem "
     "conta para manter. Atualizações dentro da mesma versão são gratuitas — você recebe o arquivo "
     "novo por e-mail.")}
{faq("Vai quebrar se eu inserir uma linha ou mudar alguma coisa?",
     "As três abas de cálculo são protegidas, então você não consegue sobrescrever uma fórmula sem "
     "querer. As abas em que você digita são linhas comuns — insira, ordene e filtre à vontade. As "
     "fórmulas já vêm preenchidas para baixo em vez de geradas dinamicamente, justamente para que "
     "editar não as perturbe.")}
{faq("Eu cobro mensalidade, não por aula. Funciona mesmo assim?",
     "Sim. Cada aluno é configurado como mensal, por aula ou por pacote, e o sistema lida com uma "
     "mistura dos três no mesmo cadastro. Alunos mensais são cobrados pela programação recorrente; "
     "alunos por aula são cobrados a partir das aulas registradas.")}
{faq("Posso usar para escola de música, dança ou idiomas?",
     "Em boa parte, sim — o lado financeiro é idêntico: mensalidade recorrente, famílias com irmãos, "
     "faltas, pagamento de instrutor. O que ele não faz é qualquer coisa específica dessas áreas, "
     "como gestão de recital ou de exame. Foi feito para tutoria e é honesto quanto a isso.")}
{faq("Meus dados vão para algum lugar?",
     "Não. É um arquivo de planilha no seu computador ou na sua própria conta do Google. Não há "
     "servidor, login, sincronização nem qualquer rastreamento dentro do arquivo. Nunca vemos um "
     "único nome de aluno.")}
{faq("Quanto tempo leva a configuração?",
     "Cerca de 20 minutos para seus ajustes, tutores e valores, mais aproximadamente um minuto por "
     "aluno para lançar o cadastro. O guia incluso conduz na ordem que evita retrabalho. Depois "
     "disso, reserve uns quinze minutos por semana.")}
{faq("Como recebo depois de pagar?",
     "O checkout é feito pela Paddle, que é a vendedora legal da transação e cuida do pagamento mais "
     "qualquer imposto que se aplique onde você está. Seu link de download aparece na hora e também "
     "é enviado por e-mail.")}
{faq("Existem avaliações?",
     "Ainda não — o TutorLedger é novo, e não vamos publicar depoimentos que não temos. É exatamente "
     "por isso que a política de reembolso é incondicional e que a calculadora gratuita permite "
     "testar o raciocínio antes de gastar qualquer coisa.")}
</div></div>'''

# ---------------------------------------------------------------- final cta
BLOCKS["finalcta"] = f'''<div class="wrap measure">
<h2>Encontre o dinheiro que você já ganhou.</h2>
<p class="lede" style="color:#c3cddb; margin-top:14px">Um arquivo. Onze abas conectadas. Dois bônus.
Trinta dias para decidir se valeu os US$ 29.</p>
<div class="price" style="margin:26px 0 20px"><span class="now num" style="color:#fff">US$ 29</span>
<span class="was num" style="color:#8496af">US$ 39</span></div>
<div class="btnrow">
<a class="btn lg onnavy glow" href="{PAY}" rel="noopener">Comprar o TutorLedger</a>
<a class="btn lg ghost" href="tutoring-profit-calculator/" style="color:#c3cddb; border-color:#2c3d5c">Testar a calculadora grátis</a>
</div>
<p class="tiny" style="color:#8496af; margin:0">Checkout seguro pela Paddle · Reembolso em 30 dias · Pagamento único</p>
</div>'''

out = os.path.join(HERE, "pt-home.json")
io.open(out, "w", encoding="utf-8", newline="").write(
    json.dumps({"blocks": BLOCKS}, ensure_ascii=False, indent=1))
size = os.path.getsize(out) / 1024
print(f"OK  pt-home.json  {len(BLOCKS)} blocks, {size:.0f} KB")
for k, v in BLOCKS.items():
    print(f"   {k:<12} {len(v):>6} chars")
