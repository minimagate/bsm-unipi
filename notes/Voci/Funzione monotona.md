---
title: Funzione monotona
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-09-30 - Simmetrie, monotonia e grafici delle funzioni elementari
alias:
- monotonia
- funzione crescente
- funzione decrescente
- funzione strettamente crescente
- funzione strettamente decrescente
sintesi: Una funzione è monotona se conserva o inverte sempre l'ordine, in senso debole o stretto.
---
Una funzione è **monotona** se, al crescere dell'argomento, il valore non cambia mai "direzione". Si distingue il caso debole da quello stretto.

## Definizione

Per $f\colon\mathbb{R}\to\mathbb{R}$ e ogni $x<y$:

| Tipo | Condizione |
|---|---|
| debolmente crescente | $f(x)\le f(y)$ |
| strettamente crescente | $f(x)<f(y)$ |
| debolmente decrescente | $f(x)\ge f(y)$ |
| strettamente decrescente | $f(x)>f(y)$ |

È monotona se rientra in uno dei quattro casi. Conviene sempre specificare quale.

## Intuizione

Una funzione strettamente crescente (o decrescente) è **iniettiva**: due punti distinti hanno immagini distinte. Una funzione solo debolmente monotona può invece essere costante su un intervallo e non essere iniettiva.

Inoltre se $f$ è strettamente crescente vale $f(u)<f(v)\iff u<v$ (conserva il verso delle disuguaglianze); se è strettamente decrescente il verso si inverte.

## Esempi

- $x^3$ è strettamente crescente su $\mathbb{R}$.
- $x^2$ è strettamente crescente su $[0,+\infty)$ e strettamente decrescente su $(-\infty,0]$.
- $\max\{x,0\}$ è debolmente crescente ma non strettamente.

## Vedi anche

- [[Funzione biettiva]]
- [[Funzione inversa]]
- [[Successione monotona]]
- [[Funzione pari e dispari]]
