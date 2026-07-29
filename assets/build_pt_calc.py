"""
Builds assets/pt-calc.json — Portuguese for the calculator page.

Only the prose blocks are swapped wholesale. The form and the results card are
translated node by node through the shared dictionary instead, because replacing
their innerHTML would destroy the elements the calculator script holds by id and
every listener bound to them.
"""

import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

BLOCKS = {}

BLOCKS["calc-hero"] = '''<div class="measure">
<p class="eyebrow">Ferramenta grátis · Sem cadastro</p>
<h1>Calculadora de Lucro para Negócios de Tutoria</h1>
<p class="lede" style="margin-top:14px">Faturamento não é lucro. Descubra quanto o seu negócio de
tutoria realmente retém depois do pagamento dos tutores, das faltas e das faturas que nunca são
pagas.</p></div>'''

BLOCKS["calc-cta"] = '''<h3>Esses dois números em vermelho são recuperáveis.</h3>
<p class="muted" style="margin:10px 0">Faltas e faturas não pagas não são custo do negócio — são
problema de controle. A maioria dos donos não consegue citar uma única família que lhe deve sem
passar meia hora dentro do extrato bancário.</p>
<p class="muted" style="margin:0 0 16px"><strong style="color:var(--ink)">TutorLedger</strong> é um
sistema em Google Sheets e Excel que mostra quem deve o quê, separado por 30/60/90 dias, quanto cada
aluno vale depois do pagamento do tutor, e quanto você vai receber no mês que vem.</p>
<a class="btn glow" href="../">Ver o que vem dentro — US$ 29</a>
<form class="emailform" action="https://formspree.io/f/mjgnlzzq" method="POST">
<input type="email" name="email" placeholder="voce@seunegocio.com" required aria-label="Seu endereço de e-mail">
<input type="hidden" name="source" value="profit-calculator">
<button class="btn ghost" type="submit">Enviar meus resultados por e-mail</button>
</form>
<p class="tiny faint" style="margin:9px 0 0">Um e-mail com seus números e uma análise curta. Sem
spam, cancele quando quiser.</p>'''

BLOCKS["calc-article"] = '''
<h2>Como calcular o que o seu negócio de tutoria realmente ganha</h2>
<p>A maioria dos donos de negócio de tutoria sabe o faturamento mensal com precisão de algumas
centenas. Pouquíssimos sabem o lucro. A diferença entre esses dois números é onde quase todo negócio
de serviço em dificuldade está perdendo dinheiro.</p>
<p>Existem quatro coisas entre uma aula agendada e o dinheiro na sua conta, e esta calculadora
percorre todas elas, na ordem.</p>

<h3>1. Aulas que você agenda contra aulas pelas quais você recebe</h3>
<p>Todo negócio de tutoria tem uma taxa de falta e cancelamento tardio. Uma taxa de <strong>5% a 10%
é normal</strong>; acima de 15% costuma significar que a política de cancelamento ou não existe, ou
não é aplicada. O custo é invisível porque nunca aparece numa fatura — você simplesmente fatura menos
do que planejou, e a diferença é atribuída a "um mês fraco".</p>
<p>O número que muda a cabeça das pessoas é o anual. Um negócio com 180 aulas por mês a US$ 60 e 8%
de faltas perde cerca de US$ 860 por mês — <strong>mais de US$ 10.000 por ano</strong> — em aulas que
estavam na agenda e nunca foram cobradas.</p>

<h3>2. Se você continua pagando o tutor pelas faltas</h3>
<p>Muitos donos pagam o tutor pelo horário reservado independentemente da presença. É justo, e mantém
bons tutores. Mas se a família não é cobrada e o tutor é pago, aquela aula tem <strong>margem
negativa de 100%</strong>. Marque essa caixa na calculadora e veja o que acontece com o lucro por
aluno. Essa única decisão de política costuma valer mais que um aumento de preço.</p>

<h3>3. Faturas emitidas que nunca são recebidas</h3>
<p>Esta é a que os donos mais subestimam. Receita faturada <em>parece</em> receita ganha, então é
contabilizada mentalmente e depois baixada silenciosamente meses adiante. Num negócio com 45 alunos,
6% de inadimplência é aproximadamente <strong>US$ 600 por mês parados na conta bancária de outra
pessoa</strong>.</p>
<p>Faturas não pagas quase nunca falham porque a família não pode pagar. Falham porque ninguém deu
seguimento no oitavo dia, e no sexagésimo a conversa já ficou constrangedora. Cobrança é problema de
agenda, não de dinheiro.</p>

<h3>4. O que sobra depois do tutor e dos custos fixos</h3>
<p>Um negócio de tutoria saudável retém entre <strong>15% e 30% de margem líquida</strong> depois do
pagamento dos tutores, dos custos fixos e do próprio salário do dono. Abaixo de 10%, você tem um
emprego com trabalho administrativo extra. Acima de 35%, normalmente ou você está pagando mal os
tutores ou está dando quase todas as aulas — e nenhum dos dois escala.</p>

<h2>Quanto eu deveria cobrar por tutoria?</h2>
<p>Calcule de trás para frente, em vez de copiar o concorrente da esquina. Defina o percentual do
tutor necessário para atrair gente boa (normalmente 50% a 60% do valor da aula), some seu custo fixo
por aula e então acrescente a margem que você quer. Teste o valor aqui antes de anunciar. Um aumento
de US$ 5 em 180 aulas por mês são <strong>US$ 10.800 por ano</strong>, e raramente custa um único
aluno.</p>

<h3>O que conta como custo fixo?</h3>
<ul>
<li>Aluguel ou locação de sala, contas de consumo, seguro</li>
<li>Software de agenda, contabilidade e pagamentos</li>
<li>Anúncios, site, taxas de listagem em diretórios</li>
<li>Material, avaliações, licenças</li>
<li><strong>Seu próprio salário</strong> — se você não se paga, sua margem é ficção</li>
</ul>

<h2>Perguntas frequentes</h2>
<h3>A calculadora é grátis?</h3>
<p>Sim, completamente, e sem cadastro. Tudo roda no seu navegador e nenhum dos seus números é enviado
ou armazenado em lugar nenhum.</p>

<h3>E se eu cobro mensalidade em vez de por aula?</h3>
<p>Divida a mensalidade pelo número de aulas incluídas para obter o valor efetivo por aula e informe
esse número. A matemática dá exatamente no mesmo.</p>

<h3>Qual é uma taxa de falta normal em tutoria?</h3>
<p>Entre 5% e 10% para a maioria dos negócios com política de cancelamento por escrito. Negócios sem
política aplicada costumam operar entre 12% e 20%.</p>

<h3>Como eu de fato reduzo a inadimplência?</h3>
<p>Três coisas, nesta ordem: uma política de pagamento assinada na matrícula, um vencimento que não
seja "quando der", e um acompanhamento enviado em datas fixas em vez de quando você lembra. A parte
difícil é a terceira, e é o motivo pelo qual a maioria dos donos acaba controlando isso num sistema
em vez de na cabeça.</p>'''

TEXT = {
    "Your numbers": "Seus números",
    "Estimates are fine. Everything runs in your browser — nothing is stored or sent anywhere.":
        "Estimativas bastam. Tudo roda no seu navegador — nada é armazenado nem enviado.",
    "Currency": "Moeda",
    "Active students": "Alunos ativos",
    "Sessions per student / month": "Aulas por aluno / mês",
    "What you charge per session": "Quanto você cobra por aula",
    "Your price to the family, not what you pay the tutor.":
        "Seu preço para a família, não o que você paga ao tutor.",
    "You pay tutors": "Você paga os tutores",
    "% of the session fee": "% do valor da aula",
    "A flat amount per session": "Valor fixo por aula",
    "Tutor share (%)": "Percentual do tutor (%)",
    "I still pay my tutors when a student no-shows":
        "Eu pago o tutor mesmo quando o aluno falta",
    "No-show / late cancel rate (%)": "Taxa de falta / cancelamento tardio (%)",
    "Sessions you don't get paid for.": "Aulas pelas quais você não recebe.",
    "Invoices unpaid past due (%)": "Faturas vencidas e não pagas (%)",
    "Money billed but not collected.": "Dinheiro faturado mas não recebido.",
    "Fixed monthly costs": "Custos fixos mensais",
    "Rent, software, insurance, marketing — and your own salary if you take one.":
        "Aluguel, software, seguro, marketing — e o seu próprio salário, se você tira um.",
    "What you actually keep": "Quanto você realmente fica",
    "Per month, based on the numbers on the left.": "Por mês, com base nos números ao lado.",
    "Sessions scheduled": "Aulas agendadas",
    "Revenue you could bill": "Receita que você poderia faturar",
    "Lost to no-shows": "Perdido com faltas",
    "Actually invoiced": "Efetivamente faturado",
    "Stuck in unpaid invoices": "Preso em faturas não pagas",
    "Cash collected": "Dinheiro recebido",
    "Tutor pay": "Pagamento de tutores",
    "Fixed costs": "Custos fixos",
    "Net profit / month": "Lucro líquido / mês",
    "Profit per student": "Lucro por aluno",
    "Net margin": "Margem líquida",
    "you@yourbusiness.com": "voce@seunegocio.com",
    "Your email address": "Seu endereço de e-mail",
}

out = os.path.join(HERE, "pt-calc.json")
io.open(out, "w", encoding="utf-8", newline="").write(
    json.dumps({"blocks": BLOCKS, "text": TEXT}, ensure_ascii=False, indent=1))
print(f"OK  pt-calc.json  {len(BLOCKS)} blocks + {len(TEXT)} strings, "
      f"{os.path.getsize(out)/1024:.0f} KB")
