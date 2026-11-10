---
title: Istruzione switch
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-11-05 - Tipi e conversioni in C, selezione e cicli for
alias:
- switch
sintesi: Una selezione a più vie che sceglie il punto di ingresso in base al valore di un'espressione intera.
---
L'**istruzione `switch`** valuta una volta un'espressione intera e salta al `case` corrispondente. È l'alternativa a una lunga cascata di `if` quando si confronta la stessa espressione con valori costanti.

## Definizione

```c
switch (giorno) {
    case 1: case 2: case 3: case 4: case 5:
        printf("Giorno lavorativo\n");
        break;
    case 6: case 7:
        printf("Week end\n");
        break;
    default:
        printf("Giorno non valido\n");
}
```

I valori dei `case` devono essere **espressioni costanti intere**, distinte fra loro: `case a < 0:` non è valido. Se nessun valore coincide si entra in `default`, se c'è; altrimenti non viene eseguito alcun ramo.

## Intuizione

Le etichette `case` sono solo punti di ingresso e **non interrompono** l'esecuzione. Dopo l'ingresso si prosegue con le istruzioni successive fino a un `break` o alla fine dello `switch`: è il *fall-through*. Si sfrutta di proposito per raggruppare più casi (`case 1: case 2:`) o per stampare più risultati, ma dimenticare un `break` è un errore comune.

## Esempi

Con `lati = 5` e lo `switch` che parte da `case 6`, senza `break` fra i primi tre casi, si stampano «pentagono, quadrilatero, triangolo». Per distinguere negativo, nullo e positivo conviene invece una cascata di `if`, perché le condizioni non sono costanti.

## Vedi anche

- [[Costante simbolica]]
- [[Ciclo for]]
- [[Conversione di tipo]]
