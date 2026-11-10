---
title: Array
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-27 - Verifica di programmi iterativi e introduzione agli array
alias:
- array
- vettore
sintesi: Una sequenza finita di valori dello stesso tipo, a cui si accede tramite un indice.
---
Un **array** è una sequenza finita di valori tutti dello stesso tipo, ciascuno individuato da un indice. Nel linguaggio del corso, un array di interi o di booleani è visto come una funzione dagli indici ai valori.

## Definizione

Astrattamente $v:[a,b)\to A$, con $[a,b)$ gli indici naturali $i$ con $a\leq i<b$ e $A$ uguale a $\mathbb Z$ o $\mathrm{Bool}$. Il dominio è $\operatorname{dom}(v)$ e gli elementi sono $b-a$: l'estremo $b$ non è un indice valido, e se $a=b$ l'array è vuoto. Si dichiara con `v : array [a,b) of int`. L'elemento di indice `E` si scrive `v[E]`, con `E` espressione intera.

Nello stato, se `v` è un array, $\sigma(v):\operatorname{dom}(v)\to A$ è una funzione, e

$$
\mathcal E(v[E],\sigma)=\sigma(v)\bigl(\mathcal E(E,\sigma)\bigr),
$$

purché $\mathcal E(E,\sigma)$ sia definito e appartenga a $\operatorname{dom}(v)$. Di conseguenza $\mathrm{def}(v[E])=\mathrm{def}(E)\land E\in\operatorname{dom}(v)$: accedere fuori dal dominio rende l'espressione indefinita.

## Intuizione

Un array è una fila di caselle numerate. Gli operatori del linguaggio lavorano sui singoli valori, non sulle file intere: `v + w` non ha senso. L'indice può essere un'espressione, anche contenente altri accessi.

## Esempi

Se `v : array [0,4) of int` e $\sigma(v)=\{0\mapsto2,\ 1\mapsto1,\ 2\mapsto10,\ 3\mapsto6\}$, allora `v[v[0]+v[1]]` vale $\sigma(v)(2+1)=6$. Invece `v[4]` è indefinito perché $4\notin[0,4)$.

## Vedi anche

- [[Aggiornamento di un array]]
- [[Stato]]
- [[Tipo di dato]]
- [[Invariante di ciclo]]
