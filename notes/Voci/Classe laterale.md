---
title: Classe laterale
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-11-09 - Classi laterali e teorema di Lagrange
alias:
- classi laterali
- classe laterale sinistra
- laterale
sintesi: L'insieme degli elementi di un gruppo ottenuti moltiplicando un elemento fissato per tutti gli elementi di un sottogruppo.
---

Una **classe laterale** di un sottogruppo $H$ in un gruppo $G$ è una "copia traslata" di $H$. Generalizza le classi di congruenza modulo $n$.

## Definizione

Sia $H\leq G$. Le relazioni $x\sim_H y\iff y^{-1}x\in H$ (sinistra) e $x\approx_H y\iff xy^{-1}\in H$ (destra) sono [[Relazione di equivalenza|relazioni di equivalenza]]. Le loro classi sono:

$$
xH=\{xh\mid h\in H\}\ \ (\text{classe laterale sinistra}),\qquad Hx=\{hx\mid h\in H\}\ \ (\text{destra}).
$$

Le classi laterali sinistre formano una partizione di $G$; la funzione $H\to xH$, $h\mapsto xh$ è biettiva, quindi $|xH|=|H|$. In un gruppo abeliano $xH=Hx$.

## Intuizione

Le classi laterali tagliano il gruppo in "fette" tutte della stessa dimensione di $H$. Nel gruppo additivo $\mathbb Z$ con $H=n\mathbb Z$ la classe di $a$ è $a+n\mathbb Z$, cioè la [[Classe di congruenza|classe di congruenza]] di $a$ modulo $n$.

## Esempi

- In $\mathbb Z/6\mathbb Z$ con $H=\{\overline0,\overline3\}$ le classi sono $\{\overline0,\overline3\}$, $\{\overline1,\overline4\}$, $\{\overline2,\overline5\}$.
- In $S_3$ con $H=\{e,(1\ 2)\}$ e $\sigma=(1\ 2\ 3)$: $\sigma H=\{\sigma,(1\ 3)\}$ ma $H\sigma=\{\sigma,(2\ 3)\}$, quindi sinistre e destre differiscono.

## Come si dimostra

Che $\sim_H$ sia di equivalenza segue da $e\in H$, dalla chiusura per inverso e dalla chiusura per prodotto; si veda la [[2026-11-09 - Classi laterali e teorema di Lagrange#3. Classi laterali sinistre|sezione sulle classi laterali sinistre]] della lezione del 9 novembre.

## Vedi anche

- [[Sottogruppo]]
- [[Teorema di Lagrange]]
- [[Indice di un sottogruppo]]
- [[Sottogruppo normale]]
