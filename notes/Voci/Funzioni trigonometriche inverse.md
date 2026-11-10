---
title: Funzioni trigonometriche inverse
type: voce
categoria: oggetto
corsi:
- Analisi 1
introdotta_in: 2026-10-01 - Funzioni trigonometriche e funzioni inverse
alias:
- arcoseno
- arcocoseno
- arcotangente
- arcsin
- arccos
- arctan
sintesi: Arcoseno, arcocoseno e arcotangente sono le inverse di seno, coseno e tangente ristretti a un intervallo su cui sono biiettivi.
---
Le **funzioni trigonometriche inverse** si ottengono invertendo seno, coseno e tangente dopo averli ristretti a un intervallo in cui sono iniettivi.

## Definizione

- $\arcsin\colon[-1,1]\to\left[-\frac\pi2,\frac\pi2\right]$, inversa di $\sin$ ristretto a $\left[-\frac\pi2,\frac\pi2\right]$;
- $\arccos\colon[-1,1]\to[0,\pi]$, inversa di $\cos$ ristretto a $[0,\pi]$;
- $\arctan\colon\mathbb{R}\to\left(-\frac\pi2,\frac\pi2\right)$, inversa di $\tan$ ristretta a $\left(-\frac\pi2,\frac\pi2\right)$.

Per esempio $\arcsin x$ è l'unico angolo in $\left[-\frac\pi2,\frac\pi2\right]$ il cui seno è $x$.

## Intuizione

Poiché seno e coseno sono periodici, non possono essere iniettivi su tutto $\mathbb{R}$: si sceglie un "ramo principale". Il grafico dell'inversa è il simmetrico di quello della funzione rispetto a $y=x$. Le semplificazioni valgono solo negli intervalli principali:

$$
\arcsin(\sin x)=x\ \text{ per }x\in\left[-\tfrac\pi2,\tfrac\pi2\right],\qquad \sin(\arcsin x)=x\ \text{ per }x\in[-1,1].
$$

## Esempi

- $\arcsin(\sin2)=\pi-2$ e $\arccos(\cos4)=2\pi-4$.
- $\arcsin x+\arccos x=\frac\pi2$ per $x\in[-1,1]$.
- $\sin(\arccos x)=\sqrt{1-x^2}$.
- $\arctan x+\arctan\frac1x=\pm\frac\pi2$ (segno di $x$).

## Vedi anche

- [[Funzioni trigonometriche]]
- [[Funzione inversa]]
- [[Funzione biettiva]]
- [[Composizione di funzioni]]
