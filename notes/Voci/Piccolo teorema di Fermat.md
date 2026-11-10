---
title: Piccolo teorema di Fermat
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-11-09 - Classi laterali e teorema di Lagrange
alias:
- teorema di Fermat-Eulero
- teorema di Eulero
- Fermat
sintesi: Se a è coprimo con m, allora a elevato a phi di m è congruente a 1 modulo m; per m primo si ottiene la forma di Fermat.
---

Il **piccolo teorema di Fermat** e la sua generalizzazione, il **teorema di Eulero**, dicono che le potenze di un numero coprimo con il modulo tornano a $1$ dopo al più $\varphi(m)$ passi.

## Enunciato

**Teorema di Eulero.** Se $\gcd(a,m)=1$ allora

$$
a^{\varphi(m)}\equiv1\pmod m,
$$

dove $\varphi(m)$ è il numero di interi tra $1$ e $m$ coprimi con $m$.

**Piccolo teorema di Fermat.** Se $p$ è primo e $p\nmid a$, allora

$$
a^{p-1}\equiv1\pmod p.
$$

## Intuizione

Le classi invertibili modulo $m$ formano un gruppo con $\varphi(m)$ elementi. In un gruppo finito, elevando un elemento alla taglia del gruppo si torna all'identità: è questo il fatto che si sta usando.

## Esempi

- $m=9$: $\varphi(9)=6$ e $2^6=64\equiv1\pmod9$.
- $p=7$, $a=3$: $3^6=729\equiv1\pmod7$.
- $\operatorname{ord}_{17}(\overline a)$ divide $\varphi(17)=16$, quindi i possibili ordini sono $1,2,4,8,16$.

## Come si dimostra

Si applica il [[Teorema di Lagrange|teorema di Lagrange]] al gruppo $(\mathbb Z/m\mathbb Z)^\times$ di ordine $\varphi(m)$: l'[[Ordine di un elemento|ordine]] di $[a]$ divide $\varphi(m)$, quindi $[a]^{\varphi(m)}=[1]$. Si veda la [[2026-11-09 - Classi laterali e teorema di Lagrange#9. Teorema di Fermat ed Eulero|sezione su Fermat ed Eulero]] della lezione del 9 novembre.

## Vedi anche

- [[Teorema di Lagrange]]
- [[Elementi invertibili modulo n]]
- [[Ordine di un elemento]]
- [[Congruenza modulo n]]
