---
title: Funzione
type: voce
categoria: oggetto
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Insiemi, applicazioni e spazi vettoriali
alias:
- applicazione
- applicazioni
- funzioni
- applicazione tra insiemi
sintesi: Una funzione associa a ogni elemento di un insieme di partenza uno e un solo elemento di un insieme di arrivo.
---

Una **funzione** (o **applicazione**) $f:X\to Y$ è una regola che a ogni elemento di $X$ associa esattamente un elemento di $Y$. È l'oggetto di base con cui si confrontano gli [[Insieme|insiemi]] fra loro.

## Definizione

Dati due insiemi $X$ (il **dominio**) e $Y$ (il **codominio**), una funzione $f:X\to Y$ associa a ogni $x\in X$ un unico elemento $f(x)\in Y$:

$$
\forall x\in X\ \exists!\,y\in Y \quad\text{tale che}\quad y=f(x).
$$

Formalmente, $f$ è individuata dal suo grafico, cioè da un sottoinsieme $\Gamma\subseteq X\times Y$ che contiene, per ogni $x\in X$, esattamente una coppia $(x,y)$. Si veda il [[Prodotto cartesiano]].

## Intuizione

Pensala come una macchina: ci metti un elemento di $X$ e ne esce uno solo di $Y$. Conta anche il contorno: la stessa legge $x\mapsto x^2$ dà funzioni diverse se cambiano dominio o codominio. Non è richiesto che ogni elemento di $Y$ venga raggiunto, né che due elementi diversi di $X$ abbiano immagini diverse: per queste proprietà si guardi la [[Funzione biettiva]].

## Esempi

- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=2x+1$.
- Tra gli esempi di spazi vettoriali, l'insieme di tutte le funzioni $f:X\to K$ ha una somma definita punto per punto: $(f+g)(x)=f(x)+g(x)$.
- $x\mapsto \pm\sqrt{x}$ non è una funzione, perché a $x>0$ associa due valori.

## Vedi anche

- [[Funzione biettiva]]
- [[Composizione di funzioni]]
- [[Funzione inversa]]
- [[Immagine e controimmagine]]
