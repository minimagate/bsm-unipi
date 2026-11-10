---
type: lecture-note
course: Aritmetica
date: '2026-10-08'
title: Fattorizzazione unica, congruenze e sistemi modulari
source_transcript: _transcripts/Aritmetica/2026-10-07 - Fattorizzazione unica, congruenze e sistemi modulari.md
source_hash: sha256:365206487b4ab9b8232c23e5429a4dccc63dc5bfaef3ab1a4bb4ebb3a4d5c4c8
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-07T11:02:00.436Z'
original_date: '2026-10-07'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Aritmetica/Lectures/2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari.md
vault_hash: 83470643b7504b41537d969e4c70135acc818e69d8455432691bcedab3f227a3
---

## 1. Fattorizzazione in numeri primi

Ci occupiamo della fattorizzazione degli interi positivi. I numeri negativi non si trattano direttamente: la fattorizzazione di un numero negativo si ottiene, se serve, aggiungendo il fattore $-1$.

Un intero $n>1$ ammette una fattorizzazione in [[Numero primo|numeri primi]], cioè si scrive come

$$
n=p_1p_2\cdots p_L,
$$

dove ogni $p_i$ è primo.

La **lunghezza** della fattorizzazione è il numero di fattori primi che vi compaiono, contando le ripetizioni. Per esempio,

$$
32=2^5=2\cdot 2\cdot 2\cdot 2\cdot 2
$$

ha una fattorizzazione di lunghezza $5$. Gli esponenti nella scrittura con le potenze indicano quante volte compare ciascun primo.

L’esistenza di una fattorizzazione era già stata dimostrata. Resta da dimostrare che è unica, a meno dell’ordine dei fattori.

---

## 2. Unicità della fattorizzazione in primi

### Teorema fondamentale dell’aritmetica

Ogni intero $n>1$ si scrive come prodotto di numeri primi in modo unico, a meno dell’ordine dei fattori. È il [[Teorema fondamentale dell'aritmetica|teorema fondamentale dell’aritmetica]].

In altre parole, se

$$
n=p_1p_2\cdots p_L=q_1q_2\cdots q_S,
$$

con tutti i $p_i$ e i $q_j$ primi, allora $L=S$ e, dopo aver riordinato opportunamente gli indici,

$$
p_i=q_i \qquad \text{per ogni } i.
$$

L’unicità si dimostra per induzione sulla lunghezza $L$ di una fattorizzazione.

### Caso base: $L=1$

Se una fattorizzazione ha lunghezza $1$, allora

$$
n=p_1
$$

è primo. Un numero primo non si può scrivere come prodotto di due interi entrambi non banali: se

$$
p_1=ab,
$$

siccome $p_1$ è primo, uno tra $a$ e $b$ deve essere $1$. Quindi non esiste una seconda fattorizzazione non banale.

### Passo induttivo

Supponiamo che l’unicità valga per tutte le fattorizzazioni di lunghezza $L-1$ e prendiamo un numero $n$ con una fattorizzazione di lunghezza $L$:

$$
n=p_1p_2\cdots p_L.
$$

Supponiamo che $n$ abbia anche un’altra fattorizzazione:

$$
n=q_1q_2\cdots q_S.
$$

Siccome $p_1$ divide $n$, si ha

$$
p_1\mid q_1q_2\cdots q_S.
$$

Usiamo il fatto fondamentale (il [[Lemma di Euclide|lemma di Euclide]] sui primi):

> Se un primo divide un prodotto, allora divide almeno uno dei fattori del prodotto.

Quindi $p_1$ divide uno dei $q_j$. Riordinando i fattori della seconda fattorizzazione, possiamo supporre

$$
p_1\mid q_1.
$$

Poiché $q_1$ è primo e anche $p_1$ è primo, l’unico modo in cui $p_1$ può dividere $q_1$ è

$$
p_1=q_1.
$$

Infatti, se $q_1=p_1k$, siccome $q_1$ è primo, $k=1$.

Le due fattorizzazioni hanno dunque lo stesso primo iniziale, e lo si può cancellare dall’uguaglianza:

$$
p_1p_2\cdots p_L=q_1q_2\cdots q_S
$$

e, siccome $p_1=q_1$,

$$
p_2\cdots p_L=q_2\cdots q_S.
$$

Il numero

$$
m=\frac{n}{p_1}
$$

ha quindi una fattorizzazione di lunghezza $L-1$. Per ipotesi induttiva, le due fattorizzazioni rimanenti coincidono a meno dell’ordine. Ne segue che coincidono anche le fattorizzazioni iniziali di $n$.

In particolare deve essere

$$
L-1=S-1,
$$

quindi $L=S$, e i fattori primi sono gli stessi, eventualmente in un ordine diverso.

> [!warning]
> Unicità non vuol dire che i fattori debbano comparire nello stesso ordine. Per esempio,
>
> $$
> 2\cdot 3\cdot 5=5\cdot 2\cdot 3.
> $$
>
> L’unicità è sempre intesa **a meno dell’ordine dei fattori**.

La dimostrazione usa due concetti distinti:

1. il concetto di numero primo;
2. la proprietà per cui un primo che divide un prodotto deve dividere uno dei fattori.

Il secondo fatto è essenziale per confrontare due fattorizzazioni.

---

## 3. Congruenze modulo $n$

Siano $a,b\in\mathbb Z$ e sia $n\in\mathbb Z$, con $n>0$.

Si dice che $a$ è **congruo** a $b$ modulo $n$, e si scrive

$$
a\equiv b\pmod n,
$$

se $n$ divide la differenza $a-b$:

$$
a\equiv b\pmod n
\quad\Longleftrightarrow\quad
n\mid(a-b).
$$

È la [[Congruenza modulo n|congruenza modulo $n$]]. In modo equivalente, esiste $k\in\mathbb Z$ tale che

$$
a-b=kn,
$$

ossia

$$
a=b+kn.
$$

Due numeri congrui modulo $n$, quindi, differiscono per un multiplo di $n$.

### Interpretazione tramite il resto

Per la [[Divisione euclidea|divisione euclidea]], ogni intero $a$ si scrive in modo unico come

$$
a=qn+r,
\qquad 0\le r<n.
$$

Il numero $r$ è il resto della divisione di $a$ per $n$.

Due interi sono congrui modulo $n$ se e solo se hanno lo stesso resto nella divisione per $n$:

$$
a\equiv b\pmod n
\quad\Longleftrightarrow\quad
\text{$a$ e $b$ hanno lo stesso resto modulo $n$}.
$$

Infatti, se

$$
a=q_1n+r,\qquad b=q_2n+r,
$$

allora

$$
a-b=(q_1-q_2)n,
$$

quindi $n\mid(a-b)$.

Viceversa, se $n\mid(a-b)$, i resti di $a$ e $b$ modulo $n$ devono coincidere.

Per esempio,

$$
17\equiv 2\pmod 5,
$$

perché

$$
17-2=15
$$

è divisibile per $5$.

Anche tutti i numeri della forma

$$
2+5k,\qquad k\in\mathbb Z,
$$

sono congrui a $2$ modulo $5$.

---

### 4. La relazione di congruenza è una relazione di equivalenza

La congruenza modulo $n$ è una [[Relazione di equivalenza|relazione di equivalenza]] su $\mathbb Z$.

#### Riflessività

Per ogni $a\in\mathbb Z$,

$$
a\equiv a\pmod n,
$$

perché

$$
a-a=0
$$

è divisibile per $n$.

#### Simmetria

Se

$$
a\equiv b\pmod n,
$$

allora $n\mid(a-b)$. Siccome

$$
b-a=-(a-b),
$$

segue anche $n\mid(b-a)$, quindi

$$
b\equiv a\pmod n.
$$

#### Transitività

Se

$$
a\equiv b\pmod n
\qquad\text{e}\qquad
b\equiv c\pmod n,
$$

allora $n\mid(a-b)$ e $n\mid(b-c)$. Sommando,

$$
(a-b)+(b-c)=a-c,
$$

perciò $n\mid(a-c)$ e quindi

$$
a\equiv c\pmod n.
$$

La transitività si vede anche con le rappresentazioni:

$$
a=b+k n,\qquad b=c+\ell n.
$$

Sostituendo la seconda nella prima,

$$
a=c+(\ell+k)n,
$$

quindi $a\equiv c\pmod n$.

---

## 5. Classi di congruenza

La [[Classe di congruenza|classe di congruenza]] di $a$ modulo $n$ è l’insieme

$$
[a]_n=\{b\in\mathbb Z:b\equiv a\pmod n\}.
$$

Equivalentemente,

$$
[a]_n=\{a+kn:k\in\mathbb Z\}.
$$

La classe $[a]_n$ è dunque una progressione aritmetica di ragione $n$.

Per esempio, modulo $5$:

$$
[0]_5=\{\ldots,-10,-5,0,5,10,\ldots\},
$$

$$
[1]_5=\{\ldots,-9,-4,1,6,11,\ldots\},
$$

$$
[2]_5=\{\ldots,-8,-3,2,7,12,\ldots\},
$$

e così via per $[3]_5$ e $[4]_5$.

Ogni intero appartiene a una e una sola delle classi

$$
[0]_n,[1]_n,\ldots,[n-1]_n.
$$

Queste sono tutte le classi di congruenza modulo $n$. L’insieme delle classi modulo $n$ si può quindi rappresentare con i resti

$$
0,1,\ldots,n-1.
$$

Per esempio, modulo $6$ le classi sono

$$
[0]_6,[1]_6,[2]_6,[3]_6,[4]_6,[5]_6.
$$

La classe $[0]_6$ contiene tutti i multipli di $6$, mentre $[2]_6$ contiene tutti gli interi congrui a $2$ modulo $6$.

> [!note]
> Un numero e la sua classe non sono esattamente lo stesso oggetto: il numero $2$ è un intero, mentre $[2]_n$ è l’insieme di tutti gli interi congrui a $2$ modulo $n$. Però, di solito, si rappresenta una classe con uno dei suoi elementi, tipicamente il resto tra $0$ e $n-1$.

---

## 6. Operazioni con le congruenze

Le congruenze sono compatibili con somma, sottrazione e moltiplicazione.

Se

$$
a\equiv b\pmod n
\qquad\text{e}\qquad
c\equiv d\pmod n,
$$

allora:

$$
a+c\equiv b+d\pmod n,
$$

$$
a-c\equiv b-d\pmod n,
$$

e

$$
ac\equiv bd\pmod n.
$$

### Dimostrazione per somma

Dalle ipotesi esistono $k,\ell\in\mathbb Z$ tali che

$$
a=b+kn,\qquad c=d+\ell n.
$$

Sommando,

$$
a+c=b+d+(k+\ell)n.
$$

Quindi

$$
a+c\equiv b+d\pmod n.
$$

### Dimostrazione per prodotto

Scriviamo ancora

$$
a=b+kn,\qquad c=d+\ell n.
$$

Allora

$$
ac=(b+kn)(d+\ell n).
$$

Sviluppando,

$$
ac=bd+b\ell n+dk n+k\ell n^2.
$$

Tutti i termini oltre a $bd$ sono multipli di $n$, quindi

$$
ac\equiv bd\pmod n.
$$

In particolare, se

$$
a\equiv b\pmod n,
$$

allora, per ogni $k\in\mathbb N$,

$$
a^k\equiv b^k\pmod n.
$$

Più in generale, in qualsiasi espressione costruita con somme e prodotti si può sostituire un numero con un altro congruo.

Per esempio, per calcolare una potenza modulo $n$ si può prima ridurre la base modulo $n$:

$$
a\equiv r\pmod n
\quad\Longrightarrow\quad
a^k\equiv r^k\pmod n.
$$

---

### Ridurre i termini prima di calcolare

Il vantaggio delle congruenze è che si possono sostituire numeri molto grandi con i loro resti modulo $n$.

Per calcolare, per esempio,

$$
85\cdot 38\pmod 7,
$$

si osserva prima che

$$
85\equiv 1\pmod 7,
\qquad
38\equiv 3\pmod 7.
$$

Quindi

$$
85\cdot 38\equiv 1\cdot 3\equiv 3\pmod 7.
$$

Lo stesso principio vale per somme, prodotti e potenze.

---

## 7. Criteri di divisibilità ottenuti dalle congruenze

### Divisibilità per $3$

Se un numero in base $10$ è

$$
N=a_0+10a_1+10^2a_2+\cdots+10^ka_k,
$$

dove $a_0,\ldots,a_k$ sono le sue cifre, allora

$$
10\equiv 1\pmod 3.
$$

Di conseguenza,

$$
10^j\equiv 1\pmod 3
\qquad\text{per ogni }j.
$$

Quindi,

$$
N\equiv a_0+a_1+\cdots+a_k\pmod 3.
$$

Ne segue il criterio:

> Un numero è divisibile per $3$ se e solo se è divisibile per $3$ la somma delle sue cifre.

Per esempio,

$$
12345\equiv 1+2+3+4+5=15\equiv 0\pmod 3,
$$

quindi $12345$ è divisibile per $3$.

### Divisibilità per $9$

Siccome

$$
10\equiv 1\pmod 9,
$$

si ha anche

$$
10^j\equiv 1\pmod 9.
$$

Quindi un numero è congruo modulo $9$ alla somma delle sue cifre:

$$
N\equiv a_0+a_1+\cdots+a_k\pmod 9.
$$

Questo dà il criterio di divisibilità per $9$.

### Divisibilità per $11$

Modulo $11$ vale

$$
10\equiv -1\pmod{11}.
$$

Quindi,

$$
10^2\equiv 1\pmod{11},\qquad
10^3\equiv -1\pmod{11},
$$

e in generale

$$
10^j\equiv (-1)^j\pmod{11}.
$$

Se

$$
N=a_0+10a_1+10^2a_2+\cdots+10^ka_k,
$$

allora

$$
N\equiv a_0-a_1+a_2-a_3+\cdots \pmod{11}.
$$

Si ottiene il criterio:

> Un numero è divisibile per $11$ se e solo se la somma alternata delle sue cifre è divisibile per $11$.

La somma alternata si può calcolare anche partendo dalla cifra più significativa: cambia al più il segno complessivo, e questo non modifica la divisibilità per $11$.

---

## 8. Cancellazione nelle congruenze

Dalle congruenze si può sempre moltiplicare per un intero. La cancellazione, invece, richiede attenzione.

Se

$$
ac\equiv bc\pmod n,
$$

allora

$$
n\mid c(a-b).
$$

Non si può sempre concludere che

$$
a\equiv b\pmod n.
$$

La cancellazione di $c$ è lecita se $c$ è invertibile modulo $n$, cioè se

$$
\gcd(c,n)=1.
$$

In tal caso esiste un intero $c^{-1}$ tale che

$$
cc^{-1}\equiv 1\pmod n,
$$

e moltiplicando la congruenza per $c^{-1}$ si ottiene

$$
a\equiv b\pmod n.
$$

Più in generale, posto

$$
d=\gcd(c,n),
$$

dalla relazione

$$
ac\equiv bc\pmod n
$$

si può dedurre soltanto

$$
a\equiv b\pmod{\frac{n}{d}}.
$$

Quindi si può cancellare un fattore $c$ modulo $n$ sostituendo il modulo $n$ con

$$
\frac{n}{\gcd(c,n)}.
$$

#### Esempio

La congruenza

$$
2a\equiv 2b\pmod 6
$$

non permette di concludere direttamente che $a\equiv b\pmod 6$. Infatti $\gcd(2,6)=2$, e dopo la cancellazione si ottiene

$$
a\equiv b\pmod 3.
$$

---

## 9. Congruenze lineari

Consideriamo una [[Congruenza lineare|congruenza lineare]]

$$
ax\equiv b\pmod n,
$$

dove $a,b\in\mathbb Z$ e $n>0$.

Per definizione,

$$
ax\equiv b\pmod n
\quad\Longleftrightarrow\quad
n\mid(ax-b).
$$

Quindi esiste $k\in\mathbb Z$ tale che

$$
ax-b=kn,
$$

ovvero

$$
ax-kn=b.
$$

Risolvere la congruenza equivale quindi a cercare le soluzioni intere dell’[[Equazione diofantea lineare|equazione diofantea]]

$$
ax+ny=b,
$$

dove si è posto $y=-k$.

---

### Teorema di esistenza delle soluzioni

Sia

$$
d=\gcd(a,n).
$$

La congruenza

$$
ax\equiv b\pmod n
$$

ha soluzione se e solo se

$$
d\mid b.
$$

#### Dimostrazione della necessità

Se $x$ è soluzione, allora

$$
ax\equiv b\pmod n,
$$

quindi esiste $k\in\mathbb Z$ tale che

$$
ax-b=kn.
$$

Perciò

$$
b=ax-kn.
$$

Siccome $d$ divide sia $a$ sia $n$, divide anche $ax$ e $kn$, e dunque la loro differenza:

$$
d\mid(ax-kn)=b.
$$

Quindi necessariamente

$$
d\mid b.
$$

#### Dimostrazione della sufficienza

Supponiamo ora che $d\mid b$. Scriviamo

$$
a=da_1,\qquad n=dn_1,\qquad b=db_1,
$$

con

$$
\gcd(a_1,n_1)=1.
$$

L’equazione

$$
ax+ny=b
$$

diventa

$$
da_1x+dn_1y=db_1,
$$

e, dividendo per $d$,

$$
a_1x+n_1y=b_1.
$$

Siccome $\gcd(a_1,n_1)=1$, l’[[Identità di Bézout|identità di Bézout]] garantisce l’esistenza di interi $u,v$ tali che

$$
a_1u+n_1v=1.
$$

Moltiplicando per $b_1$,

$$
a_1(ub_1)+n_1(vb_1)=b_1.
$$

Quindi $x=ub_1$ è una soluzione dell’equazione ridotta e dunque della congruenza iniziale.

---

### Forma delle soluzioni

Supponiamo che $d=\gcd(a,n)$ divida $b$ e che $x_0$ sia una soluzione particolare di

$$
ax\equiv b\pmod n.
$$

Allora tutte le soluzioni sono date da

$$
x\equiv x_0\pmod{\frac nd}.
$$

Equivalentemente,

$$
x=x_0+k\frac nd,
\qquad k\in\mathbb Z.
$$

Modulo $n$, le soluzioni distinte sono esattamente $d$:

$$
x_0,\quad
x_0+\frac nd,\quad
x_0+2\frac nd,\quad \ldots,\quad
x_0+(d-1)\frac nd.
$$

#### Caso particolare: $\gcd(a,n)=1$

Se

$$
\gcd(a,n)=1,
$$

allora $a$ è invertibile modulo $n$. Esiste $a^{-1}$ tale che

$$
aa^{-1}\equiv 1\pmod n.
$$

Moltiplicando la congruenza

$$
ax\equiv b\pmod n
$$

per $a^{-1}$ si ottiene l’unica soluzione modulo $n$:

$$
x\equiv a^{-1}b\pmod n.
$$

In questo caso la congruenza ha una sola classe di soluzioni modulo $n$.

> [!example] Esempio
> Risolviamo $4x\equiv 6\pmod{10}$. Qui $d=\gcd(4,10)=2$ divide $6$, quindi ci sono soluzioni, e sono $2$ modulo $10$. Una soluzione è $x_0=4$ (infatti $16\equiv 6$), e l’altra è $x_0+\frac{10}{2}=9$ (infatti $36\equiv 6$).

---

### Esempio di congruenza senza soluzione

Consideriamo una congruenza in cui il massimo comune divisore dei coefficienti non divide il termine noto. Se, per esempio,

$$
\gcd(14,21)=7
$$

e il termine noto non è divisibile per $7$, la congruenza

$$
14x\equiv b\pmod{21}
$$

non può avere soluzioni.

In particolare, se $b=15$, siccome

$$
7\nmid 15,
$$

la congruenza

$$
14x\equiv 15\pmod{21}
$$

è impossibile.

Il criterio del MCD permette quindi di stabilire se esistono soluzioni prima ancora di provare a calcolarle.

---

## 10. Calcolo dell’inverso modulo $n$

Per trovare l’[[Inverso modulo n|inverso]] di $a$ modulo $n$ bisogna risolvere

$$
ax\equiv 1\pmod n,
$$

equivalente all’equazione diofantea

$$
ax+ny=1.
$$

Questa equazione ha soluzione se e solo se

$$
\gcd(a,n)=1.
$$

L’algoritmo euclideo esteso permette di trovare esplicitamente i coefficienti di Bézout.

#### Esempio generale

Se l’algoritmo euclideo esteso fornisce

$$
ua+vn=1,
$$

allora, passando modulo $n$,

$$
ua\equiv 1\pmod n.
$$

Quindi $u$ è un inverso di $a$ modulo $n$:

$$
a^{-1}\equiv u\pmod n.
$$

Trovato l’inverso, la congruenza

$$
ax\equiv b\pmod n
$$

si risolve con

$$
x\equiv a^{-1}b\pmod n.
$$

---

## 11. Sistemi di congruenze

Consideriamo sistemi del tipo

$$
\begin{cases}
x\equiv a_1\pmod{m_1},\\
x\equiv a_2\pmod{m_2}.
\end{cases}
$$

Il problema è trovare tutti gli interi $x$ che soddisfano contemporaneamente le due congruenze.

### Riduzione a una congruenza

Dalla prima congruenza si può scrivere

$$
x=a_1+k m_1.
$$

Sostituendo nella seconda,

$$
a_1+k m_1\equiv a_2\pmod{m_2},
$$

quindi

$$
m_1k\equiv a_2-a_1\pmod{m_2}.
$$

Si ottiene così una nuova congruenza lineare nell’incognita $k$. Trovato $k$, si ricava $x$ dalla relazione

$$
x=a_1+k m_1.
$$

La risolubilità della congruenza per $k$ dipende da

$$
\gcd(m_1,m_2).
$$

Il sistema ha soluzione se e solo se

$$
\gcd(m_1,m_2)\mid(a_2-a_1).
$$

Infatti le due congruenze devono essere compatibili: la differenza tra i termini noti deve essere compatibile con i divisori comuni dei moduli.

---

### Teorema cinese del resto

Se i moduli $m_1$ e $m_2$ sono coprimi, cioè

$$
\gcd(m_1,m_2)=1,
$$

allora il sistema

$$
\begin{cases}
x\equiv a_1\pmod{m_1},\\
x\equiv a_2\pmod{m_2}
\end{cases}
$$

ha sempre soluzione, ed essa è unica modulo

$$
m_1m_2.
$$

Questo è il [[Teorema cinese del resto|teorema cinese del resto]]. La condizione di coprimalità è importante. Se i moduli non sono [[Numeri coprimi|coprimi]], il sistema può:

- non avere soluzioni;
- avere soluzioni, ma non necessariamente un’unica classe modulo $m_1m_2$.

Nel caso generale compatibile, l’unicità è modulo il [[Minimo comune multiplo|minimo comune multiplo]]:

$$
\operatorname{mcm}(m_1,m_2).
$$

Quando $m_1$ e $m_2$ sono coprimi,

$$
\operatorname{mcm}(m_1,m_2)=m_1m_2.
$$

---

### Esempio di risoluzione di un sistema

Consideriamo il sistema

$$
\begin{cases}
x\equiv a\pmod m,\\
x\equiv b\pmod n.
\end{cases}
$$

Dalla prima equazione scriviamo

$$
x=a+km.
$$

Sostituendo nella seconda,

$$
a+km\equiv b\pmod n,
$$

e quindi

$$
mk\equiv b-a\pmod n.
$$

Se $\gcd(m,n)=1$, $m$ è invertibile modulo $n$ e si ottiene

$$
k\equiv m^{-1}(b-a)\pmod n.
$$

Sostituendo il valore di $k$ nella formula

$$
x=a+km,
$$

si ottiene una soluzione particolare $x_0$. Tutte le soluzioni sono allora

$$
x\equiv x_0\pmod{mn}.
$$

La classe di soluzioni si può rappresentare con una progressione aritmetica:

$$
x=x_0+t\,mn,
\qquad t\in\mathbb Z.
$$

> [!example] Esempio
> Risolviamo $x\equiv 2\pmod 3$ e $x\equiv 3\pmod 5$. Dalla prima, $x=2+3k$; nella seconda $2+3k\equiv 3\pmod 5$, cioè $3k\equiv 1\pmod 5$, e siccome $3\cdot 2\equiv 1$ otteniamo $k\equiv 2\pmod 5$. Quindi $x=2+3\cdot 2=8$, e tutte le soluzioni sono $x\equiv 8\pmod{15}$.

---

## 12. Relazione tra congruenze e classi

Scrivere

$$
x\equiv a\pmod n
$$

significa esattamente dire che $x$ appartiene alla classe $[a]_n$:

$$
x\in[a]_n.
$$

Per esempio, se le soluzioni di una congruenza sono

$$
x=7+3k,
\qquad k\in\mathbb Z,
$$

si può scrivere

$$
x\equiv 7\pmod 3.
$$

Siccome $7\equiv 1\pmod 3$, la stessa classe si può indicare anche come

$$
x\equiv 1\pmod 3.
$$

Le scritture

$$
x\equiv 7\pmod 3
\qquad\text{e}\qquad
x\equiv 1\pmod 3
$$

descrivono quindi la stessa classe di interi.

Ecco perché, lavorando modulo $n$, si può sempre sostituire un rappresentante con un altro elemento della stessa classe.

---

## 13. Osservazioni conclusive sui metodi

Le congruenze permettono di trasformare problemi sugli interi in problemi sui loro resti modulo $n$. In pratica:

1. si sceglie il modulo appropriato;
2. si sostituiscono i numeri con elementi congrui più semplici;
3. si eseguono le operazioni nella congruenza;
4. si interpreta il risultato come informazione sulla divisibilità o sulle soluzioni intere.

Occorre però distinguere con attenzione:

- uguaglianza tra interi;
- congruenza modulo $n$;
- appartenenza a una classe di congruenza;
- cancellazione lecita o non lecita di un fattore;
- soluzione particolare e insieme completo delle soluzioni.

In particolare, da

$$
ac\equiv bc\pmod n
$$

non si può cancellare automaticamente $c$. La cancellazione è immediata solo quando $c$ è coprimo con $n$; in generale il modulo va ridotto a

$$
\frac{n}{\gcd(c,n)}.
$$
