---
type: lecture-note
course: Aritmetica
date: '2026-10-19'
title: Dimostrazione del teorema cinese del resto
source: Quando_G._Bresciani_fa__teoria_2.pdf
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Aritmetica/Lectures/2026-10-19 - Dimostrazione del teorema cinese del resto.md
vault_hash: 1b4de2f11726685d9235008a6a95fb91db3bcb15a24fe35b9353461d92a70cf2
---

# Dimostrazione del teorema cinese del resto

Lezione di teoria di G. Bresciani del 19/10. Si dimostra il **[[Teorema cinese del resto|teorema cinese del resto]]** per un numero qualsiasi di moduli a due a due [[Numeri coprimi|coprimi]]: prima un lemma sul MCD di un prodotto, poi il teorema per [[Principio di induzione|induzione]] sul numero di moduli. In coda c'è un metodo pratico per trovare l'[[Inverso modulo n|inverso moltiplicativo]] modulo $b$.

L'enunciato e il metodo di risoluzione per due congruenze compaiono anche negli appunti di Aritmetica, in [[2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari#Teorema cinese del resto|Fattorizzazione unica, congruenze e sistemi modulari]]. Qui si aggiungono la dimostrazione completa e il caso di $n$ moduli.

Notazione: $(a,b)$ indica il [[Massimo comun divisore|massimo comun divisore]] $\gcd(a,b)$.

---

## 1. Enunciato

**Teorema cinese del resto.** Siano $m_1,\dots,m_n$ interi con $(m_i,m_j)=1$ per ogni $i\neq j$. Allora il sistema

$$
\begin{cases}
x\equiv a_1\pmod{m_1}\\
\quad\vdots\\
x\equiv a_n\pmod{m_n}
\end{cases}
$$

ha soluzione, e la soluzione è **unica modulo** $\displaystyle\prod_{i=1}^n m_i$.

*Nota (mia):* gli appunti non riscrivono l'enunciato prima della dimostrazione; questa è la forma che la dimostrazione stabilisce.

> [!example] Esempio
> Il sistema $x\equiv1\pmod2$, $x\equiv2\pmod3$ ha moduli coprimi. Le soluzioni sono tutti e soli gli $x\equiv5\pmod6$: per esempio $5$ è dispari e $5=3+2$, e ogni altra soluzione differisce da $5$ per un multiplo di $6=2\cdot3$.

---

## 2. Lemma sul MCD di un prodotto

**Lemma.** Siano $a,m,n\in\mathbb Z$. Allora:

1. $(a,mn)=1\iff(a,m)=1\land(a,n)=1$;
2. $(m,n)=1\implies(a,mn)=(a,m)\cdot(a,n)$.

**Dimostrazione.** Si usano le fattorizzazioni in primi. Dati $a,b\in\mathbb Z$, siano $p_1,\dots,p_s$ i primi che dividono $a$ o $b$, e scriviamo

$$
a=\prod_{i=1}^s p_i^{\alpha_i},\qquad b=\prod_{i=1}^s p_i^{\beta_i},\qquad\alpha_i,\beta_i\geq0.
$$

Sappiamo che

$$
(a,b)=\prod_{i=1}^s p_i^{\min(\alpha_i,\beta_i)}.
$$

Quindi

$$
(a,b)=1\iff\forall i\ \min(\alpha_i,\beta_i)=0\iff a,b\text{ non hanno primi in comune}.
$$

**Punto 1.** $(a,mn)=1$ se e solo se $a$ e $mn$ non hanno primi in comune. I primi di $mn$ sono quelli di $m$ insieme a quelli di $n$. Quindi la condizione vale se e solo se $a$ non ha primi in comune né con $m$ né con $n$, cioè $(a,m)=1$ e $(a,n)=1$.

**Punto 2.** Poiché $(m,n)=1$, $m$ e $n$ non hanno primi in comune. Scriviamo

$$
m=\prod_{i=1}^t p_i^{\gamma_i},\qquad n=\prod_{j=1}^s q_j^{\delta_j},\qquad\gamma_i,\delta_j\geq0,\quad p_i\neq q_j\ \ \forall i,j.
$$

Supponiamo

$$
a=\Bigl(\prod_{i=1}^t p_i^{\alpha_i}\Bigr)\Bigl(\prod_{j=1}^s q_j^{\beta_j}\Bigr).
$$

Allora

$$
(a,mn)=\Bigl(\prod_{i=1}^t p_i^{\min(\alpha_i,\gamma_i)}\Bigr)\Bigl(\prod_{j=1}^s q_j^{\min(\beta_j,\delta_j)}\Bigr)=(a,m)\cdot(a,n).
$$

L'ultima uguaglianza viene dalla formula del MCD applicata separatamente: il primo fattore è $(a,m)$ e il secondo è $(a,n)$. $\blacksquare$

*Nota (mia):* nel punto 2 si scrive $a$ usando solo i primi di $m$ e di $n$. Eventuali altri primi di $a$ non dividono $mn$, quindi non contribuiscono a nessuno dei MCD. Nella prima riga della dimostrazione gli appunti scrivono anche «$(a,b)=1$»: va letto come il caso che si vuole caratterizzare, non come un'ipotesi. Le fattorizzazioni presuppongono inoltre $a,b\neq0$.

---

## 3. Dimostrazione del teorema

Per **induzione su $n$**, il numero di moduli.

### 3.1 Caso base: $n=2$

Consideriamo

$$
\begin{cases}
x\equiv a_1\pmod{m_1}\\
x\equiv a_2\pmod{m_2}
\end{cases}
\qquad(m_1,m_2)=1.
$$

**Esistenza.** Dalla prima congruenza scriviamo $x=a_1+\lambda m_1$ con $\lambda\in\mathbb Z$ e sostituiamo nella seconda:

$$
\lambda m_1\equiv a_2-a_1\pmod{m_2}.
$$

Per l'[[Identità di Bézout|identità di Bézout]] esistono $y,z\in\mathbb Z$ con

$$
m_1y+m_2z=1,\qquad\text{cioè}\qquad m_1y\equiv1\pmod{m_2}.
$$

Quindi $y$ è l'**inverso moltiplicativo di $m_1$ modulo $m_2$** (vedi §4 per trovarlo in pratica). Moltiplicando la congruenza in $\lambda$ per $y$ si ottiene

$$
\lambda\equiv(a_2-a_1)y\pmod{m_2}.
$$

Scegliamo $\lambda=(a_2-a_1)y+Km_2$ con $K=0$ e sostituiamo in $x=a_1+\lambda m_1$:

$$
x=a_1+(a_2-a_1)y\,m_1=a_1+(a_2-a_1)(1-m_2z)\equiv a_1+a_2-a_1=a_2\pmod{m_2}.
$$

Inoltre ovviamente $x\equiv a_1\pmod{m_1}$, quindi $x$ è soluzione.

**Unicità modulo $m_1m_2$.** Sia $x'$ un'altra soluzione: $x'\equiv a_1\pmod{m_1}$ e $x'\equiv a_2\pmod{m_2}$. Allora

$$
x-x'\equiv0\pmod{m_1},\qquad x-x'\equiv0\pmod{m_2},
$$

cioè $m_1\mid x-x'$ e $m_2\mid x-x'$. Per il punto 2 del lemma, applicato con $a=x-x'$,

$$
(x-x',m_1m_2)=(x-x',m_1)\cdot(x-x',m_2)=m_1\cdot m_2,
$$

quindi $m_1m_2\mid x-x'$, cioè $x\equiv x'\pmod{m_1m_2}$.

### 3.2 Passo induttivo

Supponiamo che ogni sistema di $n-1$ congruenze con moduli a due a due coprimi ammetta un'unica soluzione modulo il prodotto dei moduli. Consideriamo

$$
\begin{cases}
x\equiv a_1\pmod{m_1}\\
\quad\vdots\\
x\equiv a_n\pmod{m_n}
\end{cases}
\qquad(m_i,m_j)=1\ \ \forall i\neq j.
$$

Per ipotesi induttiva esiste $y\in\mathbb Z$ tale che

$$
\begin{cases}
y\equiv a_1\pmod{m_1}\\
\quad\vdots\\
y\equiv a_{n-1}\pmod{m_{n-1}}
\end{cases}
$$

e tale $y$ è unico modulo $\prod_{i=1}^{n-1}m_i$. Allora il sistema diventa

$$
\begin{cases}
x\equiv y\pmod{\prod_{i=1}^{n-1}m_i}\\
x\equiv a_n\pmod{m_n}.
\end{cases}
$$

*Esplicitazione (mia):* è qui che serve l'unicità dell'ipotesi induttiva. Un intero $x$ soddisfa le prime $n-1$ congruenze se e solo se $x\equiv y$ modulo il loro prodotto.

Per il lemma (punto 1, applicato ripetutamente)

$$
\Bigl(m_n,\prod_{i=1}^{n-1}m_i\Bigr)=\prod_{i=1}^{n-1}(m_n,m_i)=1.
$$

Il nuovo sistema ha quindi due moduli coprimi e, per il caso $n=2$, ha un'unica soluzione modulo $\prod_{i=1}^n m_i$. $\blacksquare$

---

## 4. Come trovare l'inverso moltiplicativo di $a$ modulo $b$

Vogliamo $K\in\mathbb Z$ tale che

$$
aK\equiv1\pmod b.
$$

Scriviamo $aK=1+bh$ con $h\in\mathbb Z$ e cerchiamo il **minimo $h$** tale che $a\mid bh+1$. Se $h_0$ è tale minimo, allora $aK_0=bh_0+1$ e $K_0$ è il $K$ cercato.

**Morale:** lavorare sempre con moduli piccoli.

*Esempio (mio).* Inverso di $5$ modulo $7$: si cerca $h\geq0$ con $5\mid7h+1$.

| $h$ | $7h+1$ | divisibile per $5$? |
|---|---|---|
| $0$ | $1$ | no |
| $1$ | $8$ | no |
| $2$ | $15$ | sì |

Quindi $K_0=15/5=3$, e infatti $5\cdot3=15\equiv1\pmod7$. Basta provare $h=0,1,\dots,a-1$, perché conta solo $h$ modulo $a$: il numero di tentativi dipende da $a$, ed è uno dei motivi per cui conviene tenere piccoli i numeri in gioco.

## Fonte

- Appunti «Quando G. Bresciani fa teoria 2», lezione del 19/10 (file `Quando_G._Bresciani_fa__teoria_2.pdf`, 2 pagine manoscritte).
- Le parti segnate «mia» o «mio» non compaiono negli appunti.
