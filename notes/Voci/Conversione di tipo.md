---
title: Conversione di tipo
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-05 - Tipi e conversioni in C, selezione e cicli for
alias:
- conversioni di tipo
- cast
sintesi: Il passaggio del valore di un'espressione da un tipo a un altro, in modo automatico o esplicito con un cast.
---
Una **conversione di tipo** cambia il tipo con cui un valore viene trattato. In C può essere automatica (fra operandi, o in un assegnamento) oppure esplicita, con un **cast** `(tipo) espressione`.

## Definizione

Un'espressione ha sia un valore sia un tipo. Fra operandi di tipi diversi, per i casi semplici del corso, vale lo schema

$$
\mathtt{int}\to\mathtt{long}\to\mathtt{float}\to\mathtt{double}\to\mathtt{long\ double}.
$$

`char` e `short` vengono prima promossi a `int`. Nell'assegnamento `x = espressione;` il valore è convertito al tipo di `x`. Convertire da floating a intero elimina la parte frazionaria, **troncando verso zero**. Il cast ha precedenza più alta della divisione.

## Intuizione

Il tipo della *variabile* non cambia mai: se `x` è `int` e `y` è `double`, in `x + y` si converte il *valore* di `x`. Il trucco classico è la divisione: con due `int`, `/` fa una divisione intera, qualunque sia il tipo della variabile a cui si assegna il risultato. Per ottenere il quoziente reale bisogna convertire prima della divisione.

## Esempi

Con `somma = 7` e `n = 2`, entrambi `int`:

```c
media = somma / n;          /* 3 */
media = (float)somma / n;   /* 3.5 */
```

Nel secondo caso `(float)somma / n` è `((float)somma) / n`, mentre `(float)(somma / n)` convertirebbe un risultato già troncato. Con `float x = 2.3f, y = 4.5f;` e `int i = x + y;` si ottiene `i = 6`.

## Vedi anche

- [[Tipo di dato]]
- [[Numero in virgola mobile]]
- [[Dichiarazione di variabile]]
