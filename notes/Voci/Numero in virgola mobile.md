---
title: Numero in virgola mobile
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-05 - Tipi e conversioni in C, selezione e cicli for
alias:
- virgola mobile
- floating point
- float
- double
sintesi: Un numero reale approssimato con precisione finita, scritto in notazione decimale o scientifica.
---
Un **numero in virgola mobile** (*floating point*) è la rappresentazione, con precisione finita, di un numero reale. In C i tipi principali sono `float`, `double` e `long double`.

## Definizione

`float` occupa tipicamente 4 byte; non tutti i reali sono rappresentabili esattamente. Le costanti si scrivono in notazione decimale (`3.14`, con il **punto**) o scientifica (`0.314E1`, `1234.5e-1`). Con il suffisso `f` o `F` la costante è `float`; senza suffisso, come `3.14`, è `double`. Gli operatori sono `+`, `-`, `*`, `/`; l'operatore `%` non si applica ai floating. I limiti stanno in `<float.h>`, ad esempio `FLT_MAX`.

## Intuizione

Il computer memorizza il numero in binario, e molti decimali non sono esattamente rappresentabili: `123.45f` viene stampato come `123.449997` con `%f`. Fissare i decimali con un formato come `%.3f` cambia solo la stampa, non la precisione con cui il valore è memorizzato. L'ampiezza di un campo, come in `%8.3f`, è un minimo e non tronca.

## Esempi

```c
float x = 123.45f;
printf("|%f| |%8.3f| |%-8.3f|\n", x, x, x);
```

stampa `|123.449997| | 123.450| |123.450 |`. In lettura, `%f` e `%e` accettano sia `123.456` sia `0.123456E+3`; per leggere un `double` serve `%lf`.

## Vedi anche

- [[Tipo di dato]]
- [[Conversione di tipo]]
- [[Input e output in C]]
