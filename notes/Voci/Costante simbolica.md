---
title: Costante simbolica
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-03 - Introduzione al C, variabili e input-output
alias:
- const
- #define
- costanti simboliche
sintesi: Un nome che sta al posto di un valore fisso, per rendere il codice leggibile e modificabile in un solo punto.
---
Una **costante simbolica** è un nome dato a un valore che non cambia durante l'esecuzione. In C si ottiene con la parola chiave `const` oppure con una macro `#define`.

## Definizione

```c
const float PiGreco = 3.14f;
const int N = 100;
#define Nmax 10
```

Con `const` si dichiara un oggetto con un tipo, il cui valore non si può modificare con un assegnamento. Con `#define` si definisce invece una sostituzione di testo: il preprocessore rimpiazza ogni uso di `Nmax` con `10` prima della compilazione. La direttiva non termina con `;`, e la macro non è una variabile con una propria area di memoria.

## Intuizione

Scrivere `PiGreco * raggio * raggio` è più chiaro di `3.14 * raggio * raggio`, e se il valore cambia lo si modifica in un unico posto. La differenza concettuale: `const` ha un tipo e un indirizzo, `#define` è solo testo. In C una variabile `const int` non è usabile come etichetta di un `case` in uno `switch`, mentre una macro che si espande in un intero costante sì.

## Esempi

- `area_cerchio = PiGreco * raggio * raggio;`
- Nel massimo di una sequenza, `#define N 10` fissa la lunghezza e la guardia diventa `i < N`.

## Vedi anche

- [[Dichiarazione di variabile]]
- [[Tipo di dato]]
- [[Istruzione switch]]
