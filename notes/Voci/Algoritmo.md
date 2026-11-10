---
title: Algoritmo
type: voce
categoria: definizione
corsi:
- Aritmetica
- Fondamenti di Programmazione
introdotta_in: 2026-09-19 - Pensiero computazionale, algoritmi e modelli di calcolo
alias:
- algoritmi
sintesi: Sequenza finita di passi non ambigui ed eseguibili che, a partire dai dati forniti, porta ai risultati attesi.
---

Un **algoritmo** è una sequenza di passi che, eseguita da un opportuno esecutore, porta ai risultati attesi a partire dai dati forniti. È il vero oggetto di studio dell'informatica, più della macchina che lo esegue.

## Definizione

Una procedura è un algoritmo se rispetta almeno tre requisiti:

- **finitezza**: è composta da una sequenza finita di passi elementari;
- **non ambiguità**: ogni azione è interpretata in modo univoco dall'esecutore;
- **eseguibilità**: l'esecutore può completare ogni azione in tempo finito con le risorse disponibili.

Dal punto di vista dei programmi, un algoritmo fa passare l'esecutore da uno [[Stato|stato]] iniziale a uno stato finale attraverso una sequenza di stati intermedi.

## Intuizione

È una ricetta, ma scritta per un esecutore che non improvvisa: "aggiungere sale quanto basta" non va bene per una macchina, perché è ambiguo. Lo stesso problema può avere algoritmi molto diversi, a seconda delle operazioni elementari che l'esecutore sa fare.

## Esempi

- La moltiplicazione egizia: se $A$ è pari, $A\cdot B = \frac{A}{2}\cdot 2B$; se è dispari, $A\cdot B=(A-1)\cdot B+B$.
- Il prodotto per somme ripetute: si parte da $C=0$ e finché $B>0$ si somma $A$ a $C$ e si sottrae $1$ a $B$.
- La ricerca binaria in un elenco ordinato: a ogni passo si scarta metà dello spazio di ricerca.

## Vedi anche

- [[Algoritmo di Euclide]]
- [[Macchina di Turing]]
- [[Specifica di un problema]]
- [[Pensiero computazionale]]
