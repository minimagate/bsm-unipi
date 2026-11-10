---
title: Funzione caratteristica
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio
alias:
- funzioni caratteristiche
sintesi: La funzione caratteristica di un sottoinsieme vale uno sugli elementi del sottoinsieme e zero sugli altri.
---

La **funzione caratteristica** di un sottoinsieme $A\subseteq X$ è la funzione che "segnala" l'appartenenza ad $A$.

## Definizione

$$\chi_A:X\to\{0,1\},\qquad \chi_A(x)=\begin{cases}1,&x\in A,\\0,&x\notin A.\end{cases}$$

Si trova scritta anche $\mathbf{1}_A$. Il sottoinsieme si ricostruisce come $A=\{x\in X:\chi_A(x)=1\}$, quindi $A\mapsto\chi_A$ è una biiezione tra l'[[Insieme delle parti]] di $X$ e le funzioni $X\to\{0,1\}$.

## Intuizione

Per ogni elemento decidi "dentro" ($1$) o "fuori" ($0$): una funzione caratteristica è una lista di scelte sì/no. Traduce operazioni sugli insiemi in operazioni sui numeri: $\mathbf{1}_{A\cap B}=\mathbf{1}_A\mathbf{1}_B$ e $|A|=\sum_{x\in X}\mathbf{1}_A(x)$.

## Esempi

Se $X=\{a,b,c\}$ e $A=\{a,c\}$, allora $\chi_A(a)=1$, $\chi_A(b)=0$, $\chi_A(c)=1$. Poiché le funzioni $X\to\{0,1\}$ sono $2^{|X|}$, si ottiene $|\mathcal{P}(X)|=2^{|X|}$.

## Come si dimostra

Vedi [[2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio#11. Funzioni caratteristiche e corrispondenza con l’insieme delle parti|la lezione del 29 settembre]]; l'uso per l'inclusione-esclusione è in [[2026-09-30 - Successioni ricorrenti e formule combinatorie#8. Funzioni caratteristiche|quella del 30 settembre]].

## Vedi anche

- [[Insieme delle parti]]
- [[Principio di inclusione-esclusione]]
- [[Cardinalità]]
- [[Funzione biettiva]]
