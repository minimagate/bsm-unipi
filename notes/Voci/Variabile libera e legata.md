---
title: Variabile libera e legata
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-08 - Sintassi e semantica della logica del primo ordine
alias:
- variabili libere
- variabili legate
- variabile libera
- variabile legata
- formula chiusa
- formula aperta
sintesi: Un'occorrenza di variabile è legata se sta nella portata di un quantificatore sulla stessa variabile, libera altrimenti; una formula senza variabili libere è chiusa.
---

Una variabile può essere **legata** da un quantificatore o rimanere **libera**. Questa distinzione decide se una formula ha un valore di verità fissato.

## Definizione

In $(\forall x.P)$ o $(\exists x.P)$ la sottoformula $P$ è la **portata** del quantificatore. Un'occorrenza di $x$ è **legata** se compare nella portata di un $\forall x$ o $\exists x$, altrimenti è **libera**. La nozione riguarda le singole occorrenze: la stessa variabile può essere libera in un punto e legata in un altro.

Una formula è **aperta** se ha occorrenze libere, **chiusa** altrimenti. Si scrive $P(x)$ per dire che $x$ occorre libera in $P$.

## Intuizione

Le variabili legate sono solo segnaposto: $\forall x.\operatorname{multiplo}(x,3)$ e $\forall z.\operatorname{multiplo}(z,3)$ dicono la stessa cosa, e si può ridenominare purché la nuova variabile non compaia già nella formula. Il valore di una formula chiusa dipende solo dall'interpretazione; quello di una aperta anche da quali individui rappresentano le variabili libere.

## Esempi

In $(\forall x.\,p(a,x))\land q(x,y)$ la $x$ di $p(a,x)$ è legata, mentre la $x$ e la $y$ di $q(x,y)$ sono libere.

In $\forall y.\,z=y\land(x=y\lor(\exists x.\,x=z\lor z=y))$ tutte le $y$ sono legate, tutte le $z$ libere, la $x$ di $x=y$ è libera e quella di $x=z$ è legata: la formula è aperta, con variabili libere $x$ e $z$.

Attenzione: in $\forall x.\,x\le y$ non si può rinominare $x$ in $y$, perché la $y$ libera verrebbe catturata dal quantificatore.

## Vedi anche

- [[Formula ben formata]]
- [[Quantificatore]]
- [[Interpretazione]]
- [[Skolemizzazione]]
