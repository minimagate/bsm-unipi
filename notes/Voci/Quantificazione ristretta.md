---
title: Quantificazione ristretta
type: voce
categoria: notazione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-13 - Quantificazione ristretta, uguaglianza e specifiche formali
alias:
- quantificatore ristretto
- quantificatori ristretti
sintesi: Notazione che indica il dominio di un quantificatore, abbreviando una implicazione per il "per ogni" e una congiunzione per l'"esiste".
---

La **quantificazione ristretta** è una notazione per esprimere che un quantificatore agisce solo sugli elementi che soddisfano una certa formula.

## Definizione

$$
(\forall x:P.\,Q)\ \text{abbrevia}\ (\forall x.\,P\Rightarrow Q),
\qquad
(\exists x:P.\,Q)\ \text{abbrevia}\ (\exists x.\,P\land Q).
$$

$P$ è il **dominio** del [[Quantificatore|quantificatore]]. Con $\forall$ il dominio si lega con $\Rightarrow$, con $\exists$ con $\land$.

Valgono leggi analoghe a quelle senza dominio, per esempio $(\forall x:P\lor Q.\,R)\equiv(\forall x:P.\,R)\land(\forall x:Q.\,R)$ e $\neg(\exists x:R.\,P)\equiv(\forall x:R.\,\neg P)$.

## Intuizione

Si legge come in italiano: "per ogni $x$ tale che $P$, vale $Q$" e "esiste $x$ tale che $P$ e vale $Q$". Se il dominio $P$ è vuoto, $(\forall x:P.\,Q)$ è **vacuamente vera** e $(\exists x:P.\,Q)$ è **vacuamente falsa**, qualunque sia $Q$.

## Esempi

- $(\forall x:\operatorname{studenteFPL}(x).\ \operatorname{vaAlCinema}(x)\lor\operatorname{vaAlTeatro}(x))$.
- $(\exists x:\operatorname{studenteFPL}(x).\ \operatorname{vaAlCinema}(x))$.
- «Tutti gli studenti di FPL con tre teste vanno al cinema» è vera se nessuno studente ha tre teste.

## Vedi anche

- [[Quantificatore]]
- [[Logica del primo ordine]]
- [[Implicazione]]
- [[Legge di Leibniz]]
