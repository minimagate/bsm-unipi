---
title: Insieme quoziente
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-10-21 - Relazioni di equivalenza e strutture quoziente
alias:
- quoziente
- struttura quoziente
- strutture quoziente
sintesi: L'insieme i cui elementi sono le classi di equivalenza di una relazione di equivalenza.
---

L'**insieme quoziente** di un insieme rispetto a una relazione di equivalenza è l'insieme delle sue classi di equivalenza: ogni classe diventa un unico elemento.

## Definizione

Se $R$ è una [[Relazione di equivalenza|relazione di equivalenza]] su $A$, l'insieme quoziente è

$$
A/R=\{[x]_R\mid x\in A\}.
$$

La funzione $\pi\colon A\to A/R$, $\pi(x)=[x]$, si chiama **proiezione canonica**. Le classi formano una partizione di $A$.

## Intuizione

Si "incollano" tra loro gli elementi equivalenti e si guarda il risultato come un nuovo insieme, più piccolo. Se $A$ ha una struttura (per esempio una somma), a volte si può trasportarla sul quoziente. Ma occorre controllare la [[Buona definizione|buona definizione]]: il risultato di un'operazione tra classi non deve dipendere dai rappresentanti scelti.

## Esempi

- $\mathbb Z/n\mathbb Z$ è l'insieme quoziente di $\mathbb Z$ rispetto alla [[Congruenza modulo n|congruenza modulo $n$]]; ha esattamente $n$ elementi: $[0]_n,\dots,[n-1]_n$.
- I numeri razionali si costruiscono come quoziente di $\mathbb Z\times(\mathbb Z\setminus\{0\})$ rispetto a $(a,b)\sim(c,d)\iff ad=bc$.

## Vedi anche

- [[Classe di equivalenza]]
- [[Classe di congruenza]]
- [[Relazione di equivalenza]]
- [[Anello]]
