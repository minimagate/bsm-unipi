---
title: Somma di sottospazi
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-13 - Somma diretta e dimensione dei sottospazi
alias:
- somma di due sottospazi
sintesi: La somma di due sottospazi è l'insieme di tutte le somme di un vettore del primo e un vettore del secondo, ed è il più piccolo sottospazio che li contiene entrambi.
---

La **somma** di due sottospazi $U$ e $W$ di uno spazio vettoriale $V$ è l'insieme dei vettori che si ottengono sommando un vettore di $U$ e uno di $W$. È ancora un [[Sottospazio vettoriale|sottospazio]], ed è il più piccolo che contiene sia $U$ sia $W$.

## Definizione

$$
U+W=\{u+w\mid u\in U,\ w\in W\}.
$$

Vale $U+W=\operatorname{span}(U\cup W)$, il [[Sottospazio generato|sottospazio generato]] dall'unione.

## Intuizione

L'unione $U\cup W$ in generale non è un sottospazio: può non essere chiusa rispetto alla somma. Per ottenere un sottospazio basta "aggiungere" tutte le somme possibili, ed è proprio $U+W$.

## Esempi

- In $\mathbb{R}^3$ la somma di due rette distinte per l'origine è il piano che le contiene.
- Se $U=\operatorname{span}\{e_1\}$ e $W=\operatorname{span}\{e_2\}$ in $\mathbb{R}^3$, allora $U+W=\{(a,b,0)\}$.
- Due piani distinti per l'origine in $\mathbb{R}^3$ hanno somma $\mathbb{R}^3$.
- Se $W\subseteq U$, allora $U+W=U$.

## Come si dimostra

Si verificano chiusura per somma e per prodotto per scalare: $(u_1+w_1)+(u_2+w_2)=(u_1+u_2)+(w_1+w_2)$, e così via. Per la minimalità: ogni sottospazio $Z\supseteq U\cup W$ contiene tutte le somme $u+w$. Vedi [[2026-10-13 - Somma diretta e dimensione dei sottospazi#4. Somma di due sottospazi|la somma di due sottospazi]].

## Vedi anche

- [[Somma diretta]]
- [[Formula di Grassmann]]
- [[Sottospazio generato]]
- [[Operazioni tra insiemi]]
