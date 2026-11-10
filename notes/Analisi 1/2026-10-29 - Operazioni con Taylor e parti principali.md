---
type: lecture-note
course: Analisi 1
date: '2026-10-29'
title: Operazioni con Taylor e parti principali
source_files:
- AM1_26_L029.pdf
- AM1_26_L030.pdf
source_date: '2025-10-28'
teaching_model: anthropic/claude-opus-5.5
original_date: '2026-10-28'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Analisi 1/Lectures/2026-10-29 - Operazioni con Taylor e parti principali.md
vault_hash: 8aeeab2324014a305ceb2fd172fe20dd63aefee5308b4b8eaa618784c94c6867
---

# Operazioni con Taylor e parti principali

Questa nota riunisce le parti **029 e 030** della lezione di mercoledì **28 ottobre 2026**. Prosegue [[2026-10-28 - Teorema di De L'Hôpital e sviluppi di Taylor]]: dopo aver costruito gli [[Sviluppo di Taylor|sviluppi di Taylor]] delle funzioni elementari, impariamo a combinarli, a cambiare centro e a riconoscere il primo termine che sopravvive alle cancellazioni, la **[[Parte principale|parte principale]]**.

Salvo indicazione diversa, tutti gli sviluppi sono per $x\to0$ e $m\geq1$ è un intero. I termini indicati con $o(x^m)$ (vedi [[Simboli di Landau]]) rappresentano resti, non un'unica funzione fissata: due resti dello stesso ordine possono essere diversi.

## 1. Taylor con centro in un punto qualunque

Siano $x_0\in\mathbb R$, $\delta>0$ e

$$
f:(x_0-\delta,x_0+\delta)\longrightarrow\mathbb R.
$$

Cerchiamo un polinomio $P_m$ di grado al più $m$ tale che

$$
f(x)=P_m(x-x_0)+o\bigl((x-x_0)^m\bigr)
\qquad\text{per }x\to x_0.
$$

Ponendo **$h=x-x_0$**, la stessa richiesta si scrive

$$
f(x_0+h)=P_m(h)+o(h^m)\qquad\text{per }h\to0.
$$

**Teorema di Taylor–Peano.** Condizioni sufficienti sono che $f$ sia [[Derivata|derivabile]] $m-1$ volte nell'intorno di $x_0$ e che esista anche la derivata $m$-esima in $x_0$. In tal caso

$$
\boxed{
f(x)=\sum_{k=0}^{m}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
+o\bigl((x-x_0)^m\bigr).
}
$$

**Dimostrazione a partire dal centro $0$.** Si considera $g(h)=f(x_0+h)$. Per [[Principio di induzione|induzione]] sulle derivate,

$$
g^{(k)}(h)=f^{(k)}(x_0+h),\qquad g^{(k)}(0)=f^{(k)}(x_0).
$$

Applicare Taylor–Peano a $g$ in $0$ dà esattamente lo sviluppo di $f$ in $x_0$.

## 2. Somme, differenze e prodotti

Supponiamo di conoscere, **allo stesso ordine**,

$$
f(x)=P_m(x)+o(x^m),\qquad g(x)=Q_m(x)+o(x^m).
$$

### 2.1 Somma e moltiplicazione per una costante

$$
\boxed{f(x)\pm g(x)=P_m(x)\pm Q_m(x)+o(x^m),}
$$

$$
\boxed{\lambda f(x)=\lambda P_m(x)+o(x^m)\qquad(\lambda\in\mathbb R).}
$$

Si usano $o(x^m)+o(x^m)=o(x^m)$ e $\lambda o(x^m)=o(x^m)$.

**Attenzione alla notazione.** È vero che $x^4=o(x)$ e $x^3=o(x)$, ma questo non significa che $x^4=x^3$. Le due funzioni appartengono alla stessa classe di resti rispetto a $x$.

### 2.2 Prodotto di due funzioni

$$
\boxed{f(x)g(x)=P_m(x)Q_m(x)+o(x^m).}
$$

Il prodotto $P_mQ_m$ può avere grado fino a $2m$, ma **si conservano solo i monomi di grado $\leq m$**: quelli di grado maggiore sono già $o(x^m)$.

**Dimostrazione.** Scriviamo i resti come $x^m\omega_1(x)$ e $x^m\omega_2(x)$, con $\omega_i(x)\to0$. Allora

$$
\begin{aligned}
fg
&=(P_m+x^m\omega_1)(Q_m+x^m\omega_2)\\
&=P_mQ_m+x^m\bigl(P_m\omega_2+Q_m\omega_1+x^m\omega_1\omega_2\bigr).
\end{aligned}
$$

La parentesi tende a $0$, perché i polinomi sono limitati vicino a $0$ e $\omega_1,\omega_2\to0$.

### 2.3 Esempio: $\sin x\cos x$ all'ordine $5$

$$
\begin{aligned}
\sin x\cos x
&=\left(x-\frac{x^3}{6}+\frac{x^5}{120}+o(x^5)\right)
\left(1-\frac{x^2}{2}+\frac{x^4}{24}+o(x^5)\right)\\
&=x-\frac{x^3}{2}-\frac{x^3}{6}
+\frac{x^5}{24}+\frac{x^5}{12}+\frac{x^5}{120}+o(x^5)\\
&=\boxed{x-\frac23x^3+\frac{2}{15}x^5+o(x^5)}.
\end{aligned}
$$

Non serve calcolare i prodotti che danno grado $7$ o superiore.

## 3. Composizione di sviluppi

Occorre conoscere la [[Composizione di funzioni|composizione di funzioni]]; il problema è controllare che i resti restino della giusta grandezza.

La domanda decisiva è: **l'argomento che sostituisco tende al centro dello sviluppo esterno?**

### 3.1 Sostituire $ax$ oppure $ax^b$

Se $f(t)=P_m(t)+o(t^m)$ per $t\to0$, per $a\neq0$ fissato vale

$$
f(ax)=P_m(ax)+o(x^m).
$$

Più in generale, per $b>0$,

$$
\boxed{f(ax^b)=P_m(ax^b)+o(x^{bm}).}
$$

Infatti, scrivendo il resto come $t^m\omega(t)$,

$$
(ax^b)^m\omega(ax^b)=x^{bm}\underbrace{a^m\omega(ax^b)}_{\to0}.
$$

La condizione $b>0$ garantisce che $ax^b\to0$. Se $b$ non è intero, si considera il lato su cui la potenza reale è definita; questa è una precisazione di dominio.

**Esempio: $\sin(2x)$ all'ordine $5$.** Si sostituisce $2x$ in ogni potenza:

$$
\sin(2x)=2x-\frac{(2x)^3}{6}+\frac{(2x)^5}{120}+o(x^5)
=\boxed{2x-\frac43x^3+\frac4{15}x^5+o(x^5)}.
$$

È il doppio dello sviluppo di $\sin x\cos x$, in accordo con $\sin(2x)=2\sin x\cos x$. Per [[Funzione pari e dispari|parità]] si può anche scrivere il resto $o(x^6)$.

**Esempio: $\sin(x^3)$ all'ordine $14$.** Il primo termine dopo quello di grado $9$ ha grado $15$:

$$
\sin(x^3)=x^3-\frac{x^9}{6}+\frac{x^{15}}{120}+o(x^{15})
=\boxed{x^3-\frac{x^9}{6}+o(x^{14})}.
$$

Il passaggio intermedio esplicita perché il resto è abbastanza preciso per l'ordine richiesto.

### 3.2 Composizione generale con funzione interna nulla in $0$

Siano $P_m,Q_m$ i polinomi di Taylor rispettivamente di $f,g$ in $0$, e sia **$f(0)=0$**. Allora, dove la composizione è definita,

$$
\boxed{g(f(x))=Q_m(P_m(x))+o(x^m).}
$$

Anche qui si scartano i termini di grado maggiore di $m$ nel polinomio composto, che prima del troncamento potrebbe avere grado $m^2$.

**Dimostrazione.** Dallo sviluppo di $g$,

$$
g(f(x))=Q_m(f(x))+f(x)^m\omega_2(f(x)).
$$

Occorre controllare due passaggi.

1. **Il resto composto è ancora $o(x^m)$.** Siccome $P_m(0)=f(0)=0$, esiste un polinomio $R$ tale che $P_m(x)=xR(x)$. Quindi
   $$
   f(x)=x\bigl(R(x)+x^{m-1}\omega_1(x)\bigr).
   $$
   La parentesi è limitata e $f(x)\to0$, perciò
   $$
   f(x)^m\omega_2(f(x))
   =x^m\bigl(R(x)+x^{m-1}\omega_1(x)\bigr)^m\omega_2(f(x))
   =o(x^m).
   $$

2. **Dentro il polinomio si può sostituire $f$ con $P_m$.** Per ogni monomio di grado $k\geq1$,
   $$
   f(x)^k-P_m(x)^k
   =(f(x)-P_m(x))\sum_{j=0}^{k-1}f(x)^{k-1-j}P_m(x)^j=o(x^m),
   $$
   perché il primo fattore è $o(x^m)$ e la somma è limitata. Sommando sui monomi di $Q_m$ si conclude.

L'identità per la differenza di potenze rende esplicito il passaggio che nel PDF è giustificato tramite il [[Binomio di Newton|binomio di Newton]].

## 4. Parte principale e ordine di infinitesimo

**Definizione.** Se, per $x\to0$,

$$
f(x)\sim ax^b,\qquad a\neq0,
$$

cioè

$$
f(x)=ax^b+o(x^b),
$$

il termine $ax^b$ si chiama **parte principale** di $f$ (è anche un caso di [[Equivalenza asintotica]]). Se $b>0$, $f$ è un infinitesimo e $b$ è il suo **ordine** rispetto a $x$.

Quando si usa Taylor, la parte principale è il **primo monomio non nullo**, contando dal grado più basso, dopo aver effettuato le cancellazioni.

### 4.1 Parte principale di $\sin x-\arctan x$

Gli sviluppi lineari si cancellano, quindi bisogna arrivare al grado $3$:

$$
\begin{aligned}
\sin x-\arctan x
&=\left(x-\frac{x^3}{6}+o(x^3)\right)
-\left(x-\frac{x^3}{3}+o(x^3)\right)\\
&=\boxed{\frac{x^3}{6}+o(x^3)}.
\end{aligned}
$$

La parte principale è $x^3/6$ e l'ordine è $3$.

### 4.2 Un limite con cancellazione dei termini lineari

$$
\lim_{x\to0}\frac{\sin x-\arctan x}{e^{x^3}-1}.
$$

Il numeratore è $x^3/6+o(x^3)$, mentre

$$
e^{x^3}-1=x^3+o(x^3).
$$

Pertanto

$$
\frac{\sin x-\arctan x}{e^{x^3}-1}
=\frac{x^3\bigl(\frac16+o(1)\bigr)}{x^3(1+o(1))}
\longrightarrow\boxed{\frac16}.
$$

I soli [[Limiti notevoli|limiti notevoli]] lineari non distinguono i due termini del numeratore: occorre conoscerne il comportamento cubico.

**Variante con un termine trascurabile.** Per la presenza della radice, consideriamo $x\to0^+$:

$$
\lim_{x\to0^+}
\frac{\sin x-\arctan x}{e^{x^3}-1+\sqrt{x}\log(1+x^3\sqrt{x})}.
$$

Poiché

$$
\sqrt{x}\log(1+x^3\sqrt{x})
=\sqrt{x}\bigl(x^{7/2}+o(x^{7/2})\bigr)
=x^4+o(x^4)=o(x^3),
$$

la parte principale del denominatore resta $x^3$ e il limite resta $1/6$.

## 5. Potenze e lettura delle derivate dai coefficienti

### 5.1 Sviluppo di $(\sin x)^3$ all'ordine $5$

$$
\begin{aligned}
(\sin x)^3
&=\left(x-\frac{x^3}{6}+\frac{x^5}{120}+o(x^5)\right)^3\\
&=x^3+3x^2\left(-\frac{x^3}{6}\right)+o(x^5)\\
&=\boxed{x^3-\frac12x^5+o(x^5)}.
\end{aligned}
$$

Il solo prodotto misto da conservare è quello di grado $5$; gli altri hanno grado almeno $7$.

### 5.2 Calcolare $f^{(5)}(0)$ senza derivare cinque volte

Per $f(x)=(\sin x)^3$, Taylor dà un coefficiente di $x^5$ pari a $f^{(5)}(0)/5!$. Confrontando con lo sviluppo appena trovato,

$$
\frac{f^{(5)}(0)}{5!}=-\frac12
\qquad\Longrightarrow\qquad
\boxed{f^{(5)}(0)=-60}.
$$

Qui sappiamo già che le derivate esistono: l'identificazione dei coefficienti usa la formula di Taylor e la sua unicità.

## 6. Esempi di composizione e scelta del centro

### 6.1 $\sin(x+x^3)$ all'ordine $3$

Bisogna sostituire $x+x^3$ **in tutte le occorrenze** dell'argomento:

$$
\begin{aligned}
\sin(x+x^3)
&=(x+x^3)-\frac16(x+x^3)^3+o(x^3)\\
&=x+x^3-\frac{x^3}{6}+o(x^3)\\
&=\boxed{x+\frac56x^3+o(x^3)}.
\end{aligned}
$$

Scrivere soltanto $x+x^3+o(x^3)$ dimenticherebbe il contributo cubico dello sviluppo del seno.

### 6.2 $\cos(\sin x)$ all'ordine $4$

L'argomento interno tende a $0$, quindi lo sviluppo del coseno in $0$ è adatto:

$$
\cos(\sin x)=1-\frac12(\sin x)^2+\frac1{24}(\sin x)^4+o(x^4).
$$

Usando

$$
(\sin x)^2=x^2-\frac13x^4+o(x^4),\qquad
(\sin x)^4=x^4+o(x^4),
$$

si ottiene

$$
\boxed{\cos(\sin x)=1-\frac12x^2+\frac5{24}x^4+o(x^4)}.
$$

### 6.3 $\sin(\cos x)$ all'ordine $3$: il centro esterno è $1$

Qui $\cos x\to1$. **Non si può applicare lo sviluppo del seno in $0$ all'argomento $\cos x$** e poi trattarne il resto come $o(x^3)$: la condizione sull'argomento viene meno.

Bisogna sviluppare il seno **intorno a $1$**. Dalla formula di addizione,

$$
\begin{aligned}
\sin(1+h)
&=\sin1\cos h+\cos1\sin h\\
&=\sin1+\cos1\,h-\frac{\sin1}{2}h^2-\frac{\cos1}{6}h^3+o(h^3).
\end{aligned}
$$

Ora poniamo

$$
h=\cos x-1=-\frac{x^2}{2}+o(x^3).
$$

I termini con $h^2$ e $h^3$ hanno grado almeno $4$, dunque

$$
\boxed{\sin(\cos x)=\sin1-\frac{\cos1}{2}x^2+o(x^3)}.
$$

In questo esercizio basta **conservare il termine lineare in $h$**, controllando però che lo scarto sia dell'ordine di $h^2$, come mostra lo sviluppo precedente. Dato che $h$ è dell'ordine di $x^2$, tale scarto è $o(x^3)$. La sola scrittura $\sin(1+h)=\sin1+\cos1\,h+o(h)$ non garantirebbe invece la precisione richiesta.

### 6.4 $e^x$ con centro $x_0=2$, ordine $3$

Ponendo $h=x-2$,

$$
e^{2+h}=e^2e^h
=e^2\left(1+h+\frac{h^2}{2}+\frac{h^3}{6}\right)+o(h^3).
$$

Quindi, per $x\to2$,

$$
\boxed{e^x=e^2\left(1+(x-2)+\frac{(x-2)^2}{2}+\frac{(x-2)^3}{6}\right)
+o\bigl((x-2)^3\bigr)}.
$$

### 6.5 $\log x$ con centro $x_0=2$, ordine $3$

Scrivere $\log x=\log(1+(x-1))$ non permette di usare lo sviluppo in $0$ di $\log(1+t)$, perché $x-1\to1$.

La riscrittura utile è invece

$$
\begin{aligned}
\log(2+h)
&=\log2+\log\left(1+\frac h2\right)\\
&=\boxed{\log2+\frac h2-\frac{h^2}{8}+\frac{h^3}{24}+o(h^3)}.
\end{aligned}
$$

Lo sviluppo in $x$ si ottiene sostituendo $h=x-2$.

## 7. Differenze di reciproci e potenze variabili

### 7.1 Parte principale di $\dfrac1{\sin x}-\dfrac1x$

Prima si porta a denominatore comune:

$$
\frac1{\sin x}-\frac1x=\frac{x-\sin x}{x\sin x}.
$$

Per $x\to0$,

$$
x-\sin x=\frac{x^3}{6}+o(x^3),\qquad
x\sin x=x^2+o(x^3).
$$

Di conseguenza

$$
\frac{x-\sin x}{x\sin x}
=x\frac{\frac16+o(1)}{1+o(1)}
=\boxed{\frac x6+o(x)}.
$$

La parte principale è $x/6$: la cancellazione tra i due reciproci lascia un infinitesimo di ordine $1$.

### 7.2 $(1+\sin x)^x$ all'ordine $3$

Vicino a $0$, $1+\sin x>0$. Trasformiamo la potenza in un'esponenziale:

$$
(1+\sin x)^x=\exp\bigl(x\log(1+\sin x)\bigr).
$$

Dato il fattore esterno $x$, per l'esponente è sufficiente conoscere il logaritmo fino all'ordine $2$:

$$
\log(1+\sin x)=x-\frac{x^2}{2}+o(x^2),
$$

$$
x\log(1+\sin x)=x^2-\frac{x^3}{2}+o(x^3)=:u(x).
$$

Poiché $u(x)$ è dell'ordine di $x^2$, il suo quadrato è $o(x^3)$. Usando Taylor dell'esponenziale fino al termine quadratico,

$$
e^{u(x)}=1+u(x)+\frac{u(x)^2}{2}+o(u(x)^2),
$$

otteniamo

$$
\boxed{(1+\sin x)^x=1+x^2-\frac{x^3}{2}+o(x^3)}.
$$

Questo controllo del resto è essenziale: la sola formula $e^u=1+u+o(u)$ darebbe in prima battuta un resto $o(x^2)$, insufficiente per dichiarare l'ordine $3$.

## Fonti e precisazioni

- [AM1_26_L029.pdf](/Users/michelangelogubinelli/Downloads/AM1_26_L029.pdf): Taylor in un centro qualunque; somma, prodotto e composizione degli sviluppi; relative dimostrazioni.
- [AM1_26_L030.pdf](/Users/michelangelogubinelli/Downloads/AM1_26_L030.pdf): parte principale, limiti, lettura delle derivate dai coefficienti ed esempi di composizione e cambio del centro.

Entrambi i PDF riportano **28/10/2025**, conservato in `source_date`; la data della lezione nel corso attuale, indicata dall'utente, è **28/10/2026**.

Sono stati completati i calcoli lasciati con puntini nei PDF e resi espliciti alcuni controlli sui resti. Precisazioni rispetto alla fonte:

- la definizione di parte principale richiede $a\neq0$; per potenze non intere va rispettato il dominio;
- nella dimostrazione della sostituzione $ax^b$, il fattore costante corretto è $a^m$;
- la variante con $\sqrt{x}$ è trattata come limite destro;
- per $\sin(\cos x)$ lo sviluppo esterno in $0$ non è applicabile, perché l'argomento tende a $1$: non se ne può dedurre un resto utilizzabile;
- nei passaggi con $\sin(x^3)$ e $(1+\sin x)^x$ è stata esplicitata la precisione necessaria per ottenere il resto dichiarato.
