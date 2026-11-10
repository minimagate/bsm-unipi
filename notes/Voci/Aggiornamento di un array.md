---
title: Aggiornamento di un array
type: voce
categoria: metodo
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-29 - Aggiornamento degli array e tecniche di costruzione dei cicli
alias:
- aggiornamento selettivo
- aggiornamento di array
sintesi: Assegnare a una sola posizione di un array lasciando invariate tutte le altre.
---
L'**aggiornamento di un array** (o aggiornamento selettivo) è il comando `v[E] := E'` che modifica solo l'elemento di indice `E` dell'array `v`, mettendoci il valore `E'`.

## Definizione

Nello stato $\sigma$ si calcolano $j=\mathcal E(E,\sigma)$ e $d=\mathcal E(E',\sigma)$, entrambi definiti con $j\in\operatorname{dom}(v)$. Il nuovo stato associa a `v` la sequenza $w=\sigma(v)[d/j]$, con $w(i)=d$ se $i=j$ e $w(i)=\sigma(v)(i)$ altrimenti. Per verificare una tripla vale l'assioma

$$
\{\mathrm{def}(E)\land\mathrm{def}(E')\land E\in\operatorname{dom}(v)\land P[w/v]\}\ v[E]:=E'\ \{P\},
\qquad w=v[E'/E].
$$

## Intuizione

Il comando contiene due aggiornamenti annidati: uno *interno*, che cambia un elemento della sequenza, e uno *esterno*, che aggiorna il valore di `v` nello stato. Indice e valore sono entrambi valutati nello stato di prima. Nelle dimostrazioni si sostituisce l'intera sequenza `v` nell'asserzione e si distinguono due casi, la posizione modificata e le altre.

## Esempi

- `a[k] := a[k-1] + k` estende un prefisso di somme: per $i<k$ l'elemento resta quello vecchio, per $i=k$ vale $\sum_{j=0}^{k-1}j+k=\sum_{j=0}^{k}j$.
- Per incrementare tutti gli elementi si usa `a[x] := a[x] + 1; x := x + 1` dentro un `while`, con invariante che separa la parte già incrementata da quella ancora da elaborare.

## Vedi anche

- [[Array]]
- [[Regola dell'assegnamento]]
- [[Invariante di ciclo]]
- [[Costruzione di un ciclo]]
