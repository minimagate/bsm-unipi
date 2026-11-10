---
title: Retta reale estesa
type: voce
categoria: oggetto
corsi:
- Analisi 1
introdotta_in: 2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti
alias:
- reali estesi
- R esteso
sintesi: La retta reale estesa si ottiene aggiungendo ai numeri reali i due simboli più infinito e meno infinito, con cui si può operare tranne che nei casi indeterminati.
---
La **retta reale estesa** è l'insieme $\overline{\mathbb{R}}=\mathbb{R}\cup\{+\infty,-\infty\}$.

## Definizione

Si aggiungono a $\mathbb{R}$ i due simboli $\pm\infty$, con l'ordine naturale $-\infty<x<+\infty$ per ogni $x\in\mathbb{R}$. Le operazioni si estendono in modo ragionevole:

$$
7+\infty=+\infty,\quad 5\cdot(+\infty)=+\infty,\quad -7\cdot(-\infty)=+\infty,\quad \frac{18}{+\infty}=0,\quad \frac{7}{0^+}=+\infty,\ \frac7{0^-}=-\infty.
$$

Non hanno valore definito i casi

$$
+\infty-\infty,\quad 0\cdot(\pm\infty),\quad \frac{\pm\infty}{\pm\infty},\quad \frac00,\quad \frac70
$$

(le [[Forma indeterminata|forme indeterminate]], più $\frac70$ senza segno).

## Intuizione

Scrivere $a_n\to\ell\in\overline{\mathbb{R}}$ vuol dire che il limite *esiste*, finito o infinito; si esclude solo il caso "il limite non esiste". Inoltre $\sup A\in\overline{\mathbb{R}}$ per ogni $A\ne\varnothing$.

Tutto questo è solo una comodità di notazione: $+\infty$ e $-\infty$ non sono numeri reali e non obbediscono a tutte le regole di calcolo dei numeri, per cui i casi problematici vanno trattati a parte.

## Esempi

- $2n+(+\infty)$: formalmente $+\infty$.
- $2n-n$ ha la forma $+\infty-\infty$ ma vale $n\to+\infty$; con $2n-(2n-42)$ si ottiene invece $42$.

## Vedi anche

- [[Forma indeterminata]]
- [[Teoremi algebrici sui limiti]]
- [[Limite di una successione]]
- [[Estremo superiore]]
