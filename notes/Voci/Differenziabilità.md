---
title: Differenziabilità
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-27 - Derivate, differenziabilità e regole di derivazione
alias:
- differenziabile
- differenziale
sintesi: Una funzione è differenziabile in un punto se vicino a quel punto si approssima con una retta, a meno di un errore trascurabile rispetto alla distanza.
---

Una funzione è **differenziabile** in un punto se, vicino a quel punto, coincide con una funzione lineare più un errore che tende a zero più velocemente della distanza dal punto.

## Definizione

$f$ è differenziabile in $x_0$ se esiste $\alpha\in\mathbb R$ tale che

$$
f(x_0+h)=f(x_0)+\alpha h+o(h)\qquad\text{per }h\to0.
$$

Il numero $\alpha$, se esiste, è unico. Per funzioni di una variabile reale $f$ è differenziabile in $x_0$ **se e solo se** è [[Derivata|derivabile]] in $x_0$, e in tal caso $\alpha=f'(x_0)$.

## Intuizione

Vicino a $x_0$, $f(x_0+h)$ è la somma di tre pezzi: un termine costante $f(x_0)$, un termine lineare in $h$ (la tangente) e un resto che tende a $0$ più in fretta di $h$ ([[Simboli di Landau|$o(h)$]]). Il resto è lo scarto tra il grafico e la tangente.

Da Analisi 2 in poi, con più variabili, le due nozioni non coincidono più, e per molte cose la differenziabilità è quella giusta.

## Esempi

- $(x_0+h)^2=x_0^2+2x_0h+h^2$, quindi $\alpha=2x_0$ e il resto $h^2$ è $o(h)$.
- $e^{x_0+h}=e^{x_0}(1+h+o(h))=e^{x_0}+e^{x_0}h+o(h)$, quindi $\alpha=e^{x_0}$.

## Come si dimostra

L'unicità di $\alpha$ si ottiene sottraendo due sviluppi: $(\alpha_1-\alpha_2)h=o(h)$ obbliga $\alpha_1=\alpha_2$. L'equivalenza con la derivabilità è nella [[2026-10-27 - Derivate, differenziabilità e regole di derivazione#2. Differenziabilità|lezione del 27 ottobre]].

## Vedi anche

- [[Derivata]]
- [[Simboli di Landau]]
- [[Sviluppo di Taylor]]
- [[Regole di derivazione]]
