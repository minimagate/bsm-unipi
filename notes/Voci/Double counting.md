---
title: Double counting
type: voce
categoria: metodo
corsi:
- Aritmetica
introdotta_in: 2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio
alias:
- doppio conteggio
sintesi: Tecnica che consiste nel contare lo stesso insieme in due modi diversi, deducendo che i due risultati coincidono.
---

Il **double counting** (o conteggio doppio) è una tecnica fondamentale del calcolo combinatorio: si conta uno stesso insieme finito in due modi diversi e si uguagliano i risultati.

## Definizione

Se un insieme finito viene contato con il metodo A, ottenendo $P$, e con il metodo B, ottenendo $Q$, allora

$$P=Q.$$

Per usarlo bene bisogna dichiarare con precisione *quale* insieme si sta contando e verificare che i due metodi contino davvero gli stessi elementi.

## Intuizione

È come contare gli studenti di una classe una volta per fila e una volta per colonna: i totali devono combaciare. Molte identità algebriche difficili da dimostrare diventano ovvie se si trova l'oggetto che entrambe le espressioni contano.

## Esempi

Un quadrato $n\times n$ ha $n^2$ quadratini. Dividendolo in cornici concentriche di $1,3,5,\ldots,2n-1$ quadratini si ottiene anche $\sum_{i=0}^{n-1}(2i+1)$. Quindi

$$\sum_{i=0}^{n-1}(2i+1)=n^2.$$

## Come si dimostra

Vedi [[2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio#2. Double counting: contare lo stesso insieme in due modi|la lezione del 29 settembre]].

## Vedi anche

- [[Cardinalità]]
- [[Coefficiente binomiale]]
- [[Principio di induzione]]
- [[Principio di inclusione-esclusione]]
