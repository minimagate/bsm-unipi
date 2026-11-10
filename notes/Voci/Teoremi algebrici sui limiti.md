---
title: Teoremi algebrici sui limiti
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti
alias:
- algebra dei limiti
- teoremi algebrici
sintesi: Il limite di una somma, un prodotto o un quoziente è la somma, il prodotto o il quoziente dei limiti, salvo i casi indeterminati.
---
I **teoremi algebrici sui limiti** (o *algebra dei limiti*) dicono che il limite commuta con le quattro operazioni.

## Enunciato

Se $a_n\to\ell_1\in\overline{\mathbb{R}}$ e $b_n\to\ell_2\in\overline{\mathbb{R}}$, allora

$$
a_n\pm b_n\to\ell_1\pm\ell_2,\qquad a_nb_n\to\ell_1\ell_2,\qquad \frac{a_n}{b_n}\to\frac{\ell_1}{\ell_2},
$$

**tranne nei casi di [[Forma indeterminata|forma indeterminata]]**, con le operazioni intese nella [[Retta reale estesa|retta reale estesa]].

Caso utile: se $a_n\to+\infty$ e $(b_n)$ è limitata inferiormente, allora $a_n+b_n\to+\infty$.

## Intuizione

Se i due pezzi si stabilizzano, anche la somma e il prodotto si stabilizzano. La parte tecnica è controllare gli errori: nella somma, se ogni pezzo sbaglia al più $\frac\varepsilon2$ l'errore totale è al più $\varepsilon$.

## Esempi

- $\frac{n^2+3n+1}{2n^2-7}=\frac{1+3/n+1/n^2}{2-7/n^2}\to\frac12$ ("chi comanda si raccoglie").
- $\frac{n^2+\arctan n}{n+\arctan(n^2)}\to+\infty$.

## Come si dimostra

Per la somma finita si usa la disuguaglianza triangolare $|(a_n+b_n)-(\ell_1+\ell_2)|\le|a_n-\ell_1|+|b_n-\ell_2|$; per il prodotto si aggiunge e toglie il termine misto $a_n\ell_2$. Si veda [[2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti#6.2 Somma nel caso finito|Somma nel caso finito]].

## Vedi anche

- [[Forma indeterminata]]
- [[Retta reale estesa]]
- [[Limite di una successione]]
- [[Teorema dei carabinieri]]
