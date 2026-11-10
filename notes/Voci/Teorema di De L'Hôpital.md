---
title: Teorema di De L'Hôpital
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-28 - Teorema di De L'Hôpital e sviluppi di Taylor
alias:
- De L'Hôpital
- regola di De L'Hôpital
sintesi: Per limiti di quozienti nella forma indeterminata zero su zero o infinito su infinito, si può derivare numeratore e denominatore e calcolare il limite del nuovo quoziente.
---

Il **teorema di De L'Hôpital** permette, a certe condizioni, di calcolare un limite di un quoziente $\frac fg$ sostituendolo con il limite del quoziente delle derivate $\frac{f'}{g'}$.

## Enunciato

Sia $x_0\in\overline{\mathbb R}$ (anche $x_0^+$ o $x_0^-$). Supponiamo che

1. $f$ e $g$ siano definite e derivabili in un intorno (o semiretta) adatto, e si possa dividere;
2. sia una [[Forma indeterminata|forma indeterminata]] $\frac00$ oppure $\frac{\pm\infty}{\pm\infty}$ (nel secondo caso basta che diverga il denominatore);
3. esista $\displaystyle\lim_{x\to x_0}\frac{f'(x)}{g'(x)}=\ell\in\overline{\mathbb R}$.

Allora

$$
\lim_{x\to x_0}\frac{f(x)}{g(x)}=\ell.
$$

## Intuizione

Se $f$ e $g$ tendono a zero, conta chi ci arriva più in fretta, e la velocità è data dalle derivate. Ma attenzione: è uno strumento da usare con cautela. Se $\lim\frac{f'}{g'}$ **non esiste**, il teorema non dice nulla, e il limite di partenza può comunque esistere. Nella pratica, quasi sempre conviene preferire [[Limiti notevoli|limiti notevoli]] o [[Sviluppo di Taylor|sviluppi di Taylor]].

## Esempi

- $\displaystyle\lim_{x\to0}\frac{e^x-\cos x-\sin x+x^2}{x^2}=2$: derivando due volte si ottiene $\frac{e^x+\cos x+\sin x+2}{2}\to2$.
- $\displaystyle\lim_{x\to+\infty}\frac{2x+\sin x}{x}$ è $\frac\infty\infty$, ma $\frac{2+\cos x}{1}$ non ha limite: il teorema tace, mentre il limite vale $2$ per i carabinieri.
- Non si può usare per $\lim_{x\to0}\frac{\cos x}{x}$, che non è una forma indeterminata.

## Come si dimostra

Nel corso il teorema è enunciato senza dimostrazione ("teorema misterioso"); vedi la [[2026-10-28 - Teorema di De L'Hôpital e sviluppi di Taylor#1. Il teorema di De L'Hôpital|lezione del 28 ottobre]] per gli esempi e i controesempi.

## Vedi anche

- [[Forma indeterminata]]
- [[Derivata]]
- [[Sviluppo di Taylor]]
- [[Limiti notevoli]]
