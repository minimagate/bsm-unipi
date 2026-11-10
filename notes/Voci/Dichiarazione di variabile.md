---
title: Dichiarazione di variabile
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-03 - Introduzione al C, variabili e input-output
alias:
- dichiarazione
- variabile
- variabili
- dichiarazioni
sintesi: Una dichiarazione introduce una variabile con nome e tipo, prima del suo uso, senza darle ancora un valore utile.
---
Una **dichiarazione di variabile** in C associa a un identificatore un tipo e riserva la memoria per un valore di quel tipo. Una variabile ha **nome, tipo, valore e indirizzo**.

## Definizione

Si scrive il tipo seguito dai nomi:

```c
int base, altezza, area;
float temperatura;
int x = 0;
int a, b, z = 0;
```

Nell'ultima riga è inizializzata solo `z`. Le variabili vanno dichiarate prima di essere usate: così il compilatore conosce i tipi e può segnalare, prima dell'esecuzione, un nome sbagliato. Nel corpo di `main` si mette prima la parte dichiarativa e poi quella eseguibile.

## Intuizione

L'immagine delle slide è una scatola: il nome è l'etichetta, il valore è il contenuto, il tipo dice che cosa ci può stare, l'indirizzo è la posizione. Tipo e indirizzo restano fissi, il valore cambia. Dichiarare non è inizializzare: `int base;` non assegna un valore utilizzabile, e il valore di una variabile locale non inizializzata è *indeterminato*. Occorre scriverla (con `base = 3;` o con `scanf`) prima di leggerla.

## Esempi

Se si dichiara `alfa` e poi si scrive `alba = alfa + 1;`, il compilatore segnala che `alba` non è dichiarata. Invece `int x = 0;` dichiara e inizializza in un solo passo.

## Vedi anche

- [[Tipo di dato]]
- [[Costante simbolica]]
- [[Stato]]
- [[Input e output in C]]
