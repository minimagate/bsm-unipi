---
title: Numero di Nepero
type: voce
categoria: oggetto
corsi:
- Analisi 1
introdotta_in: 2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti
alias:
- numero e
- e
- costante di Nepero
sintesi: Il numero di Nepero e è il limite della successione uno più uno su n elevato a n e vale circa 2,718.
---
Il **numero di Nepero** $e$ è il limite della successione $e_n=\left(1+\frac1n\right)^n$. Vale circa $2{,}71828\dots$ ed è compreso strettamente tra $2$ e $3$.

## Definizione

$$
e=\lim_{n\to+\infty}\left(1+\frac1n\right)^n.
$$

L'esistenza del limite segue dal teorema sulle [[Successione monotona|successioni monotone]]: $(e_n)$ è crescente e limitata superiormente.

## Intuizione

Al crescere di $n$ la base $1+\frac1n$ si avvicina a $1$ (e tenderebbe a far rimpicciolire la potenza), mentre l'esponente $n$ cresce (e tenderebbe a farla ingrandire): le due spinte si bilanciano e il risultato si stabilizza. Quel valore di equilibrio è proprio $e$; lo si ritrova anche nei rapporti di successioni come $\frac{n^n}{n!}$, il cui rapporto tra termini consecutivi tende a $e$.

## Esempi

- $e_1=2$, $e_2=\frac94$, e $e_n$ cresce verso $e$.
- $\left(\frac{n}{n+1}\right)^n=\frac{1}{e_n}\to\frac1e$.

## Come si dimostra

Tre fatti, tutti basati sulla [[Disuguaglianza di Bernoulli|disuguaglianza di Bernoulli]] e sul binomio di Newton: $e_n\ge2$; $(e_n)$ è crescente (si riconduce a Bernoulli con $x=-\frac1{n^2}$); $e_n<3$ (si maggiora il binomio con $1+1+\frac12+\frac14+\cdots$). Dettagli in [[2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti#4. Il numero di Nepero $e$|Il numero di Nepero]].

## Vedi anche

- [[Successione monotona]]
- [[Disuguaglianza di Bernoulli]]
- [[Binomio di Newton]]
- [[Gerarchia degli infiniti]]
