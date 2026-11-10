---
title: Gerarchia degli infiniti
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti
alias:
- ordine degli infiniti
- confronto tra infiniti
sintesi: Tra le successioni che divergono, le potenze sono dominate dagli esponenziali, questi dai fattoriali e i fattoriali da n alla n.
---
La **gerarchia degli infiniti** stabilisce in che ordine crescono le successioni che tendono a $+\infty$: quando se ne mette una a denominatore di un'altra, vince quella che cresce più in fretta.

## Enunciato

Per ogni $a>1$ e ogni $k$ fissato, quando $n\to+\infty$:

$$
n^k\ \prec\ a^n\ \prec\ n!\ \prec\ n^n,
$$

nel senso che il rapporto tra una successione e quella che la segue tende a $0$. In particolare:

$$
\frac{a^n}{n^k}\to+\infty,\qquad \frac{n!}{a^n}\to+\infty,\qquad \frac{n^n}{n!}\to+\infty.
$$

## Intuizione

L'esponenziale ($a^n$) comanda su ogni potenza di $n$, il fattoriale comanda su ogni esponenziale, e $n^n$ comanda sul fattoriale. È lo strumento per decidere "chi comanda" quando si calcola un limite, e quindi cosa raccogliere.

## Esempi

- $\frac{3^n}{n^{78}}\to+\infty$ (esponenziale contro potenza).
- $\frac{n!}{3^n}\to+\infty$.
- $\frac{\sqrt[n]{n!}}{n}\to\frac1e$.

## Come si dimostra

Per ciascun rapporto si applica il [[Criterio del rapporto|criterio del rapporto]]: ad esempio per $\frac{3^n}{n^{78}}$ il rapporto tra termini consecutivi è $3\left(\frac n{n+1}\right)^{78}\to3>1$. Si veda [[2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti#6. Gerarchia degli infiniti: esempi con il rapporto|Gerarchia degli infiniti: esempi con il rapporto]].

## Vedi anche

- [[Criterio del rapporto]]
- [[Criterio della radice]]
- [[Numero di Nepero]]
- [[Forma indeterminata]]
