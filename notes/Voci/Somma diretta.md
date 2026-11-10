---
title: Somma diretta
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-13 - Somma diretta e dimensione dei sottospazi
alias:
- somme dirette
- sottospazio supplementare
- sottospazi supplementari
- supplementare
sintesi: Una somma di due sottospazi è diretta quando la loro intersezione è nulla, e in tal caso ogni vettore della somma si scrive in modo unico.
---

La somma $U+W$ di due sottospazi è una **somma diretta**, e si scrive $U\oplus W$, quando $U\cap W=\{0\}$. In tal caso ogni vettore della somma si scrive in un solo modo come $u+w$. Se $U\oplus W=V$, ciascuno dei due si dice **supplementare** dell'altro.

## Definizione

$$
U\oplus W
\iff
U\cap W=\{0\}.
$$

Equivalentemente, per ogni $z\in U+W$ esiste un'unica coppia $(u,w)\in U\times W$ con $z=u+w$. Se $U\oplus W$ è somma diretta, allora

$$
\dim(U\oplus W)=\dim U+\dim W.
$$

## Intuizione

Le due parti non si sovrappongono: non c'è nessun vettore (a parte lo zero) che "conta due volte". Per questo la decomposizione è unica e le dimensioni si sommano. Se un insieme linearmente indipendente si divide in due blocchi, i due span sono in somma diretta.

## Esempi

- Due rette distinte per l'origine in $\mathbb{R}^2$: $\mathbb{R}^2=U\oplus W$.
- Un piano e una retta non contenuta nel piano in $\mathbb{R}^3$: $\mathbb{R}^3=U\oplus W$.
- Due piani in $\mathbb{R}^3$ non possono essere in somma diretta (si intersecano in una retta).
- $M_n(\mathbb{R})=\mathcal S_n\oplus\mathcal A_n$: ogni matrice è somma di una parte simmetrica e una antisimmetrica (vedi [[Matrice trasposta]]).

## Come si dimostra

Se $u+w=u'+w'$ allora $u-u'=w'-w$ sta in $U\cap W=\{0\}$, quindi le due decomposizioni coincidono; viceversa un vettore non nullo $v\in U\cap W$ ha le due scritture $v+0$ e $0+v$. Vedi [[2026-10-13 - Somma diretta e dimensione dei sottospazi#6. Caratterizzazione della somma diretta tramite l’unicità|la caratterizzazione tramite l'unicità]].

## Vedi anche

- [[Somma di sottospazi]]
- [[Formula di Grassmann]]
- [[Dimensione di uno spazio vettoriale]]
