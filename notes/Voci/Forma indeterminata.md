---
title: Forma indeterminata
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti
alias:
- forme indeterminate
sintesi: Una forma indeterminata è un caso in cui i limiti dei singoli pezzi non bastano a determinare il limite dell'operazione.
---
Una **forma indeterminata** è una combinazione di limiti per cui i teoremi algebrici non permettono di concludere: il risultato dipende dalle successioni concrete.

## Definizione

Le forme indeterminate sono i "casi problematici" dell'algebra dei limiti in $\overline{\mathbb{R}}$:

$$
+\infty-\infty,\qquad 0\cdot(\pm\infty),\qquad \frac{\pm\infty}{\pm\infty},\qquad \frac00.
$$

(Il caso $\frac70$ si comporta in modo diverso: è accettabile se si conosce il segno del denominatore.)

## Intuizione

**Attenzione:** "forma indeterminata" non significa "il limite non esiste", ma "non è deducibile solo dai limiti dei due pezzi". Con $a_n=2n$ e $b_n\to+\infty$ la differenza $a_n-b_n$ può fare qualsiasi cosa:

| $b_n$ | $a_n-b_n$ | limite |
|---|---|---|
| $n$ | $n$ | $+\infty$ |
| $3n$ | $-n$ | $-\infty$ |
| $2n-42+\frac1n$ | $42-\frac1n$ | $42$ |
| $2n+(-1)^n$ | $-(-1)^n$ | non esiste |

## Esempi

- $\frac{n^2+3n+1}{2n^2-7}$ è del tipo $\frac{\infty}{\infty}$ ma si risolve raccogliendo "chi comanda": il limite è $\frac12$.
- $n^2-n\cos n$ è del tipo $+\infty-\infty$ ma si risolve raccogliendo $n$: $n(n-\cos n)\to+\infty$.

## Vedi anche

- [[Retta reale estesa]]
- [[Teoremi algebrici sui limiti]]
- [[Limite di una successione]]
- [[Gerarchia degli infiniti]]
