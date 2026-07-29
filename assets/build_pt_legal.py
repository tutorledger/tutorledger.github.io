"""
Builds assets/pt-legal.json — Portuguese for the three legal pages.

A translation, not a re-drafting. The English remains the version that governs:
these pages are a courtesy for Portuguese readers, and the notice that appears
alongside them says the product and the checkout are in English.
"""

import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MAIL = "tutorledger.support@gmail.com"
M = f'<a href="mailto:{MAIL}">{MAIL}</a>'

B = {}

B["terms"] = f'''
<p class="eyebrow">Jurídico</p>
<h1 style="font-size:34px">Termos de Venda</h1>
<p class="tiny faint">Última atualização: <span class="upd">28 de julho de 2026</span></p>

<h2>1. De quem você está comprando</h2>
<p>O TutorLedger é um produto digital publicado e mantido sob o nome comercial
<strong>TutorLedger</strong>, por um desenvolvedor independente. Você pode nos contatar a qualquer
momento em {M}, e respondemos toda mensagem.</p>
<p><strong>Sua compra não é diretamente conosco.</strong> O checkout e o pagamento são conduzidos pela
<strong>Paddle.com Market Ltd</strong>, que atua como <em>merchant of record</em> em todas as vendas.
A Paddle é a vendedora na transação, é responsável por recolher e repassar impostos sobre vendas e
VAT onde quer que você esteja, e os termos e dados societários dela se aplicam. Você os encontra na
página de checkout e no seu recibo.</p>
<p>Se precisar dos nossos dados de registro ou contato para uma nota, um registro fiscal ou uma
reclamação formal, escreva para nós e forneceremos.</p>

<h2>2. O que você está comprando</h2>
<p>O TutorLedger é um arquivo de planilha em formato <code>.xlsx</code>, acompanhado de um guia de
implementação escrito e dos arquivos bônus descritos na página do produto. É entregue como download
imediato após o pagamento.</p>
<p><strong>Não</strong> é uma assinatura, um serviço hospedado nem um aplicativo. Não há conta, não há
componente de servidor e não há obrigação de serviço contínuo. Depois de baixado, o arquivo roda
inteiramente na sua própria cópia do Microsoft Excel ou na sua própria conta do Google.</p>

<h2>3. Licença</h2>
<p>Na compra você recebe uma licença perpétua, não exclusiva e intransferível para usar o TutorLedger
no seu próprio negócio, incluindo quaisquer negócios que você possua ou administre.</p>
<p>Você <strong>pode</strong>: usar o arquivo para um número ilimitado de alunos, tutores e unidades
dentro do seu próprio negócio; modificá-lo como quiser; fazer cópias de segurança; e compartilhá-lo
com a sua própria equipe.</p>
<p>Você <strong>não pode</strong>: revender, sublicenciar, redistribuir ou publicar o arquivo ou
qualquer parte substancial dele; incluí-lo em um pacote, curso ou área de membros; nem oferecê-lo
como download gratuito. Uma compra cobre um negócio.</p>

<h2>4. Preço e impostos</h2>
<p>Os preços são exibidos em dólares americanos, salvo se o seu checkout indicar outra moeda. VAT ou
imposto sobre vendas aplicável é calculado e acrescentado no checkout pela Paddle conforme a sua
localização.</p>
<p>Preços promocionais valem apenas pelo período indicado na página do produto. Podemos alterar o
preço a qualquer momento; o preço que você pagou é o que se aplica à sua compra.</p>

<h2>5. Reembolsos</h2>
<p>Oferecemos reembolso incondicional de 30 dias. A política completa está na página de
<a href="refund-policy.html">Política de Reembolso</a> e faz parte destes termos.</p>

<h2>6. Atualizações</h2>
<p>Correções e melhorias dentro da mesma versão principal são fornecidas gratuitamente aos clientes
existentes, enviadas para o e-mail usado no checkout. Não garantimos nenhuma atualização, recurso ou
cronograma de lançamento específico.</p>

<h2>7. Suporte</h2>
<p>O suporte cobre o produto em si: problemas de download, erros de fórmula e dúvidas sobre como cada
aba deve ser usada. Respondemos todo e-mail, normalmente em até dois dias úteis.</p>
<p>O suporte não inclui desenvolver recursos sob medida, adaptar o arquivo a um modelo de negócio
diferente, migrar os seus dados existentes ou orientar sobre a sua contabilidade.</p>

<h2>8. O que este produto não é</h2>
<p>O TutorLedger é uma ferramenta de controle. <strong>Não é aconselhamento contábil, fiscal,
financeiro ou jurídico</strong>, e não substitui um profissional qualificado. Todo número que ele
produz deriva dos dados que você informa, e é sua responsabilidade verificar esses dados e quaisquer
conclusões que você tire deles.</p>
<p>O Contrato e Política de Pagamento incluso é apenas um modelo operacional. A lei contratual varia
por país e por estado. Peça a um profissional qualificado para revisar antes de usá-lo com
clientes.</p>

<h2>9. Responsabilidade</h2>
<p>O produto é fornecido "no estado em que se encontra". Na máxima extensão permitida por lei, nossa
responsabilidade total decorrente da sua compra ou uso do TutorLedger limita-se ao valor que você
pagou por ele.</p>
<p>Não somos responsáveis por perdas indiretas ou consequenciais, incluindo receita perdida, lucro
perdido, dados perdidos ou decisões tomadas com base em números que o arquivo produziu. Mantenha suas
próprias cópias de segurança.</p>
<p>Nada nestes termos limita qualquer direito que você tenha sob a legislação consumerista
obrigatória do seu país, incluindo seus direitos como consumidor no Reino Unido ou na União
Europeia.</p>

<h2>10. Alterações nestes termos</h2>
<p>Podemos atualizar estes termos. A versão vigente no momento da sua compra é a que se aplica a
você.</p>

<hr class="rule">
<p class="tiny faint">Dúvidas sobre qualquer ponto? Escreva para {M} antes de comprar — preferimos
muito mais responder uma pergunta do que processar um reembolso.</p>'''

B["privacy"] = f'''
<p class="eyebrow">Jurídico</p>
<h1 style="font-size:34px">Privacidade</h1>
<p class="tiny faint">Última atualização: <span class="upd">28 de julho de 2026</span></p>

<div class="guarantee" style="border-color:var(--accent); background:var(--accent-soft); margin:26px 0">
<h3 style="color:var(--accent-ink)">A versão curta</h3>
<p class="muted" style="margin:0">Este site não usa cookies, não roda analytics e não carrega nada de
servidores de terceiros. A calculadora de lucro roda inteiramente no seu navegador — seus números
nunca são transmitidos. Os nomes dos seus alunos nunca chegam até nós, porque o produto é um arquivo
no seu próprio computador.</p></div>

<h2>1. Quem é o responsável</h2>
<p>Este site e produto são operados sob o nome comercial <strong>TutorLedger</strong>, por um
desenvolvedor independente. Para qualquer questão ou solicitação de privacidade, escreva para {M}.
Respondemos toda mensagem e atendemos qualquer solicitação válida gratuitamente.</p>
<p>As compras são conduzidas pela <strong>Paddle.com Market Ltd</strong>, merchant of record de todas
as vendas e controladora dos dados da própria transação de pagamento. O aviso de privacidade dela
cobre o que acontece no checkout. Se precisar dos nossos dados completos para exercer um direito de
proteção de dados, escreva para nós e forneceremos.</p>

<h2>2. Quando você navega neste site</h2>
<p>Não usamos cookies, analytics, gerenciadores de tag, pixels de anúncio, fontes externas nem
scripts de terceiros. Todo o estilo e o código são servidos por este próprio site.</p>
<p>Nosso host, o GitHub Pages, registra logs padrão de requisição incluindo endereço IP, conforme as
próprias práticas de privacidade do GitHub. Não temos acesso a esses logs e não conseguimos
identificar visitantes a partir deles.</p>

<h2>3. Quando você usa a calculadora</h2>
<p>Cada número que você digita é processado no seu navegador e descartado quando você fecha a aba.
Nada é enviado, salvo ou transmitido. Não há conta nem cadastro.</p>

<h2>4. Se você informar seu e-mail</h2>
<p>A calculadora tem um formulário opcional para enviar seus resultados por e-mail. Se você usá-lo, o
endereço digitado é processado pelo <strong>Formspree</strong>, nosso provedor de formulários, e
encaminhado a nós.</p>
<p>Usamos para enviar os resultados que você pediu e, ocasionalmente, uma novidade sobre o produto.
Não vendemos, alugamos nem compartilhamos. Toda mensagem tem link de descadastro, e você pode pedir a
exclusão do seu endereço a qualquer momento por e-mail.</p>
<p>Base legal, onde o GDPR do Reino Unido ou da UE se aplica: o seu consentimento, dado ao enviar o
formulário.</p>

<h2>5. Se você comprar o produto</h2>
<p>O checkout é conduzido inteiramente pela <strong>Paddle</strong>. Os dados do seu cartão são
processados pela Paddle e por seus provedores de pagamento, e nunca são vistos nem transmitidos a
nós.</p>
<p>De uma compra concluída recebemos seu e-mail, o produto adquirido e o país usado para fins
fiscais. Usamos isso para entregar o download, enviar atualizações gratuitas da mesma versão, prestar
suporte e processar reembolsos. Mantemos registros de compra pelo prazo exigido para fins fiscais e
contábeis.</p>

<h2>6. Seus dados dentro do produto</h2>
<p>O TutorLedger é um arquivo de planilha que vive no seu dispositivo ou na sua própria conta do
Google. Seus alunos, responsáveis, faturas e pagamentos permanecem inteiramente sob o seu controle. O
arquivo não contém rastreamento, não faz chamadas de rede de nenhum tipo. <strong>Nunca vemos nada
disso.</strong></p>
<p>Observe que você é o controlador dos dados pessoais dos seus alunos e das famílias deles. Tratá-los
é responsabilidade sua, conforme a legislação de privacidade que se aplica a você.</p>

<h2>7. Seus direitos</h2>
<p>Dependendo de onde você mora, você pode ter o direito de acessar, corrigir, excluir ou receber uma
cópia dos dados pessoais que mantemos sobre você, e de se opor ao tratamento ou restringi-lo. Escreva
para nós e atenderemos qualquer solicitação válida, normalmente em até 30 dias e sempre sem
custo.</p>
<p>Se você está no Reino Unido ou na UE e considera que tratamos seus dados de forma inadequada,
também tem o direito de reclamar à autoridade nacional de proteção de dados.</p>

<h2>8. Terceiros dos quais dependemos</h2>
<ul>
<li><strong>GitHub Pages</strong> — hospedagem do site e logs de servidor</li>
<li><strong>Paddle</strong> — checkout, processamento de pagamento, tratamento fiscal global e entrega do arquivo</li>
<li><strong>Formspree</strong> — formulário opcional de e-mail na página da calculadora</li>
</ul>
<p>Não usamos nenhum outro operador, e não adicionamos nenhum sem atualizar esta página.</p>

<h2>9. Alterações</h2>
<p>Se esta política mudar de forma relevante, atualizaremos a data no topo desta página.</p>'''

B["refund"] = f'''
<p class="eyebrow">Jurídico</p>
<h1 style="font-size:34px">Política de Reembolso</h1>
<p class="tiny faint">Última atualização: <span class="upd">28 de julho de 2026</span></p>

<div class="guarantee" style="margin:26px 0">
<h3>30 dias. Sem perguntas. Sem formulários.</h3>
<p class="muted" style="margin:0">Escreva para {M} em até 30 dias da compra, informando o e-mail que
você usou no checkout. Devolvemos o valor integral. Você não precisa explicar por quê, apagar o
arquivo, nem responder a uma única pergunta de acompanhamento.</p></div>

<h2>Como funciona</h2>
<ol>
<li>Escreva em até 30 dias da compra, a partir do endereço usado no checkout ou citando-o.</li>
<li>Confirmamos e emitimos o reembolso pela Paddle, normalmente em até dois dias úteis.</li>
<li>Seu banco ou emissor devolve o valor, tipicamente em 5 a 10 dias úteis conforme o provedor.</li>
</ol>
<p>Você não vai receber pesquisa de satisfação, oferta de desconto nem tentativa de dissuasão.</p>

<h2>Por que a política é assim tão simples</h2>
<p>O TutorLedger é novo e ainda não tem avaliações. Pedir a alguém que gaste dinheiro num produto
desconhecido de um vendedor desconhecido é um risco real, e a maneira honesta de lidar com isso é
carregar esse risco nós mesmos em vez de pedir que você carregue.</p>
<p>Se o sistema não te mostrar mais do que o próprio preço em receita vazando dentro de um mês, ele
não mereceu o que você pagou.</p>

<h2>Seus direitos legais</h2>
<p>Esta política é oferecida voluntariamente e fica <em>por cima</em> dos seus direitos legais — não
os substitui.</p>
<p>Consumidores no Reino Unido e na União Europeia normalmente têm 14 dias de direito de arrependimento
numa compra à distância. Para conteúdo digital baixável, esse direito pode se encerrar assim que o
download começa e você reconhece isso. Nossa política de 30 dias é deliberadamente mais longa e menos
condicional que o mínimo legal, então na prática você pode se apoiar nela.</p>

<h2>O único limite</h2>
<p>Reservamo-nos o direito de recusar reembolso quando houver evidência clara de abuso — por exemplo,
ciclos repetidos de compra e reembolso do mesmo comprador, ou redistribuição do arquivo em violação
dos <a href="terms.html">termos de licença</a>. Isso não tem nada a ver com não gostar do produto,
mudar de ideia ou concluir que não serviu para o seu negócio. Todos esses casos estão cobertos sem
questionamento.</p>

<h2>Chargebacks</h2>
<p>Por favor, escreva para nós antes de abrir uma disputa com o seu banco. Um chargeback nos custa uma
taxa e leva meses para ser resolvido, enquanto um pedido de reembolso nos toma cerca de dois minutos.
Nunca recusamos nenhum.</p>

<hr class="rule">
<p class="tiny faint">Os pagamentos são processados pela Paddle.com Market Ltd, merchant of record de
todas as vendas. Reembolsos são emitidos no método de pagamento original.</p>'''

out = os.path.join(HERE, "pt-legal.json")
io.open(out, "w", encoding="utf-8", newline="").write(
    json.dumps({"blocks": B}, ensure_ascii=False, indent=1))
print(f"OK  pt-legal.json  {len(B)} blocks, {os.path.getsize(out)/1024:.0f} KB")
for k, v in B.items():
    print(f"   {k:<9} {len(v.split()):>4} words")
