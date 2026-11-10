---
title: Regola di inferenza
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-25 - Stati, algoritmi e fondamenti della logica formale
alias:
- regole di inferenza
sintesi: Legge che permette di derivare nuovi asserti a partire da asserti già noti, in modo puramente sintattico.
---

Una **regola di inferenza** è una legge che permette di derivare uno o più asserti a partire da altri asserti, senza guardare il significato dei simboli.

## Definizione

Una regola ha la forma

$$
\frac{\delta_1,\ \dots,\ \delta_k}{\delta}
$$

con premesse $\delta_1,\dots,\delta_k$ e conseguenza $\delta$. Se $k=0$ si chiama **assioma**. Una dimostrazione di $\varphi$ da un insieme di premesse $\Gamma$ è una sequenza di formule in cui ciascuna è una premessa oppure è ottenuta con una regola; si scrive $\Gamma\vdash\varphi$. Un insieme di regole è **corretto** se $\Gamma\vdash\varphi$ implica $\Gamma\models\varphi$, ed è **completo** se vale il viceversa.

## Intuizione

Dimostrare diventa un gioco meccanico: si prende un asserto, si applica una regola, se ne ottiene un altro e si va avanti fino alla conclusione. Come per un algoritmo, conta solo la forma dei passaggi. Se le regole sono corrette, ciò che si dimostra è davvero [[Conseguenza logica|conseguenza logica]] delle premesse.

## Esempi

- **Modus ponens**: da $Q\rightarrow R$ e $Q$ si deduce $R$.
- **Istanziazione**: da $\forall x\,P(x)$ si deduce $P(a)$ per ogni individuo $a$.
- Con queste due si dimostra il sillogismo di Socrate: da $\forall x(\mathrm{uomo}(x)\rightarrow\mathrm{mortale}(x))$ e $\mathrm{uomo}(\mathrm{Socrate})$ si ottiene $\mathrm{mortale}(\mathrm{Socrate})$.

## Vedi anche

- [[Conseguenza logica]]
- [[Principio di sostituzione]]
- [[Teorema di deduzione]]
- [[Logica del primo ordine]]
