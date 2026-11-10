---
title: Stato
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-25 - Stati, algoritmi e fondamenti della logica formale
alias:
- stati
- configurazione
sintesi: Insieme di associazioni tra nomi simbolici e valori che descrive le informazioni rilevanti in un dato momento dell'esecuzione, con al più un valore per nome.
---

Lo **stato** è l'insieme delle informazioni rilevanti in un certo momento dell'esecuzione di un algoritmo. È il concetto attorno a cui ruota tutta la programmazione imperativa.

## Definizione

Uno stato è un insieme di associazioni tra nomi simbolici e valori, scritte $X\mapsto\mathrm{val}$. Vincolo fondamentale: a ogni nome è associato **al più un valore**. Quindi $\{A\mapsto 45,\ B\mapsto 150,\ B\mapsto 0\}$ non è uno stato, mentre è lecito che un nome non abbia alcun valore.

Formalmente è una funzione parziale $\sigma:\mathrm{Ide}\to\mathrm{Val}$ dagli identificatori ai valori (interi e booleani).

## Intuizione

Per il bambino che moltiplica con carta e penna lo stato è il contenuto dei riquadri $A$, $B$, $C$ sul quaderno; per un calcolatore, secondo il [[Modello di von Neumann|modello di von Neumann]], è il contenuto della memoria. Un [[Algoritmo|algoritmo]] è una sequenza di passi che trasformano lo stato:

$$
S_0\longrightarrow S_1\longrightarrow\cdots\longrightarrow S_f.
$$

Nel linguaggio C l'azione che modifica lo stato è l'assegnamento.

## Esempi

Per l'algoritmo del prodotto con $A=5$, $B=3$ gli stati attraversati sono

$$
\{A\mapsto5,B\mapsto3,C\mapsto0\},\ \{A\mapsto5,B\mapsto2,C\mapsto5\},\ \{A\mapsto5,B\mapsto1,C\mapsto10\},\ \{A\mapsto5,B\mapsto0,C\mapsto15\}.
$$

Lo stato finale contiene $C\mapsto 15=5\cdot3$.

## Vedi anche

- [[Specifica di un problema]]
- [[Algoritmo]]
- [[Precondizione e postcondizione]]
- [[Modello di von Neumann]]
