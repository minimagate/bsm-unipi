---
title: Legge di Leibniz
type: voce
categoria: teorema
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-13 - Quantificazione ristretta, uguaglianza e specifiche formali
alias:
- uguaglianza
- leggi del singoletto
sintesi: Se due termini sono uguali, una proprietà dell'uno vale se e solo se vale dell'altro; da qui seguono le leggi del singoletto.
---

La **legge di Leibniz** esprime il significato dell'uguaglianza nella logica del primo ordine: oggetti uguali sono indistinguibili.

## Enunciato

$$
x=y\Rightarrow(P\equiv P[y/x]),
$$

dove $P[y/x]$ è $P$ con le occorrenze libere di $x$ sostituite da $y$. Forme equivalenti:

$$
x=y\land P\equiv x=y\land P[y/x],
\qquad
(x=y\land P)\Rightarrow P[y/x].
$$

Dalla legge discendono le **leggi del singoletto**:

$$
(\forall x.\,(x=y)\Rightarrow P)\equiv P[y/x],
\qquad
(\exists x.\,(x=y)\land P)\equiv P[y/x].
$$

## Intuizione

Se $x$ e $y$ sono lo stesso individuo, dire $P(x)$ o $P(y)$ è la stessa cosa. La condizione $x=y$ restringe il dominio a un solo elemento, quindi quantificare su $x$ equivale a sostituire $y$ al posto di $x$.

## Esempi

Con $y=3$ e $P=\operatorname{pari}(x)$: $(\exists x.\,x=3\land\operatorname{pari}(x))\equiv\operatorname{pari}(3)$.

L'uguaglianza serve anche per dire "tutti tranne uno": «tutti gli studenti di FPL tranne uno vanno al cinema» si scrive

$$
\exists x.\bigl(\operatorname{segueFPL}(x)\land\neg\operatorname{vaCinema}(x)\land\forall y.(\operatorname{segueFPL}(y)\land\neg(x=y)\Rightarrow\operatorname{vaCinema}(y))\bigr).
$$

## Come si dimostra

La seconda legge del singoletto si ottiene con Leibniz, la distributività e $(\exists x.\,x=y)\equiv\mathrm T$; la prima ne discende con De Morgan. Vedi [[2026-10-13 - Quantificazione ristretta, uguaglianza e specifiche formali#2.2 Leggi del singoletto|nella lezione del 13 ottobre]].

## Vedi anche

- [[Quantificazione ristretta]]
- [[Principio di sostituzione]]
- [[Skolemizzazione]]
- [[Quantificatore]]
