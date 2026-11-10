---
type: lecture-note
course: Analisi 1
date: '2026-10-30'
title: Funzioni iperboliche ed esercizi sugli sviluppi di Taylor
source_files:
- AM1_26_L031.pdf
- AM1_26_L032.pdf
source_date: '2025-10-29'
teaching_model: anthropic/claude-opus-5.5
original_date: '2026-10-29'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Analisi 1/Lectures/2026-10-30 - Funzioni iperboliche ed esercizi sugli sviluppi di Taylor.md
vault_hash: 613eea0e9c99ffac00a5755065c3ab3452f850b93ab1fdbc20c33fb14280c1db
---

# Funzioni iperboliche ed esercizi sugli sviluppi di Taylor

Questa nota riunisce le parti **031 e 032** della lezione di giovedì **29 ottobre 2026**. La prima parte presenta le **[[Funzioni iperboliche|funzioni iperboliche]]**, le loro inverse e l'interpretazione geometrica. La seconda applica le tecniche di [[2026-10-29 - Operazioni con Taylor e parti principali]] a [[Sviluppo di Taylor|sviluppi di Taylor]], [[Limite di una funzione|limiti]] e [[Successione|successioni]].

## 1. Definizione delle funzioni iperboliche

Per ogni $x\in\mathbb R$ si definiscono

$$
\boxed{\sinh x=\frac{e^x-e^{-x}}2,\qquad
\cosh x=\frac{e^x+e^{-x}}2,\qquad
\tanh x=\frac{\sinh x}{\cosh x}.}
$$

Si chiamano rispettivamente **seno iperbolico**, **coseno iperbolico** e **tangente iperbolica**. Il denominatore della tangente iperbolica non si annulla mai, perché $\cosh x>0$ per ogni $x$.

### 1.1 Simmetrie, limiti e grafici

Il seno iperbolico e la tangente iperbolica sono **dispari**, mentre il coseno iperbolico è **pari** (vedi [[Funzione pari e dispari]]):

$$
\sinh(-x)=-\sinh x,\qquad
\tanh(-x)=-\tanh x,\qquad
\cosh(-x)=\cosh x.
$$

Nessuna delle tre funzioni è [[Funzione periodica|periodica]]. I limiti agli infiniti sono

$$
\begin{array}{c|cc}
&x\to+\infty&x\to-\infty\\ \hline
\sinh x&+\infty&-\infty\\
\cosh x&+\infty&+\infty\\
\tanh x&1&-1
\end{array}
$$

Per esempio,

$$
\tanh x=\frac{e^x-e^{-x}}{e^x+e^{-x}}
=\frac{1-e^{-2x}}{1+e^{-2x}}\longrightarrow1
\qquad(x\to+\infty).
$$

I grafici hanno le seguenti caratteristiche:

- **$\sinh$** passa per $(0,0)$ ed è [[Funzione monotona|strettamente crescente]] su $\mathbb R$;
- **$\cosh$** passa per $(0,1)$, è simmetrica rispetto all'asse verticale ed è strettamente crescente su $[0,+\infty)$; il suo minimo è $1$;
- **$\tanh$** passa per $(0,0)$ ed è strettamente crescente su $\mathbb R$, con asintoti orizzontali $y=1$ e $y=-1$.

## 2. Identità fondamentali e duplicazione

Dalle definizioni,

$$
\sinh^2x=\frac{e^{2x}+e^{-2x}-2}{4},\qquad
\cosh^2x=\frac{e^{2x}+e^{-2x}+2}{4}.
$$

Sottraendo si ottiene la **relazione fondamentale**

$$
\boxed{\cosh^2x-\sinh^2x=1}.
$$

Sommando si trova invece

$$
\boxed{\cosh(2x)=\cosh^2x+\sinh^2x}.
$$

> [!example] Esempio
> Per $x=\log2$ si ha $e^x=2$, quindi $\cosh x=\frac{2+1/2}2=\frac54$ e $\sinh x=\frac{2-1/2}2=\frac34$. La relazione fondamentale torna: $\frac{25}{16}-\frac9{16}=1$.

La formula di duplicazione del seno iperbolico è

$$
\boxed{\sinh(2x)=2\sinh x\cosh x},
$$

infatti

$$
2\sinh x\cosh x
=\frac{(e^x-e^{-x})(e^x+e^{-x})}{2}
=\frac{e^{2x}-e^{-2x}}2.
$$

I segni distinguono queste identità da quelle trigonometriche: nella relazione fondamentale iperbolica compare una **differenza** di quadrati. Il PDF osserva che, con calcoli analoghi, si ricavano anche formule di addizione, sottrazione e trasformazioni tra prodotti e somme, senza svilupparle qui.

## 3. Derivate

Derivando le definizioni esponenziali (con le [[Regole di derivazione]]),

$$
\boxed{(\sinh x)'=\cosh x,\qquad (\cosh x)'=\sinh x}.
$$

Nella derivata del coseno iperbolico il segno è **positivo**. Per la tangente iperbolica, usando il quoziente e la relazione fondamentale,

$$
\begin{aligned}
(\tanh x)'
&=\frac{\cosh^2x-\sinh^2x}{\cosh^2x}\\
&=\boxed{\frac1{\cosh^2x}=1-\tanh^2x}.
\end{aligned}
$$

In particolare, la derivata di $\tanh$ è sempre positiva, in accordo con la stretta crescita del grafico.

## 4. Sviluppi di Taylor di seno e coseno iperbolici

Per $x\to0$,

$$
\boxed{\sinh x=x+\frac{x^3}{3!}+\frac{x^5}{5!}+o(x^5),}
$$

$$
\boxed{\cosh x=1+\frac{x^2}{2!}+\frac{x^4}{4!}+o(x^5).}
$$

A ogni ordine si continua con le sole potenze dispari per $\sinh$ e con le sole potenze pari per $\cosh$, **sempre con coefficienti positivi**.

La fonte presenta due modi per ricavare gli sviluppi.

**Dalle derivate.** Le derivate di $\sinh$ alternano $\sinh$ e $\cosh$; in $0$ assumono i valori $0,1,0,1,\dots$. Per $\cosh$ si ottiene $1,0,1,0,\dots$. Si applica la formula di Taylor–Peano (vedi [[Sviluppo di Taylor]]).

**Dallo sviluppo dell'esponenziale.** Si scrivono, a un ordine fissato,

$$
e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\cdots,
\qquad
e^{-x}=1-x+\frac{x^2}{2}-\frac{x^3}{6}+\cdots,
$$

con il rispettivo resto di Peano. La semisomma conserva i termini pari, la semidifferenza quelli dispari. In questo senso $\cosh$ e $\sinh$ sono la parte pari e la parte dispari di $e^x$. Esattamente, per ogni $x$,

$$
\boxed{\cosh x+\sinh x=e^x}.
$$

## 5. Funzioni inverse: i settori iperbolici

Le [[Funzione inversa|inverse]] vengono chiamate **settori** iperbolici. Nei PDF si usa la notazione “Sett”; qui la scriviamo con $\operatorname{Sett}$.

| Funzione invertita | Dominio e immagine della funzione | Inversa |
|---|---|---|
| $\sinh$ | $\mathbb R\to\mathbb R$ | $\operatorname{Sett}\sinh:\mathbb R\to\mathbb R$ |
| $\cosh$ ristretto ai non negativi | $[0,+\infty)\to[1,+\infty)$ | $\operatorname{Sett}\cosh:[1,+\infty)\to[0,+\infty)$ |
| $\tanh$ | $\mathbb R\to(-1,1)$ | $\operatorname{Sett}\tanh:(-1,1)\to\mathbb R$ |

La restrizione del coseno iperbolico è necessaria: su tutto $\mathbb R$ la funzione è pari, quindi non è [[Funzione biettiva|iniettiva]]. I grafici delle inverse si ottengono riflettendo i grafici delle funzioni corrispondenti rispetto a $y=x$.

### 5.1 Formula esplicita del settore coseno iperbolico

Dato $y\geq1$, cerchiamo l'unico $x\geq0$ per cui $\cosh x=y$:

$$
\frac{e^x+e^{-x}}2=y.
$$

Ponendo $z=e^x>0$,

$$
z+\frac1z=2y
\quad\Longleftrightarrow\quad
z^2-2yz+1=0.
$$

Le soluzioni sono

$$
z_\pm=y\pm\sqrt{y^2-1}.
$$

Sono entrambe positive e il loro prodotto è $1$. Per $y>1$ una è maggiore di $1$ e l'altra minore di $1$; per $y=1$ coincidono. Poiché $x\geq0$ impone $e^x\geq1$, scegliamo $z_+$:

$$
\boxed{\operatorname{Sett}\cosh y=\log\left(y+\sqrt{y^2-1}\right),\qquad y\geq1.}
$$

L'altra radice darebbe il valore opposto di $x$, perché $z_-z_+=1$ e quindi $\log z_-=-\log z_+$.

## 6. Interpretazione geometrica e collegamento con la trigonometria

### 6.1 Parametrizzazione dell'iperbole

La relazione fondamentale mostra che

$$
P(\alpha)=(\cosh\alpha,\sinh\alpha)
$$

appartiene all'iperbole

$$
x^2-y^2=1.
$$

Per $\alpha\geq0$, il punto si trova nella parte superiore del ramo destro. Nel PDF si enuncia, **senza dimostrazione**, il seguente fatto geometrico: il settore delimitato dal segmento dall'origine a $(1,0)$, dall'arco di iperbole fino a $P(\alpha)$ e dal segmento $OP(\alpha)$ ha **area $\alpha/2$**.

Il parametro iperbolico è dunque legato a un'area, da cui il nome delle funzioni inverse, i “settori”. La fonte anticipa anche un collegamento tra rotazioni iperboliche e forme quadratiche con un segno positivo e uno negativo; non ne sviluppa la teoria.

### 6.2 Argomenti immaginari

La seconda anticipazione usa la formula di Eulero

$$
e^{ix}=\cos x+i\sin x.
$$

Estendendo le definizioni esponenziali agli argomenti immaginari,

$$
\cosh(ix)=\frac{e^{ix}+e^{-ix}}2=\boxed{\cos x},
$$

$$
\sinh(ix)=\frac{e^{ix}-e^{-ix}}2=\boxed{i\sin x}.
$$

Formalmente, sostituire $ix$ nelle potenze pari cambia i segni alterni:

$$
\cos(ix)=1+\frac{x^2}{2!}+\frac{x^4}{4!}+\cdots=\cosh x.
$$

Questo collegamento è presentato come anticipazione, non come conseguenza del solo teorema reale di Taylor con resto di Peano: la scrittura infinita richiede la teoria delle serie e l'estensione complessa delle funzioni.

## 7. Sviluppo di $\tan x$ all'ordine $5$

La parte 032 torna alla **tangente trigonometrica**. La fonte propone tre metodi: derivate successive, quoziente seno/coseno e inversione dello sviluppo dell'arcotangente.

### 7.1 Metodo del quoziente

Scriviamo

$$
\tan x=\frac{\sin x}{\cos x}
=\left(x-\frac{x^3}{6}+\frac{x^5}{120}+o(x^5)\right)
\left(1-\frac{x^2}{2}+\frac{x^4}{24}+o(x^5)\right)^{-1}.
$$

Per il reciproco usiamo $(1+t)^{-1}=1-t+t^2+\cdots$. Qui $t$ è dell'ordine di $x^2$; applicando Taylor fino al grado $3$ in $t$, i termini da $t^3$ in poi sono trascurabili rispetto a $x^5$:

$$
\frac1{\cos x}
=1+\frac{x^2}{2}-\frac{x^4}{24}+\frac{x^4}{4}+o(x^5)
=1+\frac{x^2}{2}+\frac5{24}x^4+o(x^5).
$$

Moltiplicando e conservando i gradi al più $5$,

$$
\begin{aligned}
\tan x
&=x+\left(\frac12-\frac16\right)x^3
+\left(\frac5{24}-\frac1{12}+\frac1{120}\right)x^5+o(x^5)\\
&=\boxed{x+\frac{x^3}{3}+\frac{2x^5}{15}+o(x^5)}.
\end{aligned}
$$

Poiché la tangente è dispari e derivabile a ogni ordine vicino a $0$, lo stesso polinomio vale all'ordine $6$, con resto $o(x^6)$.

### 7.2 Metodo dell'inversa

Sapendo che la tangente è dispari, regolare vicino a $0$ e ha derivata $1$ in $0$, scriviamo

$$
\tan x=x+ax^3+bx^5+o(x^5).
$$

Vicino a $0$ vale $\arctan(\tan x)=x$. Usiamo

$$
\arctan t=t-\frac{t^3}{3}+\frac{t^5}{5}+o(t^5).
$$

Dato che

$$
(\tan x)^3=x^3+3ax^5+o(x^5),\qquad
(\tan x)^5=x^5+o(x^5),
$$

otteniamo

$$
\arctan(\tan x)
=x+\left(a-\frac13\right)x^3
+\left(b-a+\frac15\right)x^5+o(x^5)=x.
$$

Per unicità dei coefficienti,

$$
a=\frac13,\qquad b=a-\frac15=\frac2{15}.
$$

## 8. Ordine di infinitesimo di $(1+x)^{1/x}-e$

Per $x\to0$, con $x\neq0$ e $1+x>0$,

$$
(1+x)^{1/x}=\exp\left(\frac{\log(1+x)}x\right).
$$

Lo sviluppo del logaritmo dà

$$
\frac{\log(1+x)}x
=\frac{x-\frac{x^2}{2}+o(x^2)}x
=1-\frac x2+o(x).
$$

Separando il termine costante nell'esponente,

$$
\begin{aligned}
(1+x)^{1/x}-e
&=e\left(e^{-x/2+o(x)}-1\right)\\
&=e\left(-\frac x2+o(x)\right)\\
&=\boxed{-\frac e2x+o(x)}.
\end{aligned}
$$

La [[Parte principale|parte principale]] è $-ex/2$ e l'ordine di infinitesimo è **$1$**.

## 9. Successioni: conta l'argomento dello sviluppo

### 9.1 Limite di $n^2\bigl(1-n\arctan(1/n)\bigr)$

Per $n\to+\infty$, l'argomento $1/n$ tende a $0$, quindi lo sviluppo in $0$ è applicabile:

$$
\arctan\frac1n=\frac1n-\frac1{3n^3}+o\left(\frac1{n^4}\right).
$$

Moltiplicando per $n$ e poi per $n^2$,

$$
\begin{aligned}
n^2\left(1-n\arctan\frac1n\right)
&=n^2\left(\frac1{3n^2}+o\left(\frac1{n^3}\right)\right)\\
&=\frac13+o\left(\frac1n\right)
\longrightarrow\boxed{\frac13}.
\end{aligned}
$$

Si può anche porre $x=1/n$ e ricondursi a un limite di funzioni per $x\to0^+$.

### 9.2 Un uso sbagliato di Taylor: $\dfrac{2\cos n-2+n^2}{n^4}$

Qui l'argomento del coseno è $n\to+\infty$. È **sbagliato** sostituire

$$
\cos n\ \overset{\text{errato}}{=}\ 1-\frac{n^2}{2}+\frac{n^4}{24}+\cdots
$$

trattandolo come uno sviluppo locale in $0$. Quel procedimento darebbe erroneamente $1/12$.

Il limite corretto si legge invece dalla limitatezza del coseno:

$$
\frac{2\cos n-2+n^2}{n^4}
=\frac1{n^2}+\frac{2\cos n-2}{n^4}
\longrightarrow\boxed0.
$$

Taylor descrive il comportamento **vicino al centro**: non basta che la formula della funzione assomigli a un esempio già svolto.

## 10. Limiti di funzioni con cancellazioni

### 10.1 $\log(1+\sin^2x)-x^2$ e un denominatore composto

Calcolare

$$
\lim_{x\to0}
\frac{\log(1+\sin^2x)-x^2}{\sin^2(\tanh^2x)-x^5}.
$$

**Denominatore.** Dalle derivate in $0$, oppure dalle definizioni,

$$
\tanh x\sim x,\qquad \tanh^2x\sim x^2,\qquad
\sin(\tanh^2x)\sim x^2.
$$

Quindi

$$
\sin^2(\tanh^2x)-x^5=x^4+o(x^4),
$$

perché $x^5=o(x^4)$. Non servono sviluppi più lunghi al denominatore.

**Numeratore.** Bisogna invece raggiungere l'ordine $4$, perché il termine quadratico viene sottratto:

$$
\sin^2x=\left(x-\frac{x^3}{6}+o(x^4)\right)^2
=x^2-\frac13x^4+o(x^4).
$$

Con $t=\sin^2x$ e $\log(1+t)=t-t^2/2+o(t^2)$,

$$
\begin{aligned}
\log(1+\sin^2x)
&=x^2-\frac13x^4-\frac12x^4+o(x^4)\\
&=x^2-\frac56x^4+o(x^4).
\end{aligned}
$$

Il rapporto è dunque

$$
\frac{-\frac56x^4+o(x^4)}{x^4+o(x^4)}
\longrightarrow\boxed{-\frac56}.
$$

### 10.2 Somma di due radici cubiche

$$
\lim_{x\to0}
\frac{\sqrt[3]{1+x}+\sqrt[3]{1-x}-2}{1-\cos x+x^4}.
$$

Il denominatore ha parte principale $x^2/2$:

$$
1-\cos x+x^4=\frac{x^2}{2}+o(x^2).
$$

Per il numeratore usiamo lo sviluppo binomiale con esponente $1/3$:

$$
(1+x)^{1/3}=1+\frac x3+\frac{\frac13(\frac13-1)}2x^2+o(x^2)
=1+\frac x3-\frac{x^2}{9}+o(x^2),
$$

$$
(1-x)^{1/3}=1-\frac x3-\frac{x^2}{9}+o(x^2).
$$

I termini costanti e lineari si cancellano, lasciando

$$
\sqrt[3]{1+x}+\sqrt[3]{1-x}-2=-\frac29x^2+o(x^2).
$$

Pertanto il limite vale

$$
\boxed{\frac{-2/9}{1/2}=-\frac49}.
$$

## 11. Altri sviluppi e parti principali

### 11.1 Parte principale di $\sqrt{n+1}-\sqrt n$

Per $n\to+\infty$ raccogliamo $\sqrt n$ per far comparire l'argomento $1/n\to0$:

$$
\begin{aligned}
\sqrt{n+1}-\sqrt n
&=\sqrt n\left(\sqrt{1+\frac1n}-1\right)\\
&=\sqrt n\left(1+\frac1{2n}+o\left(\frac1n\right)-1\right)\\
&=\boxed{\frac1{2\sqrt n}+o\left(\frac1{\sqrt n}\right)}.
\end{aligned}
$$

La parte principale è $1/(2\sqrt n)$.

### 11.2 Taylor di $\dfrac{3+x^2}{2+x}$ in $x_0=1$, ordine $3$

Poniamo $h=x-1$. Allora

$$
\begin{aligned}
f(1+h)
&=\frac{3+(1+h)^2}{3+h}\\
&=\frac13(4+2h+h^2)\left(1+\frac h3\right)^{-1}\\
&=\frac13(4+2h+h^2)
\left(1-\frac h3+\frac{h^2}{9}-\frac{h^3}{27}+o(h^3)\right).
\end{aligned}
$$

Moltiplicando e conservando i termini fino al grado $3$,

$$
\boxed{f(1+h)=\frac43+\frac29h+\frac7{27}h^2-\frac7{81}h^3+o(h^3)}.
$$

Equivalentemente, per $x\to1$,

$$
\boxed{
\frac{3+x^2}{2+x}
=\frac43+\frac29(x-1)+\frac7{27}(x-1)^2-\frac7{81}(x-1)^3
+o\bigl((x-1)^3\bigr).
}
$$

### 11.3 Parte principale di $\dfrac{n^3+5}{n^3-2}-\sqrt[n]{4}$

Per $n\to+\infty$ entrambi i termini tendono a $1$. Le velocità di avvicinamento sono però diverse:

$$
\frac{n^3+5}{n^3-2}=1+\frac7{n^3-2}=1+o\left(\frac1n\right),
$$

$$
\sqrt[n]{4}=e^{(\log4)/n}
=1+\frac{\log4}{n}+o\left(\frac1n\right).
$$

Sottraendo,

$$
\boxed{
\frac{n^3+5}{n^3-2}-\sqrt[n]{4}
=-\frac{\log4}{n}+o\left(\frac1n\right).
}
$$

La parte principale è $-(\log4)/n$: per individuarla basta sviluppare il termine che si discosta da $1$ più lentamente.

## Fonti e precisazioni

- [AM1_26_L031.pdf](/Users/michelangelogubinelli/Downloads/AM1_26_L031.pdf): definizioni e proprietà delle funzioni iperboliche, inverse, settore coseno iperbolico e anticipazioni geometriche e complesse.
- [AM1_26_L032.pdf](/Users/michelangelogubinelli/Downloads/AM1_26_L032.pdf): tangente trigonometrica, ordini di infinitesimo, limiti e sviluppi di funzioni e successioni.

Entrambi i PDF riportano **29/10/2025**, conservato in `source_date`; la data della lezione nel corso attuale, indicata dall'utente, è **29/10/2026**.

Sono stati completati i prodotti e i coefficienti lasciati da calcolare nella fonte. Le principali precisazioni sono:

- nella formula complessa di $\sinh(ix)$ il numeratore corretto è $e^{ix}-e^{-ix}$: nel PDF compare un segno $+$, incompatibile con la definizione e con il risultato $i\sin x$;
- per i passaggi sugli sviluppi infiniti e sugli argomenti complessi è stato distinto il collegamento anticipato in lezione dal teorema reale di Taylor–Peano;
- il controllo del resto nello sviluppo di $1/\cos x$ è stato esplicitato; il resto $o(x^6)$ per la tangente usa anche la sua regolarità e disparità;
- nell'esercizio con $\cos n$ il procedimento che dà $1/12$ è un esempio di errore: il limite corretto è $0$;
- la notazione delle successioni è stata uniformata a $n$, e le condizioni sui domini e sul ramo dell'inversa del coseno iperbolico sono state rese esplicite.
