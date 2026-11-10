---
title: Campo
type: voce
categoria: oggetto
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-28 - Assiomi dei reali e proprietà di completezza
alias:
- campi
- assiomi di campo
sintesi: Un campo è un insieme con somma e prodotto che godono delle usuali proprietà algebriche e in cui si può sempre sottrarre e dividere per elementi non nulli.
---
Un **campo** è un insieme dotato di due operazioni, somma e prodotto, che soddisfano le proprietà algebriche usuali dei numeri. Sono campi $\mathbb{Q}$, $\mathbb{R}$ e $\mathbb{C}$.

## Definizione

Un insieme $K$ con $+$ e $\cdot$ è un campo se per ogni $a,b,c\in K$:

- **somma**: associativa, commutativa, esiste $0$ con $a+0=a$, esiste l'opposto $-a$ con $a+(-a)=0$;
- **prodotto**: associativo, commutativo, esiste $1\ne 0$ con $a\cdot1=a$, per $a\ne0$ esiste l'inverso $a^{-1}$ con $aa^{-1}=1$;
- **distributività**: $a(b+c)=ab+ac$.

Sottrazione e divisione non sono primitive: $a-b=a+(-b)$ e $a/b=a\cdot b^{-1}$ (per $b\ne0$).

## Intuizione

Un campo è "il posto in cui le quattro operazioni funzionano come ci si aspetta". $\mathbb{N}$ e $\mathbb{Z}$ non sono campi: nel primo non si può sempre sottrarre, nel secondo non si può sempre dividere.

## Esempi

- $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ sono campi.
- $\mathbb{Z}$ non è un campo: $2$ non ha inverso moltiplicativo in $\mathbb{Z}$.

Dai soli assiomi si dimostrano fatti come $0\cdot x=0$, $(-1)x=-x$, $(-x)(-y)=xy$. Quello che distingue $\mathbb{R}$ da $\mathbb{Q}$ non sono gli assiomi di campo ma l'[[Assioma di completezza]].

## Vedi anche

- [[Numero reale]]
- [[Assioma di completezza]]
- [[Numero complesso]]
- [[Anello]]
