---
title: Funzioni iperboliche
type: voce
categoria: oggetto
corsi:
- Analisi 1
introdotta_in: 2026-10-30 - Funzioni iperboliche ed esercizi sugli sviluppi di Taylor
alias:
- seno iperbolico
- coseno iperbolico
- settore iperbolico
sintesi: Funzioni costruite con l'esponenziale che per l'iperbole giocano lo stesso ruolo che seno e coseno hanno per la circonferenza.
---

Le **funzioni iperboliche** sono il seno iperbolico, il coseno iperbolico e la tangente iperbolica: combinazioni di $e^x$ e $e^{-x}$ che hanno proprietà molto simili a quelle trigonometriche.

## Definizione

Per ogni $x\in\mathbb R$

$$
\sinh x=\frac{e^x-e^{-x}}2,\qquad \cosh x=\frac{e^x+e^{-x}}2,\qquad \tanh x=\frac{\sinh x}{\cosh x}.
$$

Valgono $\cosh^2x-\sinh^2x=1$ e $\cosh x+\sinh x=e^x$. Il seno e la tangente iperbolici sono dispari, il coseno iperbolico è pari. Le derivate sono $(\sinh x)'=\cosh x$, $(\cosh x)'=\sinh x$, $(\tanh x)'=\frac1{\cosh^2x}$.

## Intuizione

Il punto $(\cosh\alpha,\sinh\alpha)$ sta sull'iperbole $x^2-y^2=1$, come $(\cos\alpha,\sin\alpha)$ sta sulla circonferenza $x^2+y^2=1$. Per questo i segni delle identità sono quasi gli stessi, con una differenza al posto della somma. Le inverse (i **settori iperbolici**) si chiamano così perché il parametro è legato a un'area di settore.

Il coseno iperbolico ha minimo $1$ in $0$; la tangente iperbolica tende a $\pm1$ agli infiniti.

## Esempi

- Per $x=\log2$: $\cosh x=\frac54$, $\sinh x=\frac34$, e infatti $\frac{25}{16}-\frac9{16}=1$.
- Lo sviluppo di Taylor è $\sinh x=x+\frac{x^3}{3!}+\frac{x^5}{5!}+o(x^5)$, tutto con segni positivi.
- L'inverso del coseno iperbolico, ristretto a $[0,+\infty)$, è $\log\bigl(y+\sqrt{y^2-1}\bigr)$ per $y\ge1$.

## Come si dimostra

Le identità si ricavano direttamente dalle definizioni esponenziali, come nella [[2026-10-30 - Funzioni iperboliche ed esercizi sugli sviluppi di Taylor#2. Identità fondamentali e duplicazione|lezione del 30 ottobre]]; per gli sviluppi si veda anche lo [[Sviluppo di Taylor|sviluppo di Taylor]].

## Vedi anche

- [[Funzioni trigonometriche]]
- [[Sviluppo di Taylor]]
- [[Funzione inversa]]
- [[Numero di Nepero]]
