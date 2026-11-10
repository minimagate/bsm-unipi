---
title: Isomorfismo
type: voce
categoria: definizione
corsi:
- Aritmetica
- Geometria 1
introdotta_in: 2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali
alias:
- isomorfismi
- isomorfi
- isomorfismo di spazi vettoriali
- isomorfismo di gruppi
sintesi: Un isomorfismo è una corrispondenza biunivoca che rispetta le operazioni, per cui due strutture isomorfe sono la stessa struttura con nomi diversi.
---

Un **isomorfismo** è un'applicazione biettiva che rispetta le operazioni della struttura in gioco. Due strutture tra cui esiste un isomorfismo si dicono **isomorfe** e, dal punto di vista algebrico, sono indistinguibili.

## Definizione

Per gli [[Spazio vettoriale|spazi vettoriali]] su $K$ un isomorfismo è un'applicazione $\Phi:V\to W$ che è:

- lineare: $\Phi(v+w)=\Phi(v)+\Phi(w)$ e $\Phi(\alpha v)=\alpha\Phi(v)$;
- una [[Funzione biettiva|biezione]].

Si scrive $V\cong W$. Lo stesso schema vale per i gruppi e gli anelli, dove un isomorfismo è un omomorfismo biettivo.

## Intuizione

Se $V\cong W$ possiamo tradurre ogni fatto di $V$ in un fatto di $W$ e viceversa, perché la corrispondenza rispetta somma e prodotto per scalare. Per questo, scelta una base, ogni spazio di dimensione $n$ è "lo stesso" di $K^n$. L'inversa di un isomorfismo è ancora un isomorfismo.

## Esempi

- La mappa delle coordinate $\Phi_{\mathcal B}:V\to K^n$ è un isomorfismo.
- $\mathbb{C}\cong\mathbb{R}^2$ come spazi vettoriali su $\mathbb{R}$.
- $M_{m,n}(K)\cong K^{mn}$, mettendo gli elementi in una lista.

## Come si dimostra

Per l'isomorfismo delle coordinate: linearità dal calcolo diretto della somma, iniettività e suriettività dall'unicità e dall'esistenza dello sviluppo. Vedi [[2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali#La mappa delle coordinate è un isomorfismo|la lezione del 7 ottobre]].

## Vedi anche

- [[Coordinate rispetto a una base]]
- [[Funzione biettiva]]
- [[Funzione inversa]]
- [[Dimensione di uno spazio vettoriale]]
