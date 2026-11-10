---
title: Disuguaglianza di Bernoulli
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-09-24 - Funzioni, composizione e principio d’induzione
alias:
- Bernoulli
sintesi: Per ogni naturale n e ogni x maggiore o uguale a meno uno, la potenza n-esima di uno più x è almeno uno più n per x.
---
La **disuguaglianza di Bernoulli** confronta una potenza con la sua approssimazione lineare.

## Enunciato

Per ogni $n\in\mathbb{N}$ e per ogni $x\ge -1$:

$$
(1+x)^n\ge 1+nx.
$$

## Intuizione

Il grafico di $(1+x)^n$ sta sopra la sua retta tangente in $x=0$, cioè $y=1+nx$. È uno strumento molto usato in Analisi per ottenere stime dal basso: per esempio dà $a^n\to+\infty$ se $a>1$ e controlla $e_n=(1+1/n)^n$.

Nota bene: l'ipotesi $x\ge-1$ equivale a $1+x\ge0$ e serve per poter moltiplicare le disuguaglianze nel passo induttivo senza cambiarne il verso; per $x<-1$ la disuguaglianza può essere falsa.

## Esempi

- Con $x=1$: $2^n\ge 1+n$, quindi $2^n\to+\infty$.
- Con $x=\tfrac1n$: $\left(1+\tfrac1n\right)^n\ge 2$.

## Come si dimostra

Per [[Principio di induzione|induzione]] su $n$, fissando $x\ge-1$. Il passo induttivo è
$(1+x)^{n+1}=(1+x)^n(1+x)\ge(1+nx)(1+x)=1+(n+1)x+nx^2\ge1+(n+1)x$:
la prima disuguaglianza usa $1+x\ge0$ (qui serve l'ipotesi $x\ge-1$). I dettagli sono nella lezione: [[2026-09-24 - Funzioni, composizione e principio d’induzione#12. Disuguaglianza di Bernoulli|Disuguaglianza di Bernoulli]].

## Vedi anche

- [[Principio di induzione]]
- [[Numero di Nepero]]
- [[Limite di una successione]]
- [[Teorema dei carabinieri]]
