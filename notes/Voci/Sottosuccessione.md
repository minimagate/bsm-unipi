---
title: Sottosuccessione
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-22 - Sottosuccessioni, limiti che non esistono e razionalizzazioni
alias:
- sottosuccessioni
sintesi: Una successione ottenuta scegliendo solo alcuni termini di un'altra, nel loro ordine originale.
---

Una **sottosuccessione** di $(a_n)$ si ottiene tenendo solo alcuni termini della successione, senza cambiarne l'ordine.

## Definizione

Sia $(n_k)_{k\in\mathbb N}$ una successione strettamente crescente di numeri naturali. La sottosuccessione di $(a_n)$ associata a $(n_k)$ è

$$
k\longmapsto a_{n_k}.
$$

Si può anche richiedere soltanto che $n_k\to+\infty$.

## Intuizione

È come cancellare alcuni termini e leggere quelli rimasti: $a_{2k}$ prende i termini di indice pari, $a_{2k+1}$ quelli di indice dispari, $a_{k^2}$ quelli di indice quadrato perfetto.

Il fatto chiave è che se $a_n\to\ell\in\overline{\mathbb R}$, **ogni** sottosuccessione tende allo stesso $\ell$. Quindi, se due sottosuccessioni hanno limiti diversi, la successione di partenza **non ha limite**: è il criterio standard per dimostrare che un limite non esiste.

## Esempi

- Per $a_n=(-1)^n$ si ha $a_{2k}=1\to1$ e $a_{2k+1}=-1\to-1$, quindi $(a_n)$ non ha limite.
- Per $a_n=n^3+(-1)^nn^5$ si ha $a_{2k}\to+\infty$ e $a_{2k+1}\to-\infty$.
- Per $a_n=\sin\left(\frac\pi7n\right)$, $a_{14k}=0$ mentre $a_{14k+1}=\sin\frac\pi7\neq0$.

## Come si dimostra

Si usa $n_k\geq k$, che si prova per induzione: se $a_n$ soddisfa una proprietà per $n\geq n_0$, la sottosuccessione la soddisfa per $k\geq n_0$. Il dettaglio è nella [[2026-10-22 - Sottosuccessioni, limiti che non esistono e razionalizzazioni#1.1 Le sottosuccessioni ereditano il limite|lezione del 22 ottobre]].

## Vedi anche

- [[Successione]]
- [[Limite di una successione]]
- [[Proprietà definitivamente vera]]
- [[Limite di una funzione]]
