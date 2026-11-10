---
title: Linguaggio C
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-03 - Introduzione al C, variabili e input-output
alias:
- C
sintesi: Un linguaggio di programmazione compilato, efficiente e vicino alla macchina, in cui il corso traduce gli algoritmi studiati.
---
Il **linguaggio C** è un linguaggio di programmazione imperativo, nato ai Bell Labs negli anni Settanta. Da questa lezione il corso passa dal linguaggio didattico a C, che ha le stesse idee di base (espressioni, stato, assegnamenti, cicli) ma rende espliciti tipi, dichiarazioni e input/output.

## Definizione

Il C fu sviluppato da Dennis Ritchie nel 1972 come evoluzione del linguaggio B di Ken Thompson, nel contesto di UNIX. Il corso prende come riferimento l'ANSI C del 1989. Un programma minimo è:

```c
#include <stdio.h>

int main(void)
{
    printf("Ciao mondo!\n");
    return 0;
}
```

`main` è la funzione da cui parte l'esecuzione; `#include <stdio.h>` rende disponibili `printf` e `scanf`.

## Intuizione

Dal linguaggio didattico a C cambia soprattutto la scrittura. Ad esempio `div` diventa `/` (con operandi interi), `mod` diventa `%`, `=` diventa `==`, `:=` diventa `=`, `and`, `or`, `not` diventano `&&`, `||`, `!`. Al posto di `then`, `fi`, `do`, `endw` ci sono le graffe `{ }`. Per le condizioni `0` vale falso e ogni valore diverso da `0` vale vero.

## Esempi

- `x = 3;` assegna, `x == 3` confronta.
- `while (b > 0) { c = c + a; b = b - 1; }` è il `while` del linguaggio didattico, con graffe obbligatorie per più istruzioni.

## Vedi anche

- [[Dichiarazione di variabile]]
- [[Tipo di dato]]
- [[Input e output in C]]
- [[Algoritmo]]
