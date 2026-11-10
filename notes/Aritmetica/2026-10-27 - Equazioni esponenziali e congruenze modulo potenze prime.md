---
type: lecture-note
course: Aritmetica
date: '2026-10-27'
title: Equazioni esponenziali e congruenze modulo potenze prime
source_transcript: _transcripts/Aritmetica/2026-10-27 - Equazioni esponenziali e congruenze modulo potenze
  prime.md
source_hash: sha256:ef6d913ea121163e2010d5dae761a938686332fd9dd0ebb316b2bcb99fbc9055
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-27T22:03:44.980Z'
vault_path: Notes/Aritmetica/Lectures/2026-10-27 - Equazioni esponenziali e congruenze modulo potenze prime.md
vault_hash: d076583d8a2b1daa02522d155f925abec24a765746d0160c690c6a1ab8103ae9
---

# Equazioni esponenziali e congruenze modulo potenze prime

## 1. Potenze in una congruenza e periodicità

Quando si lavora modulo $m$, le potenze di un elemento invertibile sono periodiche. Se $\gcd(a,m)=1$, esiste un intero positivo $k$ tale che

$$
a^k \equiv 1 \pmod m.
$$

Il **periodo minimo** delle potenze di $a$ modulo $m$ si chiama **[[Ordine di un elemento|ordine]] di $a$ modulo $m$** e si indica con

$$
\operatorname{ord}_m(a)
=
\min\{k>0 : a^k\equiv 1\pmod m\}.
$$

Che tale intero esista segue dal fatto che, essendo $a$ [[Elementi invertibili modulo n|invertibile modulo $m$]], le potenze

$$
1,a,a^2,\dots
$$

stanno nel gruppo degli elementi invertibili modulo $m$, che è finito. Prima o poi una potenza si ripete, e dalla ripetizione si ricava una potenza uguale a $1$.

Una volta trovato l’ordine $r=\operatorname{ord}_m(a)$, vale

$$
a^{x+r}\equiv a^x\pmod m
$$

per ogni intero $x$. Quindi, per studiare una congruenza esponenziale con base $a$, basta considerare gli esponenti modulo $r$.

> [!warning]
> La periodicità delle potenze in questa forma richiede che $a$ sia invertibile modulo $m$, cioè $\gcd(a,m)=1$. Se la base non è invertibile il comportamento delle potenze può essere diverso, e il ragionamento tramite l’ordine non si applica automaticamente.

---

## 2. Esempio: le potenze di $3$ modulo $13$

Consideriamo la congruenza

$$
3^x\equiv 1\pmod{13}.
$$

Calcoliamo le prime potenze:

$$
3^0\equiv 1\pmod{13},
$$

$$
3^1\equiv 3\pmod{13},
$$

$$
3^2\equiv 9\pmod{13},
$$

$$
3^3=27\equiv 1\pmod{13}.
$$

Pertanto

$$
\operatorname{ord}_{13}(3)=3.
$$

Le potenze si ripetono con periodo $3$:

$$
3^{x+3}\equiv 3^x\pmod{13}.
$$

Ne segue che

$$
3^x\equiv 1\pmod{13}
$$

se e solo se l’esponente è multiplo di $3$, cioè

$$
x\equiv 0\pmod 3.
$$

### Dimostrazione per divisione euclidea

Per dimostrare che non ci sono altre soluzioni, si scrive ogni intero $x$ come

$$
x=3q+r,
\qquad r\in\{0,1,2\}.
$$

Allora

$$
3^x=3^{3q+r}=(3^3)^q3^r\equiv 3^r\pmod{13}.
$$

Si guardano i tre possibili resti:

- se $r=0$, allora $3^x\equiv 1$;
- se $r=1$, allora $3^x\equiv 3$;
- se $r=2$, allora $3^x\equiv 9$.

Solo nel primo caso si ottiene $1$ modulo $13$. Quindi necessariamente $r=0$, ossia $x\equiv0\pmod3$.

Il procedimento è generale: quando si conosce l’ordine di $a$ modulo $m$, si divide l’esponente per tale ordine e si controllano i possibili resti.

---

## 3. Risoluzione generale di $a^x\equiv b\pmod m$

Supponiamo che $\gcd(a,m)=1$ e poniamo

$$
r=\operatorname{ord}_m(a).
$$

Le potenze di $a$ formano il [[Gruppo ciclico|sottogruppo ciclico]]

$$
\langle a\rangle
=
\{a^x : x\in\mathbb Z\}
$$

del gruppo degli elementi invertibili modulo $m$.

La congruenza

$$
a^x\equiv b\pmod m
$$

ha soluzione se e solo se la classe di $b$ appartiene a $\langle a\rangle$, cioè se $b$ è congruente a una potenza di $a$.

Se $x_0$ è una soluzione, tutte le soluzioni sono

$$
x\equiv x_0\pmod r.
$$

Infatti:

- se $x\equiv x_0\pmod r$, allora $x=x_0+kr$ e quindi

  $$
  a^x=a^{x_0}(a^r)^k\equiv a^{x_0}\equiv b\pmod m;
  $$

- viceversa, se $a^x\equiv a^{x_0}\pmod m$, allora

  $$
  a^{x-x_0}\equiv 1\pmod m,
  $$

  e per la minimalità dell’ordine si ottiene

  $$
  r\mid x-x_0.
  $$

Quindi le soluzioni sono esattamente una classe modulo l’ordine di $a$.

---

## 4. Esempio: potenze di $4$ modulo $17$

Consideriamo le potenze di $4$ modulo $17$:

$$
4^2=16\equiv -1\pmod{17},
$$

e quindi

$$
4^4\equiv (-1)^2\equiv 1\pmod{17}.
$$

Le potenze sono dunque

$$
4^0\equiv 1,
\qquad
4^1\equiv 4,
\qquad
4^2\equiv -1,
\qquad
4^3\equiv -4,
\qquad
4^4\equiv 1
\pmod{17}.
$$

Pertanto

$$
\operatorname{ord}_{17}(4)=4.
$$

Le sole classi rappresentate dalle potenze di $4$ sono

$$
1,\quad 4,\quad -1,\quad -4
\pmod{17}.
$$

Di conseguenza, la congruenza

$$
4^x\equiv b\pmod{17}
$$

è risolvibile se e solo se

$$
b\equiv 1,\,-1,\,4,\,-4\pmod{17}.
$$

In ciascun caso l’esponente è determinato modulo $4$:

$$
\begin{array}{c|c}
b & x\pmod 4\\
\hline
1 & 0\\
4 & 1\\
-1 & 2\\
-4 & 3
\end{array}
$$

Ad esempio,

$$
4^x\equiv -1\pmod{17}
$$

ha come soluzioni

$$
x\equiv 2\pmod4.
$$

---

## 5. Strategia per una congruenza esponenziale con modulo composto

Quando il modulo si fattorizza, conviene spesso spezzare la congruenza in congruenze modulo fattori più semplici.

Supponiamo, ad esempio, di voler risolvere

$$
a^x\equiv b\pmod{mn}.
$$

Se $\gcd(m,n)=1$, per il [[Teorema cinese del resto|teorema cinese del resto]] questa congruenza è equivalente al sistema

$$
\begin{cases}
a^x\equiv b\pmod m,\\
a^x\equiv b\pmod n.
\end{cases}
$$

Si risolvono separatamente le due congruenze esponenziali, ottenendo condizioni sull’esponente $x$, e poi si risolve il sistema di congruenze in $x$.

Così si evita di calcolare direttamente molte potenze modulo un numero grande.

---

## 6. Esempio: $3^x\equiv61\pmod{91}$

Consideriamo

$$
3^x\equiv61\pmod{91}.
$$

Poiché

$$
91=7\cdot13,
\qquad
\gcd(7,13)=1,
$$

si considera il sistema

$$
\begin{cases}
3^x\equiv61\pmod7,\\
3^x\equiv61\pmod{13}.
\end{cases}
$$

### Congruenza modulo $7$

Poiché $61\equiv5\pmod7$, si deve risolvere

$$
3^x\equiv5\pmod7.
$$

Le potenze di $3$ modulo $7$ sono

$$
3^0\equiv1,\quad
3^1\equiv3,\quad
3^2\equiv2,\quad
3^3\equiv6\equiv-1,
$$

$$
3^4\equiv4,\quad
3^5\equiv5,\quad
3^6\equiv1
\pmod7.
$$

L’ordine di $3$ modulo $7$ è quindi $6$ e la congruenza dà

$$
x\equiv5\pmod6,
$$

equivalentemente

$$
x\equiv-1\pmod6.
$$

Nel transcript l’esponente viene indicato anche come $x_0=-2$ in un passaggio; il calcolo diretto delle potenze modulo $7$ mostra invece che per $3^x\equiv5\pmod7$ si ottiene $x\equiv5\pmod6$.

### Congruenza modulo $13$

Poiché

$$
61\equiv9\pmod{13}
$$

e

$$
3^2\equiv9\pmod{13},
$$

si ottiene

$$
x\equiv2\pmod3,
$$

perché l’ordine di $3$ modulo $13$ è $3$.

Il sistema per l’esponente è dunque

$$
\begin{cases}
x\equiv5\pmod6,\\
x\equiv2\pmod3.
\end{cases}
$$

La seconda congruenza è già soddisfatta dalla prima, poiché $5\equiv2\pmod3$. Quindi

$$
x\equiv5\pmod6.
$$

Ne segue che le soluzioni della congruenza iniziale sono

$$
\boxed{x\equiv5\pmod6}.
$$

---

## 7. Sistema di congruenze con moduli non necessariamente coprimi

Il teorema cinese del resto nella forma usuale richiede moduli coprimi. La versione generale considera il sistema

$$
\begin{cases}
x\equiv a\pmod m,\\
x\equiv b\pmod n.
\end{cases}
$$

Poniamo

$$
d=\gcd(m,n).
$$

### Teorema cinese del resto generalizzato

Il sistema è risolvibile se e solo se

$$
d\mid(b-a).
$$

Quando è risolvibile, la soluzione è unica modulo

$$
\operatorname{lcm}(m,n)
=
\frac{mn}{\gcd(m,n)}.
$$

#### Dimostrazione della condizione di compatibilità

Scriviamo la prima congruenza come

$$
x=a+mk.
$$

Sostituendo nella seconda:

$$
a+mk\equiv b\pmod n,
$$

cioè

$$
mk\equiv b-a\pmod n.
$$

La [[Congruenza lineare|congruenza lineare]] in $k$ è risolvibile se e solo se

$$
\gcd(m,n)\mid(b-a).
$$

Questa è la condizione di compatibilità.

Se $d\mid(b-a)$, dividendo per $d$ si ottiene

$$
\frac md k\equiv\frac{b-a}{d}\pmod{\frac nd}.
$$

Poiché

$$
\gcd\left(\frac md,\frac nd\right)=1,
$$

il coefficiente $m/d$ è invertibile modulo $n/d$ e si trova una soluzione $k_0$. Tutte le soluzioni sono

$$
k=k_0+\frac nd\,t.
$$

Sostituendo in $x=a+mk$ si ottiene

$$
x=a+mk_0+\frac{mn}{d}t.
$$

Pertanto tutte le soluzioni sono congruenti modulo

$$
\frac{mn}{d}=\operatorname{lcm}(m,n).
$$

Nel caso particolare $\gcd(m,n)=1$ la condizione è sempre verificata e si recupera il teorema cinese del resto usuale: esiste un’unica soluzione modulo $mn$.

> [!example] Esempio
> Il sistema $x\equiv1\pmod4$, $x\equiv3\pmod6$ ha $d=\gcd(4,6)=2$ e $b-a=2$, divisibile per $2$: è risolvibile, con soluzione unica modulo $\operatorname{lcm}(4,6)=12$. Per esempio $x=9$ funziona ($9=2\cdot4+1$ e $9=6+3$). Invece $x\equiv0\pmod4$, $x\equiv1\pmod6$ non ha soluzioni, perché $2\nmid1$.

---

## 8. Attenzione alla cancellazione nelle congruenze

Nelle congruenze non si può cancellare automaticamente un fattore. Se

$$
ac\equiv bc\pmod m,
$$

si può cancellare $c$ solo quando $c$ è invertibile modulo $m$, cioè quando

$$
\gcd(c,m)=1.
$$

In generale, dalla congruenza

$$
ac\equiv bc\pmod m
$$

si ricava soltanto

$$
m\mid c(a-b).
$$

Se $c$ non è coprimo con $m$, non si può concludere direttamente che $a\equiv b\pmod m$.

La cancellazione vale invece nei [[Campo|campi]], ad esempio modulo un numero primo $p$, per ogni fattore non nullo modulo $p$.

> [!example] Esempio
> Modulo $6$ si ha $2\cdot2=4$ e $2\cdot5=10\equiv4$, quindi $2\cdot2\equiv2\cdot5\pmod6$. Ma $2\not\equiv5\pmod6$: il fattore $2$ non è invertibile modulo $6$, e non si può semplificare.

---

## 9. Principio di annullamento modulo un primo

Se $p$ è primo e

$$
uv\equiv0\pmod p,
$$

allora

$$
u\equiv0\pmod p
\qquad\text{oppure}\qquad
v\equiv0\pmod p.
$$

È il principio di annullamento del prodotto nel campo $\mathbb Z/p\mathbb Z$.

Ad esempio,

$$
x(x-1)\equiv0\pmod p
$$

implica

$$
x\equiv0\pmod p
\qquad\text{oppure}\qquad
x\equiv1\pmod p.
$$

Il principio però non vale in generale modulo $p^e$ con $e>1$. Per esempio, modulo $4$:

$$
2\cdot2=4\equiv0\pmod4,
$$

ma né $2\equiv0\pmod4$ né l’altro fattore è nullo modulo $4$.

Quindi da

$$
uv\equiv0\pmod{p^e}
$$

non si può concludere automaticamente che uno dei due fattori sia nullo modulo $p^e$: la divisibilità per $p^e$ può distribuirsi tra i due fattori.

---

### 10. Esempio: $x(x-1)\equiv0\pmod4$

Consideriamo

$$
x(x-1)\equiv0\pmod4.
$$

I fattori $x$ e $x-1$ sono consecutivi. Tra due numeri consecutivi almeno uno è pari, ma non è detto che uno dei due sia divisibile per $4$.

Controllando le classi modulo $4$:

- $x\equiv0$: $x(x-1)\equiv0$;
- $x\equiv1$: $x(x-1)\equiv0$;
- $x\equiv2$: $2\cdot1\equiv2\not\equiv0$;
- $x\equiv3$: $3\cdot2=6\equiv2\not\equiv0$.

Le soluzioni sono quindi

$$
\boxed{x\equiv0\pmod4
\quad\text{oppure}\quad
x\equiv1\pmod4}.
$$

Il ragionamento tramite il principio di annullamento vale modulo $p$, ma va sostituito da un’analisi della divisibilità dei fattori quando il modulo è una potenza di primo.

---

## 11. Equazioni quadratiche modulo un primo

Consideriamo una congruenza quadratica

$$
ax^2+bx+c\equiv0\pmod p,
$$

dove $p$ è un primo dispari e $p\nmid a$.

Come nel caso reale, si può usare il discriminante

$$
\Delta=b^2-4ac.
$$

La formula risolutiva modulo $p$ è

$$
x\equiv\frac{-b\pm\sqrt{\Delta}}{2a}\pmod p.
$$

La formula è lecita perché $p\neq2$ e quindi $2a$ è invertibile modulo $p$.

La congruenza ha soluzioni se e solo se $\Delta$ è un quadrato modulo $p$, cioè se esiste $y$ tale che

$$
y^2\equiv\Delta\pmod p.
$$

Se $\Delta$ non è un quadrato modulo $p$, la congruenza non ha soluzioni.

### Caso $p=2$

Quando il modulo è $2$ non si può usare la formula, che richiede di dividere per $2$. In questo caso si controllano direttamente le classi modulo $2$.

---

### 12. Esempio: congruenza modulo $5$

Consideriamo

$$
x^2\equiv1\pmod5.
$$

Si porta tutto a sinistra:

$$
x^2-1\equiv0\pmod5,
$$

e si fattorizza:

$$
(x-1)(x+1)\equiv0\pmod5.
$$

Poiché $5$ è primo, vale il principio di annullamento:

$$
x-1\equiv0\pmod5
\quad\text{oppure}\quad
x+1\equiv0\pmod5.
$$

Pertanto

$$
\boxed{x\equiv1\pmod5
\quad\text{oppure}\quad
x\equiv-1\pmod5}.
$$

---

### 13. Esempio: una congruenza senza soluzioni modulo $11$

Consideriamo

$$
x^2+5x+3\equiv0\pmod{11}.
$$

Il discriminante è

$$
\Delta=5^2-4\cdot1\cdot3=25-12=13\equiv2\pmod{11}.
$$

Dobbiamo quindi verificare se $2$ è un quadrato modulo $11$.

I quadrati modulo $11$ sono rappresentati da

$$
0^2,\ \pm1^2,\ \pm2^2,\ \pm3^2,\ \pm4^2,\ \pm5^2.
$$

Calcolando:

$$
0^2\equiv0,
$$

$$
(\pm1)^2\equiv1,
$$

$$
(\pm2)^2\equiv4,
$$

$$
(\pm3)^2\equiv9,
$$

$$
(\pm4)^2\equiv16\equiv5,
$$

$$
(\pm5)^2\equiv25\equiv3
\pmod{11}.
$$

L’insieme dei residui quadratici modulo $11$ è quindi

$$
\{0,1,3,4,5,9\}.
$$

Poiché $2$ non appartiene a questo insieme, la congruenza non ha soluzioni modulo $11$.

---

## 14. Passaggio da modulo $p$ a modulo $p^2$

Una soluzione modulo $p$ non è automaticamente una soluzione modulo $p^2$. Se

$$
f(x)\equiv0\pmod p,
$$

bisogna verificare se la soluzione si può correggere, o **sollevare**, a una soluzione modulo $p^2$.

Sia $x_0$ una soluzione modulo $p$. Ogni possibile sollevamento modulo $p^2$ ha la forma

$$
x=x_0+ph,
$$

dove $h$ è considerato modulo $p$.

Consideriamo, per semplicità, un polinomio quadratico

$$
f(x)=x^2+ax+b.
$$

Poiché $x_0$ è soluzione modulo $p$, esiste un intero $\gamma$ tale che

$$
f(x_0)=x_0^2+ax_0+b=p\gamma.
$$

Sostituiamo $x=x_0+ph$:

$$
\begin{aligned}
f(x_0+ph)
&=(x_0+ph)^2+a(x_0+ph)+b\\
&=x_0^2+2px_0h+p^2h^2+ax_0+aph+b\\
&=f(x_0)+p h(2x_0+a)+p^2h^2.
\end{aligned}
$$

Usando $f(x_0)=p\gamma$:

$$
f(x_0+ph)
=
p\gamma+p h(2x_0+a)+p^2h^2.
$$

Per imporre

$$
f(x_0+ph)\equiv0\pmod{p^2},
$$

si divide per $p$ e si lavora modulo $p$:

$$
\gamma+h(2x_0+a)+ph^2\equiv0\pmod p.
$$

Poiché $ph^2\equiv0\pmod p$, resta la congruenza lineare

$$
\boxed{\gamma+h(2x_0+a)\equiv0\pmod p}.
$$

È una nuova congruenza, ora nell’incognita $h$.

Se

$$
2x_0+a\not\equiv0\pmod p,
$$

il coefficiente di $h$ è invertibile modulo $p$ e si ottiene un unico valore di $h$ modulo $p$. Quindi la soluzione $x_0$ modulo $p$ ha un unico sollevamento modulo $p^2$.

Se invece

$$
2x_0+a\equiv0\pmod p,
$$

il termine con $h$ scompare e bisogna controllare $\gamma$:

- se $\gamma\not\equiv0\pmod p$, non esiste alcun sollevamento;
- se $\gamma\equiv0\pmod p$, possono esistere più sollevamenti.

È il meccanismo che sta alla base del sollevamento delle soluzioni alle potenze successive di un primo.

> [!example] Esempio
> Sia $f(x)=x^2-2$, $p=7$. Modulo $7$ la soluzione $x_0=3$ funziona: $f(3)=7=7\cdot1$, quindi $\gamma=1$. Qui $2x_0+a=6\not\equiv0\pmod7$ (con $a=0$), e la condizione $1+6h\equiv0\pmod7$ dà $h\equiv1$. Il sollevamento è $x=3+7\cdot1=10$, e infatti $f(10)=98=2\cdot7^2\equiv0\pmod{49}$.

---

### 15. Forma generale del sollevamento

Per un polinomio

$$
f(x)=Ax^2+Bx+C,
$$

scrivendo

$$
x=x_0+ph
$$

si ottiene

$$
\begin{aligned}
f(x_0+ph)
&=A(x_0+ph)^2+B(x_0+ph)+C\\
&=f(x_0)+p h(2Ax_0+B)+Ap^2h^2.
\end{aligned}
$$

Se

$$
f(x_0)=p\gamma,
$$

la condizione modulo $p^2$ diventa

$$
\gamma+h(2Ax_0+B)\equiv0\pmod p.
$$

La quantità

$$
2Ax_0+B
$$

è la derivata formale $f'(x_0)$ nel caso quadratico. Se è non nulla modulo $p$, il sollevamento è unico.

Il procedimento si può iterare:

1. si trovano le soluzioni modulo $p$;
2. per ciascuna soluzione $x_0$ si cerca un sollevamento $x_0+ph$ modulo $p^2$;
3. si ripete il procedimento per passare da $p^2$ a $p^3$, e così via.

Se una soluzione non si può sollevare già da modulo $p$ a modulo $p^2$, non può produrre soluzioni modulo potenze superiori di $p$.

---

## 16. Strategia generale per problemi modulo potenze prime

Quando compare un modulo fattorizzabile o una potenza di primo, conviene procedere in quest’ordine:

1. **Fattorizzare il modulo**, se possibile:
   $$
   m=p_1^{e_1}\cdots p_r^{e_r}.
   $$

2. **Separare il problema** modulo i diversi fattori primi o potenze prime.

3. Per una congruenza esponenziale $a^x\equiv b$:
   - verificare che $a$ sia invertibile;
   - calcolare o determinare l’ordine di $a$;
   - verificare se $b$ appartiene al sottogruppo generato da $a$;
   - determinare $x$ modulo l’ordine.

4. Per una congruenza polinomiale modulo $p$:
   - sfruttare il principio di annullamento se l’espressione è fattorizzabile;
   - per una quadratica usare il discriminante;
   - controllare i residui quadratici se necessario.

5. Per passare da modulo $p$ a modulo $p^e$:
   - non assumere che una soluzione modulo $p$ rimanga automaticamente soluzione;
   - scrivere $x=x_0+ph$;
   - sostituire e dividere per $p$;
   - risolvere la congruenza risultante per $h$.

6. Infine, ricombinare le condizioni ottenute usando il teorema cinese del resto generalizzato.

> [!warning]
> Una soluzione modulo $p$ può non sollevarsi a modulo $p^2$. Inoltre, modulo $p^e$ non valgono in generale né il principio di annullamento del prodotto né tutte le regole di cancellazione valide modulo un primo.
