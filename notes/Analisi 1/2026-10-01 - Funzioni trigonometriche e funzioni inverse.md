---
type: lecture-note
course: Analisi 1
date: '2026-10-01'
title: Funzioni trigonometriche e funzioni inverse
source_transcript: _transcripts/Analisi 1/2026-10-01 - Funzioni trigonometriche e funzioni inverse.md
source_hash: sha256:f219828e05ace401a5b9b6213189b4ad834c199c0acc9df76dbdc4d2651b6d00
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-01T09:17:05.676Z'
vault_path: Notes/Analisi 1/Lectures/2026-10-01 - Funzioni trigonometriche e funzioni inverse.md
vault_hash: 2dd7bb9df562e0c29ce25152415353d83aa2ee23f157da574a35f45b7e25cd1a
---

# Funzioni trigonometriche e funzioni inverse

## 1. La circonferenza trigonometrica

Le [[Funzioni trigonometriche|funzioni trigonometriche]] vengono presentate con una definizione geometrica, operativa e solo semirigorosa. Una definizione completamente rigorosa richiederebbe di formalizzare bene concetti come arco, lunghezza di un arco e area di un settore circolare.

La **circonferenza trigonometrica** è la circonferenza di centro l’origine e raggio $1$:

$$
x^2+y^2=1.
$$

Si indica con $A=(1,0)$ il punto di partenza.

Dato un angolo $\alpha$, si parte da $A$ e si percorre sulla circonferenza un arco di lunghezza $\alpha$, ottenendo un punto $P$.

Poiché il raggio è $1$, la misura dell’angolo in radianti coincide numericamente con la lunghezza dell’arco percorso. Equivalentemente, si può descrivere il punto con l’area del settore circolare $OAP$: se l’arco ha lunghezza $\alpha$, l’area del settore è

$$
\frac{\alpha}{2}.
$$

Infatti, per un settore di raggio $r$ e angolo $\alpha$ in radianti, l’area è

$$
\frac{1}{2}r^2\alpha;
$$

nella circonferenza trigonometrica $r=1$, quindi,

$$
\operatorname{Area}(OAP)=\frac{\alpha}{2}.
$$

Lunghezza dell’arco e area del settore sono dunque due modi equivalenti di descrivere lo stesso punto.

### Verso di percorrenza e angoli arbitrari

- Se $\alpha>0$, si percorre la circonferenza in senso antiorario.
- Se $\alpha<0$, si percorre in senso orario.
- Se $\alpha\geq 2\pi$, si compiono uno o più giri completi.
- In generale ogni $\alpha\in\mathbb{R}$ è ammesso: si possono fare quanti giri si vuole, anche in verso negativo.

Dopo un giro completo, cioè dopo un angolo $2\pi$, si ritorna al punto di partenza. Perciò angoli che differiscono per un multiplo intero di $2\pi$ individuano lo stesso punto della circonferenza.

---

## 2. Seno e coseno

Sia $P$ il punto della circonferenza trigonometrica individuato dall’angolo $\alpha$. Le sue coordinate sono

$$
P=(\cos\alpha,\sin\alpha).
$$

Quindi:

- $\cos\alpha$ è la coordinata $x$ di $P$;
- $\sin\alpha$ è la coordinata $y$ di $P$.

Dalla relazione $x^2+y^2=1$ si ottiene l’identità fondamentale:

$$
\sin^2\alpha+\cos^2\alpha=1.
$$

I segni di seno e coseno dipendono dal quadrante in cui si trova $P$:

- nel primo quadrante: $\sin\alpha>0$, $\cos\alpha>0$;
- nel secondo quadrante: $\sin\alpha>0$, $\cos\alpha<0$;
- nel terzo quadrante: $\sin\alpha<0$, $\cos\alpha<0$;
- nel quarto quadrante: $\sin\alpha<0$, $\cos\alpha>0$.

---

## 3. Tangente

La tangente è definita, quando $\cos\alpha\neq 0$, da

$$
\tan\alpha=\frac{\sin\alpha}{\cos\alpha}.
$$

### Interpretazione geometrica

Si considera la retta tangente alla circonferenza trigonometrica nel punto $A=(1,0)$, cioè la retta verticale $x=1$. Si prolunga la semiretta $OP$ fino a incontrare questa retta in un punto $Q$.

La lunghezza orientata del segmento $AQ$ dà la tangente di $\alpha$:

$$
\tan\alpha=\text{lunghezza orientata di }AQ.
$$

La lunghezza è orientata: nel secondo quadrante, per esempio, l’intersezione con la retta tangente sta sotto $A$ e la tangente risulta negativa.

La costruzione non è possibile quando $P$ sta sull’asse $y$, cioè quando

$$
\cos\alpha=0.
$$

Ciò avviene per

$$
\alpha=\frac{\pi}{2}+k\pi,\qquad k\in\mathbb{Z}.
$$

In questi casi la semiretta $OP$ è parallela alla retta tangente $x=1$, quindi non esiste un punto di intersezione finito.

---

## 4. Simmetrie e periodicità

### Seno

Geometricamente, sostituire $\alpha$ con $-\alpha$ significa riflettere il punto $P$ rispetto all’asse $x$. La coordinata $x$ resta invariata, mentre la coordinata $y$ cambia segno. Pertanto:

$$
\sin(-\alpha)=-\sin\alpha.
$$

Il seno è quindi una funzione **dispari**.

Inoltre, dopo un giro completo il punto torna nella posizione iniziale:

$$
\sin(\alpha+2\pi)=\sin\alpha.
$$

Il seno è periodico di periodo minimo $2\pi$.

### Coseno

La sostituzione $\alpha\mapsto-\alpha$ riflette il punto rispetto all’asse $x$ e lascia invariata la coordinata $x$. Dunque:

$$
\cos(-\alpha)=\cos\alpha.
$$

Il coseno è una funzione **pari**.

Anche il coseno è periodico di periodo minimo $2\pi$:

$$
\cos(\alpha+2\pi)=\cos\alpha.
$$

### Tangente

Poiché il seno è dispari e il coseno è pari,

$$
\tan(-\alpha)
=
\frac{\sin(-\alpha)}{\cos(-\alpha)}
=
\frac{-\sin\alpha}{\cos\alpha}
=
-\tan\alpha.
$$

La tangente è quindi dispari.

Aggiungere $\pi$ all’angolo significa fare mezzo giro: il punto va nella posizione opposta e cambiano contemporaneamente di segno seno e coseno. Pertanto:

$$
\begin{aligned}
\tan(\alpha+\pi)
&=
\frac{\sin(\alpha+\pi)}{\cos(\alpha+\pi)}\\
&=
\frac{-\sin\alpha}{-\cos\alpha}\\
&=
\tan\alpha.
\end{aligned}
$$

La tangente è periodica di periodo $\pi$.

Per vedere che $\pi$ è il periodo minimo basta osservare che gli zeri della tangente sono esattamente

$$
\alpha=k\pi,\qquad k\in\mathbb{Z}.
$$

Non esiste quindi un periodo positivo più piccolo di $\pi$.

---

## 5. Grafici delle funzioni trigonometriche

### Grafico del seno

Il seno oscilla tra $-1$ e $1$ ed è periodico di periodo $2\pi$. In un periodo:

- $\sin 0=0$;
- $\sin\frac{\pi}{2}=1$;
- $\sin\pi=0$;
- $\sin\frac{3\pi}{2}=-1$;
- $\sin 2\pi=0$.

Il grafico si ripete identico in ogni intervallo di lunghezza $2\pi$.

### Grafico del coseno

Il coseno parte dal valore $1$:

$$
\cos 0=1.
$$

Inoltre:

- $\cos\frac{\pi}{2}=0$;
- $\cos\pi=-1$;
- $\cos\frac{3\pi}{2}=0$;
- $\cos 2\pi=1$.

Anche il grafico del coseno si ripete con periodo $2\pi$.

### Grafico della tangente

La tangente è definita solo quando $\cos x\neq0$, quindi presenta discontinuità e asintoti verticali nei punti

$$
x=\frac{\pi}{2}+k\pi,\qquad k\in\mathbb{Z}.
$$

In particolare gli asintoti sono in

$$
x=-\frac{\pi}{2},\quad x=\frac{\pi}{2},\quad x=\frac{3\pi}{2},\ldots
$$

La funzione è strettamente crescente in ciascun intervallo del tipo

$$
\left(-\frac{\pi}{2}+k\pi,\frac{\pi}{2}+k\pi\right)
$$

e si ripete con periodo $\pi$.

---

## 6. Funzioni inverse trigonometriche

Una funzione periodica non è iniettiva su tutto il suo dominio. Per invertirla si restringe il dominio a un intervallo in cui diventa iniettiva, conservando allo stesso tempo l’immagine desiderata. Le [[Funzioni trigonometriche inverse|funzioni trigonometriche inverse]] nascono così.

### 6.1. Arcoseno

Si considera la restrizione del seno

$$
f\colon\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\longrightarrow[-1,1],
\qquad
f(x)=\sin x.
$$

In questo intervallo il seno è strettamente crescente, quindi è iniettivo, ed è suriettivo su $[-1,1]$. Pertanto è biiettivo e ammette inversa.

La funzione inversa si chiama **arcoseno** e si indica con

$$
\arcsin x
\qquad\text{o}\qquad
\arcsin(x).
$$

Il suo dominio e il suo codominio sono

$$
\arcsin\colon[-1,1]\longrightarrow
\left[-\frac{\pi}{2},\frac{\pi}{2}\right].
$$

Per definizione, $\arcsin x$ è l’unico angolo appartenente a $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ il cui seno è $x$.

In particolare:

$$
\arcsin(x)\in
\left[-\frac{\pi}{2},\frac{\pi}{2}\right].
$$

Esempio: $\arcsin(0{,}5)$ è l’angolo compreso tra $-\frac{\pi}{2}$ e $\frac{\pi}{2}$ il cui seno vale $0{,}5$.

### 6.2. Arcocoseno

Si considera la restrizione del coseno

$$
f\colon[0,\pi]\longrightarrow[-1,1],
\qquad
f(x)=\cos x.
$$

Nell’intervallo $[0,\pi]$ il coseno è strettamente decrescente, quindi è iniettivo e suriettivo su $[-1,1]$.

La sua inversa è l’**arcocoseno**:

$$
\arccos\colon[-1,1]\longrightarrow[0,\pi].
$$

Per definizione, $\arccos x$ è l’unico angolo appartenente a $[0,\pi]$ il cui coseno è $x$.

Da ricordare bene:

$$
\arccos(x)\in[0,\pi].
$$

In particolare, l’arcocoseno non restituisce mai valori negativi.

### 6.3. Arcotangente

Si considera la restrizione della tangente

$$
f\colon\left(-\frac{\pi}{2},\frac{\pi}{2}\right)\longrightarrow\mathbb{R},
\qquad
f(x)=\tan x.
$$

In questo intervallo la tangente è strettamente crescente, quindi è iniettiva e suriettiva su $\mathbb{R}$.

La sua inversa è l’**arcotangente**:

$$
\arctan\colon\mathbb{R}\longrightarrow
\left(-\frac{\pi}{2},\frac{\pi}{2}\right).
$$

Per definizione, $\arctan x$ è l’unico angolo compreso tra $-\frac{\pi}{2}$ e $\frac{\pi}{2}$ la cui tangente è $x$.

Gli estremi non sono inclusi perché la tangente non assume mai valori finiti in $\pm\frac{\pi}{2}$.

> [!example] Esempio
> Poiché $\tan\frac{\pi}{4}=1$ e $\frac{\pi}{4}\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$, si ha $\arctan 1=\frac{\pi}{4}$. Invece $\arctan(-1)=-\frac{\pi}{4}$, perché l’arcotangente è dispari come la tangente.

---

## 7. Grafici delle funzioni inverse

Il grafico della funzione inversa si ottiene riflettendo il grafico della funzione rispetto alla retta

$$
y=x.
$$

Questa riflessione scambia i ruoli degli assi: dominio e codominio vengono scambiati.

- Il ramo del seno su $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ si riflette nel grafico dell’arcoseno.
- Il ramo del coseno su $[0,\pi]$ si riflette nel grafico dell’arcocoseno.
- Il ramo della tangente su $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$ si riflette nel grafico dell’arcotangente.

Gli asintoti verticali della tangente diventano asintoti orizzontali dell’arcotangente:

$$
y=\pm\frac{\pi}{2}.
$$

---

## 8. Interpretazione geometrica delle funzioni inverse

### 8.1. Interpretazione di $\arcsin\lambda$

Per calcolare $\arcsin\lambda$, con $\lambda\in[-1,1]$, si considera la retta orizzontale

$$
y=\lambda.
$$

Essa interseca la circonferenza trigonometrica in due punti, tranne nei casi estremi. Si sceglie l’intersezione che appartiene al ramo corrispondente agli angoli

$$
\left[-\frac{\pi}{2},\frac{\pi}{2}\right].
$$

L’angolo associato a quel punto è $\arcsin\lambda$.

L’altra intersezione non si sceglie perché corrisponde a un angolo fuori dall’intervallo di definizione dell’arcoseno.

### 8.2. Interpretazione di $\arccos\lambda$

Per calcolare $\arccos\lambda$, con $\lambda\in[-1,1]$, si considera la retta verticale

$$
x=\lambda.
$$

Essa interseca la circonferenza in due punti. Si sceglie quello appartenente al ramo con angoli in

$$
[0,\pi].
$$

L’angolo corrispondente è $\arccos\lambda$.

### 8.3. Interpretazione di $\arctan\lambda$

Per calcolare $\arctan\lambda$, con $\lambda\in\mathbb{R}$, si considera la retta orizzontale

$$
y=\lambda.
$$

Si individua il punto della circonferenza corrispondente al ramo della tangente con angoli in

$$
\left(-\frac{\pi}{2},\frac{\pi}{2}\right).
$$

L’angolo individuato è $\arctan\lambda$.

---

## 9. Attenzione alle composizioni con le inverse

Se $f\colon A\to B$ è biiettiva e $g=f^{-1}\colon B\to A$, allora

$$
g(f(a))=a\qquad\forall a\in A
$$

e

$$
f(g(b))=b\qquad\forall b\in B.
$$

Le due identità valgono quindi su insiemi diversi: una sul dominio di $f$, l’altra sul dominio di $g$.

### 9.1. Seno e arcoseno

Poiché il seno è stato ristretto a

$$
\left[-\frac{\pi}{2},\frac{\pi}{2}\right],
$$

si ha

$$
\arcsin(\sin x)=x
\qquad
\forall x\in
\left[-\frac{\pi}{2},\frac{\pi}{2}\right].
$$

Invece,

$$
\sin(\arcsin x)=x
\qquad
\forall x\in[-1,1].
$$

Occhio: non si può scrivere $\arcsin(\sin x)=x$ per ogni $x\in\mathbb{R}$, perché l’arcoseno restituisce sempre un valore nel suo intervallo principale.

### 9.2. Coseno e arcocoseno

Poiché il coseno è stato ristretto a $[0,\pi]$,

$$
\arccos(\cos x)=x
\qquad
\forall x\in[0,\pi].
$$

Invece,

$$
\cos(\arccos x)=x
\qquad
\forall x\in[-1,1].
$$

Anche qui, fuori da $[0,\pi]$ la semplificazione $\arccos(\cos x)=x$ non vale in generale.

### 9.3. Tangente e arcotangente

Poiché la tangente è stata ristretta a $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$,

$$
\arctan(\tan x)=x
\qquad
\forall x\in
\left(-\frac{\pi}{2},\frac{\pi}{2}\right).
$$

Invece,

$$
\tan(\arctan x)=x
\qquad
\forall x\in\mathbb{R}.
$$

Il dominio giusto è fondamentale: le formule di semplificazione con le inverse valgono solo nei rispettivi intervalli principali.

---

## 10. Esempi di composizioni

### 10.1. $\arcsin(\sin 2)$

L’angolo $2$ non appartiene a $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$, quindi non si può semplificare direttamente.

Geometricamente, l’angolo $2$ si trova nel secondo quadrante. L’arcoseno deve restituire l’angolo corrispondente nell’intervallo principale. Si ottiene:

$$
\arcsin(\sin 2)=\pi-2.
$$

Infatti $\pi-2\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ e

$$
\sin(\pi-2)=\sin 2.
$$

### 10.2. $\arccos(\cos 4)$

L’angolo $4$ non appartiene a $[0,\pi]$. Dopo un giro completo, lo stesso punto si può rappresentare con l’angolo

$$
2\pi-4.
$$

Poiché $2\pi-4\in[0,\pi]$, si ha

$$
\arccos(\cos 4)=2\pi-4.
$$

Il risultato non è $4$, perché l’arcocoseno restituisce soltanto valori in $[0,\pi]$.

### 10.3. Dominio di $\arccos(\cos x)$ e di $\cos(\arccos x)$

Le due composizioni si comportano in modo diverso:

- $\arccos(\cos x)$ è definita per ogni $x\in\mathbb{R}$, perché $\cos x\in[-1,1]$ e quindi si può applicare l’arcocoseno;
- $\cos(\arccos x)$ è definita soltanto per $x\in[-1,1]$, perché l’arcocoseno accetta solo argomenti in $[-1,1]$.

Quindi una composizione può essere definita anche quando non si semplifica nell’identità.

---

## 11. Funzioni periodiche ottenute per composizione

Se la funzione interna di una [[Composizione di funzioni|composizione]] è periodica, anche la composizione è periodica.

Se $g$ è periodica di periodo $T$, allora per ogni funzione $f$ per cui la composizione ha senso:

$$
g(x+T)=g(x)
$$

e quindi

$$
f(g(x+T))=f(g(x)).
$$

Pertanto $f\circ g$ è periodica di periodo $T$, anche se il periodo minimo potrebbe essere più piccolo.

Per esempio:

$$
\sin^3 x=(\sin x)^3
$$

è periodica di periodo $2\pi$, perché la funzione interna $\sin x$ è periodica.

Espressioni come

$$
\sin(x^2)
\qquad\text{o}\qquad
\sin(x^3)
$$

invece non hanno la stessa struttura: qui $x^2$ o $x^3$ stanno dentro la funzione seno e comprimono sempre di più le oscillazioni. Gli zeri di $\sin(x^2)$, per esempio, non sono equidistanziati come richiederebbe una periodicità.

In genere è facile dimostrare che una funzione è periodica: basta esibire un periodo e verificare direttamente l’uguaglianza. Dimostrare che non è periodica è più delicato.

---

## 12. Identità utili con seno e coseno inversi

### 12.1. Somma di arcoseno e arcocoseno

Per ogni $x\in[-1,1]$ vale

$$
\arcsin x+\arccos x=\frac{\pi}{2}.
$$

Infatti, se $\alpha=\arcsin x$, allora $\alpha\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ e l’angolo complementare $\frac{\pi}{2}-\alpha$ appartiene a $[0,\pi]$ e ha coseno uguale a $x$.

### 12.2. Calcolo di $\sin(\arccos x)$

Sia

$$
\alpha=\arccos x.
$$

Allora $\alpha\in[0,\pi]$ e

$$
\cos\alpha=x.
$$

Dall’identità fondamentale:

$$
\sin^2\alpha+\cos^2\alpha=1
$$

segue

$$
\sin^2\alpha=1-x^2.
$$

Poiché $\alpha\in[0,\pi]$, il seno è non negativo. Si deve quindi scegliere la radice positiva:

$$
\sin\alpha=\sqrt{1-x^2}.
$$

Quindi

$$
\boxed{\sin(\arccos x)=\sqrt{1-x^2}}
\qquad
\forall x\in[-1,1].
$$

La condizione sull’intervallo è indispensabile: se non si sapesse che $\alpha$ appartiene a $[0,\pi]$, non si potrebbe stabilire in automatico il segno del seno.

Analogamente:

$$
\boxed{\cos(\arcsin x)=\sqrt{1-x^2}}
\qquad
\forall x\in[-1,1],
$$

perché $\arcsin x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ e in questo intervallo il coseno è non negativo.

---

## 13. Identità con l’arcotangente

Per $x>0$ vale

$$
\arctan x+\arctan\frac{1}{x}=\frac{\pi}{2}.
$$

#### Dimostrazione

Poniamo

$$
\alpha=\arctan x.
$$

Allora

$$
\alpha\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)
\qquad\text{e}\qquad
x=\tan\alpha.
$$

Se $x>0$, allora $\alpha\in\left(0,\frac{\pi}{2}\right)$. Usando la relazione tra angoli complementari:

$$
\tan\left(\frac{\pi}{2}-\alpha\right)
=
\frac{\cos\alpha}{\sin\alpha}
=
\frac{1}{\tan\alpha}
=
\frac{1}{x}.
$$

Inoltre,

$$
\frac{\pi}{2}-\alpha\in
\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
$$

cioè nell’intervallo principale dell’arcotangente. Pertanto:

$$
\arctan\frac{1}{x}
=
\frac{\pi}{2}-\alpha.
$$

Sommando $\alpha=\arctan x$:

$$
\arctan x+\arctan\frac{1}{x}
=
\frac{\pi}{2}.
$$

Per $x<0$, invece, $\alpha<0$ e l’angolo $\frac{\pi}{2}-\alpha$ non appartiene all’intervallo principale dell’arcotangente. Bisogna scegliere l’angolo equivalente ottenuto sottraendo $\pi$. Si ottiene:

$$
\boxed{
\arctan x+\arctan\frac{1}{x}
=
-\frac{\pi}{2}
}
\qquad\text{per }x<0.
$$

In forma complessiva:

$$
\arctan x+\arctan\frac{1}{x}
=
\begin{cases}
\frac{\pi}{2}, & x>0,\\[4pt]
-\frac{\pi}{2}, & x<0.
\end{cases}
$$

Il punto delicato della dimostrazione è verificare che l’angolo trovato appartenga all’intervallo principale dell’arcotangente. Non basta verificare che la sua tangente sia $1/x$.

---

## 14. Composizione $\arccos(\sin x)$

La funzione

$$
\arccos(\sin x)
$$

è definita per ogni $x\in\mathbb{R}$, perché $\sin x\in[-1,1]$. È inoltre periodica di periodo $2\pi$, poiché la funzione interna $\sin x$ è periodica di periodo $2\pi$.

Usando

$$
\sin x=\cos\left(\frac{\pi}{2}-x\right)
$$

e ricordando che l’arcocoseno deve restituire un valore in $[0,\pi]$, nel primo periodo si ottengono le espressioni lineari:

$$
\arccos(\sin x)=
\begin{cases}
\frac{\pi}{2}-x,
& -\frac{\pi}{2}\leq x\leq\frac{\pi}{2},\\[6pt]
x-\frac{\pi}{2},
& \frac{\pi}{2}\leq x\leq\frac{3\pi}{2}.
\end{cases}
$$

La funzione si ripete poi con periodo $2\pi$. Il grafico ha una forma a “dente di sega” o a “capannina triangolare”.

In particolare:

$$
\arccos(\sin 2)=2-\frac{\pi}{2}.
$$

---

## 15. Immagine e controimmagine

Sia

$$
f\colon A\to B
$$

una funzione.

### 15.1. Immagine di un insieme

Dato un sottoinsieme $E\subseteq A$, l’[[Immagine e controimmagine|immagine]] di $E$ mediante $f$ è

$$
f(E)=\{f(a):a\in E\}.
$$

L’immagine contiene tutti i valori assunti dalla funzione quando l’argomento varia in $E$.

Graficamente:

1. si parte dall’intervallo o insieme sull’asse $x$;
2. si considera la parte del grafico corrispondente;
3. si proiettano i punti del grafico sull’asse $y$.

Non basta sostituire gli estremi dell’intervallo: bisogna determinare tutti i valori assunti dalla funzione nel tratto considerato, tenendo conto di massimi e minimi interni.

### 15.2. Controimmagine di un insieme

Dato un sottoinsieme $E\subseteq B$, la controimmagine di $E$ è

$$
f^{-1}(E)=\{a\in A:f(a)\in E\}.
$$

La controimmagine non è necessariamente una funzione inversa e non è necessariamente un singolo numero: è un sottoinsieme del dominio.

Graficamente:

1. si parte dall’intervallo o insieme sull’asse $y$;
2. si considera la parte del grafico contenuta tra le rette orizzontali corrispondenti;
3. si proiettano i punti sull’asse $x$.

La controimmagine è sempre definita, purché l’insieme considerato sia un sottoinsieme del codominio. Non serve che $f$ sia iniettiva o suriettiva.

Va distinta dalla [[Funzione inversa|funzione inversa]]:

- $f^{-1}(E)$ può essere definita per qualsiasi funzione;
- la funzione inversa $f^{-1}$ esiste come funzione solo quando $f$ è biiettiva;
- la scrittura $1/f$ indica invece il reciproco della funzione, non la sua inversa.

Il significato della notazione va dedotto dal contesto.

---

## 16. Esempio di immagine e controimmagine

Consideriamo

$$
f(x)=|x^2-4|.
$$

Il grafico si costruisce in più passaggi:

1. si parte dal grafico di $y=x^2$;
2. si trasla il grafico verso il basso di $4$, ottenendo $y=x^2-4$;
3. si applica il valore assoluto, riflettendo rispetto all’asse $x$ la parte del grafico che sta sotto l’asse.

Gli zeri sono dati da

$$
|x^2-4|=0
\iff x^2=4
\iff x=\pm2.
$$

Il valore in $x=0$ è

$$
f(0)=4.
$$

### 16.1. Calcolo dell’immagine $f([1,4])$

Si considera l’intervallo di partenza $[1,4]$.

Nel tratto considerato:

- $f(1)=3$;
- $f(2)=0$;
- $f(4)=12$.

La funzione prima decresce da $3$ a $0$, poi cresce da $0$ a $12$. Quindi assume tutti i valori compresi tra $0$ e $12$:

$$
\boxed{f([1,4])=[0,12]}.
$$

Non è corretto calcolare l’immagine di un intervallo sostituendo soltanto gli estremi: qui $f(1)=3$ e $f(4)=12$, ma l’immagine non è $[3,12]$, perché la funzione assume anche valori tra $0$ e $3$.

### 16.2. Calcolo della controimmagine $f^{-1}([-2,1])$

Cerchiamo tutti gli $x$ tali che

$$
f(x)\in[-2,1].
$$

Poiché $f(x)=|x^2-4|\geq0$, la parte $[-2,0)$ non dà alcun contributo. Basta risolvere:

$$
|x^2-4|\leq1.
$$

Equivalentemente:

$$
-1\leq x^2-4\leq1.
$$

Da cui:

$$
3\leq x^2\leq5.
$$

Pertanto:

$$
\sqrt{3}\leq |x|\leq\sqrt{5},
$$

e quindi

$$
\boxed{
f^{-1}([-2,1])
=
[-\sqrt5,-\sqrt3]\cup[\sqrt3,\sqrt5].
}
$$

La controimmagine è dunque unione di due intervalli, perché la funzione non è iniettiva.

---

## 17. Strategie grafiche per gli esercizi

### Iniettività

Per verificare graficamente se una funzione è iniettiva si usa il criterio delle rette orizzontali:

- se ogni retta orizzontale interseca il grafico al massimo una volta, la funzione è iniettiva;
- se esiste una retta orizzontale che interseca il grafico in più punti, la funzione non è iniettiva.

### Suriettività

La suriettività dipende dal codominio dichiarato. Graficamente, bisogna verificare che ogni valore del codominio sia assunto dalla funzione, cioè che ogni retta orizzontale corrispondente a un valore del codominio intersechi il grafico.

### Numero di soluzioni di un’equazione

Per determinare il numero di soluzioni di

$$
f(x)=\lambda,
$$

si disegna il grafico di $f$ e si conta il numero di intersezioni con la retta orizzontale

$$
y=\lambda.
$$

Variando $\lambda$, il numero di intersezioni può cambiare.

### Funzioni pari e dispari

Per verificare che una funzione sia pari o dispari di solito basta un calcolo simbolico:

- $f$ è pari se

  $$
  f(-x)=f(x);
  $$

- $f$ è dispari se

  $$
  f(-x)=-f(x).
  $$

Dimostrare che una funzione non è pari o non è dispari è in generale più delicato, ma spesso basta un controesempio. Per esempio, se per una funzione $f$ si ha

$$
f(1)\neq f(-1),
$$

allora $f$ non è pari. Se inoltre

$$
f(1)\neq -f(-1),
$$

allora non è dispari.

La strategia generale è:

- per dimostrare che una proprietà vale, si cerca una dimostrazione valida per ogni $x$;
- per dimostrare che non vale, basta trovare un caso in cui fallisce;
- per la periodicità, esibire un periodo è facile; dimostrare che non esiste alcun periodo è in genere più difficile.
