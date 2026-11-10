---
type: lecture-note
course: Analisi 1
date: '2026-09-30'
title: Simmetrie, monotonia e grafici delle funzioni elementari
source_transcript: _transcripts/Analisi 1/2026-09-30 - Simmetrie, monotonia e grafici delle funzioni elementari.md
source_hash: sha256:acf8c406bfb075458f303e5843955f72b3da79f833a8e7ca99aeef789d8b0090
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-30T14:07:17.430Z'
vault_path: Notes/Analisi 1/Lectures/2026-09-30 - Simmetrie, monotonia e grafici delle funzioni elementari.md
vault_hash: 219351c6da54e47f5a0152e975661b5dbb30919e86213c0cf468e34fe9a766f6
---

# Simmetrie, monotonia e grafici delle funzioni elementari

## 1. Funzioni reali e grafico

Una **funzione reale** è una [[Funzione|funzione]]

$$
f\colon A\to\mathbb{R},
$$

dove $A\subseteq\mathbb{R}$ è l’insieme di partenza, in genere non vuoto. L’insieme di arrivo è $\mathbb{R}$, salvo diversa indicazione.

Il **grafico** di $f$ è l’insieme delle coppie ordinate

$$
\operatorname{Graf}(f)
=
\left\{(x,y)\in\mathbb{R}^2 : x\in A,\ y=f(x)\right\}.
$$

Equivalentemente,

$$
\operatorname{Graf}(f)
=
\left\{(x,f(x)) : x\in A\right\}.
$$

Il grafico permette di leggere geometricamente molte proprietà della funzione, tra cui:

- simmetrie;
- monotonia;
- iniettività e suriettività;
- numero di soluzioni di equazioni e disequazioni;
- operazioni algebriche e trasformazioni del grafico.

---

## 2. Proprietà di simmetria

### 2.1 Funzioni pari

Sia $f\colon\mathbb{R}\to\mathbb{R}$. La funzione si dice **[[Funzione pari e dispari|pari]]** se

$$
\forall x\in\mathbb{R},\qquad f(-x)=f(x).
$$

La definizione richiede che il dominio sia simmetrico rispetto a $0$: se $x$ sta nel dominio, deve starci anche $-x$.

#### Interpretazione geometrica

Il grafico di una funzione pari è simmetrico rispetto all’asse $y$.

Se si conosce il grafico per $x\geq 0$, il resto si ottiene riflettendo la parte nota rispetto all’asse $y$.

---

### 2.2 Funzioni dispari

Sia $f\colon\mathbb{R}\to\mathbb{R}$. La funzione si dice **dispari** se

$$
\forall x\in\mathbb{R},\qquad f(-x)=-f(x).
$$

Anche qui il dominio deve essere simmetrico rispetto all’origine.

#### Interpretazione geometrica

Il grafico di una funzione dispari è simmetrico rispetto all’origine.

Se si conosce il grafico per $x\geq 0$, il resto si ottiene con una rotazione di $180^\circ$ attorno all’origine, cioè ribaltando rispetto all’origine.

---

### 2.3 Funzioni periodiche

Una funzione $f\colon\mathbb{R}\to\mathbb{R}$ si dice **[[Funzione periodica|periodica]]** se esiste un numero $T>0$ tale che

$$
\forall x\in\mathbb{R},\qquad f(x+T)=f(x).
$$

Un tale $T$ si chiama **periodo** della funzione.

Geometricamente, il grafico si ripete traslando orizzontalmente un suo tratto di ampiezza $T$. Conoscendo il grafico su un intervallo di lunghezza $T$, si ricostruisce il grafico completo per ripetizione.

> [!example] Esempio
> La funzione “parte frazionaria” $f(x)=x-\lfloor x\rfloor$ (dove $\lfloor x\rfloor$ è il più grande intero $\leq x$) è periodica di periodo $T=1$: il suo grafico è una “dentatura” che ripete lo stesso tratto di segmento su ogni intervallo $[k,k+1)$.

#### Il periodo non è unico

Se $T$ è un periodo, in generale anche i multipli interi positivi di $T$ sono periodi:

$$
T,\ 2T,\ 3T,\dots
$$

Perciò il periodo non è mai unico in senso assoluto.

A volte esiste un periodo positivo più piccolo di tutti gli altri, che si chiama **periodo minimo**.

> [!warning]
> Non confondere l’intuizione grafica con una proprietà generale. In particolare, la somma di due funzioni periodiche non è necessariamente periodica.

Se $f$ e $g$ sono periodiche con lo stesso periodo $T$, anche $f+g$ è periodica con periodo $T$. Se invece hanno periodi diversi, la somma può non essere periodica. Esistono infatti funzioni periodiche $f$ e $g$ tali che $f+g$ non sia periodica; costruire esempi rigorosi richiede strumenti teorici che non abbiamo ancora.

---

### 2.4 Costruzione di funzioni pari e dispari

Supponiamo di conoscere una funzione soltanto per $x\geq 0$.

#### Costruzione della funzione pari

Per renderla pari, si riflette il grafico della parte destra rispetto all’asse $y$. In formule, la parte negativa si definisce imponendo

$$
f(-x)=f(x).
$$

#### Costruzione della funzione dispari

Per renderla dispari, si riflette la parte destra rispetto all’origine. In formule, si impone

$$
f(-x)=-f(x).
$$

Questa costruzione è utile per completare graficamente una funzione definita inizialmente solo su $[0,+\infty)$.

---

## 3. Monotonia

La [[Funzione monotona|monotonia]] descrive il comportamento di crescita o decrescita di una funzione.

Occorre specificare sempre se la funzione è **debolmente** o **strettamente** crescente/decrescente.

### 3.1 Funzione debolmente crescente

Una funzione $f\colon\mathbb{R}\to\mathbb{R}$ è **debolmente crescente** se

$$
\forall x,y\in\mathbb{R},\qquad
x<y \Longrightarrow f(x)\leq f(y).
$$

In questa definizione può succedere che $f(x)=f(y)$ anche con $x\neq y$.

Si può usare anche la formulazione equivalente

$$
x\leq y \Longrightarrow f(x)\leq f(y).
$$

> [!example] Esempio
> La funzione $f(x)=\max\{x,0\}$ è debolmente crescente ma non strettamente: vale $0$ su tutta la semiretta $(-\infty,0]$ e poi cresce come $x$. Invece $g(x)=x^3$ è strettamente crescente.

---

### 3.2 Funzione strettamente crescente

La funzione è **strettamente crescente** se

$$
\forall x,y\in\mathbb{R},\qquad
x<y \Longrightarrow f(x)<f(y).
$$

La differenza rispetto alla crescenza debole è il passaggio da $\leq$ a $<$.

---

### 3.3 Funzione debolmente decrescente

La funzione è **debolmente decrescente** se

$$
\forall x,y\in\mathbb{R},\qquad
x<y \Longrightarrow f(x)\geq f(y).
$$

---

### 3.4 Funzione strettamente decrescente

La funzione è **strettamente decrescente** se

$$
\forall x,y\in\mathbb{R},\qquad
x<y \Longrightarrow f(x)>f(y).
$$

---

### 3.5 Funzione monotona

Una funzione si dice **monotona** se rientra in uno di questi casi:

- debolmente crescente;
- strettamente crescente;
- debolmente decrescente;
- strettamente decrescente.

Meglio non dire “monotona” in modo generico: quando serve, va specificato il tipo di monotonia.

---

### 3.6 Stretta monotonia e iniettività

Ogni funzione strettamente crescente o strettamente decrescente è iniettiva.

Infatti, supponiamo per esempio che $f$ sia strettamente crescente e prendiamo $x_1\neq x_2$. Uno dei due numeri è necessariamente maggiore dell’altro. Se, ad esempio,

$$
x_1<x_2,
$$

allora

$$
f(x_1)<f(x_2),
$$

e quindi $f(x_1)\neq f(x_2)$.

Lo stesso ragionamento vale per una funzione strettamente decrescente.

La monotonia debole, invece, non garantisce l’iniettività: una funzione debolmente crescente può essere costante su un intervallo.

---

## 4. Potenze con esponente intero positivo

Consideriamo la funzione

$$
f(x)=x^k,
\qquad k\in\mathbb{N},\ k>0.
$$

Il comportamento dipende molto dalla parità di $k$.

---

### 4.1 Potenze pari

Sia $k$ pari. Allora

$$
f(x)=x^k
$$

è una funzione pari, perché

$$
f(-x)=(-x)^k=x^k=f(x).
$$

Il grafico è simmetrico rispetto all’asse $y$.

#### Considerata su $\mathbb{R}$

Come funzione

$$
f\colon\mathbb{R}\to\mathbb{R},
$$

la potenza pari:

- non è iniettiva, perché $f(x)=f(-x)$;
- non è suriettiva su $\mathbb{R}$, perché $x^k\geq 0$ per ogni $x$;
- ha immagine $[0,+\infty)$;
- non è strettamente monotona su tutto $\mathbb{R}$;
- è debolmente decrescente su $(-\infty,0]$;
- è strettamente crescente su $[0,+\infty)$.

Per esempio, per $k=2$,

$$
(-3)^2=3^2.
$$

Quindi la funzione non è iniettiva.

#### Restrizione a $[0,+\infty)$

Consideriamo invece

$$
f\colon[0,+\infty)\to[0,+\infty),
\qquad
f(x)=x^k.
$$

In questo caso la funzione è:

- strettamente crescente;
- iniettiva;
- suriettiva;
- quindi biiettiva e invertibile.

La sua inversa è la funzione radice di indice $k$:

$$
f^{-1}(x)=\sqrt[k]{x}.
$$

Per $k$ pari, la radice è definita come funzione

$$
\sqrt[k]{\phantom{x}}\colon[0,+\infty)\to[0,+\infty).
$$

Quindi:

- l’argomento della radice deve essere maggiore o uguale a $0$;
- il risultato della radice è sempre maggiore o uguale a $0$.

---

### 4.2 Dimostrazione della stretta crescenza delle potenze pari su $[0,+\infty)$

Siano

$$
0\leq x<y.
$$

Si vuole dimostrare che

$$
x^k<y^k
$$

per $k$ pari.

Nel caso $k=2$:

$$
0\leq x<y.
$$

Moltiplicando la relazione $x<y$ per $x\geq 0$ si ottiene

$$
x^2\leq xy.
$$

Moltiplicando invece $x<y$ per $y>0$ si ottiene

$$
xy<y^2.
$$

Pertanto

$$
x^2\leq xy<y^2,
$$

da cui

$$
x^2<y^2.
$$

Il ragionamento per le potenze pari di ordine superiore si basa sulle proprietà dell’ordine e della moltiplicazione nei numeri reali.

La parte sulla stretta crescenza, e quindi sull’iniettività, è abbastanza elementare. La parte più delicata è la suriettività.

---

### 4.3 Il ruolo dell’assioma di completezza

Dire che la funzione

$$
x\mapsto x^2
$$

da $[0,+\infty)$ a $[0,+\infty)$ è suriettiva significa affermare che per ogni $y\geq 0$ esiste $x\geq 0$ tale che

$$
x^2=y.
$$

In particolare, si afferma l’esistenza di un numero reale il cui quadrato è $2$.

Questa non è una conseguenza immediata delle sole proprietà algebriche dei numeri razionali. Sui razionali positivi la funzione $x\mapsto x^2$ è strettamente crescente, ma non è suriettiva sui razionali positivi: non esiste alcun razionale $q$ tale che $q^2=2$.

La suriettività sulle parti positive dei reali dipende dall’**[[Assioma di completezza|assioma di completezza]]** dei numeri reali, che è essenziale per garantire l’esistenza delle radici.

Le potenze sono definite direttamente a partire dalla moltiplicazione:

$$
x^2=x\cdot x,
$$

$$
x^4=x\cdot x\cdot x\cdot x.
$$

Le radici, invece, nascono come inverse delle potenze e richiedono che le funzioni potenza siano biiettive sui domini opportuni.

---

### 4.4 Potenze dispari

Sia $k$ dispari. Allora

$$
f(x)=x^k
$$

è una funzione dispari, perché

$$
f(-x)=(-x)^k=-x^k=-f(x).
$$

Come funzione

$$
f\colon\mathbb{R}\to\mathbb{R},
$$

la potenza dispari è:

- dispari;
- strettamente crescente;
- iniettiva;
- suriettiva;
- quindi biiettiva e invertibile.

La sua inversa è

$$
f^{-1}(x)=\sqrt[k]{x}.
$$

A differenza delle radici di indice pari, le radici di indice dispari sono definite su tutti i reali:

$$
\sqrt[k]{\phantom{x}}\colon\mathbb{R}\to\mathbb{R},
\qquad k\ \text{dispari}.
$$

Per esempio,

$$
\sqrt[3]{-27}=-3.
$$

Invece $\sqrt[4]{-27}$ non è un numero reale.

#### Confronto tra radici pari e dispari

- Indice pari:

  $$
  \sqrt[k]{\phantom{x}}\colon[0,+\infty)\to[0,+\infty).
  $$

- Indice dispari:

  $$
  \sqrt[k]{\phantom{x}}\colon\mathbb{R}\to\mathbb{R}.
  $$

Le due situazioni vanno tenute ben distinte.

---

## 5. Grafici delle potenze e delle radici

### 5.1 Confronto tra potenze pari

Nel primo quadrante, confrontando per esempio $x^2$, $x^4$ e $x^6$:

- per $0<x<1$, aumentando l’esponente il valore diminuisce:

  $$
  x^6<x^4<x^2;
  $$

- per $x>1$, aumentando l’esponente il valore aumenta:

  $$
  x^2<x^4<x^6.
  $$

Tutti i grafici passano per i punti

$$
(0,0)
\qquad\text{e}\qquad
(1,1).
$$

Le potenze pari sono simmetriche rispetto all’asse $y$.

---

### 5.2 Confronto tra potenze dispari

I grafici di $x^3$ e $x^5$ sono simmetrici rispetto all’origine e passano per

$$
(-1,-1),\qquad (0,0),\qquad (1,1).
$$

Per $x>1$ la potenza con esponente maggiore cresce più in fretta; per $0<x<1$ invece è più piccola.

---

### 5.3 Grafico di una funzione e della sua inversa

Se $f$ è invertibile, il grafico di $f^{-1}$ si ottiene riflettendo il grafico di $f$ rispetto alla bisettrice del primo e del terzo quadrante:

$$
y=x.
$$

La ragione formale è questa.

Se $(a,b)$ appartiene al grafico di $f$, allora

$$
b=f(a).
$$

Applicando l’inversa a entrambi i membri,

$$
a=f^{-1}(b).
$$

Quindi $(b,a)$ appartiene al grafico di $f^{-1}$.

Il punto $(b,a)$ è proprio il simmetrico di $(a,b)$ rispetto alla retta $y=x$.

Questo spiega il rapporto tra:

- il grafico di $x^2$ ristretto a $[0,+\infty)$;
- il grafico di $\sqrt{x}$;

e tra:

- il grafico di $x^3$;
- il grafico di $\sqrt[3]{x}$.

---

## 6. Interpretazione grafica di equazioni e proprietà funzionali

### 6.1 Risolvere l’equazione $f(x)=\lambda$

Sia $\lambda\in\mathbb{R}$. Risolvere

$$
f(x)=\lambda
$$

significa cercare i punti di intersezione tra:

- il grafico di $f$;
- la retta orizzontale

  $$
  y=\lambda.
  $$

Le soluzioni dell’equazione sono le ascisse dei punti di intersezione.

---

### 6.2 Interpretazione grafica della suriettività

La funzione $f\colon A\to B$ è suriettiva se

$$
\forall \lambda\in B,\ \exists x\in A
\quad\text{tale che}\quad
f(x)=\lambda.
$$

Graficamente, ogni retta orizzontale $y=\lambda$, con $\lambda\in B$, interseca il grafico almeno una volta.

Quindi:

> La suriettività significa che ogni livello dell’insieme di arrivo viene raggiunto almeno una volta.

Conta l’insieme di arrivo giusto: la stessa legge può essere suriettiva o no a seconda dell’insieme di arrivo scelto.

---

### 6.3 Interpretazione grafica dell’iniettività

La funzione $f$ è iniettiva se

$$
f(x_1)=f(x_2)\Longrightarrow x_1=x_2.
$$

Equivalentemente, ogni valore $\lambda$ dell’insieme di arrivo è assunto al massimo una volta.

Graficamente, ogni retta orizzontale interseca il grafico in al più un punto.

Quindi il numero di soluzioni di

$$
f(x)=\lambda
$$

è sempre $0$ oppure $1$.

Il criterio grafico si chiama **test della retta orizzontale**:

- se una retta orizzontale interseca il grafico in due punti distinti, la funzione non è iniettiva;
- se ogni retta orizzontale lo interseca al massimo una volta, la funzione è iniettiva.

---

### 6.4 Esempio: $x^2$

Consideriamo inizialmente

$$
f\colon\mathbb{R}\to\mathbb{R},
\qquad f(x)=x^2.
$$

La funzione:

- non è iniettiva, perché $f(x)=f(-x)$;
- non è suriettiva su $\mathbb{R}$, perché non assume valori negativi.

Se la consideriamo invece come

$$
f\colon[0,+\infty)\to[0,+\infty),
\qquad f(x)=x^2,
$$

stiamo guardando soltanto il ramo destro della parabola. In questo caso:

- ogni $\lambda\geq 0$ è assunto;
- ogni $\lambda\geq 0$ è assunto una sola volta;
- la funzione è iniettiva e suriettiva;
- la funzione è invertibile.

La scelta di dominio e codominio cambia quindi le proprietà della funzione, anche se la legge $f(x)=x^2$ resta la stessa.

---

## 7. Interpretazione grafica delle disequazioni

### 7.1 Disequazione $f(x)\leq\lambda$

Risolvere

$$
f(x)\leq \lambda
$$

significa:

1. tracciare il grafico di $f$;
2. tracciare la retta orizzontale $y=\lambda$;
3. individuare i punti del grafico che stanno sotto oppure sulla retta;
4. proiettare questi punti sull’asse $x$;
5. prendere le ascisse ottenute.

Allo stesso modo:

- $f(x)<\lambda$: punti del grafico strettamente sotto la retta;
- $f(x)\geq\lambda$: punti del grafico sopra oppure sulla retta;
- $f(x)>\lambda$: punti del grafico strettamente sopra la retta.

---

### 7.2 Esempio: disequazione quadratica

Per risolvere

$$
x^2\leq 4,
$$

si considera la parabola $y=x^2$ e la retta $y=4$.

I punti di intersezione corrispondono alle soluzioni dell’equazione

$$
x^2=4,
$$

cioè

$$
x=-2,\qquad x=2.
$$

La parabola è sotto la retta nell’intervallo compreso tra le due intersezioni. Quindi

$$
x^2\leq 4
\Longleftrightarrow
x\in[-2,2].
$$

Richiama il metodo generale delle disequazioni di secondo grado: per una parabola rivolta verso l’alto, la condizione “minore o uguale a” individua la regione interna compresa tra le radici.

---

## 8. Funzione valore assoluto

### 8.1 Definizione

La funzione [[Valore assoluto|valore assoluto]] è

$$
f\colon\mathbb{R}\to\mathbb{R},
\qquad
f(x)=|x|,
$$

dove

$$
|x|=
\begin{cases}
x, & x\geq 0,\\
-x, & x<0.
\end{cases}
$$

In $x=0$ le due definizioni sono compatibili, perché entrambe danno $0$.

Il grafico è una “V” con vertice nell’origine.

---

### 8.2 Proprietà del valore assoluto

Come funzione $\mathbb{R}\to\mathbb{R}$, $|x|$ è:

- pari, perché

  $$
  |-x|=|x|;
  $$

- non iniettiva, perché

  $$
  |x|=|-x|;
  $$

- non suriettiva su $\mathbb{R}$, perché assume solo valori maggiori o uguali a $0$;
- suriettiva se considerata come funzione

  $$
  |x|\colon\mathbb{R}\to[0,+\infty);
  $$
- strettamente decrescente su $(-\infty,0]$;
- strettamente crescente su $[0,+\infty)$.

La restrizione

$$
|x|\colon[0,+\infty)\to[0,+\infty)
$$

coincide con la funzione identità, quindi è invertibile.

---

### 8.3 Attenzione all’insieme di arrivo

Non è corretto definire semplicemente

$$
|x|\colon\mathbb{R}\to(-\infty,0)
$$

come funzione, perché $|x|$ non produce valori negativi. Per esempio,

$$
|x|\geq 0
$$

per ogni $x\in\mathbb{R}$.

Una funzione $f\colon A\to B$ deve associare a ogni elemento di $A$ un elemento di $B$. Se alcuni valori prodotti dalla legge non stanno in $B$, non è una funzione da $A$ a $B$.

---

## 9. Operazioni sui grafici

### 9.1 Traslazioni verticali

Dato il grafico di $f$, il grafico di

$$
f(x)+a
$$

si ottiene traslando verticalmente il grafico:

- verso l’alto di $a$ se $a>0$;
- verso il basso di $|a|$ se $a<0$.

Esempi:

$$
f(x)+7
$$

è il grafico di $f$ spostato verso l’alto di $7$;

$$
f(x)-3
$$

è il grafico spostato verso il basso di $3$.

---

### 9.2 Traslazioni orizzontali

Il grafico di

$$
f(x+a)
$$

si ottiene traslando orizzontalmente il grafico di $f$:

- verso sinistra di $a$ se $a>0$;
- verso destra di $|a|$ se $a<0$.

Il segno può sembrare controintuitivo. Se $f$ si annulla in $x=3$, allora $f(x+3)$ si annulla quando

$$
x+3=3,
$$

cioè in $x=0$. Il grafico si è quindi spostato verso sinistra.

Analogamente, $f(x-3)$ sposta il grafico verso destra di $3$.

---

### 9.3 Simmetria rispetto all’asse $y$

Il grafico di

$$
f(-x)
$$

si ottiene riflettendo il grafico di $f$ rispetto all’asse $y$.

Un punto che aveva ascissa $a$ passa all’ascissa $-a$.

---

### 9.4 Valore assoluto esterno

Il grafico di

$$
|f(x)|
$$

si ottiene dal grafico di $f$ lasciando inalterata la parte sopra l’asse $x$ e riflettendo rispetto all’asse $x$ la parte che sta sotto.

In altri termini, tutte le ordinate negative diventano le corrispondenti ordinate positive.

---

### 9.5 Valore assoluto interno

Il grafico di

$$
f(|x|)
$$

si costruisce così:

1. si considera la parte del grafico di $f$ corrispondente a $x\geq 0$;
2. la si lascia invariata;
3. la si riflette rispetto all’asse $y$.

Il risultato è sempre una funzione pari, perché

$$
f(|-x|)=f(|x|).
$$

---

## 10. Esercizi grafici

### 10.1 Numero di soluzioni di $(x-3)^2=\lambda$

Si vuole determinare, al variare di $\lambda\in\mathbb{R}$, il numero di soluzioni dell’equazione

$$
(x-3)^2=\lambda.
$$

Il grafico di $y=(x-3)^2$ è una parabola ottenuta traslando verso destra di $3$ il grafico di $y=x^2$. Il vertice è

$$
(3,0).
$$

Si interseca la parabola con la retta orizzontale $y=\lambda$.

- Se $\lambda<0$, la retta è sotto il vertice: nessuna soluzione.
- Se $\lambda=0$, la retta è tangente al vertice: una soluzione,

  $$
  x=3.
  $$

- Se $\lambda>0$, la retta interseca la parabola in due punti: due soluzioni,

  $$
  x-3=\pm\sqrt{\lambda},
  $$

  quindi

  $$
  x=3\pm\sqrt{\lambda}.
  $$

Pertanto:

$$
\begin{cases}
0 & \text{se }\lambda<0,\\
1 & \text{se }\lambda=0,\\
2 & \text{se }\lambda>0.
\end{cases}
$$

---

### 10.2 Numero di soluzioni di $|x^2-2026|=\lambda$

Nel transcript l’esercizio è riportato con la costante $2026$:

$$
|x^2-2026|=\lambda.
$$

Il grafico di $x^2-2026$ si ottiene traslando verso il basso di $2026$ il grafico di $x^2$. Applicando il valore assoluto, la parte negativa viene riflessa sopra l’asse $x$.

Gli zeri di $x^2-2026$ sono

$$
x=\pm\sqrt{2026}.
$$

Si studiano le intersezioni con la retta $y=\lambda$.

#### Caso $\lambda<0$

Il valore assoluto è sempre non negativo, quindi non ci sono soluzioni:

$$
0\quad\text{soluzioni}.
$$

#### Caso $\lambda=0$

Si risolve

$$
|x^2-2026|=0
\Longleftrightarrow
x^2=2026.
$$

Le soluzioni sono

$$
x=\pm\sqrt{2026},
$$

quindi ci sono $2$ soluzioni.

#### Caso $0<\lambda<2026$

La retta orizzontale interseca il grafico in quattro punti: due sul ramo interno e due sui rami esterni.

Quindi ci sono $4$ soluzioni.

#### Caso $\lambda=2026$

Si ottengono tre punti di intersezione: uno in $x=0$ e due simmetrici esterni. Quindi ci sono $3$ soluzioni.

#### Caso $\lambda>2026$

Il livello è maggiore dell’altezza del vertice riflesso e restano soltanto due intersezioni sui rami esterni.

Quindi ci sono $2$ soluzioni.

Il numero di soluzioni è dunque

$$
\begin{cases}
0 & \lambda<0,\\
2 & \lambda=0,\\
4 & 0<\lambda<2026,\\
3 & \lambda=2026,\\
2 & \lambda>2026.
\end{cases}
$$

---

### 10.3 Disequazione $\sqrt{x+6}>x$

Si considera la disequazione

$$
\sqrt{x+6}>x.
$$

#### Dominio

La radice è definita quando

$$
x+6\geq 0,
$$

cioè

$$
x\geq -6.
$$

#### Interpretazione grafica

Il grafico di $\sqrt{x+6}$ si ottiene traslando verso sinistra di $6$ il grafico di $\sqrt{x}$. Va confrontato con la retta $y=x$.

Le intersezioni si trovano risolvendo

$$
\sqrt{x+6}=x.
$$

Poiché il membro sinistro è non negativo, ogni soluzione dell’equazione deve soddisfare $x\geq 0$.

Elevando al quadrato:

$$
x+6=x^2,
$$

quindi

$$
x^2-x-6=0,
$$

e dunque

$$
(x-3)(x+2)=0.
$$

Le soluzioni candidate sono

$$
x=3,\qquad x=-2.
$$

Vanno però verificate nell’equazione originale:

- per $x=3$:

  $$
  \sqrt{3+6}=\sqrt{9}=3;
  $$

  la soluzione è valida;

- per $x=-2$:

  $$
  \sqrt{-2+6}=\sqrt{4}=2\neq -2;
  $$

  la soluzione non è valida.

L’unica intersezione è quindi $x=3$.

Dal grafico, $\sqrt{x+6}$ sta sopra la retta $y=x$ per

$$
-6\leq x<3.
$$

La soluzione è

$$
\boxed{[-6,3)}.
$$

---

### 10.4 Perché il quadramento può introdurre soluzioni estranee

Nel passaggio

$$
a=b\Longrightarrow a^2=b^2
$$

l’implicazione è corretta. Il viceversa, però, non è sempre vero:

$$
a^2=b^2
\not\Longrightarrow
a=b.
$$

Infatti può succedere che

$$
a=-b.
$$

Nel caso dell’equazione

$$
\sqrt{x+6}=x,
$$

dopo aver elevato al quadrato si ottiene un’equazione con due soluzioni candidate, $x=3$ e $x=-2$. La seconda risolve l’equazione al quadrato, ma non quella originale.

Geometricamente, la soluzione estranea $x=-2$ corrisponde all’intersezione con il ramo “fantasma” della parabola $y^2=x+6$ che non appartiene al grafico della radice principale. La funzione radice considera solo il ramo con ordinata $y\geq 0$.

> [!warning]
> Quando si eleva al quadrato un’equazione, bisogna sempre verificare le soluzioni ottenute nell’equazione originale.

---

## 11. Identità importanti con le radici

Un errore frequente è confondere

$$
\sqrt{x^2}
$$

con $x$.

La relazione corretta è

$$
\sqrt{x^2}=|x|
\qquad\text{per ogni }x\in\mathbb{R}.
$$

Infatti la radice quadrata restituisce per definizione il valore non negativo. Se $x<0$, allora $\sqrt{x^2}=-x$, non $x$.

Se invece si sa già che $x\geq 0$, allora

$$
\sqrt{x^2}=x.
$$

Analogamente, per $x\geq 0$,

$$
\sqrt[2k]{x^{2k}}=x,
$$

mentre per $x\in\mathbb{R}$ la formula generale è

$$
\sqrt[2k]{x^{2k}}=|x|^k.
$$

---

## 12. Uso dell’iniettività nelle equazioni

Una funzione iniettiva soddisfa

$$
f(a)=f(b)\Longrightarrow a=b.
$$

Questa proprietà permette di “eliminare” la stessa funzione applicata ai due membri di un’equazione, purché gli argomenti stiano nel dominio della funzione.

Per esempio, se $f$ è iniettiva,

$$
f(u)=f(v)
\Longrightarrow
u=v.
$$

È il principio che permette di applicare il logaritmo, o di confrontare esponenti, in molti esercizi.

Occorre però distinguere il caso crescente da quello decrescente.

### 12.1 Funzione strettamente crescente

Se $f$ è strettamente crescente, allora

$$
f(u)<f(v)
\Longleftrightarrow
u<v.
$$

La funzione conserva il verso delle disuguaglianze.

### 12.2 Funzione strettamente decrescente

Se $f$ è strettamente decrescente, allora

$$
f(u)<f(v)
\Longleftrightarrow
u>v.
$$

La funzione inverte il verso delle disuguaglianze.

### 12.3 Perché la crescenza debole non basta

Se $f$ è soltanto debolmente crescente, non è necessariamente iniettiva: può assumere lo stesso valore in corrispondenza di argomenti diversi.

Perciò non si può dedurre in generale

$$
f(u)=f(v)\Longrightarrow u=v
$$

senza l’ipotesi di iniettività, garantita per esempio dalla stretta monotonia.

---

## 13. Condizioni di dominio nelle manipolazioni algebriche

Ogni trasformazione deve rispettare il dominio delle funzioni coinvolte.

Per esempio, il logaritmo $\log(t)$ è definito soltanto se

$$
t>0.
$$

Quindi, quando si applica il logaritmo a un’equazione, bisogna prima imporre che tutti gli argomenti dei logaritmi siano positivi.

Analogamente:

- una radice di indice pari richiede argomento $\geq 0$;
- un denominatore deve essere diverso da $0$;
- applicare una funzione ai due membri è lecito solo se gli argomenti appartengono al suo dominio;
- per usare l’iniettività di una funzione, gli argomenti devono appartenere all’insieme su cui la funzione è davvero iniettiva.

Per esempio, $x\mapsto x^2$ non è iniettiva su $\mathbb{R}$, ma lo è su $[0,+\infty)$. Quindi da

$$
x^2=y^2
$$

non si può concludere $x=y$ se $x$ e $y$ sono reali arbitrari; la conclusione è lecita se si sa che $x,y\geq 0$.

---

## 14. Anticipazione sull’esponenziale

La prossima lezione introdurrà le funzioni esponenziali.

L’idea è trovare una funzione che estenda in modo coerente le potenze già note e che soddisfi proprietà algebriche come

$$
a^{x+y}=a^x a^y,
$$

oltre alle proprietà di ordine e monotonia adatte.

Definire rigorosamente l’esponenziale richiede una costruzione più delicata: non basta assegnare valori arbitrari sui reali. Esistono infatti molte possibili estensioni di una funzione definita inizialmente sui razionali, e servono condizioni aggiuntive per escludere comportamenti patologici.

L’idea geometrica citata è richiedere che esista almeno un rettangolo del piano, contenuto nella regione $y>0$, che non intersechi il grafico. Questa condizione serve a escludere funzioni estremamente irregolari il cui grafico attraversi ogni rettangolo del piano.

La costruzione rigorosa dell’esponenziale sarà affrontata in seguito.
