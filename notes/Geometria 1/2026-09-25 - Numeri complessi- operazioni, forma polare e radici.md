---
type: lecture-note
course: Geometria 1
date: '2026-09-25'
title: Numeri complessi- operazioni, forma polare e radici
source_transcript: _transcripts/Geometria 1/2026-09-25 - Numeri complessi- operazioni, forma polare e
  radici.md
source_hash: sha256:5a8f706bd903b1fde9fbd3d3ae6bd71d9611dddfc9d36122fc7f52eb951c7757
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-25T18:16:05.917Z'
vault_path: Notes/Geometria 1/Lectures/2026-09-25 - Numeri complessi- operazioni, forma polare e radici.md
vault_hash: e41678afb94129e7cc6b4eea06378ce5804cf743180d44bcd5de6e1b68d78e13
---
## 1. Costruzione dell’insieme dei numeri complessi

I [[Numero complesso|numeri complessi]] sono un altro esempio di [[Campo|campo]], dopo i razionali, i reali e i campi finiti già visti.

Si introduce un simbolo $i$, detto **unità immaginaria**, con la proprietà

$$
i^2=-1.
$$

Un numero complesso si scrive nella forma

$$
z=a+ib,
$$

dove $a,b\in\mathbb{R}$.

L’insieme dei numeri complessi è quindi

$$
\mathbb{C}
=
\{a+ib\mid a,b\in\mathbb{R}\}.
$$

Ogni numero complesso è determinato in modo unico dalla coppia $(a,b)\in\mathbb{R}^2$, quindi si può pensare a $\mathbb{C}$ come all’insieme delle coppie ordinate di numeri reali:

$$
a+ib \longleftrightarrow (a,b).
$$

Nella scrittura $z=a+ib$:

- $a$ è la **parte reale** di $z$ e si indica con $\operatorname{Re}(z)$;
- $b$ è la **parte immaginaria** di $z$ e si indica con $\operatorname{Im}(z)$.

Quindi:

$$
\operatorname{Re}(z)=a,
\qquad
\operatorname{Im}(z)=b.
$$

La scrittura $a+ib$ è solo un modo di rappresentare il numero complesso. Occhio: il simbolo $+$ al suo interno non è la somma tra numeri complessi, serve semplicemente a separare la parte reale dalla parte immaginaria.

---

## 2. Somma di numeri complessi

La somma è definita **componente per componente**. Se

$$
z=a+ib,
\qquad
w=c+id,
$$

allora si pone

$$
z+w
:=
(a+c)+i(b+d).
$$

Qui $a+c$ e $b+d$ sono somme tra numeri reali.

In termini di coppie:

$$
(a,b)+(c,d)=(a+c,b+d).
$$

In pratica si usano le operazioni già note sui numeri reali, applicate separatamente alla parte reale e alla parte immaginaria.

### Esempio

$$
(2+i)+(3-2i)
=
(2+3)+i(1-2)
=
5-i.
$$

Il simbolo $:=$ (due punti prima dell’uguale) indica che si sta dando una **definizione**: non è una semplice trasformazione algebrica di un’espressione già nota, si sta stabilendo il significato di ciò che sta a sinistra.

---

## 3. Prodotto di numeri complessi

Anche il prodotto prende due numeri complessi e restituisce un numero complesso. Se

$$
z=a+ib,
\qquad
w=c+id,
$$

si definisce il prodotto sviluppando formalmente le parentesi e usando la relazione $i^2=-1$:

$$
\begin{aligned}
zw
&=(a+ib)(c+id)\\
&=ac+aid+ibc+i^2bd\\
&=ac+iad+ibc-bd\\
&=(ac-bd)+i(ad+bc).
\end{aligned}
$$

Quindi la definizione esplicita del prodotto è

$$
(a+ib)(c+id)
:=
(ac-bd)+i(ad+bc).
$$

I prodotti $ac$, $bd$, $ad$ e $bc$ sono prodotti di numeri reali.

La presenza del termine $-bd$ nella parte reale deriva precisamente dalla sostituzione

$$
i^2=-1.
$$

### Esempio

Calcoliamo

$$
(2+i)(3-2i).
$$

Applicando la formula:

$$
\begin{aligned}
(2+i)(3-2i)
&=(2\cdot 3-1\cdot(-2))
+i\bigl(2\cdot(-2)+1\cdot 3\bigr)\\
&=(6+2)+i(-4+3)\\
&=8-i.
\end{aligned}
$$

Nota bene, vanno distinti:

- il simbolo $+$ nella scrittura $a+ib$;
- l’operazione di somma tra numeri complessi;
- le somme e i prodotti tra numeri reali che compaiono nella formula del prodotto complesso.

---

## 4. Il significato di $i^2=-1$

Dalla definizione del prodotto, ponendo $z=w=i$, oppure scrivendo $i=0+i\cdot 1$, si ottiene

$$
i^2=-1.
$$

Infatti:

$$
(0+i)(0+i)
=
(0\cdot 0-1\cdot 1)+i(0\cdot 1+1\cdot 0)
=
-1+0i
=
-1.
$$

Analogamente,

$$
i(-1)=-i.
$$

Non sono proprietà aggiunte a mano: discendono dalle definizioni di somma e prodotto.

---

## 5. Interpretazione geometrica: il piano complesso

Il numero complesso

$$
z=a+ib
$$

si rappresenta nel [[Numero complesso|piano complesso]] (il piano cartesiano) con il punto di coordinate $(a,b)$.

- L’asse orizzontale rappresenta i numeri reali.
- L’asse verticale rappresenta i numeri della forma $ib$, con $b\in\mathbb{R}$.
- Il numero complesso $a+ib$ corrisponde al vettore che parte dall’origine e arriva al punto $(a,b)$.

In questo senso:

$$
\mathbb{C}\simeq\mathbb{R}^2.
$$

### I numeri reali dentro $\mathbb{C}$

Un numero reale $a$ può essere identificato con il numero complesso

$$
a+i\cdot 0.
$$

Per questo motivo si considera $\mathbb{R}$ come sottoinsieme di $\mathbb{C}$:

$$
\mathbb{R}\subseteq\mathbb{C}.
$$

Se si sommano o si moltiplicano due numeri complessi con parte immaginaria nulla, le definizioni date coincidono con le usuali operazioni sui reali. Per esempio:

$$
(a+i0)+(c+i0)=(a+c)+i0,
$$

e

$$
(a+i0)(c+i0)=ac+i0.
$$

Quindi $\mathbb{R}$ è un sottoinsieme di $\mathbb{C}$ chiuso rispetto alle stesse operazioni di somma e prodotto.

### Somma come parallelogramma

Se $z$ e $w$ sono rappresentati come vettori nel piano, la somma $z+w$ si ottiene con la regola del parallelogramma. Se

$$
z=a+ib,
\qquad
w=c+id,
$$

allora

$$
z+w=(a+c)+i(b+d),
$$

che corrisponde alla somma delle coordinate dei due vettori.

---

## 6. Verifica delle proprietà di campo

Finora abbiamo solo definito le operazioni: non abbiamo ancora dimostrato che $\mathbb{C}$ sia un campo. Per farlo bisogna verificare gli assiomi di campo.

Molte verifiche sono dirette e si riducono alle proprietà note dei numeri reali.

### Elemento neutro della somma

L’elemento neutro della somma è

$$
0+0i.
$$

Infatti:

$$
(a+ib)+(0+0i)=a+ib.
$$

### Opposto additivo

L’opposto di

$$
z=a+ib
$$

è

$$
-z=-a-ib.
$$

Infatti:

$$
(a+ib)+(-a-ib)=0+0i.
$$

### Associatività della somma

Per $z,w,u\in\mathbb{C}$ si verifica che

$$
(z+w)+u=z+(w+u).
$$

La verifica si fa scrivendo i tre numeri in forma cartesiana e usando l’associatività della somma in $\mathbb{R}$, separatamente per parte reale e parte immaginaria.

### Commutatività della somma

Analogamente:

$$
z+w=w+z.
$$

Questa proprietà segue dalla commutatività della somma tra numeri reali.

Le altre proprietà del campo, tra cui la distributività e l’esistenza dell’inverso moltiplicativo per ogni numero complesso non nullo, vanno verificate a partire dalle definizioni: non si possono dare per vere solo perché si è detto che $\mathbb{C}$ è un campo.

> [!warning]
> Le proprietà delle operazioni sui numeri complessi vanno dedotte dalle definizioni. La verifica può essere meccanica e un po’ noiosa, ma serve a distinguere una proprietà dimostrata da una semplice affermazione.

---

## 7. Modulo o norma di un numero complesso

Sia

$$
z=a+ib.
$$

Il **[[Modulo di un numero complesso|modulo]]** o **norma** di $z$ è definito da

$$
|z|:=\sqrt{a^2+b^2}.
$$

Il modulo è un numero reale non negativo:

$$
|z|\in\mathbb{R}_{\geq 0}.
$$

Geometricamente, se $z$ è rappresentato dal punto $(a,b)$, allora $|z|$ è la distanza di quel punto dall’origine.

La formula deriva dal teorema di Pitagora: il segmento che congiunge l’origine al punto $(a,b)$ è l’ipotenusa di un triangolo rettangolo con cateti di lunghezza $|a|$ e $|b|$.

In questa formula non compare $i$, perché il modulo è definito direttamente a partire dalle coordinate reali $a$ e $b$.

### Esempi

Se $z=3$, allora formalmente $z=3+0i$ e

$$
|z|=\sqrt{3^2+0^2}=3.
$$

Se $z=-2$, allora

$$
|-2|=\sqrt{(-2)^2+0^2}=2.
$$

Il modulo di un numero reale coincide quindi con il suo [[Valore assoluto|valore assoluto]].

---

## 8. Quando il modulo è nullo

Poiché $a^2\geq 0$ e $b^2\geq 0$, si ha

$$
|z|=\sqrt{a^2+b^2}=0
$$

se e solo se

$$
a^2+b^2=0.
$$

Una somma di due quadrati reali è nulla se e solo se sono nulli entrambi. Pertanto:

$$
|z|=0
\iff
a=0\ \text{e}\ b=0
\iff
z=0.
$$

Quindi l’unico numero complesso di modulo zero è il numero complesso nullo.

---

## 9. Coniugio complesso

Il **[[Coniugio complesso|coniugato]]** del numero complesso

$$
z=a+ib
$$

è definito come

$$
\overline{z}:=a-ib.
$$

Il coniugio mantiene invariata la parte reale e cambia segno alla parte immaginaria:

$$
\operatorname{Re}(\overline z)=\operatorname{Re}(z),
$$

$$
\operatorname{Im}(\overline z)=-\operatorname{Im}(z).
$$

### Interpretazione geometrica

Nel piano complesso, il coniugio corrisponde alla riflessione rispetto all’asse reale.

Il punto $(a,b)$ viene mandato nel punto $(a,-b)$. I punti dell’asse reale rimangono fissi.

### Numeri reali come punti fissi del coniugio

Si ha

$$
z=\overline z
$$

se e solo se

$$
a+ib=a-ib.
$$

Questo accade esattamente quando

$$
b=0.
$$

Pertanto:

$$
z=\overline z
\iff
\operatorname{Im}(z)=0
\iff
z\in\mathbb{R}.
$$

Il coniugio, quindi, è una trasformazione di $\mathbb{C}$ in sé che permette di riconoscere i numeri reali dentro i complessi.

---

## 10. Proprietà del coniugio

Per $z,w\in\mathbb{C}$ valgono le proprietà:

$$
\overline{z+w}=\overline z+\overline w,
$$

$$
\overline{zw}=\overline z\,\overline w,
$$

e

$$
\overline{\overline z}=z.
$$

L’ultima uguaglianza è evidente: si cambia due volte il segno della parte immaginaria.

### Verifica della proprietà rispetto alla somma

Siano

$$
z=a+ib,
\qquad
w=c+id.
$$

Allora:

$$
z+w=(a+c)+i(b+d),
$$

quindi

$$
\overline{z+w}
=
(a+c)-i(b+d).
$$

D’altra parte:

$$
\overline z+\overline w
=
(a-ib)+(c-id)
=
(a+c)-i(b+d).
$$

I due risultati coincidono:

$$
\overline{z+w}=\overline z+\overline w.
$$

La verifica della proprietà rispetto al prodotto si esegue nello stesso modo, usando la formula del prodotto complesso.

---

## 11. Relazione tra modulo e coniugio

Consideriamo il prodotto tra $z$ e il suo coniugato:

$$
z\overline z
=
(a+ib)(a-ib).
$$

Sviluppando:

$$
\begin{aligned}
z\overline z
&=a^2-abi+abi-i^2b^2\\
&=a^2+b^2.
\end{aligned}
$$

I termini misti si cancellano e, poiché $i^2=-1$, si ottiene

$$
z\overline z=a^2+b^2.
$$

Dalla definizione del modulo,

$$
|z|^2=a^2+b^2.
$$

Quindi:

$$
\boxed{z\overline z=|z|^2}.
$$

Il prodotto $z\overline z$ è sempre un numero reale non negativo.

Questa relazione è la chiave per costruire l’inverso moltiplicativo di un numero complesso non nullo.

---

## 12. Inverso moltiplicativo

Sia $z\neq 0$. Per dimostrare che $\mathbb{C}$ è un campo bisogna trovare un numero complesso $z^{-1}$ tale che

$$
zz^{-1}=1.
$$

Poiché

$$
z\overline z=|z|^2,
$$

e $z\neq 0$ implica $|z|\neq 0$, il numero reale $|z|^2$ è diverso da zero e possiede l’inverso reale

$$
\frac{1}{|z|^2}.
$$

Allora:

$$
z\left(\frac{\overline z}{|z|^2}\right)
=
\frac{z\overline z}{|z|^2}
=
\frac{|z|^2}{|z|^2}
=
1.
$$

Pertanto:

$$
\boxed{
z^{-1}=\frac{\overline z}{|z|^2}
}.
$$

Se $z=a+ib$, la formula diventa

$$
\frac{1}{a+ib}
=
\frac{a-ib}{a^2+b^2},
\qquad
a+ib\neq 0.
$$

Il coniugio permette quindi di eliminare la parte immaginaria dal denominatore.

### Unicità dell’inverso

L’inverso moltiplicativo, quando esiste, è unico. Non è una proprietà specifica dei complessi: vale in ogni campo.

Supponiamo che $B$ e $B'$ siano due inversi dello stesso elemento $A$. Allora:

$$
AB=1,
\qquad
AB'=1.
$$

Usando associatività, commutatività e l’elemento neutro:

$$
\begin{aligned}
B
&=B\cdot 1\\
&=B(AB')\\
&=(BA)B'\\
&=1\cdot B'\\
&=B'.
\end{aligned}
$$

Quindi $B=B'$.

---

## 13. Esempio di divisione tra numeri complessi

Calcoliamo

$$
\frac{3-2i}{1-i}.
$$

Si moltiplica numeratore e denominatore per il coniugato del denominatore:

$$
\frac{3-2i}{1-i}
=
(3-2i)\frac{1+i}{|1-i|^2}.
$$

Il modulo al quadrato del denominatore è

$$
|1-i|^2=1^2+(-1)^2=2.
$$

Quindi:

$$
\begin{aligned}
\frac{3-2i}{1-i}
&=\frac{(3-2i)(1+i)}{2}\\
&=\frac{3+3i-2i-2i^2}{2}\\
&=\frac{3+i+2}{2}\\
&=\frac{5+i}{2}.
\end{aligned}
$$

Dunque:

$$
\boxed{
\frac{3-2i}{1-i}
=
\frac52+\frac12 i
}.
$$

---

## 14. Coordinate polari e forma trigonometrica

La rappresentazione cartesiana

$$
z=a+ib
$$

descrive un numero complesso tramite le coordinate del punto $(a,b)$.

Si può usare un altro sistema di coordinate, le **coordinate polari**: il numero complesso viene descritto da:

1. la distanza $\rho$ dall’origine;
2. un angolo $\theta$ che indica la direzione del vettore.

La distanza è il modulo:

$$
\rho=|z|=\sqrt{a^2+b^2}.
$$

L’angolo $\theta$ viene misurato a partire dalla semiretta reale positiva, in senso antiorario.

Se $z\neq 0$, l’angolo è detto **argomento** di $z$ e si scrive

$$
\arg(z)=\theta.
$$

Per $z=0$ l’argomento non è definito: il vettore nullo non ha una direzione determinata.

### 14.1 Periodicità dell’argomento

Gli angoli

$$
\theta,\qquad
\theta+2\pi,\qquad
\theta-2\pi,\qquad
\theta+2k\pi
$$

rappresentano tutti la stessa direzione, dove $k\in\mathbb{Z}$.

Perciò l’argomento non è un singolo numero reale determinato univocamente, ma è definito a meno di multipli interi di $2\pi$:

$$
\arg(z)=\theta+2k\pi,
\qquad
k\in\mathbb{Z}.
$$

Non è un problema quando si usano [[Funzioni trigonometriche|seno e coseno]], perché hanno periodo $2\pi$:

$$
\cos(\theta+2k\pi)=\cos\theta,
$$

$$
\sin(\theta+2k\pi)=\sin\theta.
$$

### 14.2 Passaggio da coordinate polari a cartesiane

Dal triangolo rettangolo associato al punto $(a,b)$ si ricava:

$$
a=\rho\cos\theta,
$$

$$
b=\rho\sin\theta.
$$

Quindi:

$$
\boxed{
z=\rho\cos\theta+i\rho\sin\theta
}
$$

oppure, raccogliendo $\rho$:

$$
\boxed{
z=\rho(\cos\theta+i\sin\theta)
}.
$$

Questa è la **forma trigonometrica** o **[[Forma polare|forma polare]]** del numero complesso.

> [!example] Esempio
> Per $z=-1$ si ha $\rho=1$ e $\theta=\pi$, quindi $-1=\cos\pi+i\sin\pi$. Anche $\theta=-\pi$ o $3\pi$ vanno bene: l’argomento è definito a meno di multipli di $2\pi$.

### 14.3 Passaggio da coordinate cartesiane a polari

Dato $z=a+ib$, il modulo si calcola con

$$
\rho=\sqrt{a^2+b^2}.
$$

Per l’angolo, quando $a\neq 0$, si può usare la relazione

$$
\tan\theta=\frac{b}{a}.
$$

In prima approssimazione si può scrivere

$$
\theta=\arctan\left(\frac{b}{a}\right),
$$

ma questa formula va corretta in base al quadrante, perché punti in quadranti diversi possono avere lo stesso rapporto $b/a$ (qui compare l’[[Funzioni trigonometriche inverse|arcotangente]]).

In particolare:

- se $a>0$, l’angolo può essere determinato direttamente tramite l’arco tangente, scegliendo il quadrante corretto;
- se $a<0$, occorre aggiungere o sottrarre $\pi$;
- se $a=0$ e $b>0$, allora $\theta=\frac{\pi}{2}$;
- se $a=0$ e $b<0$, allora $\theta=-\frac{\pi}{2}$ oppure $\frac{3\pi}{2}$;
- se $a=b=0$, l’argomento non è definito.

Il punto è che la tangente fissa la pendenza, ma da sola non individua il quadrante.

---

## 15. Prodotto in forma polare

La forma cartesiana rende immediata la somma, ma il prodotto è meno trasparente. In forma polare, invece, il prodotto ha un significato geometrico molto semplice.

Siano

$$
z=\rho(\cos\theta+i\sin\theta),
$$

e

$$
w=\lambda(\cos\varphi+i\sin\varphi).
$$

Allora:

$$
\begin{aligned}
zw
&=
\rho\lambda
(\cos\theta+i\sin\theta)
(\cos\varphi+i\sin\varphi)\\
&=
\rho\lambda
\bigl[
\cos\theta\cos\varphi
-\sin\theta\sin\varphi\\
&\qquad\qquad
+i(\cos\theta\sin\varphi
+\sin\theta\cos\varphi)
\bigr].
\end{aligned}
$$

Usando le formule trigonometriche di addizione:

$$
\cos(\theta+\varphi)
=
\cos\theta\cos\varphi-\sin\theta\sin\varphi,
$$

$$
\sin(\theta+\varphi)
=
\sin\theta\cos\varphi+\cos\theta\sin\varphi,
$$

si ottiene

$$
\boxed{
zw
=
\rho\lambda
\left[
\cos(\theta+\varphi)
+i\sin(\theta+\varphi)
\right]
}.
$$

Di conseguenza:

$$
\boxed{|zw|=|z|\,|w|}
$$

e

$$
\boxed{\arg(zw)=\arg(z)+\arg(w)}
\quad\text{modulo }2\pi.
$$

#### Interpretazione geometrica

Per moltiplicare due numeri complessi in forma polare:

- si moltiplicano i moduli;
- si sommano gli argomenti.

Quindi il prodotto corrisponde a:

1. una dilatazione o contrazione con fattore pari al prodotto dei moduli;
2. una rotazione di angolo pari alla somma degli angoli.

Così il prodotto, che in coordinate cartesiane è una formula piuttosto macchinosa, diventa un’operazione geometrica chiara.

---

## 16. Potenze di numeri complessi

Se

$$
z=\rho(\cos\theta+i\sin\theta),
$$

allora la potenza $n$-esima si ottiene moltiplicando $z$ per sé stesso $n$ volte.

A ogni prodotto:

- i moduli si moltiplicano;
- gli argomenti si sommano.

Pertanto:

$$
\boxed{
z^n
=
\rho^n
\left[
\cos(n\theta)+i\sin(n\theta)
\right]
}.
$$

Questa formula è la **formula di De Moivre**.

In termini geometrici, elevare un numero complesso alla potenza $n$-esima significa:

- elevare il modulo alla potenza $n$;
- moltiplicare l’argomento per $n$.

La forma polare rende quindi molto semplice il calcolo delle potenze.

> [!example] Esempio
> Per $z=1+i=\sqrt2\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right)$ si ha $z^8=(\sqrt2)^8(\cos 2\pi+i\sin 2\pi)=16$.

---

## 17. Radici $n$-esime di un numero complesso

Consideriamo l’equazione

$$
z^n=w,
$$

dove $w$ è un numero complesso noto e $z$ è l’incognita. Le soluzioni sono le [[Radice n-esima di un numero complesso|radici]] $n$-esime di $w$.

Supponiamo inizialmente che

$$
w\neq 0.
$$

Scriviamo $w$ in forma polare:

$$
w=R(\cos\theta+i\sin\theta),
$$

con $R=|w|>0$.

Cerchiamo $z$ nella forma

$$
z=\rho(\cos\varphi+i\sin\varphi).
$$

Dalla formula delle potenze:

$$
z^n
=
\rho^n
\left[
\cos(n\varphi)+i\sin(n\varphi)
\right].
$$

Per avere $z^n=w$ devono valere due condizioni.

### 17.1 Condizione sui moduli

Deve essere

$$
\rho^n=R.
$$

Poiché $R\geq 0$, nei reali esiste un’unica radice $n$-esima non negativa:

$$
\boxed{
\rho=\sqrt[n]{R}
}.
$$

Il modulo della radice è quindi univocamente determinato.

### 17.2 Condizione sugli argomenti

Gli argomenti di $w$ sono

$$
\theta+2k\pi,
\qquad
k\in\mathbb{Z}.
$$

Dunque deve essere

$$
n\varphi=\theta+2k\pi.
$$

Dividendo per $n$:

$$
\boxed{
\varphi_k
=
\frac{\theta+2k\pi}{n}
=
\frac{\theta}{n}+\frac{2k\pi}{n}
}.
$$

Le soluzioni sono quindi

$$
\boxed{
z_k
=
\sqrt[n]{R}
\left[
\cos\left(\frac{\theta+2k\pi}{n}\right)
+
i\sin\left(\frac{\theta+2k\pi}{n}\right)
\right]
}.
$$

Per ottenere tutte le soluzioni distinte è sufficiente prendere

$$
k=0,1,\ldots,n-1.
$$

Se si aumenta $k$ di $n$, infatti:

$$
\frac{\theta+2(k+n)\pi}{n}
=
\frac{\theta+2k\pi}{n}+2\pi,
$$

che rappresenta nuovamente la stessa direzione.

Pertanto, se $w\neq 0$, l’equazione $z^n=w$ ha esattamente $n$ soluzioni complesse distinte.

Geometricamente, le soluzioni stanno su una circonferenza di raggio $\sqrt[n]{R}$ e sono i vertici di un poligono regolare con $n$ lati, centrato nell’origine.

---

### 18. Caso particolare: $w=0$

Se

$$
z^n=0,
$$

allora necessariamente

$$
z=0.
$$

Quindi l’equazione ha una sola soluzione distinta:

$$
\boxed{z=0}.
$$

La formula delle radici qui non si applica, perché l’argomento del numero complesso nullo non è definito.

---

### 19. Esempio: soluzione di $z^3=-8$

Consideriamo

$$
z^3=-8.
$$

Nei numeri reali si vede immediatamente una soluzione:

$$
z=-2.
$$

Nei numeri complessi, però, le radici cubiche sono tre.

#### Modulo

Il modulo del numero a destra è

$$
|-8|=8.
$$

Quindi il modulo di ogni radice è

$$
|z|=\sqrt[3]{8}=2.
$$

#### Argomento

Il numero $-8$ si trova sull’asse reale negativo, quindi un suo argomento è

$$
\theta=\pi.
$$

Gli argomenti delle radici sono

$$
\varphi_k
=
\frac{\pi+2k\pi}{3},
\qquad
k=0,1,2.
$$

Si ottengono:

- per $k=0$:

$$
\varphi_0=\frac{\pi}{3};
$$

- per $k=1$:

$$
\varphi_1=\pi;
$$

- per $k=2$:

$$
\varphi_2=\frac{5\pi}{3}.
$$

Le tre radici sono quindi

$$
z_k=2(\cos\varphi_k+i\sin\varphi_k).
$$

Calcolandole:

#### Prima radice

$$
z_0
=
2\left(\cos\frac{\pi}{3}+i\sin\frac{\pi}{3}\right)
=
2\left(\frac12+i\frac{\sqrt3}{2}\right)
=
1+i\sqrt3.
$$

#### Seconda radice

$$
z_1
=
2(\cos\pi+i\sin\pi)
=
2(-1+0i)
=
-2.
$$

#### Terza radice

$$
z_2
=
2\left(\cos\frac{5\pi}{3}+i\sin\frac{5\pi}{3}\right)
=
2\left(\frac12-i\frac{\sqrt3}{2}\right)
=
1-i\sqrt3.
$$

Pertanto:

$$
\boxed{
z\in\{-2,\ 1+i\sqrt3,\ 1-i\sqrt3\}
}.
$$

Le tre soluzioni sono i vertici di un triangolo equilatero inscritto nella circonferenza di raggio $2$ e centrato nell’origine.

---

### 20. Esercizi proposti

Sono stati proposti esercizi del tipo:

$$
z^3=1,
$$

e

$$
z^4=1.
$$

Si risolvono con la formula generale delle radici $n$-esime.

Per esempio, se

$$
z^n=1,
$$

si scrive

$$
1=\cos(2k\pi)+i\sin(2k\pi),
$$

e quindi le soluzioni sono

$$
z_k
=
\cos\left(\frac{2k\pi}{n}\right)
+
i\sin\left(\frac{2k\pi}{n}\right),
\qquad
k=0,\ldots,n-1.
$$

Sono i vertici di un poligono regolare inscritto nella circonferenza unitaria (le radici dell’unità).

---

## 21. Teorema fondamentale dell’algebra

Il fatto che un numero complesso non nullo abbia esattamente $n$ radici $n$-esime fa parte di un quadro più generale, quello dei [[Polinomio|polinomi]] complessi.

Il **[[Teorema fondamentale dell'algebra|teorema fondamentale dell’algebra]]** afferma:

> Ogni polinomio non costante a coefficienti complessi possiede almeno una radice complessa.

In forma matematica, se

$$
P(z)\in\mathbb{C}[z]
$$

è un polinomio non costante, allora esiste $z_0\in\mathbb{C}$ tale che

$$
P(z_0)=0.
$$

Questo risultato non vale analogamente nei numeri reali. Ad esempio, il polinomio

$$
x^2+1
$$

non ha radici reali, perché

$$
x^2+1>0
\qquad
\text{per ogni }x\in\mathbb{R}.
$$

Nei numeri complessi, invece, ha le due radici

$$
x=i
\qquad\text{e}\qquad
x=-i.
$$

I numeri complessi sono quindi un campo abbastanza grande da garantire una radice a ogni polinomio non costante a coefficienti complessi.

### 21.1 Fattorizzazione dopo aver trovato una radice

Se $P(z)$ è un polinomio e $z_0$ è una sua radice, cioè

$$
P(z_0)=0,
$$

allora il polinomio $z-z_0$ divide $P(z)$ ($z_0$ è una [[Radice di un polinomio|radice]] di $P$). Esiste quindi un polinomio $Q(z)$ tale che

$$
P(z)=(z-z_0)Q(z).
$$

Se $P$ ha grado $n$, allora $Q$ ha grado $n-1$.

Ripetendo il procedimento si possono trovare tutte le radici e fattorizzare il polinomio in fattori lineari complessi:

$$
P(z)
=
a_n(z-z_1)(z-z_2)\cdots(z-z_n),
$$

contando le radici con la loro molteplicità.

Il teorema fondamentale dell’algebra non dice che le radici siano tutte diverse: una stessa radice può comparire più volte nella fattorizzazione.
