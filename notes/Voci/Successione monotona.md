---
title: Successione monotona
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti
alias:
- teorema sulle successioni monotone
- successioni monotone
sintesi: Una successione monotona ha sempre limite e converge all'estremo superiore dei suoi valori se è crescente e all'estremo inferiore se è decrescente.
---
Una **successione monotona** non può oscillare senza limite: o converge a un numero reale oppure diverge nel verso della monotonia.

## Enunciato

Se $(a_n)$ è debolmente crescente (cioè $a_{n+1}\ge a_n$ per ogni $n$), allora

$$
a_n\to\sup\{a_n : n\in\mathbb{N}\}\in\mathbb{R}\cup\{+\infty\}.
$$

Se è debolmente decrescente, $a_n\to\inf\{a_n\}\in\mathbb{R}\cup\{-\infty\}$.

**Corollario.** Una successione debolmente crescente e limitata superiormente converge (analogamente per decrescente e limitata inferiormente).

## Intuizione

Una successione che sale e non può salire all'infinito si accumula contro il suo tetto, che è il supremo. Se è *strettamente* crescente e limitata, il limite $\ell$ si raggiunge da sinistra: $a_n\to\ell^-$.

## Esempi

- $e_n=\left(1+\frac1n\right)^n$ è crescente e limitata da $3$: converge al [[Numero di Nepero|numero di Nepero]].
- $a_n=n$ è crescente e illimitata: $\sup=+\infty$ e $a_n\to+\infty$.

## Come si dimostra

Si usa la caratterizzazione dell'[[Estremo superiore|estremo superiore]]: per ogni $\varepsilon$ esiste $n_0$ con $a_{n_0}\ge\ell-\varepsilon$ e per monotonia $a_n\ge\ell-\varepsilon$ per ogni $n\ge n_0$; l'altra disuguaglianza vale perché $\ell$ è un maggiorante. Si veda [[2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti#3. Teorema sulle successioni monotone|Teorema sulle successioni monotone]].

## Vedi anche

- [[Estremo superiore]]
- [[Numero di Nepero]]
- [[Limite di una successione]]
- [[Funzione monotona]]
