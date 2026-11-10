---
title: Formula di Grassmann
type: voce
categoria: teorema
corsi:
- Geometria 1
introdotta_in: 2026-10-13 - Somma diretta e dimensione dei sottospazi
alias:
- formula della dimensione della somma
- formula di Grassmann
sintesi: Per due sottospazi, la dimensione della somma è la somma delle dimensioni meno la dimensione dell'intersezione.
---

La **formula di Grassmann** lega le dimensioni di due sottospazi, della loro somma e della loro intersezione.

## Enunciato

Siano $U$ e $W$ sottospazi di uno spazio vettoriale $V$ di dimensione finita. Allora

$$
\dim(U+W)=\dim U+\dim W-\dim(U\cap W).
$$

In particolare, se la somma è [[Somma diretta|diretta]], $U\cap W=\{0\}$ e $\dim(U\oplus W)=\dim U+\dim W$.

## Intuizione

Sommando $\dim U+\dim W$ si contano due volte i vettori che stanno in entrambi i sottospazi, cioè quelli di $U\cap W$: la formula corregge questo doppio conteggio. Più l'intersezione è grande, più la somma è piccola.

## Esempi

- Due piani distinti per l'origine in $\mathbb{R}^3$: $\dim(U+W)=2+2-1=3$, quindi $U+W=\mathbb{R}^3$, ma la somma non è diretta.
- Un piano e una retta che lo incontra solo nell'origine: $2+1-0=3$ e $\mathbb{R}^3=U\oplus W$.
- Due rette distinte in $\mathbb{R}^2$: $1+1-0=2$.

## Come si dimostra

Si prende una base $\{v_1,\dots,v_q\}$ di $U\cap W$ e la si estende a una base di $U$ e a una base di $W$; l'insieme formato dai $v_i$ e dai vettori aggiunti nelle due basi è una base di $U+W$ ed ha $n+p-q$ elementi. Vedi [[2026-10-13 - Somma diretta e dimensione dei sottospazi#10. Dimostrazione della formula generale|la dimostrazione nella lezione del 13 ottobre]].

## Vedi anche

- [[Somma di sottospazi]]
- [[Somma diretta]]
- [[Dimensione di uno spazio vettoriale]]
