---
title: Limite di una successione
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-06 - Successioni, limiti e teoremi di confronto
alias:
- limite
- successione convergente
- successione divergente
- limiti di successioni
sintesi: Il limite di una successione descrive a quale valore, finito o infinito, i termini si avvicinano da un certo indice in poi.
---
Il **limite** di una successione $(a_n)$ descrive il comportamento di $a_n$ per $n\to+\infty$. Ci sono quattro possibilità: limite $\ell\in\mathbb{R}$ (successione *convergente*), $+\infty$ o $-\infty$ (*divergente*), oppure il limite non esiste.

## Definizione

Con la nozione di [[Proprietà definitivamente vera|"definitivamente"]]:

$$
a_n\to+\infty\iff\forall M\in\mathbb{R},\ a_n\ge M\ \text{definitivamente},
$$

$$
a_n\to-\infty\iff\forall M\in\mathbb{R},\ a_n\le M\ \text{definitivamente},
$$

$$
a_n\to\ell\in\mathbb{R}\iff\forall\varepsilon>0,\ |a_n-\ell|\le\varepsilon\ \text{definitivamente}.
$$

Esplicitando: $\forall\varepsilon>0\ \exists n_0\ \forall n\ge n_0:\ |a_n-\ell|\le\varepsilon$. Si scrive $a_n\to\ell^+$ (o $\ell^-$) se inoltre $a_n>\ell$ (o $a_n<\ell$) definitivamente.

## Intuizione

Il numero $\varepsilon$ è una tolleranza arbitrariamente piccola: da un certo indice in poi *tutti* i termini restano entro $\varepsilon$ da $\ell$. Attenzione alle false intuizioni: divergere a $+\infty$ non implica crescere, e convergere a $0$ non implica arrivare da un solo lato ($\frac{(-1)^n}{n}\to0$). Ogni successione convergente è limitata, ma non viceversa.

## Esempi

- $n^2\to+\infty$, $\frac1n\to0^+$.
- $(-1)^n$ non ha limite: $1$ e $-1$ compaiono infinite volte.
- $0,1,0,1,\dots$ è limitata ma non converge.

## Come si dimostra

Le dimostrazioni dei limiti elementari e le proprietà (limitatezza, permanenza del segno) sono nella lezione: [[2026-10-06 - Successioni, limiti e teoremi di confronto#3. Limite di una successione|Limite di una successione]].

## Vedi anche

- [[Successione]]
- [[Permanenza del segno]]
- [[Teorema dei carabinieri]]
- [[Teoremi algebrici sui limiti]]
