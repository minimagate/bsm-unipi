---
title: Simboli di Landau
type: voce
categoria: notazione
corsi:
- Analisi 1
introdotta_in: 2026-10-26 - Simboli di Landau, o piccolo e sviluppi dei limiti notevoli
alias:
- o piccolo
- O grande
- Landau
sintesi: Una notazione per confrontare quanto in fretta due funzioni tendono a zero o all'infinito, che permette di scrivere gli errori di approssimazione senza calcolarli.
---

I **simboli di Landau** ($o$ piccolo e $O$ grande) servono a confrontare la "velocità" di due funzioni vicino a un punto, e a nascondere in un unico simbolo tutto ciò che è trascurabile.

## Definizione

Siano $f,g:D\to\mathbb R$ e $x_0$ un punto in cui ha senso fare il limite (anche $\pm\infty$ o $x_0^\pm$). Si scrive $f(x)=o\bigl(g(x)\bigr)$ per $x\to x_0$ se esiste $\omega:D\to\mathbb R$ con

$$
f(x)=g(x)\,\omega(x)\qquad\text{e}\qquad\lim_{x\to x_0}\omega(x)=0.
$$

Se $g\neq0$ vicino a $x_0$ equivale a $\lim_{x\to x_0}\frac{f(x)}{g(x)}=0$. Si scrive $f=O(g)$ se $\omega$ è solo **limitata** in un intorno di $x_0$.

## Intuizione

"$f=o(g)$" significa che $f$ è molto più piccola di $g$ nel limite: se $g\to0$, $f$ tende a $0$ più in fretta. Per $x\to0$ vince la potenza più alta: $x^a=o(x^b)$ se e solo se $a>b$.

Le regole di calcolo sono comode: $o(g)\pm o(g)=o(g)$, $\lambda\,o(g)=o(g)$, $o(g)\cdot o(g)=o(g^2)$, $o(o(g))=o(g)$. Invece il quoziente $\frac{o(g)}{o(g)}$ non dice niente di preciso. I limiti notevoli si riscrivono così: $\sin x=x+o(x)$, $\cos x=1-\frac{x^2}2+o(x^2)$.

## Esempi

- $x^3=o(x)$ per $x\to0$, perché $\frac{x^3}{x}=x^2\to0$.
- $\sin(x^2)\arctan x=o(x^2)$ per $x\to0$.
- $\sin(2x)\arctan^2x=o(x^2)$ ma non $o(x^3)$: dividendo per $x^3$ il limite vale $2$.

## Come si dimostra

Le regole di calcolo si dimostrano scrivendo i resti come $g\,\omega$ con $\omega\to0$ e moltiplicando o sommando le $\omega$ (vedi la [[2026-10-26 - Simboli di Landau, o piccolo e sviluppi dei limiti notevoli#2. Proprietà dell'o piccolo|lezione del 26 ottobre]]).

## Vedi anche

- [[Equivalenza asintotica]]
- [[Limiti notevoli]]
- [[Sviluppo di Taylor]]
- [[Parte principale]]
