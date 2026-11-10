---
title: Conseguenza logica
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- conseguenza
sintesi: Una formula è conseguenza logica di un insieme di premesse quando è vera in ogni interpretazione che rende vere tutte le premesse.
---

Una formula $\varphi$ è **conseguenza logica** di un insieme di formule $\Gamma$ (le premesse) quando la conclusione non può essere falsa se le premesse sono tutte vere.

## Definizione

Un'[[Interpretazione|interpretazione]] $I$ è un **modello** di $\varphi$ se $I\models\varphi$, cioè $\llbracket\varphi\rrbracket_I=\mathsf t$; è modello di un insieme $\Gamma$ se è modello di ogni formula di $\Gamma$. Allora:

$$
\Gamma\models\varphi
\quad\Longleftrightarrow\quad
\text{per ogni }I,\ I\models\Gamma\Rightarrow I\models\varphi.
$$

Per un insieme finito di premesse, $\{\varphi_1,\ldots,\varphi_n\}\models\varphi$ equivale a dire che $(\varphi_1\land\cdots\land\varphi_n)\Rightarrow\varphi$ è una [[Tautologia|tautologia]].

## Intuizione

Non importa se le premesse siano davvero vere nel mondo: conta che **se** lo fossero, la conclusione seguirebbe per forza. «Tutti gli uomini sono mortali, Socrate è un uomo, quindi Socrate è mortale» è valido; «tutti gli uomini sono mortali, Socrate è mortale, quindi è un uomo» no, perché Socrate potrebbe essere un cane.

## Esempi

Con $\Gamma=\{p,\ p\Rightarrow q\}$ l'unico modello è $\{p\mapsto\mathsf t,\ q\mapsto\mathsf t\}$, quindi $\Gamma\models q$ (modus ponens).

Dalle premesse $c\Rightarrow a$ e $a\Rightarrow b$ segue $c\Rightarrow b$ ma non $b\Rightarrow c$: per $b\mapsto\mathsf t$, $c\mapsto\mathsf f$ le premesse sono vere e $b\Rightarrow c$ è falsa.

## Vedi anche

- [[Interpretazione]]
- [[Tautologia]]
- [[Regola di inferenza]]
- [[Implicazione]]
