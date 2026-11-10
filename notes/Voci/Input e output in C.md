---
title: Input e output in C
type: voce
categoria: metodo
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-03 - Introduzione al C, variabili e input-output
alias:
- scanf
- printf
sintesi: In C si legge con scanf, passando gli indirizzi delle variabili, e si scrive con printf, passando i valori.
---
In C l'**input e output** non sono comandi del linguaggio ma **funzioni di libreria** (da `<stdio.h>`). Le due principali sono `scanf`, per leggere, e `printf`, per scrivere, entrambe con una stringa di formato.

## Definizione

```c
scanf("%d", &x);
printf("Area: %d\n", area);
printf("Base: %d, altezza: %d\n", base, altezza);
```

`%d` indica un intero decimale. In `scanf`, `&x` è l'**indirizzo di `x`**, cioè dove scrivere il risultato; se la conversione riesce, il vecchio valore di `x` è sostituito. A ogni specificatore deve corrispondere un argomento adatto, nello stesso ordine. In `printf` si passano i **valori** da stampare. Il carattere `\n` va a capo; chiamate consecutive a `printf` non vanno a capo da sole.

## Intuizione

`printf` si limita a guardare lo stato, `scanf` lo modifica scrivendo nelle variabili. Per questo la lettura è una forma di assegnamento: gli esempi del corso assumono che l'input sia corretto e rappresentabile nel tipo richiesto. Il nome termina con `f` per *formatted*.

## Esempi

```c
int base, altezza, area;
scanf("%d", &base);
scanf("%d", &altezza);
area = base * altezza;
printf("Area: %d\n", area);
```

Con input `5` e `4` stampa `Area: 20`. Per i reali si usano `%f` e `%e`, e per i caratteri `%c`.

## Vedi anche

- [[Linguaggio C]]
- [[Dichiarazione di variabile]]
- [[Numero in virgola mobile]]
- [[Stato]]
