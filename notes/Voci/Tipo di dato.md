---
title: Tipo di dato
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-03 - Introduzione al C, variabili e input-output
alias:
- tipo
- tipi
- tipi di dato
- tipi semplici
sintesi: Un tipo specifica un insieme di valori, le operazioni ammesse su di essi e come sono rappresentati in memoria.
---
Un **tipo di dato** specifica tre cose: un insieme di valori, le operazioni ammesse su di essi e una rappresentazione in memoria. Permette di ragionare sui dati senza gestire ogni volta la codifica binaria e consente di scoprire alcuni errori prima dell'esecuzione.

## Definizione

- Un **tipo semplice** rappresenta un valore logicamente indivisibile: un intero (`int`), un numero in virgola mobile (`float`, `double`), un carattere (`char`).
- Un **tipo strutturato** aggrega componenti: un array, una matrice, una data fatta da giorno, mese e anno.

Il C offre tipi predefiniti e meccanismi per costruirne di nuovi. Lo spazio occupato da un tipo è dato da `sizeof(int)`, `sizeof(float)`, `sizeof(char)`, misurato in byte C; `sizeof` è un **operatore**, non una funzione.

## Intuizione

Il tipo è la parte della variabile che dice che cosa ci può stare. Occhio: `int` non è l'insieme $\mathbb Z$ ma un intervallo finito, con $n$ bit in complemento a due da $-2^{n-1}$ a $2^{n-1}-1$. Le dimensioni dipendono dall'implementazione (spesso 32 bit per `int`).

## Esempi

- `int numero = 12;` e `float temperatura = 25.378f;` sono due dichiarazioni di tipi semplici.
- `'2'` ha tipo `char` ed è il *codice* di una cifra, non il numero `2`.
- Nel controllo dei tipi del linguaggio didattico, `(x + 5) and (x > y)` è scorretto perché `and` richiede booleani.

## Vedi anche

- [[Dichiarazione di variabile]]
- [[Numero in virgola mobile]]
- [[Conversione di tipo]]
- [[Array]]
