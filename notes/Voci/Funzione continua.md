---
title: Funzione continua
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-12 - Limiti di funzioni, continuità e limiti notevoli
alias:
- continuità
- funzioni continue
sintesi: Una funzione è continua in un punto quando il suo limite lì coincide con il valore che assume, cioè il grafico non ha salti.
---

Una **funzione continua** in un punto è una funzione il cui limite in quel punto coincide con il suo valore. In modo informale, il grafico si può disegnare senza staccare la penna dal foglio.

## Definizione

Sia $f:D\to\mathbb{R}$ e $x_0\in D$. La funzione $f$ è **continua in $x_0$** se

$$
\lim_{x\to x_0}f(x)=f(x_0),
$$

ossia se $\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D\cap[x_0-\delta,x_0+\delta]\ |f(x)-f(x_0)|\leq\varepsilon$. Si dice **continua in $D$** se lo è in ogni punto di $D$. Se $x_0$ è isolato in $D$ la continuità vale per convenzione.

## Intuizione

Piccole variazioni di $x$ producono piccole variazioni di $f(x)$. Il vantaggio pratico è che per le funzioni continue il limite si calcola semplicemente sostituendo: $\lim_{x\to x_0}f(x)=f(x_0)$.

Le funzioni ottenute dalle elementari con operazioni algebriche e composizioni sono continue dove non hanno "problemi burocratici" (denominatori nulli, logaritmi di numeri non positivi).

## Esempi

- $f(x)=2^x$ è continua su tutto $\mathbb{R}$.
- La parte intera $\lfloor x\rfloor$ non è continua negli interi: fa un salto.
- Se $f$ è continua in $x_0$ e $g$ è continua in $f(x_0)$, allora $g(f(x))$ è continua in $x_0$.

## Come si dimostra

La continuità di $2^x$ e quella della composizione sono dimostrate nella [[2026-10-12 - Limiti di funzioni, continuità e limiti notevoli#7. Due dimostrazioni di continuità|lezione del 12 ottobre]], con la tecnica "$\varepsilon$ e $\delta$ a catena".

## Vedi anche

- [[Limite di una funzione]]
- [[Derivata]]
- [[Composizione di funzioni]]
