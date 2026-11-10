---
title: Limite di una funzione
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-12 - Limiti di funzioni, continuità e limiti notevoli
alias:
- limiti di funzioni
- limite destro
- limite sinistro
sintesi: Il limite dice a quale valore si avvicina una funzione quando la variabile si avvicina a un punto o all'infinito, senza guardare cosa succede nel punto stesso.
---

Il **limite di una funzione** descrive il valore (finito o infinito) verso cui tende $f(x)$ quando $x$ si avvicina a un punto $x_0$, oppure va a $+\infty$ o $-\infty$. È la versione per funzioni del [[Limite di una successione|limite di una successione]].

## Definizione

Sia $D\subseteq\mathbb{R}$ non vuoto, $f:D\to\mathbb{R}$ e $x_0$ un [[Punto di accumulazione|punto di accumulazione]] di $D$. Si scrive $\lim_{x\to x_0}f(x)=\ell\in\mathbb{R}$ se

$$
\forall\varepsilon>0\ \exists\delta>0\ \text{t.c.}\ |f(x)-\ell|\leq\varepsilon\quad\forall x\in\big(D\cap[x_0-\delta,x_0+\delta]\big)\setminus\{x_0\}.
$$

Per $\ell=\pm\infty$ si chiede $f(x)\geq M$ (risp. $f(x)\leq M$) per ogni $M\in\mathbb{R}$. Per $x\to\pm\infty$ si sostituisce l'intorno di $x_0$ con una semiretta $D\cap[k,+\infty)$ o $D\cap(-\infty,k]$. Il **limite destro** $x\to x_0^+$ e il **limite sinistro** $x\to x_0^-$ usano solo i punti a destra o a sinistra di $x_0$. L'esito può essere $\ell\in\mathbb{R}$, $+\infty$, $-\infty$ oppure "non esiste".

## Intuizione

È un gioco di sfida e risposta. Qualcuno sceglie la tolleranza $\varepsilon$ (o la soglia $M$), e noi dobbiamo trovare quanto vicino a $x_0$ (cioè $\delta$) bisogna stare perché $f(x)$ rispetti la tolleranza. Il valore $f(x_0)$ non conta, e può anche non esistere: il limite è una "previsione" basata su quello che succede lì vicino.

## Esempi

- $\lim_{x\to+\infty}\frac1x=0$: dato $\varepsilon$ basta prendere $k=\frac1\varepsilon$.
- $\lim_{x\to1}\frac{x^2-1}{x-1}=2$, anche se la funzione in $1$ non è definita, perché per $x\neq1$ vale $x+1$.
- $\lim_{x\to0^+}\frac1x=+\infty$ mentre $\lim_{x\to0^-}\frac1x=-\infty$, quindi $\lim_{x\to0}\frac1x$ non esiste.

## Come si dimostra

Per i calcoli si usano gli stessi strumenti delle successioni (confronto, [[Teorema dei carabinieri|carabinieri]], [[Teoremi algebrici sui limiti|teoremi algebrici]]) più i [[Limiti notevoli|limiti notevoli]]. Le definizioni complete sono nella [[2026-10-12 - Limiti di funzioni, continuità e limiti notevoli#1. Setting|lezione del 12 ottobre]].

## Vedi anche

- [[Punto di accumulazione]]
- [[Funzione continua]]
- [[Limite di una successione]]
- [[Limiti notevoli]]
