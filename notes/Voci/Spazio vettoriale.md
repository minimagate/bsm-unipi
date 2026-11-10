---
title: Spazio vettoriale
type: voce
categoria: oggetto
corsi:
- Geometria 1
introdotta_in: 2026-09-23 - Insiemi, applicazioni e spazi vettoriali
alias:
- spazi vettoriali
- K-spazio vettoriale
sintesi: Uno spazio vettoriale è un insieme di vettori che si possono sommare e moltiplicare per scalari di un campo, rispettando otto assiomi.
---

Uno **spazio vettoriale** su un [[Campo|campo]] $K$ è un insieme $V$ i cui elementi, detti **vettori**, si possono sommare tra loro e moltiplicare per gli elementi di $K$, detti **scalari**, in modo che valgano gli assiomi che generalizzano le proprietà dei vettori geometrici.

## Definizione

Sono date due operazioni, $+:V\times V\to V$ e $\cdot:K\times V\to V$. Gli assiomi sono:

1. $(V,+)$ è un [[Gruppo|gruppo abeliano]] (associatività, commutatività, vettore nullo $\mathbf 0$, opposto);
2. $\alpha(\mathbf u+\mathbf v)=\alpha\mathbf u+\alpha\mathbf v$;
3. $(\alpha+\beta)\mathbf v=\alpha\mathbf v+\beta\mathbf v$;
4. $(\alpha\beta)\mathbf v=\alpha(\beta\mathbf v)$;
5. $1_K\mathbf v=\mathbf v$.

## Intuizione

L'idea è dimenticare cosa siano "davvero" i vettori e ricordare solo cosa si può fare con loro: sommarli e scalarli. Frecce nel piano, colonne di numeri, polinomi, funzioni e matrici obbediscono alle stesse regole, quindi si studiano tutti insieme.

## Esempi

- I vettori geometrici del piano o dello spazio, con la regola del parallelogramma.
- Lo [[Spazio K^n]] delle $n$-uple, con operazioni componente per componente.
- I [[Polinomio|polinomi]] $K[x]$ e le [[Matrice|matrici]] $M_{m,n}(K)$.
- $\mathbb C$ è uno spazio vettoriale sia su $\mathbb C$ sia su $\mathbb R$ (e le dimensioni sono diverse).

## Come si dimostra

Per un esempio concreto si verificano gli assiomi riducendosi a quelli di $K$; alcune conseguenze, come $0\mathbf v=\mathbf 0$, si ricavano subito: vedi [[2026-09-30 - Spazi vettoriali, esempi e sottospazi#6. Proprietà derivate dagli assiomi|le proprietà derivate dagli assiomi]].

## Vedi anche

- [[Sottospazio vettoriale]]
- [[Base di uno spazio vettoriale]]
- [[Dimensione di uno spazio vettoriale]]
- [[Applicazione lineare]]
