"""
Static blog generator for TutorLedger.

Posts are defined below as plain dicts. Running this writes each article, the
index, sitemap.xml and robots.txt. Adding a post means adding a dict and running
it again — no build tooling, no dependencies, nothing to keep up to date.

The table of contents is derived from the <h2> ids in the body, so it can never
drift out of sync with the article.
"""

import os
import re
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
BASE = "https://tutorledger.github.io"
CALC = BASE + "/tutoring-profit-calculator/"

LOGO = ('<svg viewBox="0 0 32 32" width="27" height="27" aria-hidden="true">'
        '<rect width="32" height="32" rx="7.5" fill="#16233D"/>'
        '<rect x="8" y="8.5" width="9" height="3" rx="1.5" fill="#7CA0F0"/>'
        '<rect x="8" y="14.5" width="16" height="3" rx="1.5" fill="#FFFFFF"/>'
        '<rect x="8" y="20.5" width="12.5" height="3" rx="1.5" fill="#7CA0F0" opacity=".55"/></svg>')


def cta(title, text, label="Open the free calculator", href=None):
    return f'''<div class="inline-cta rise">
  <h3>{title}</h3>
  <p>{text}</p>
  <a class="btn glow" href="{href or CALC}">{label}</a>
</div>'''


POSTS = [
{
 "slug": "track-tutoring-payments-google-sheets",
 "date": "2026-07-20",
 "minutes": 8,
 "title": "How to Track Tutoring Payments in Google Sheets (Without It Falling Apart)",
 "seo_title": "How to Track Tutoring Payments in Google Sheets",
 "description": "A practical structure for tracking tuition, invoices and payments in Google Sheets — including the one modelling mistake that makes most tutoring spreadsheets useless after three months.",
 "standfirst": "Most tutoring spreadsheets work for a term and then quietly stop being trusted. The reason is almost always the same, and it is fixable in an afternoon.",
 "body": f'''
<p class="opening">Nearly every tutoring business starts with a spreadsheet, and nearly every one of
those spreadsheets is abandoned within a year. Not because spreadsheets are the wrong tool — they
are a perfectly good tool for a business with fewer than two hundred students — but because of one
structural decision made in the first ten minutes that cannot be undone later without retyping
everything.</p>

<p>This is how to make that decision correctly, and what to build around it.</p>

<h2 id="one-sheet">The mistake: one sheet, one row per payment</h2>

<p>The instinctive first move is a single sheet where each row is a payment: date, student name,
amount. It works beautifully for about six weeks.</p>

<p>Then a parent pays for two children in one transfer. Then someone pays half now and half next
week. Then a student pauses for a month and you need to know whether they still owe for March. Each
of these breaks a flat list, and the usual fix is a new column, then another, until the sheet has
nineteen columns and nobody trusts the total.</p>

<blockquote class="pull">A payment list tells you what came in. It cannot tell you what is
still owed, and that is the number you actually need.</blockquote>

<h2 id="three-ledgers">The structure: three lists that reconcile</h2>

<p>Accounting solved this a long time ago, and the solution is smaller than it sounds. You need
three separate lists, not one.</p>

<div class="tablewrap"><table>
<thead><tr><th>List</th><th>One row per</th><th>Answers</th></tr></thead>
<tbody>
<tr><td><strong>Invoices</strong></td><td>bill you issued</td><td>what was charged, to whom, and when it was due</td></tr>
<tr><td><strong>Payments</strong></td><td>amount received</td><td>what actually arrived</td></tr>
<tr><td><strong>Sessions</strong></td><td>lesson taught</td><td>what was delivered, and what it cost you</td></tr>
</tbody></table></div>

<p>Invoices minus payments is the balance. That single subtraction is the thing a flat payment list
can never give you, and it is why this structure survives contact with reality.</p>

<h2 id="family-id">The column that decides everything: Family ID</h2>

<p>Here is the ten-minute decision. <strong>Money arrives by household, not by student.</strong> One
parent, one bank transfer, two children. If your sheet is keyed on student name, you will spend the
rest of its life splitting transfers by hand and never quite reconciling.</p>

<p>Give every household a short code — <code>FAM-01</code>, <code>FAM-02</code> — and put it on every
student, every invoice and every payment. Siblings share it. Then:</p>

<ul>
<li><strong>Billing and chasing</strong> aggregate by family, because that is how the money moves</li>
<li><strong>Lessons and profitability</strong> aggregate by student, because that is how the work moves</li>
</ul>

<p>Retrofitting this later means touching every historic row. Doing it on day one costs nothing.</p>

<div class="callout">
<span class="label">Practical note</span>
<p>Do not use the parent's surname as the key. Blended families, different surnames, and two
unrelated Smiths will all break it within a year. Use a meaningless code and put the name in its own
column.</p>
</div>

<h2 id="due-dates">Give every invoice a due date, or nothing is ever late</h2>

<p>This sounds obvious and is skipped constantly. If an invoice has no due date, no formula can tell
you it is overdue, so it never appears on any list of things to chase. It simply sits there being
forty days old and feeling fine.</p>

<p>Pick a rule and apply it without exception: issued on the 1st, due on the 5th, with a grace period
of seven days. The grace period matters — it is what separates "recently issued" from "actually
late", and it stops you chasing someone on day two.</p>

<h2 id="aging">Age the balances into buckets</h2>

<p>Once every invoice has a due date and a balance, you can sort what is owed by how old it is. In
accounting this is called an aged debtors report, and it is standard practice in businesses of every
size except, oddly, small service businesses.</p>

<div class="tablewrap"><table>
<thead><tr><th>Bucket</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>Current</td><td>Issued, not yet past the grace period</td></tr>
<tr><td>1–30 days</td><td>Late. A reminder is appropriate</td></tr>
<tr><td>31–60 days</td><td>Needs a firm message with a date in it</td></tr>
<tr><td>61–90 days</td><td>Formal notice territory</td></tr>
<tr><td>90+ days</td><td>Phone call. Collection rates fall sharply past this point</td></tr>
</tbody></table></div>

<p>The formula is a nested <code>IF</code> on days overdue. It is not sophisticated. What is
sophisticated is having it at all — the reason most owners chase the largest debt rather than the
oldest is simply that nobody ever showed them the age.</p>

{cta("Before you build anything, get the number", "The free profit calculator shows what no-shows and unpaid invoices are costing you a year, using your own figures. No sign-up, nothing stored, about a minute.")}

<h2 id="formulas">Formulas that survive other people using them</h2>

<p>If anyone other than you will ever open this file — and eventually someone will — a few rules
save a lot of grief.</p>

<ul>
<li><strong>Fill formulas down in advance</strong>, to row 500 or so, wrapped in
<code>IFERROR(…,"")</code> so empty rows stay blank. Then typing in the next row just works.</li>
<li><strong>Protect the calculated columns.</strong> One stray paste over a formula and the sheet
silently starts lying.</li>
<li><strong>Avoid dynamic array formulas</strong> if the file will ever move between Excel and Google
Sheets. Plain <code>SUMIFS</code> and <code>INDEX/MATCH</code> behave identically in both.</li>
<li><strong>Never put a decimal inside a criteria string.</strong> <code>"&gt;0.005"</code> is parsed
using the machine's decimal separator, so it silently matches nothing on any computer configured for
a comma. Round the value and compare against <code>"&gt;0"</code> instead.</li>
</ul>

<p>That last one is not theoretical. It produces confident, wrong totals with no error message, and
it only shows up on someone else's computer.</p>

<h2 id="weekly">The fifteen minutes that make it worth having</h2>

<p>A tracking system nobody opens is worse than no system, because it creates the feeling of being on
top of things without the substance. Tie it to a fixed slot:</p>

<ol>
<li><strong>Log last week's sessions.</strong> Mark no-shows honestly — the whole point is to see what
they cost.</li>
<li><strong>Read the aged list and send two emails.</strong> Oldest first, not largest.</li>
<li><strong>Once a month</strong>, raise the invoices and look at collection rate: money received
divided by money invoiced. Below 90% means chasing has stopped being a habit.</li>
</ol>

<p>Fifteen minutes, once a week. The businesses that recover their unpaid tuition are not the ones
with better spreadsheets. They are the ones that open theirs.</p>
''',
 "related": ["client-wont-pay-tutoring", "tutoring-business-profit-margin"],
},
{
 "slug": "client-wont-pay-tutoring",
 "date": "2026-07-22",
 "minutes": 7,
 "title": "What to Do When a Tutoring Client Won't Pay",
 "seo_title": "What to Do When a Tutoring Client Won't Pay",
 "description": "A calm, five-stage escalation for unpaid tuition — what to send at 7, 30, 60 and 90 days, why chasing by age beats chasing by amount, and when to pause lessons.",
 "standfirst": "Unpaid tuition is rarely a money problem. It is almost always a follow-up problem, and it compounds quietly while you decide how to word the message.",
 "body": f'''
<p class="opening">Almost nobody stops chasing an unpaid invoice because they forgot about it. They
stop because writing the message feels awkward, so it gets postponed — and every week it is
postponed, it becomes more awkward to send. Eventually the debt is four months old and the
conversation feels impossible.</p>

<p>The way out is to remove the decision. Fixed stages, fixed wording, sent on a schedule rather than
when you happen to feel brave.</p>

<h2 id="age-not-size">Chase by age, not by amount</h2>

<p>The instinct is to start with whoever owes the most. It is the wrong order.</p>

<p>Money that is five months old is far less likely ever to arrive than money that is three weeks old.
Recovery rates fall sharply after ninety days, so a smaller debt that is much older is usually worth
more of your attention than a larger recent one.</p>

<blockquote class="pull">A family owing $400 for five months should be contacted before one
owing $900 for three weeks.</blockquote>

<p>A workable priority is simply the balance multiplied by an age weight — 1 for under thirty days, 2
under sixty, 3 under ninety, 4 beyond. Sort descending and work down. It takes ten seconds to build
and it changes what you do on a Monday morning.</p>

<h2 id="stages">The five stages</h2>

<div class="tablewrap"><table>
<thead><tr><th>Days late</th><th>Send</th><th>Tone</th></tr></thead>
<tbody>
<tr><td>1–7</td><td>Friendly nudge</td><td>Assume they forgot. Give them an exit that costs no face</td></tr>
<tr><td>8–30</td><td>Second reminder</td><td>Short, direct, still warm. Ask <em>when</em>, not <em>whether</em></td></tr>
<tr><td>31–60</td><td>Firm reminder</td><td>Name the late fee. Offer a payment plan in the same message</td></tr>
<tr><td>61–90</td><td>Final written notice</td><td>Dated, specific, lists what came before. This is a record</td></tr>
<tr><td>90+</td><td>Pause and phone</td><td>State the consequence already in force, then call</td></tr>
</tbody></table></div>

<h3>Three rules that apply at every stage</h3>

<ul>
<li><strong>Never apologise for asking.</strong> "Sorry to bother you about this" tells the reader the
request is optional. You delivered the lessons.</li>
<li><strong>Always name the amount, the invoice and a date.</strong> Vague reminders get vague
responses. "Could you let me know when I can expect it?" requires an answer; "please pay soon" does
not.</li>
<li><strong>Write to the person who pays.</strong> The guardian on the account, never the student, and
never in front of them.</li>
</ul>

<h2 id="cannot-pay">When they say they cannot pay</h2>

<p>Take it at face value. A family that tells you money is difficult is doing you a favour compared to
one that goes silent, and the correct response is not sympathy alone — it is structure.</p>

<div class="callout">
<span class="label">What to send</span>
<p>Thanks for telling me — genuinely, that is much better than silence. Let's split the $600 into
three payments of $200 on the 5th of each month. Lessons continue as normal as long as we keep to
that. Reply "agreed" and I'll set it up.</p>
</div>

<p>Then record each instalment as its own invoice with its own due date. Now the plan is what gets
chased, not the original debt, and if an instalment slips you find out in days rather than months.</p>

<h2 id="pausing">Pausing lessons without losing the family</h2>

<p>Suspension feels like the nuclear option and is usually treated as one. It works better framed as a
consequence already in force than as a threat about to land.</p>

<p>The difference is small and matters. "If you don't pay we will have to stop lessons" invites
negotiation. "As set out in my notice of the 12th, lessons are paused from Monday while the balance
is outstanding — this is reversible today" states a fact and leaves the door open.</p>

<p>Two things make it land without burning the relationship: give a date by which the slot will be
released to another family, and offer the phone. Accounts this old are settled on a call far more
often than by email.</p>

{cta("Find out what this is costing you", "Unpaid invoices and no-shows rarely feel like much individually. The free calculator prices both, annually, from your own numbers.")}

<h2 id="prevention">Most of this is prevented at enrolment</h2>

<p>Every stage above is damage control. The actual fix happens before the first lesson.</p>

<ul>
<li><strong>A written payment policy, signed.</strong> Due date, grace period, late fee, what happens
at thirty days. Unpaid invoices trace back to terms that were never agreed far more often than to
families who genuinely cannot pay.</li>
<li><strong>Payment in advance.</strong> Tuition covering lessons already delivered is a debt. Tuition
covering lessons not yet delivered is a deposit, and it is a fundamentally easier conversation.</li>
<li><strong>A due date that is a date.</strong> Not "at the start of the month". The 5th.</li>
</ul>

<h2 id="write-off">When to stop</h2>

<p>At some point the pursuit costs more than the debt. For a few hundred dollars, that point arrives
well before small claims court.</p>

<p>A reasonable rule: after the phone call at ninety days and one more attempt at a payment plan, stop
active chasing, keep the record, and do not take the family back without settling first. Write it off
in your own accounting, tell your accountant, and move on. The energy is worth more spent on
collecting the invoices that are only thirty days old — the ones you can still save.</p>
''',
 "related": ["tutoring-cancellation-no-show-policy", "track-tutoring-payments-google-sheets"],
},
{
 "slug": "tutoring-business-profit-margin",
 "date": "2026-07-24",
 "minutes": 7,
 "title": "Tutoring Business Profit Margin: What's Normal, and Where It Goes",
 "seo_title": "Tutoring Business Profit Margin: What's Normal",
 "description": "Healthy tutoring businesses keep 15–30% after tutor pay and fixed costs. Here is how to work out yours, what the benchmarks mean, and the three places the margin usually disappears.",
 "standfirst": "Most owners can quote their monthly revenue to the nearest hundred. Very few can quote their margin, and the gap between those two numbers is where the business actually lives.",
 "body": f'''
<p class="opening">Revenue is a comforting number. It goes up when you are busy, it is easy to
remember, and it has almost nothing to do with whether the business is working. Margin is the
uncomfortable number, and it is the one that decides whether you can hire, raise rates, or take a
holiday.</p>

<h2 id="calculate">How to work it out</h2>

<p>Net margin is what is left after everything, divided by what you invoiced. The order matters, so
work down:</p>

<div class="tablewrap"><table>
<thead><tr><th>Step</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Sessions scheduled (45 students × 4)</td><td>180</td></tr>
<tr><td>Revenue you could bill, at $60</td><td>$10,800</td></tr>
<tr><td>Less no-shows never billed (8%)</td><td>−$864</td></tr>
<tr><td>Actually invoiced</td><td>$9,936</td></tr>
<tr><td>Less unpaid invoices (6%)</td><td>−$596</td></tr>
<tr><td>Cash collected</td><td>$9,340</td></tr>
<tr><td>Less tutor pay (55% of held sessions)</td><td>−$5,465</td></tr>
<tr><td>Less fixed costs</td><td>−$1,800</td></tr>
<tr><td><strong>Net profit</strong></td><td><strong>$2,075 — 20.9%</strong></td></tr>
</tbody></table></div>

<p>That business is healthy. It is also losing $17,522 a year, which we will come to.</p>

<div class="callout">
<span class="label">Include your own salary</span>
<p>If you teach lessons yourself and pay yourself nothing for them, your margin is fiction. Put
yourself in as a tutor at a real rate. A business that only works because the owner is free is not a
business you can sell, hire into, or step back from.</p>
</div>

<h2 id="benchmarks">What the numbers should look like</h2>

<div class="tablewrap"><table>
<thead><tr><th>Metric</th><th>Healthy</th><th>What it means outside that range</th></tr></thead>
<tbody>
<tr><td>Net margin</td><td>15–30%</td><td>Below 10% you own a job with extra admin. Above 35% usually means you teach most lessons yourself, which does not scale</td></tr>
<tr><td>Tutor share</td><td>50–60% of session fee</td><td>Below 45% and good tutors leave. Above 65% and there is nothing left for the business</td></tr>
<tr><td>No-show rate</td><td>5–10%</td><td>Above 15% means the cancellation policy either does not exist or is not enforced</td></tr>
<tr><td>Collection rate</td><td>95%+</td><td>Below 90% means chasing has stopped being a habit</td></tr>
</tbody></table></div>

{cta("Compare your own numbers", "The free calculator runs the table above on your figures and shows the annual cost of each leak. No sign-up.")}

<h2 id="where-it-goes">The three places margin disappears</h2>

<h3>1. Sessions that were scheduled and never billed</h3>

<p>Every no-show and late cancellation is revenue you planned for and did not receive. It never
appears on an invoice, so it never appears anywhere — you simply bill less than expected and blame a
slow month.</p>

<div class="figures rise">
<div><span class="n loss">$864</span><span class="k">Per month, at an 8% no-show rate</span></div>
<div><span class="n loss">$10,368</span><span class="k">Per year, from the same business</span></div>
</div>

<h3>2. Paying for what you did not charge for</h3>

<p>Many owners pay the tutor for a booked slot regardless of attendance. It is fair and it keeps good
tutors. But if the family is not charged and the tutor is paid, that lesson has a <strong>100%
negative margin</strong> — you are buying it.</p>

<p>In the example business, that single policy costs $475 a month. It is usually worth more than a
price rise, and it is a decision rather than a market condition.</p>

<h3>3. Invoiced revenue that never arrives</h3>

<p>This is the one owners consistently underestimate, because invoiced revenue <em>feels</em> earned.
It gets counted mentally, then quietly written off months later. At 45 students, a 6% unpaid rate is
roughly $600 a month sitting in someone else's bank account.</p>

<h2 id="improving">Improving it, in order of effort</h2>

<ol>
<li><strong>Enforce the cancellation policy you already have.</strong> Costs nothing, recovers the
largest leak, requires one uncomfortable conversation.</li>
<li><strong>Chase the aged list weekly.</strong> Fifteen minutes. Moves collection rate more than any
pricing change.</li>
<li><strong>Decide whether you pay for missed sessions.</strong> One line in your tutor agreement.</li>
<li><strong>Then raise prices.</strong> A $5 increase across 180 sessions a month is $10,800 a year and
rarely costs a single student — but doing it before the three items above just means leaking a
larger number.</li>
</ol>

<h2 id="student-level">Look at margin per student, not just overall</h2>

<p>A blended margin hides the shape of the business. Take revenue per student, subtract what you pay
the tutor who teaches them, and rank the list.</p>

<p>It is uncomfortable reading. There are usually a handful of students carrying the business, a long
middle, and a few who are close to free — group sessions at a discount, taught by your most expensive
tutor, with a sibling discount stacked on top. You do not necessarily drop them. But you should know
which ones they are before you decide the business needs more students.</p>
''',
 "related": ["track-tutoring-payments-google-sheets", "tutoring-cancellation-no-show-policy"],
},
{
 "slug": "tutoring-cancellation-no-show-policy",
 "date": "2026-07-26",
 "minutes": 6,
 "title": "How to Write a Tutoring Cancellation and No-Show Policy That Holds",
 "seo_title": "Tutoring Cancellation and No-Show Policy: How to Write One",
 "description": "What belongs in a tutoring cancellation policy, how much notice to require, whether to charge for no-shows, and why the policy you do not enforce is worse than no policy at all.",
 "standfirst": "Most tutoring businesses have a cancellation policy. Far fewer have one they enforce, and an unenforced policy teaches clients that none of your terms are real.",
 "body": f'''
<p class="opening">A cancellation policy is not paperwork. It is the single document that decides
whether 5% or 20% of your sessions evaporate, and whether the ones that evaporate cost you money or
merely cost you time.</p>

<p>It needs to answer four questions, and it needs to be signed before the first lesson.</p>

<h2 id="notice">How much notice, and what happens either side of it</h2>

<p>Twenty-four hours is the common standard and it works. Long enough that a family can genuinely give
it, short enough that you can sometimes fill the slot.</p>

<div class="tablewrap"><table>
<thead><tr><th>Situation</th><th>Standard treatment</th></tr></thead>
<tbody>
<tr><td>Cancelled with 24h+ notice</td><td>Not charged. Makeup offered subject to availability</td></tr>
<tr><td>Cancelled inside 24h</td><td>Charged in full — the tutor reserved the time and is paid for it</td></tr>
<tr><td>No-show, no contact</td><td>Charged in full. No makeup</td></tr>
<tr><td>You cancel</td><td>Not charged. Makeup offered, or credited to the next invoice</td></tr>
</tbody></table></div>

<p>State the reason inside the policy itself, in one sentence: <em>the tutor has reserved the time and
is paid for it</em>. A rule with a reason attached is argued with far less than a rule without one.</p>

<h2 id="charge">Should you charge for no-shows?</h2>

<p>Yes — and the more useful question is what you do with the money, because charging for no-shows is
what makes the policy credible rather than decorative.</p>

<p>The alternative has a cost you can calculate. If the family is not charged and the tutor is paid,
that lesson has a 100% negative margin. Across a year, in a business of forty-five students, this is
routinely five figures.</p>

<div class="callout">
<span class="label">The honest version</span>
<p>Write down what you actually do, not what you wish you did. If your policy says you charge for
no-shows but in practice you always waive them, your real policy is that you do not charge — and your
clients already know it. Either enforce it or change the wording.</p>
</div>

{cta("Price your own no-shows first", "The free calculator shows what missed sessions cost you a year — including the ones where you still paid the tutor. It is usually the number that settles the argument.")}

<h2 id="makeups">Makeup sessions: the clause that quietly eats your calendar</h2>

<p>Makeups feel generous and are the most commonly mismanaged part of a tutoring policy. Left
undefined, they accumulate — a family arrives in June with nine credits from October and a reasonable
expectation you will honour them.</p>

<p>Three limits keep it manageable:</p>

<ul>
<li><strong>An expiry.</strong> Thirty days is normal. Say it in the policy.</li>
<li><strong>Subject to availability.</strong> A makeup is offered from existing gaps, not by opening
new ones.</li>
<li><strong>No cash value.</strong> Makeups are not refundable and do not carry over on leaving.</li>
</ul>

<p>Note that a makeup still costs you the tutor's time while earning nothing new. It is a goodwill
expense, which is fine — as long as it is a bounded one.</p>

<h2 id="pausing">Pausing and holidays</h2>

<p>Two clauses that prevent most awkward conversations before they start.</p>

<p><strong>Holidays.</strong> List the dates you do not run. Then say explicitly that monthly tuition
is averaged across the year and is not reduced in shorter months. Without that sentence you will
re-litigate it every December.</p>

<p><strong>Pausing.</strong> Allow it, bound it, and require notice — up to four weeks a year with
fourteen days' notice is reasonable. Be clear about whether the time slot is held. A family that can
pause properly is a family that comes back; one that cannot simply leaves.</p>

<h2 id="enforce">Enforcing it without becoming the villain</h2>

<p>The first time you apply the policy is the only difficult one, and how you do it sets the tone for
every family afterwards.</p>

<ul>
<li><strong>Apply it the first time it happens</strong>, not the third. Waiving it twice and charging
on the third occasion looks arbitrary; charging every time looks like a policy.</li>
<li><strong>Reference the signed document</strong>, not your judgement. "Under the terms agreed at
enrolment" is a fact. "I've decided to charge you" is a position.</li>
<li><strong>Give one goodwill waiver per family, deliberately.</strong> Name it as a one-off in
writing. It buys enormous goodwill and it sets a precedent you control.</li>
</ul>

<blockquote class="pull">A policy you enforce inconsistently is worse than no policy, because it
teaches clients that your terms are opening positions.</blockquote>

<h2 id="signature">Get it signed, and keep it somewhere you can find it</h2>

<p>An emailed policy is a suggestion. A signed one is an agreement, and the difference only becomes
visible at the moment you need it — which is exactly the moment you cannot go back and fix it.</p>

<p>Send it with the enrolment form, ask for it back signed before the first lesson, and store it where
you can produce it in thirty seconds. When an account reaches sixty days overdue, being able to quote
the clause the family agreed to changes the conversation entirely.</p>
''',
 "related": ["client-wont-pay-tutoring", "tutoring-business-profit-margin"],
},
]

BY_SLUG = {p["slug"]: p for p in POSTS}


def head(title, desc, canonical, css_extra="", jsonld=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}/assets/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{css_extra}assets/logo.svg">
<link rel="stylesheet" href="{css_extra}assets/tl.css">
<link rel="stylesheet" href="{css_extra}assets/blog.css">
{jsonld}
</head>
<body class="blog">
<div class="progress"></div>
<header class="site-head">
  <nav class="wrap nav">
    <a class="logo" href="{css_extra or './'}">{LOGO} TutorLedger</a>
    <div class="nav-spacer"></div>
    <a class="navlink hide-sm" href="{css_extra}blog/">Blog</a>
    <a class="navlink" href="{css_extra}tutoring-profit-calculator/">Free calculator</a>
    <a class="btn glow" href="{css_extra or './'}">The system — $19</a>
  </nav>
</header>
'''


FOOT = '''
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div style="min-width:220px">
        <p class="tiny faint" style="max-width:260px">Practical money tools for people who run tutoring businesses.</p>
      </div>
      <div>
        <h4>Product</h4>
        <a href="{r}">TutorLedger — $19</a>
        <a href="{r}tutoring-profit-calculator/">Free profit calculator</a>
        <a href="{r}blog/">Blog</a>
      </div>
      <div>
        <h4>Legal</h4>
        <a href="{r}terms.html">Terms of sale</a>
        <a href="{r}privacy.html">Privacy</a>
        <a href="{r}refund-policy.html">Refund policy</a>
      </div>
      <div>
        <h4>Support</h4>
        <a href="mailto:tutorledger.support@gmail.com">tutorledger.support@gmail.com</a>
      </div>
    </div>
    <p class="legal">Articles here are general business guidance, not accounting, tax or legal advice.
      © <span id="yr">2026</span> TutorLedger.</p>
  </div>
</footer>
<script src="{r}assets/tl.js" defer></script>
<script src="{r}assets/blog.js" defer></script>
<script>document.getElementById("yr").textContent=new Date().getFullYear();</script>
</body>
</html>
'''


def pretty(iso):
    y, m, dd = iso.split("-")
    return f"{int(dd)} {['January','February','March','April','May','June','July','August','September','October','November','December'][int(m)-1]} {y}"


def build_post(p):
    canonical = f"{BASE}/blog/{p['slug']}/"
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', p["body"], re.S)
    toc = "\n".join(f'      <a href="#{i}">{re.sub("<[^>]+>", "", t)}</a>' for i, t in heads)

    jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article",
 "headline":{p["seo_title"]!r},
 "description":{p["description"]!r},
 "datePublished":"{p['date']}","dateModified":"{p['date']}",
 "author":{{"@type":"Organization","name":"TutorLedger"}},
 "publisher":{{"@type":"Organization","name":"TutorLedger"}},
 "mainEntityOfPage":"{canonical}",
 "image":"{BASE}/assets/og-cover.png"}}
</script>'''.replace("'", '"')

    rel = "".join(f'''
      <a href="../{s}/"><b>{BY_SLUG[s]["title"]}</b><span>{BY_SLUG[s]["minutes"]} min read</span></a>'''
                  for s in p["related"])

    html = head(p["seo_title"] + " — TutorLedger", p["description"], canonical, "../../", jsonld) + f'''
<main class="wrap">

  <div class="article-head">
    <p class="kicker">TutorLedger Journal</p>
    <h1>{p["title"]}</h1>
    <p class="standfirst">{p["standfirst"]}</p>
    <div class="byline">
      <span><b>{pretty(p["date"])}</b></span>
      <span>{p["minutes"]} min read</span>
      <span><a href="../" style="color:inherit">All articles</a></span>
    </div>
  </div>

  <div class="layout">
    <nav class="toc" aria-label="On this page">
      <h4>On this page</h4>
{toc}
    </nav>

    <div class="prose">
      <article class="post">{p["body"]}</article>

      <div class="article-foot">
        <p class="kicker">Keep reading</p>
        <div class="related">{rel}
        </div>
      </div>
    </div>
  </div>
</main>
''' + FOOT.replace("{r}", "../../")

    out = os.path.join(HERE, p["slug"])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="").write(html)
    return len(re.sub(r"<[^>]+>", " ", p["body"]).split())


def build_index():
    cards = "".join(f'''
    <a class="post-card rise" href="{p['slug']}/">
      <div class="when">{pretty(p['date'])}<br>{p['minutes']} min</div>
      <div>
        <h2>{p['title']}</h2>
        <p>{p['standfirst']}</p>
        <span class="more">Read the article <span>&rarr;</span></span>
      </div>
    </a>''' for p in sorted(POSTS, key=lambda x: x["date"], reverse=True))

    html = head("Blog — TutorLedger",
                "Practical writing on tuition, collections and margin for people who run tutoring businesses.",
                f"{BASE}/blog/", "../") + f'''
<main class="wrap">
  <div class="blog-hero">
    <p class="kicker">TutorLedger Journal</p>
    <h1>Getting paid, and knowing what you keep.</h1>
    <p class="lede">Writing for people who run tutoring businesses — collections, margin, policy and
      the spreadsheet mechanics underneath. No growth hacks, no funnels. Just the money side, done
      properly.</p>
  </div>

  <div class="posts">{cards}
  </div>
</main>
''' + FOOT.replace("{r}", "../")
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8", newline="").write(html)


def build_sitemap():
    urls = [(BASE + "/", "1.0"), (CALC, "0.9"), (BASE + "/blog/", "0.7")]
    urls += [(f"{BASE}/blog/{p['slug']}/", "0.6") for p in POSTS]
    today = date.today().isoformat()
    body = "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>\n"
                   for u, pr in urls)
    open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8", newline="").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n')
    open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8", newline="").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")


words = [build_post(p) for p in POSTS]
build_index()
build_sitemap()

# Regenerating a page wipes its cache-busting stamp, so re-apply it here rather
# than relying on remembering to run bump-assets.py afterwards.
import subprocess, sys
subprocess.run([sys.executable, os.path.join(SITE, "bump-assets.py")],
               capture_output=True, check=False)

print(f"{len(POSTS)} articles + index + sitemap")
for p, w in zip(POSTS, words):
    print(f"   /blog/{p['slug']:<44} {w:>5} words   {p['minutes']} min")
print(f"   total {sum(words)} words")
