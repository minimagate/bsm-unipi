---
title: Sottogruppo normale
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-11-09 - Classi laterali e teorema di Lagrange
alias:
- sottogruppi normali
- normalità
sintesi: Un sottogruppo le cui classi laterali sinistre e destre coincidono.
---

Un **sottogruppo normale** è un sottogruppo per cui non c'è differenza tra classi laterali sinistre e destre. Sono i sottogruppi con cui si possono costruire i gruppi quoziente.

## Definizione

Sia $H\leq G$. Si dice che $H$ è normale in $G$, e si scrive $H\trianglelefteq G$, se per ogni $g\in G$ vale

$$
gHg^{-1}=H,
$$

o, equivalentemente, $gH=Hg$ per ogni $g\in G$. Basta verificare l'inclusione $gHg^{-1}\subseteq H$ per ogni $g$ (applicandola a $g^{-1}$ si ottiene l'altra).

Attenzione: $gH=Hg$ è un'uguaglianza di insiemi, non vuol dire che $g$ commuti con ogni elemento di $H$.

## Intuizione

Coniugare $H$ con un qualsiasi $g$ lo lascia al suo posto. In un gruppo abeliano questo succede sempre.

## Esempi

- Ogni sottogruppo di un gruppo abeliano è normale.
- Il [[Centro di un gruppo|centro]] $Z(G)$ è normale in $G$: se $x\in Z(G)$ allora $gxg^{-1}=x$.
- Il [[Nucleo|nucleo]] di un [[Omomorfismo|omomorfismo]] è normale: se $f(k)=e$ allora $f(gkg^{-1})=f(g)f(g)^{-1}=e$.
- In $S_3$ il sottogruppo $\{e,(1\ 2)\}$ non è normale, perché $\sigma H\neq H\sigma$ per $\sigma=(1\ 2\ 3)$.

## Come si dimostra

Si veda la [[2026-11-09 - Classi laterali e teorema di Lagrange#11. Quando coincidono le classi sinistre e destre?|sezione sulle classi sinistre e destre]] della lezione del 9 novembre per le condizioni equivalenti.

## Vedi anche

- [[Sottogruppo]]
- [[Classe laterale]]
- [[Centro di un gruppo]]
- [[Nucleo]]
