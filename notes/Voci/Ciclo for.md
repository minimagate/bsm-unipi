---
title: Ciclo for
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-05 - Tipi e conversioni in C, selezione e cicli for
alias:
- for
- iterazione determinata
sintesi: Un ciclo che raccoglie in un'unica intestazione inizializzazione, guardia e aggiornamento, adatto a ripetizioni di numero noto.
---
Il **ciclo `for`** è il costrutto C per l'*iterazione determinata*, cioè un ciclo il cui numero di ripetizioni è fissato all'ingresso. Mette in un'unica riga l'inizializzazione, la guardia e l'aggiornamento della variabile di controllo.

## Definizione

```c
for (inizializzazione; guardia; aggiornamento) {
    /* corpo */
}
```

Si esegue una volta l'inizializzazione; poi, finché la guardia è vera, si esegue il corpo e quindi l'aggiornamento. Equivale a

```c
inizializzazione;
while (guardia) {
    /* corpo */
    aggiornamento;
}
```

Le tre parti sono espressioni e si possono omettere, ma i due punti e virgola restano; se manca la guardia è considerata vera.

## Intuizione

È un `while` con la "contabilità" del contatore in evidenza. Conviene quando lo schema è quello consueto; altrimenti, per cicli con strutture meno regolari, è meglio il `while`. Anche un `for` ha un invariante e una funzione di terminazione, spesso la distanza tra il contatore e il limite.

## Esempi

| Intestazione | Valori di `i` |
|---|---|
| `for (i = 1; i <= 10; i = i + 1)` | $1,2,\ldots,10$ |
| `for (i = -4; i <= 4; i = i + 2)` | $-4,-2,0,2,4$ |

Due `for` annidati stampano la tavola pitagorica:

```c
for (riga = 1; riga <= 10; riga = riga + 1) {
    for (colonna = 1; colonna <= 10; colonna = colonna + 1)
        printf("%d ", riga * colonna);
    putchar('\n');
}
```

## Vedi anche

- [[Comando iterativo]]
- [[Invariante di ciclo]]
- [[Istruzione switch]]
- [[Linguaggio C]]
