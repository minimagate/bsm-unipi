---
type: lecture-note
course: Aritmetica
date: '2026-11-01'
title: Gruppi ciclici, ordini e sottogruppi modulari
source_transcript: _transcripts/Aritmetica/2026-11-01 - Gruppi ciclici, ordini e sottogruppi modulari.md
source_hash: sha256:5f9520e88a48e5f8c6b641f99a6c7f1ed776f4d0d62bac07e384a364a94dc4d2
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-11-01T08:07:38.115Z'
vault_path: Notes/Aritmetica/Lectures/2026-11-01 - Gruppi ciclici, ordini e sottogruppi modulari.md
vault_hash: 93e0103336396432084b621e3ec0da3c06a38cf2acb1f6bf6da7ea951ee7611a
---

# Gruppi ciclici, ordini e sottogruppi modulari

## 1. Gruppi ciclici

Un [[Gruppo|gruppo]] $G$ si dice **[[Gruppo ciclico|ciclico]]** se esiste un elemento $g\in G$ che genera tutto il gruppo:

$$
G=\langle g\rangle.
$$

In notazione moltiplicativa:

$$
\langle g\rangle=\{g^n:n\in\mathbb Z\}.
$$

In notazione additiva:

$$
\langle g\rangle=\{ng:n\in\mathbb Z\}.
$$

L’elemento $g$ si chiama **generatore** di $G$.

Dire che $G$ è ciclico significa quindi che ogni elemento di $G$ è una potenza di $g$:

$$
\forall x\in G\ \exists n\in\mathbb Z\quad x=g^n.
$$

Nel caso additivo, la stessa affermazione si scrive:

$$
\forall x\in G\ \exists n\in\mathbb Z\quad x=ng.
$$

La notazione moltiplicativa e quella additiva descrivono lo stesso tipo di struttura, ma vanno usate in modo coerente:

- in un gruppo moltiplicativo si scrivono $g^n$, $g^{-1}$ e $gh$;
- in un gruppo additivo si scrivono $ng$, $-g$ e $g+h$.

### Proprietà fondamentale delle potenze

Per ogni $n,m\in\mathbb Z$ vale:

$$
g^n g^m=g^{n+m}.
$$

Infatti, per gli interi l’esponente del prodotto è la somma degli esponenti. Questa identità mostra che l’applicazione

$$
\mathbb Z\longrightarrow G,\qquad n\longmapsto g^n
$$

è un [[Omomorfismo|omomorfismo]] di gruppi.

Se il gruppo è scritto additivamente, l’analoga proprietà è:

$$
ng+mg=(n+m)g.
$$

---

## 2. Esempi di gruppi ciclici

### 2.1 Il gruppo $(\mathbb Z,+)$

Il gruppo degli interi è ciclico:

$$
\mathbb Z=\langle 1\rangle.
$$

Infatti ogni intero è una potenza additiva di $1$, cioè:

$$
n=n\cdot 1.
$$

Anche $-1$ è un generatore:

$$
\mathbb Z=\langle -1\rangle.
$$

In generale, gli unici generatori di $(\mathbb Z,+)$ sono $1$ e $-1$. Se $a\in\mathbb Z$ e $|a|>1$, allora

$$
\langle a\rangle=a\mathbb Z
$$

è il sottoinsieme dei multipli di $a$, quindi non coincide con tutto $\mathbb Z$.

### 2.2 Il gruppo ciclico finito $\mathbb Z/n\mathbb Z$

Il gruppo additivo delle classi modulo $n$ è ciclico:

$$
\mathbb Z/n\mathbb Z=\langle \overline{1}\rangle.
$$

Le sue potenze additive sono:

$$
\overline{0},\overline{1},\overline{2},\ldots,\overline{n-1}.
$$

In particolare,

$$
k\overline{1}=\overline{k}.
$$

Poiché $\overline{n}=\overline{0}$, si ha:

$$
n\overline{1}=\overline{0}.
$$

L’ordine del gruppo è $n$.

Più in generale, la classe $\overline{a}$ genera il sottogruppo

$$
\langle \overline{a}\rangle
=
\{\overline{ka}:k\in\mathbb Z\}.
$$

Questo sottogruppo coincide con

$$
\langle \overline{\gcd(a,n)}\rangle.
$$

Di conseguenza:

$$
\left|\langle \overline a\rangle\right|
=
\frac{n}{\gcd(a,n)}.
$$

In particolare, $\overline a$ genera tutto $\mathbb Z/n\mathbb Z$ se e solo se

$$
\gcd(a,n)=1.
$$

Quindi i generatori di $\mathbb Z/n\mathbb Z$ sono proprio le classi $\overline a$ coprime con $n$. Il loro numero è la funzione di Eulero $\varphi(n)$.

> [!example] Esempio
> In $\mathbb Z/10\mathbb Z$ i generatori sono le classi coprime con $10$, cioè $\overline1,\overline3,\overline7,\overline9$ (sono $\varphi(10)=4$). Per esempio $\langle\overline3\rangle=\{\overline3,\overline6,\overline9,\overline2,\overline5,\overline8,\overline1,\overline4,\overline7,\overline0\}$ è tutto il gruppo, mentre $\langle\overline4\rangle=\{\overline0,\overline4,\overline8,\overline2,\overline6\}$ ha solo $10/\gcd(4,10)=5$ elementi.

### 2.3 Gruppi moltiplicativi di classi invertibili

Nel gruppo moltiplicativo delle [[Elementi invertibili modulo n|classi invertibili]] modulo $n$ si usa la notazione

$$
(\mathbb Z/n\mathbb Z)^\times.
$$

Gli elementi sono le classi $\overline a$ tali che

$$
\gcd(a,n)=1.
$$

L’operazione è la moltiplicazione modulo $n$.

L’elemento neutro è $\overline 1$ e l’inverso di $\overline a$ è la classe $\overline b$ tale che

$$
ab\equiv 1\pmod n.
$$

Il numero di elementi di questo gruppo è

$$
\left|(\mathbb Z/n\mathbb Z)^\times\right|=\varphi(n).
$$

Per il [[Piccolo teorema di Fermat|teorema di Eulero]], se $\gcd(a,n)=1$, allora

$$
a^{\varphi(n)}\equiv 1\pmod n.
$$

Equivalentemente, nel gruppo moltiplicativo:

$$
\overline a^{\,\varphi(n)}=\overline 1.
$$

> [!warning]
> Il gruppo additivo $\mathbb Z/n\mathbb Z$ contiene tutte le classi modulo $n$, mentre $(\mathbb Z/n\mathbb Z)^\times$ contiene solo le classi invertibili. Sono due gruppi diversi: non vanno confusi.

---

## 3. Ordine di un elemento

Sia $g$ un elemento di un gruppo $G$. L’**[[Ordine di un elemento|ordine]] di $g$** è il minimo intero positivo $m$ tale che

$$
g^m=e,
$$

dove $e$ è l’elemento neutro del gruppo.

Si indica con $\operatorname{ord}(g)$ oppure $o(g)$.

In notazione additiva, la definizione diventa: l’ordine di $g$ è il minimo intero positivo $m$ tale che

$$
mg=0.
$$

Se non esiste alcun intero positivo con questa proprietà, si dice che $g$ ha ordine infinito.

### Ordine e sottogruppo generato

L’ordine di un elemento coincide con la cardinalità del sottogruppo che esso genera:

$$
\operatorname{ord}(g)=|\langle g\rangle|.
$$

Infatti:

- se $g$ ha ordine infinito, le potenze
  $$
  \ldots,g^{-2},g^{-1},e,g,g^2,\ldots
  $$
  sono tutte distinte;
- se $g$ ha ordine $m$, allora
  $$
  \langle g\rangle=\{e,g,g^2,\ldots,g^{m-1}\}.
  $$

Le potenze successive si ripetono con periodo $m$:

$$
g^{k+m}=g^k
\qquad\text{per ogni }k\in\mathbb Z.
$$

### Gruppo generato da un elemento di ordine finito

Se $\operatorname{ord}(g)=m$, allora:

$$
\langle g\rangle=\{g^0,g^1,\ldots,g^{m-1}\}.
$$

Gli elementi $g^r$ e $g^s$ coincidono se e solo se

$$
r\equiv s\pmod m.
$$

Infatti:

$$
g^r=g^s
\iff
g^{r-s}=e
\iff
m\mid(r-s).
$$

---

## 4. Gruppi ciclici finiti e generatori

Se $G$ è un gruppo ciclico finito di ordine $n$, allora esiste $g\in G$ tale che

$$
G=\langle g\rangle
\qquad\text{e}\qquad
\operatorname{ord}(g)=n.
$$

Per essere ciclico, un gruppo finito deve quindi contenere almeno un elemento il cui ordine sia uguale all’ordine del gruppo.

Se tutti gli elementi hanno ordine strettamente minore di $|G|$, nessun elemento può generare tutto il gruppo.

### Esempio: il gruppo delle unità modulo $8$

Il gruppo

$$
(\mathbb Z/8\mathbb Z)^\times
=
\{\overline1,\overline3,\overline5,\overline7\}
$$

ha quattro elementi. Però:

$$
\overline3^{\,2}=\overline9=\overline1,
$$

$$
\overline5^{\,2}=\overline{25}=\overline1,
$$

$$
\overline7^{\,2}=\overline{49}=\overline1.
$$

Quindi tutti gli elementi diversi dall’identità hanno ordine $2$:

$$
\operatorname{ord}(\overline3)
=
\operatorname{ord}(\overline5)
=
\operatorname{ord}(\overline7)=2.
$$

Di conseguenza nessun elemento può generare un gruppo di ordine $4$. Pertanto $(\mathbb Z/8\mathbb Z)^\times$ non è ciclico.

Il transcript sembra riferirsi a questo gruppo quando parla di "$Z_8$" e afferma che tutti gli elementi hanno ordine $2$; il gruppo additivo $\mathbb Z/8\mathbb Z$, invece, è ciclico ed è generato da $\overline1$.

---

## 5. Proprietà dell’ordine in un gruppo finito

Sia $G$ un gruppo finito e sia $g\in G$. Allora l’ordine di $g$ divide l’ordine del gruppo:

$$
\operatorname{ord}(g)\mid |G|.
$$

Segue dal [[Teorema di Lagrange|teorema di Lagrange]] applicato al sottogruppo $\langle g\rangle$:

$$
|\langle g\rangle|
=
\operatorname{ord}(g)
\mid |G|.
$$

Di conseguenza, se $g^m=e$, anche l’ordine di $g$ divide $m$:

$$
g^m=e
\quad\Longrightarrow\quad
\operatorname{ord}(g)\mid m.
$$

La ragione è che, se $d=\operatorname{ord}(g)$, dividendo $m$ per $d$ si scrive

$$
m=qd+r,
\qquad 0\le r<d.
$$

Allora:

$$
g^m=g^{qd+r}
=(g^d)^qg^r
=e^qg^r
=g^r.
$$

Se $g^m=e$, segue $g^r=e$. Per la minimalità di $d$, deve essere $r=0$, quindi $d\mid m$.

Questa proprietà è molto utile per restringere i possibili ordini degli elementi.

---

## 6. Ordine di una potenza

Sia $g$ un elemento di ordine finito $n$:

$$
\operatorname{ord}(g)=n.
$$

Per ogni intero $k$, l’ordine di $g^k$ è

$$
\boxed{
\operatorname{ord}(g^k)
=
\frac{n}{\gcd(n,k)}
}.
$$

### Dimostrazione

Cerchiamo il minimo intero positivo $m$ tale che

$$
(g^k)^m=e.
$$

Usando le proprietà delle potenze:

$$
(g^k)^m=g^{km}.
$$

Poiché $g$ ha ordine $n$:

$$
g^{km}=e
\iff
n\mid km.
$$

Poniamo

$$
d=\gcd(n,k),
\qquad
n=dn_1,
\qquad
k=dk_1,
$$

con $\gcd(n_1,k_1)=1$.

La condizione $n\mid km$ diventa:

$$
dn_1\mid dk_1m
\iff
n_1\mid k_1m.
$$

Poiché $n_1$ e $k_1$ sono coprimi, dal [[Lemma di Euclide|lemma di Euclide]] segue:

$$
n_1\mid m.
$$

Il minimo intero positivo possibile è dunque $m=n_1$, cioè

$$
m=\frac nd=\frac{n}{\gcd(n,k)}.
$$

Quindi:

$$
\operatorname{ord}(g^k)
=
\frac{n}{\gcd(n,k)}.
$$

### Conseguenza

L’elemento $g^k$ è un generatore di $\langle g\rangle$ se e solo se ha ordine $n$. Dalla formula:

$$
\operatorname{ord}(g^k)=n
\iff
\frac{n}{\gcd(n,k)}=n
\iff
\gcd(n,k)=1.
$$

Pertanto, in un gruppo ciclico di ordine $n$, i generatori sono esattamente gli elementi

$$
g^k
\qquad\text{con}\qquad
\gcd(k,n)=1.
$$

Il numero dei generatori è quindi

$$
\varphi(n).
$$

---

## 7. Esempi sull’ordine delle potenze

Supponiamo che $g$ abbia ordine $6$.

Allora:

$$
\operatorname{ord}(g^2)
=
\frac{6}{\gcd(6,2)}
=
\frac62=3.
$$

Infatti:

$$
(g^2)^3=g^6=e.
$$

Invece:

$$
\operatorname{ord}(g^5)
=
\frac{6}{\gcd(6,5)}
=
6.
$$

Quindi $g^5$ è ancora un generatore.

Per $g^3$ si ottiene:

$$
\operatorname{ord}(g^3)
=
\frac{6}{\gcd(6,3)}
=
2.
$$

La formula permette di evitare il calcolo diretto di tutte le potenze.

---

## 8. Sottogruppi di un gruppo ciclico

### Teorema

Ogni [[Sottogruppo|sottogruppo]] di un gruppo ciclico è ciclico.

Sia

$$
G=\langle g\rangle
$$

e sia $H\le G$.

Allora esiste un intero $n_0\ge 0$ tale che

$$
H=\langle g^{n_0}\rangle.
$$

In altre parole, ogni sottogruppo è generato da una potenza del generatore di $G$.

### Dimostrazione

Se $H=\{e\}$, allora $H$ è il sottogruppo banale e si può scrivere

$$
H=\langle g^0\rangle=\langle e\rangle.
$$

Supponiamo ora che $H$ contenga almeno un elemento diverso da $e$. Poiché $G=\langle g\rangle$, ogni elemento di $H$ è una potenza di $g$. Se $g^r\in H$ con $r\ne 0$, anche il suo inverso appartiene a $H$:

$$
(g^r)^{-1}=g^{-r}\in H.
$$

Quindi possiamo trovare una potenza positiva di $g$ appartenente a $H$.

Consideriamo l’insieme degli esponenti positivi che producono elementi di $H$:

$$
S=\{k\in\mathbb N_{>0}:g^k\in H\}.
$$

L’insieme $S$ è non vuoto. Per il [[Principio del minimo|principio del buon ordinamento]] ha un minimo; chiamiamolo $n_0$:

$$
n_0=\min S.
$$

Mostriamo che:

$$
H=\langle g^{n_0}\rangle.
$$

Prima di tutto, poiché $g^{n_0}\in H$ e $H$ è un sottogruppo:

$$
\langle g^{n_0}\rangle\subseteq H.
$$

Resta da dimostrare l’inclusione opposta. Sia $g^k\in H$. Dividiamo $k$ per $n_0$ ([[Divisione euclidea|divisione euclidea]]):

$$
k=qn_0+r,
\qquad
0\le r<n_0.
$$

Allora:

$$
g^k=g^{qn_0+r}
=(g^{n_0})^qg^r.
$$

Poiché $g^k\in H$ e $(g^{n_0})^q\in H$, anche $g^r\in H$. Per la minimalità di $n_0$, l’unica possibilità è $r=0$. Quindi $n_0\mid k$ e:

$$
g^k=(g^{n_0})^q\in\langle g^{n_0}\rangle.
$$

Pertanto:

$$
H\subseteq\langle g^{n_0}\rangle.
$$

Le due inclusioni danno:

$$
H=\langle g^{n_0}\rangle.
$$

---

## 9. Sottogruppi di un gruppo ciclico finito

Sia $G=\langle g\rangle$ un gruppo ciclico di ordine $n$.

Per ogni divisore $d$ di $n$ esiste un unico sottogruppo di ordine $d$, precisamente:

$$
H_d=\left\langle g^{n/d}\right\rangle.
$$

Infatti, usando la formula dell’ordine di una potenza:

$$
\operatorname{ord}\left(g^{n/d}\right)
=
\frac{n}{\gcd(n,n/d)}
=
\frac{n}{n/d}
=d.
$$

Quindi:

$$
\left|\left\langle g^{n/d}\right\rangle\right|=d.
$$

Viceversa, ogni sottogruppo di $G$ è di questa forma.

Pertanto:

- i sottogruppi di un gruppo ciclico finito sono in corrispondenza biunivoca con i divisori dell’ordine del gruppo;
- il numero dei sottogruppi di $G$ è $\tau(n)$, il numero dei divisori positivi di $n$;
- per ogni divisore $d\mid n$ esiste esattamente un sottogruppo di ordine $d$.

### Esempio

Se $G=\langle g\rangle$ ha ordine $12$, i sottogruppi hanno ordini:

$$
1,2,3,4,6,12.
$$

Sono:

$$
\langle g^{12}\rangle=\{e\},
$$

$$
\langle g^6\rangle \quad\text{di ordine }2,
$$

$$
\langle g^4\rangle \quad\text{di ordine }3,
$$

$$
\langle g^3\rangle \quad\text{di ordine }4,
$$

$$
\langle g^2\rangle \quad\text{di ordine }6,
$$

$$
\langle g\rangle=G \quad\text{di ordine }12.
$$

---

## 10. Elementi di un dato ordine

In un gruppo ciclico $G=\langle g\rangle$ di ordine $n$, gli elementi di ordine $d$ esistono solo se

$$
d\mid n.
$$

Il numero di elementi di ordine esattamente $d$ è:

$$
\boxed{\varphi(d)}.
$$

Infatti l’unico sottogruppo di ordine $d$ è

$$
H_d=\left\langle g^{n/d}\right\rangle,
$$

e gli elementi di ordine $d$ sono esattamente i generatori di $H_d$. Essendo $H_d$ ciclico di ordine $d$, il numero dei suoi generatori è $\varphi(d)$.

Gli elementi di ordine $d$ sono quindi:

$$
\left(g^{n/d}\right)^k
\qquad
\text{con }\gcd(k,d)=1.
$$

> [!example] Esempio
> In $\mathbb Z/12\mathbb Z$ (scritto additivamente, con generatore $\overline1$) gli elementi di ordine $4$ sono $\varphi(4)=2$: sono $\overline3$ e $\overline9$, cioè $k\cdot\overline{12/4}$ con $k=1,3$. Infatti $4\cdot\overline3=\overline{12}=\overline0$ e $2\cdot\overline3=\overline6\neq\overline0$.

---

## 11. Ordini nel gruppo moltiplicativo modulo $n$

Sia $\overline a\in(\mathbb Z/n\mathbb Z)^\times$. Il suo ordine moltiplicativo è il minimo intero positivo $m$ tale che

$$
\overline a^{\,m}=\overline1,
$$

equivalentemente:

$$
a^m\equiv1\pmod n.
$$

Per il teorema di Eulero:

$$
a^{\varphi(n)}\equiv1\pmod n.
$$

Di conseguenza:

$$
\operatorname{ord}(\overline a)\mid\varphi(n).
$$

Questa informazione è utile perché riduce la ricerca dell’ordine ai divisori di $\varphi(n)$.

### Esempio: ordine di $\overline 7$ modulo $100$

Poiché $\gcd(7,100)=1$, la classe $\overline7$ è invertibile modulo $100$. Inoltre:

$$
\varphi(100)=40.
$$

Si può calcolare direttamente:

$$
7^2=49,
$$

$$
7^4=49^2=2401\equiv1\pmod{100}.
$$

Poiché $7^2\not\equiv1\pmod{100}$, l’ordine non è $1$ né $2$. Pertanto:

$$
\operatorname{ord}_{100}(\overline7)=4.
$$

In generale, per determinare l’ordine di $\overline a$ modulo $n$:

1. si calcola $\varphi(n)$;
2. si considerano i divisori di $\varphi(n)$;
3. si cerca il più piccolo divisore $d$ tale che
   $$
   a^d\equiv1\pmod n.
   $$

### Esempio concettuale modulo $17$

Poiché $17$ è primo:

$$
\left|(\mathbb Z/17\mathbb Z)^\times\right|=\varphi(17)=16.
$$

Quindi, per ogni $a\not\equiv0\pmod{17}$:

$$
\operatorname{ord}_{17}(\overline a)\mid16.
$$

I possibili ordini sono dunque:

$$
1,2,4,8,16.
$$

Non serve che ogni elemento abbia ordine $16$: succede solo se il gruppo è generato da quell’elemento.

---

## 12. Calcolo dell’ordine tramite divisori

Supponiamo di sapere che

$$
\operatorname{ord}(g)=n
\qquad\text{e}\qquad
g^k
$$

è un elemento del gruppo generato da $g$.

Per trovare l’ordine di $g^k$ si può usare:

$$
\operatorname{ord}(g^k)=\frac{n}{\gcd(n,k)}.
$$

In alternativa, si può cercare il minimo divisore $d$ di $n$ tale che:

$$
(g^k)^d=e.
$$

Poiché:

$$
(g^k)^d=g^{kd},
$$

la condizione equivale a:

$$
n\mid kd.
$$

Il minimo $d$ che soddisfa questa divisibilità è esattamente:

$$
d=\frac{n}{\gcd(n,k)}.
$$

---

## 13. Un criterio di divisibilità per l’ordine

Se $g$ ha ordine $n$ e si verifica che

$$
g^m=e,
$$

allora:

$$
n\mid m.
$$

Il criterio si usa di solito così:

- per dimostrare che l’ordine di $g$ divide un certo numero, si trova una potenza di $g$ uguale all’identità;
- per dimostrare che l’ordine è esattamente un certo numero, si escludono i divisori propri.

Per esempio, se $g^6=e$, l’ordine di $g$ può essere soltanto uno dei divisori di $6$:

$$
1,2,3,6.
$$

Se inoltre $g^2\ne e$ e $g^3\ne e$, allora necessariamente:

$$
\operatorname{ord}(g)=6.
$$

---

## 14. Relazione tra ordine di un elemento e ordine del gruppo

Se $G$ è ciclico e $G=\langle g\rangle$, allora:

$$
\operatorname{ord}(g)=|G|.
$$

Se invece si prende una potenza $g^k$, in generale si ottiene un sottogruppo proprio:

$$
\langle g^k\rangle\le G.
$$

La sua cardinalità è:

$$
|\langle g^k\rangle|
=
\frac{|G|}{\gcd(|G|,k)}.
$$

Quindi:

- se $\gcd(|G|,k)=1$, allora $\langle g^k\rangle=G$;
- se $\gcd(|G|,k)>1$, allora $\langle g^k\rangle$ è un sottogruppo proprio.

---

## 15. Classi modulo $n$ e passaggio a un modulo divisore

Supponiamo che $d\mid n$. Allora si può considerare la riduzione modulo $d$:

$$
\mathbb Z/n\mathbb Z
\longrightarrow
\mathbb Z/d\mathbb Z,
\qquad
\overline a\longmapsto\overline a.
$$

La classe modulo $n$ di un numero determina una classe modulo $d$, poiché $d\mid n$.

Una stessa classe modulo $d$ ha più rappresentanti distinti modulo $n$. Precisamente, la classe $\overline a$ modulo $d$ viene sollevata alle classi modulo $n$:

$$
\overline a,\ 
\overline{a+d},\ 
\overline{a+2d},\ 
\ldots,\ 
\overline{a+\left(\frac nd-1\right)d}.
$$

Il numero di sollevamenti è:

$$
\frac nd.
$$

Infatti:

$$
a+qd\equiv a\pmod d
$$

per ogni intero $q$, e i valori distinti di $q$ modulo $n/d$ sono:

$$
q=0,1,\ldots,\frac nd-1.
$$

### Esempio

Consideriamo il passaggio da modulo $6$ a modulo $2$. La classe $\overline1$ modulo $2$ è rappresentata, modulo $6$, dalle classi:

$$
\overline1,\ \overline3,\ \overline5.
$$

Infatti sono tutte dispari e quindi congrue a $1$ modulo $2$.

La classe $\overline0$ modulo $2$ è rappresentata, modulo $6$, dalle classi:

$$
\overline0,\ \overline2,\ \overline4.
$$

Ogni classe modulo $2$ ha dunque:

$$
\frac62=3
$$

sollevamenti modulo $6$.

In generale, se $d\mid n$, ogni classe modulo $d$ ha esattamente $n/d$ rappresentanti distinti modulo $n$.

---

## 16. Osservazioni metodologiche

Per risolvere esercizi sugli ordini modulari conviene distinguere i seguenti problemi:

1. **Determinare se una classe è invertibile modulo $n$**:
   $$
   \gcd(a,n)=1.
   $$

2. **Determinare l’ordine moltiplicativo di una classe**:
   trovare il minimo $m>0$ tale che
   $$
   a^m\equiv1\pmod n.
   $$

3. **Usare il teorema di Eulero**:
   se $\gcd(a,n)=1$, allora
   $$
   \operatorname{ord}_n(a)\mid\varphi(n).
   $$

4. **Usare la formula dell’ordine di una potenza**:
   se $\operatorname{ord}(g)=n$, allora
   $$
   \operatorname{ord}(g^k)=\frac{n}{\gcd(n,k)}.
   $$

5. **Determinare un sottogruppo ciclico**:
   calcolare
   $$
   \langle g^k\rangle
   $$
   e il suo ordine.

6. **Controllare la ciclicità di un gruppo finito**:
   cercare un elemento il cui ordine sia uguale alla cardinalità del gruppo. Se nessun elemento ha tale ordine, il gruppo non è ciclico.
