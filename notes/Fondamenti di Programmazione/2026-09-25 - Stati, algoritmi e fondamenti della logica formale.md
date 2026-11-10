---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-09-25'
title: Stati, algoritmi e fondamenti della logica formale
source_transcript: _transcripts/Fondamenti di Programmazione/2026-09-25 - Stati, algoritmi e fondamenti
  della logica formale.md
source_hash: sha256:232fff73d178b953c16fac63a878142ddce6b59d11a15f510cff88e5d24b4483
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-25T19:33:38.894Z'
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-09-25 - Stati, algoritmi e fondamenti della logica formale.md
vault_hash: 0c00aa2d06bd590c105cc08c9e9aa601f91a405179ea76d6be371fc4d68d8a75
---

## 1. Dal problema al programma

I linguaggi di programmazione offrono strumenti per rappresentare gli [[Algoritmo|algoritmi]] sotto forma di programmi, in modo che un elaboratore elettronico possa capirli ed eseguirli.

Per rappresentare un algoritmo bisogna poter descrivere:

- i dati e le informazioni iniziali;
- le informazioni usate durante l'elaborazione;
- le informazioni finali, cioè i risultati del calcolo.

Questi elementi corrispondono, rispettivamente, a:

- dati di ingresso;
- dati ausiliari;
- dati di uscita.

Nel corso si studierà il linguaggio di programmazione imperativo [[Linguaggio C|**C**]].

La programmazione comprende almeno queste fasi:

1. definizione o specifica del problema;
2. progettazione dell'algoritmo;
3. traduzione dell'algoritmo in un programma;
4. esecuzione del programma;
5. verifica e messa a punto del risultato.

L'esecuzione consiste nel far girare il programma su un sistema di runtime, cioè su un ambiente che permette di avviarlo e osservarne il comportamento.

Nella pratica, soprattutto per problemi non banali, il programma eseguito può:

- non produrre il risultato desiderato;
- contenere errori;
- avere comportamenti inattesi;
- non gestire alcuni casi particolari.

La fase di revisione e messa a punto, detta anche **debugging**, può coinvolgere qualunque fase della programmazione:

- la specifica iniziale può essere sbagliata;
- l'algoritmo può non aver previsto alcuni casi;
- la traduzione dell'algoritmo nel linguaggio di programmazione può contenere errori;
- il programma può essere corretto rispetto all'algoritmo, ma l'algoritmo stesso può essere inadeguato.

Gli strumenti software che aiutano a individuare e correggere gli errori dei programmi si chiamano **debugger**. Il termine *bug* indica un errore, mentre *debugger* richiama l'idea di eliminare gli errori.

---

## 2. Specifica di un problema e algoritmo

Per introdurre i concetti si può usare un linguaggio pseudonaturale, cioè un italiano leggermente adattato, insieme alle normali notazioni matematiche per numeri e operazioni aritmetiche.

### 2.1 Esempio: prodotto di due interi positivi

La [[Specifica di un problema|specifica del problema]] è:

> Dati due valori interi positivi, indicati con $A$ e $B$, l'output deve essere il valore del prodotto $A \cdot B$.

La specifica indica quindi:

- lo stato iniziale: sono disponibili due valori interi positivi $A$ e $B$;
- lo stato finale atteso: è disponibile il valore $A \cdot B$.

#### Esecutore dotato di moltiplicazione

Se l'esecutore sa fare direttamente le normali operazioni aritmetiche, l'algoritmo può essere:

1. acquisisci il primo valore;
2. acquisisci il secondo valore;
3. esegui l'operazione $A \cdot B$.

Un possibile esecutore è una persona con una calcolatrice.

Tradurre l'algoritmo nel linguaggio della calcolatrice significa:

1. digitare in sequenza le cifre decimali del primo numero;
2. digitare il tasto `*`;
3. digitare in sequenza le cifre decimali del secondo numero;
4. digitare il tasto `=`.

L'esecuzione avviene quando si preme `=` e la calcolatrice mostra il risultato.

#### Esecutore con capacità più limitate

Supponiamo ora che l'esecutore sappia fare soltanto:

- somme;
- sottrazioni;
- confronti tra numeri.

Non può quindi applicare direttamente la moltiplicazione, e serve un algoritmo diverso:

1. acquisisci il valore di $A$;
2. acquisisci il valore di $B$;
3. associa $0$ a una variabile ausiliaria $C$;
4. finché $B > 0$:
   1. somma $A$ a $C$;
   2. sottrai $1$ a $B$;
5. il risultato è il valore contenuto in $C$.

L'idea è che:

$$
A \cdot B =
\underbrace{A + A + \cdots + A}_{B\text{ volte}}.
$$

In questo algoritmo:

- $A$ mantiene il valore da sommare;
- $B$ conta quante somme restano da fare;
- $C$ accumula il risultato parziale.

Lo stesso algoritmo va poi tradotto nel linguaggio concreto dell'esecutore. Se l'esecutore è un bambino che sa solo sommare, sottrarre e confrontare numeri naturali, e che sa scrivere su un quaderno, si possono usare tre riquadri etichettati $A$, $B$ e $C$:

1. scrivere il primo valore nel riquadro $A$;
2. scrivere il secondo valore nel riquadro $B$;
3. scrivere $0$ nel riquadro $C$;
4. se il valore nel riquadro $B$ è maggiore di $0$:
   - calcolare la somma tra $A$ e $C$;
   - cancellare il contenuto di $C$ e scrivere il nuovo risultato;
   - sottrarre $1$ al valore di $B$;
   - cancellare il vecchio contenuto di $B$ e scrivere il nuovo valore;
   - ripetere;
5. terminare quando nel riquadro $B$ compare $0$.

Questo esempio mostra che la forma concreta di un algoritmo dipende dalle capacità dell'esecutore e dalle operazioni elementari che sa fare.

> [!warning]
> Un algoritmo non è caratterizzato solo dal problema che risolve: bisogna considerare anche l'esecutore e le operazioni elementari che sa comprendere ed eseguire.

---

## 3. Stato, configurazione ed esecuzione

La specifica astratta di un problema consiste nella descrizione di:

- uno **stato iniziale**, che descrive i dati iniziali del problema;
- uno **stato finale**, che descrive i risultati attesi.

Lo [[Stato|stato]] si può vedere come una particolare configurazione delle informazioni rilevanti in un certo momento dell'esecuzione.

Nel caso del bambino, lo stato è il contenuto dei riquadri del quaderno. Durante l'esecuzione i valori dei riquadri cambiano e si passa da una configurazione a un'altra.

Nel caso di un calcolatore, lo stato si può pensare come il contenuto della memoria, secondo il [[Modello di von Neumann|modello di von Neumann]]. Durante l'esecuzione il contenuto della memoria viene modificato progressivamente.

L'idea di stato non riguarda solo i calcolatori. Per esempio, lo stato di un ascensore può essere la sua posizione, cioè il piano dell'edificio in cui si trova. L'azione da eseguire dipende dallo stato:

- se l'ascensore si trova al piano $2$ e l'utente seleziona il piano $3$, deve salire;
- se si trova al piano $4$ e l'utente seleziona il piano $2$, deve scendere.

In generale, l'azione da eseguire dipende sia dallo stato corrente sia dall'operazione richiesta.

### Definizione intuitiva di algoritmo

Un algoritmo è una sequenza di passi elementari che l'esecutore sa eseguire e che modificano progressivamente lo stato fino a raggiungere lo stato desiderato.

L'esecuzione di un algoritmo si può quindi vedere come una sequenza di stati:

$$
S_0 \longrightarrow S_1 \longrightarrow S_2 \longrightarrow \cdots \longrightarrow S_f,
$$

dove:

- $S_0$ è lo stato iniziale;
- $S_f$ è lo stato finale;
- ogni passaggio da uno stato al successivo è prodotto da un'operazione dell'esecutore.

Nel paradigma imperativo deve esserci almeno un'azione che modifica lo stato. Nel linguaggio C questa azione sarà soprattutto l'**assegnamento**, il cui effetto è modificare una parte della memoria.

---

## 4. Rappresentazione astratta dello stato

Per non legarsi a esempi concreti come il quaderno del bambino o la memoria del calcolatore, si introduce una nozione astratta di stato.

Uno stato è un [[Insieme|insieme]] di associazioni tra:

- nomi simbolici;
- valori.

Un'associazione tra il nome simbolico $X$ e il valore $\mathrm{val}$ si può scrivere:

$$
X \mapsto \mathrm{val}.
$$

Uno stato è quindi un insieme di associazioni di questo tipo.

Per esempio, sono possibili gli stati:

$$
\{
\mathrm{nome} \mapsto \mathrm{Antonio},
\mathrm{cognome} \mapsto \mathrm{Rossi},
\mathrm{età} \mapsto 25
\},
$$

$$
\{
\mathrm{importo} \mapsto 1650,
\mathrm{tasso} \mapsto 2\%,
\mathrm{interesse} \mapsto 165
\},
$$

oppure:

$$
\{
A \mapsto 25,
B \mapsto 350
\}.
$$

Uno stato si può anche rappresentare come un insieme di coppie ordinate:

$$
\{(\mathrm{nome},\mathrm{Antonio}),
(\mathrm{cognome},\mathrm{Rossi}),
(\mathrm{età},25)\}.
$$

### Vincolo fondamentale sugli stati

A ogni nome simbolico deve essere associato **al più un valore** nello stesso stato.

Per esempio, il seguente oggetto non è uno stato corretto:

$$
\{
\mathrm{nome} \mapsto \mathrm{Antonio},
\mathrm{nome} \mapsto \mathrm{Paolo},
\mathrm{età} \mapsto 25
\}.
$$

Il problema è che, dato il nome simbolico $\mathrm{nome}$, non si saprebbe se il valore associato è Antonio oppure Paolo.

Allo stesso modo non è corretto uno stato in cui:

$$
A \mapsto 45,
\qquad
B \mapsto 150,
\qquad
B \mapsto 0.
$$

Se dovessimo eseguire l'operazione $A \cdot B$, non sarebbe chiaro quale valore di $B$ usare.

È invece possibile che a un nome simbolico non sia associato alcun valore. Per esempio, in uno stato che descrive una persona tramite nome, cognome ed età, i simboli $X$ o $\mathrm{Trump}$ possono semplicemente non comparire.

> [!note]
> Uno stato è un insieme di associazioni nome-valore tale che ogni nome simbolico è associato ad al più un valore.

### Insiemi e multinsiemi

Dal punto di vista insiemistico, un insieme non contiene duplicati. Un multinsieme, invece, permette che uno stesso elemento compaia più volte.

Esempi:

- $\{1,2,3,4\}$ è un insieme;
- $\{1,1,2,3\}$ rappresenta un multinsieme;
- $\{10,40,-3\}$ è un insieme di numeri.

Gli stati sono insiemi di coppie nome-valore. Anche se le coppie sono oggetti distinti dal punto di vista insiemistico, l'astrazione dello stato impone il vincolo aggiuntivo che non possano esistere due coppie con lo stesso nome e valori diversi.

---

## 5. Specifica del problema del prodotto tramite stati

Il problema:

> Dati due interi positivi, calcolare il loro prodotto.

si può esprimere in termini di stato iniziale e stato finale.

Lo stato iniziale contiene due associazioni:

$$
\mathrm{fattore1} \mapsto a,
\qquad
\mathrm{fattore2} \mapsto b.
$$

Lo stato finale deve contenere l'associazione:

$$
\mathrm{prodotto} \mapsto a \cdot b.
$$

In forma schematica:

$$
\{
\mathrm{fattore1} \mapsto a,
\mathrm{fattore2} \mapsto b
\}
\longrightarrow
\{
\mathrm{prodotto} \mapsto a \cdot b
\}.
$$

I simboli $a$ e $b$ rappresentano valori generici, non numeri specifici. In questo contesto si chiamano **variabili di specifica**.

La specifica non fissa necessariamente i valori finali di tutte le altre associazioni. Per esempio, non importa quale valore avranno nello stato finale:

- $\mathrm{fattore1}$;
- $\mathrm{fattore2}$;
- altri nomi non pertinenti al risultato.

Conta solo che nello stato finale il nome simbolico $\mathrm{prodotto}$ sia associato al valore $a \cdot b$, dove $a$ e $b$ sono i valori inizialmente associati ai due fattori.

### Esempio di esecuzione corretta

Consideriamo inizialmente:

$$
A \mapsto 5,
\qquad
B \mapsto 3,
\qquad
C \mapsto 0.
$$

Applicando l'algoritmo della moltiplicazione tramite somme successive:

1. $B=3>0$:
   - $C \leftarrow C+A = 0+5=5$;
   - $B \leftarrow B-1=2$.

   Nuovo stato:

   $$
   A \mapsto 5,\qquad B \mapsto 2,\qquad C \mapsto 5.
   $$

2. $B=2>0$:
   - $C \leftarrow C+A = 5+5=10$;
   - $B \leftarrow B-1=1$.

   Nuovo stato:

   $$
   A \mapsto 5,\qquad B \mapsto 1,\qquad C \mapsto 10.
   $$

3. $B=1>0$:
   - $C \leftarrow C+A = 10+5=15$;
   - $B \leftarrow B-1=0$.

   Stato finale:

   $$
   A \mapsto 5,\qquad B \mapsto 0,\qquad C \mapsto 15.
   $$

Il risultato si trova in $C$:

$$
C=15=5\cdot 3.
$$

Durante la spiegazione in aula era stato inizialmente commesso un errore di calcolo, ottenendo $18$ invece di $15$. L'errore non riguardava l'algoritmo, ma l'esecuzione manuale dei calcoli. Quindi vanno distinte:

- la correttezza dell'algoritmo;
- la correttezza dell'esecuzione concreta dei singoli passi.

---

## 6. Introduzione alla logica

La logica è una disciplina antica, nata dal tentativo di formalizzare il ragionamento umano, cioè di individuare le regole che governano i processi di ragionamento.

I primi studi sistematici risalgono ai filosofi dell'antica Grecia, in particolare ad Aristotele. Negli *Analitici primi* Aristotele introduce concetti relativi a:

- premesse;
- termini;
- sillogismi;
- dimostrazioni.

### 6.1 Il sillogismo

Un esempio classico di ragionamento è:

1. tutti gli uomini sono mortali;
2. Socrate è un uomo;
3. quindi Socrate è mortale.

La conclusione deriva logicamente dalle premesse.

La logica moderna si è sviluppata soprattutto alla fine dell'Ottocento, anche per dare basi formali alla matematica.

### Scopi della logica

In matematica la logica serve principalmente a:

- esprimere asserti in modo rigoroso e non ambiguo;
- formalizzare il concetto di dimostrazione;
- studiare la derivazione di teoremi, tesi e conseguenze a partire da premesse.

Per esempio, l'enunciato informale:

> Tutti i numeri pari maggiori di $2$ non sono primi.

si può esprimere formalmente come:

$$
\forall n\,
\bigl(
(n \text{ è pari} \land n>2)
\rightarrow
(n \text{ non è primo})
\bigr).
$$

La formalizzazione rende esplicita la struttura dell'enunciato e ne riduce l'ambiguità.

### 6.2 Logica e informatica

La logica è strettamente legata all'informatica e ne costituisce una parte dei fondamenti teorici.

Tra gli usi della logica in informatica ci sono:

- formalizzazione dei requisiti del software;
- studio delle proprietà dei programmi;
- verifica dei programmi;
- verifica di sistemi complessi;
- rappresentazione della conoscenza in intelligenza artificiale;
- programmazione logica;
- teoria dei tipi;
- studio dei linguaggi funzionali.

Nel corso si introdurrà anche la **logica di Hoare**, usata per ragionare formalmente sulle proprietà dei programmi.

Il linguaggio **Prolog** è un esempio di linguaggio di programmazione logica: vi si scrivono premesse e regole, dalle quali il sistema cerca di ricavare conclusioni tramite regole di inferenza.

---

## 7. Ragionamenti validi e ragionamenti non validi

### 7.1 Il problema degli amici al cinema

Si considerino tre amici: Antonio, Bruno e Corrado. Sappiamo che:

- se Corrado va al cinema, allora anche Antonio va al cinema;
- condizione necessaria affinché Antonio vada al cinema è che Bruno vada al cinema.

Ci si chiede quali conclusioni si possano affermare con certezza, tra cui:

- se Corrado è andato al cinema, allora è andato anche Bruno;
- nessuno dei tre è andato al cinema;
- se Bruno è andato al cinema, allora è andato anche Corrado;
- se Corrado non è andato al cinema, allora non è andato nemmeno Bruno.

Il problema richiede di:

1. formalizzare gli enunciati espressi in linguaggio naturale;
2. applicare regole di inferenza;
3. individuare la conclusione corretta;
4. dimostrare che la conclusione è corretta;
5. dimostrare, eventualmente, che le altre conclusioni non seguono dalle premesse.

### 7.2 Conseguenza logica

In un ragionamento non è essenziale, all'inizio, stabilire se le premesse siano davvero vere nel mondo reale.

Il ragionamento:

1. tutti gli uomini sono mortali;
2. Socrate è un uomo;
3. Socrate è mortale;

è valido perché, **se le premesse sono vere**, allora anche la conclusione deve essere vera.

In altre parole, non è possibile che:

- entrambe le premesse siano vere;
- la conclusione sia falsa.

Si dice che la conclusione è una [[Conseguenza logica|conseguenza logica]] delle premesse.

### Ragionamento non valido

Consideriamo invece:

1. tutti gli uomini sono mortali;
2. Socrate è mortale;
3. quindi Socrate è un uomo.

Questo ragionamento non è valido. Il nome «Socrate» potrebbe riferirsi al filosofo, ma anche a un cane chiamato Socrate. In entrambi i casi Socrate potrebbe essere mortale, ma dal fatto di essere mortale non segue necessariamente che sia un uomo.

La struttura logica non garantisce la conclusione.

> [!warning]
> La verità delle premesse non basta a garantire la validità di un ragionamento. Bisogna anche che la conclusione segua logicamente dalle premesse.

---

## 8. Regole di inferenza

Una [[Regola di inferenza|regola di inferenza]] è una legge che permette di derivare uno o più asserti a partire da altri asserti.

Due schemi fondamentali sono:

### Regola di implicazione

Se valgono:

$$
Q \rightarrow R
$$

e

$$
Q,
$$

allora si può dedurre:

$$
R.
$$

Questa è la struttura del *modus ponens*.

Esempio:

- se un numero è pari e maggiore di $2$, allora non è primo;
- $8$ è pari e maggiore di $2$;
- quindi $8$ non è primo.

### Regola di istanziazione

Se per ogni individuo $x$ vale una proprietà $P(x)$, allora la proprietà vale anche per uno specifico individuo $a$:

$$
\forall x\,P(x)
\quad\Longrightarrow\quad
P(a).
$$

Questa regola permette di passare da un'affermazione universale a un caso particolare.

### 8.1 Dimostrazione del caso di Socrate

Introduciamo i predicati:

- $\mathrm{uomo}(x)$: $x$ è un uomo;
- $\mathrm{mortale}(x)$: $x$ è mortale.

Le premesse sono:

$$
\forall x\,
\bigl(
\mathrm{uomo}(x)\rightarrow \mathrm{mortale}(x)
\bigr)
$$

e

$$
\mathrm{uomo}(\mathrm{Socrate}).
$$

Applichiamo la regola di istanziazione alla prima premessa, scegliendo come individuo specifico Socrate:

$$
\mathrm{uomo}(\mathrm{Socrate})
\rightarrow
\mathrm{mortale}(\mathrm{Socrate}).
$$

Usando anche la seconda premessa e applicando la regola di implicazione, otteniamo:

$$
\mathrm{mortale}(\mathrm{Socrate}).
$$

La dimostrazione è fatta di passi meccanici:

1. si prende una premessa;
2. si applica una regola di inferenza;
3. si ottiene un nuovo asserto;
4. si applica un'altra regola agli asserti disponibili;
5. si continua fino a ottenere la conclusione.

La stessa struttura serve per dimostrare che $8$ non è primo. Cambiano i significati dei simboli, ma la struttura formale della dimostrazione resta la stessa.

### 8.2 Sintassi e significato

Se si sostituiscono i simboli con lettere prive di significato, lo schema diventa:

$$
\forall x\,(P(x)\rightarrow Q(x))
$$

insieme a:

$$
P(a).
$$

Da questi si ricava:

$$
Q(a).
$$

La validità della dimostrazione dipende solo dalla forma e dalle regole applicate, non dal significato concreto dei simboli.

Una dimostrazione è quindi una sequenza di trasformazioni simboliche eseguite secondo regole meccaniche. In questo senso somiglia a un algoritmo.

---

## 9. Logica classica e proposizioni

Una [[Proposizione|proposizione]], o asserto, è un enunciato dichiarativo a cui è associato un valore di verità:

- vero;
- falso.

Il corso considera la **logica classica**, nella quale valgono i principi:

### Principio del terzo escluso

Ogni proposizione è vera oppure falsa:

$$
p \text{ è vera} \quad \lor \quad p \text{ è falsa}.
$$

Non è ammesso un terzo valore di verità.

### Principio di non contraddittorietà

Una proposizione non può essere contemporaneamente vera e falsa.

Esistono altre logiche, come la logica intuizionista, che possono adottare impostazioni diverse; in questo corso si considera la logica classica.

### 9.1 Esempi di proposizioni

Sono proposizioni:

- «Roma è la capitale d'Italia»;
- «La Francia è uno Stato del continente asiatico»;
- $1+1=2$;
- $1+2=3$.

Ciascun enunciato ha un valore di verità, anche se può essere falso. Per esempio, «La Francia è uno Stato del continente asiatico» è una proposizione falsa.

Non sono proposizioni:

- «Che ore è?»: è una domanda;
- «Leggete queste note con attenzione»: è una raccomandazione o un comando;
- $x+1=2$, se non è specificato il valore di $x$.

L'espressione $x+1=2$ è problematica perché il suo valore di verità dipende dall'interpretazione di $x$:

- se $x=1$, l'asserzione è vera;
- se $x=47$, l'asserzione è falsa.

---

## 10. Interpretazioni, modelli e conseguenza logica

Una dimostrazione simbolica opera sui simboli senza considerarne il significato. Il significato entra in gioco tramite il concetto di **interpretazione**.

### 10.1 Interpretazione

Un'[[Interpretazione|interpretazione]] attribuisce un significato ai simboli presenti negli asserti.

Consideriamo l'asserto:

$$
P(A).
$$

Possibili interpretazioni:

1. $P$ significa «essere un essere umano» e $A$ indica il filosofo Socrate;
2. $P$ significa «essere un essere umano» e $A$ indica un cane chiamato Socrate;
3. $P$ significa «essere un numero pari» e $A$ indica il numero naturale $4$;
4. $P$ significa «essere maggiore di $10$» e $A$ indica ancora il numero naturale $4$.

Allora:

- nell'interpretazione 1, $P(A)$ è vero;
- nell'interpretazione 2, $P(A)$ è falso;
- nell'interpretazione 3, $P(A)$ è vero;
- nell'interpretazione 4, $P(A)$ è falso.

Lo stesso asserto sintattico può quindi essere vero in alcune interpretazioni e falso in altre.

### 10.2 Modello

Sia $\Gamma$ un insieme di asserti.

Un'interpretazione è un **modello di $\Gamma$** se rende veri tutti gli asserti appartenenti a $\Gamma$.

In simboli, informalmente:

$$
I \models \Gamma
$$

significa che l'interpretazione $I$ rende veri tutti gli asserti di $\Gamma$.

### 10.3 Conseguenza logica

Un asserto $Q$ è una conseguenza logica dell'insieme di asserti $\Gamma$ se $Q$ è vero in tutti i modelli di $\Gamma$.

Si indica normalmente con:

$$
\Gamma \models Q.
$$

Il significato è:

> non esiste un'interpretazione nella quale tutti gli asserti di $\Gamma$ siano veri e $Q$ sia falso.

Equivalentemente:

$$
\Gamma \models Q
$$

se e solo se ogni interpretazione che rende vere tutte le premesse rende vero anche $Q$.

Questa è la formalizzazione precisa dell'idea intuitiva secondo cui una conclusione segue logicamente dalle premesse.

---

## 11. Dimostrazione sintattica e semantica

Il concetto di conseguenza logica è semantico: riguarda la verità degli asserti nelle possibili interpretazioni.

In generale, però, non è pratico elencare tutti i modelli di un insieme di premesse e verificare che la conclusione sia vera in ciascuno: i modelli possono essere infiniti.

La dimostrazione offre invece un metodo sintattico e meccanico:

1. si parte dalle premesse;
2. si applicano regole di inferenza;
3. si costruisce una sequenza di asserti;
4. si arriva alla conclusione desiderata.

Se si riesce a derivare $Q$ da $\Gamma$ con regole di inferenza corrette, si può essere certi che:

$$
\Gamma \models Q.
$$

La dimostrazione non usa il significato dei simboli: è una manipolazione puramente sintattica.

### 11.1 Correttezza delle regole

Un insieme di regole di inferenza è **corretto** se ogni conclusione ottenuta applicando una regola è davvero conseguenza logica delle premesse usate.

In forma concettuale:

> applicando una regola corretta non si può derivare una conclusione falsa in un'interpretazione in cui tutte le premesse sono vere.

### 11.2 Completezza delle regole

Un insieme di regole è **completo** se permette di dimostrare ogni conseguenza logica.

In altri termini, se:

$$
\Gamma \models Q,
$$

allora deve essere possibile costruire una dimostrazione di $Q$ a partire da $\Gamma$ usando le regole disponibili.

La correttezza garantisce che non si dimostrino conclusioni illegittime; la completezza garantisce che le conseguenze logiche si possano effettivamente dimostrare.

---

## 12. Calcolo proposizionale

Per formalizzare con rigore i ragionamenti si introduce un linguaggio simbolico. Il primo linguaggio logico studiato è il [[Calcolo proposizionale|calcolo proposizionale]].

Il calcolo proposizionale:

- è il linguaggio logico formale più semplice;
- permette di rappresentare proposizioni vere o false;
- consente di costruire proposizioni complesse a partire da proposizioni più semplici;
- ha un potere espressivo limitato;
- è il nucleo di base di linguaggi logici più potenti, come il calcolo dei predicati del [[Logica del primo ordine|primo ordine]].

Lo studio comprenderà:

1. la sintassi delle formule;
2. la semantica delle formule;
3. il concetto di interpretazione;
4. il concetto di conseguenza logica;
5. le dimostrazioni.

### 12.1 Proposizioni atomiche e non atomiche

Una **proposizione atomica** è una proposizione che non viene scomposta in proposizioni più semplici.

Una **proposizione non atomica** è costruita combinando proposizioni atomiche o altre proposizioni con dei connettivi logici.

Esempi:

- «Roma è la capitale d'Italia» è atomica;
- «Parigi è una città italiana» è atomica;
- «Roma è la capitale d'Italia e Parigi è una città italiana» è non atomica;
- «Se piove, porto l'ombrello» è non atomica;
- «Chiudo la finestra oppure indosso la felpa» è non atomica;
- «Roma non è la capitale d'Italia» è ottenuta negando una proposizione.

I [[Connettivo logico|connettivi logici]] hanno un ruolo analogo a quello degli operatori aritmetici: combinano componenti per costruire espressioni più complesse.

---

## 13. Connettivi logici

I principali connettivi introdotti sono:

- negazione;
- congiunzione;
- disgiunzione;
- implicazione;
- equivalenza.

Date due proposizioni $p$ e $q$, le notazioni usate sono:

| Operazione | Notazione | Lettura |
|---|---|---|
| Negazione | $\neg p$ | non $p$ |
| Congiunzione | $p \land q$ | $p$ e $q$ |
| Disgiunzione | $p \lor q$ | $p$ oppure $q$ |
| Implicazione | $p \rightarrow q$ | se $p$, allora $q$ |
| Equivalenza | $p \leftrightarrow q$ | $p$ se e soltanto se $q$ |

L'equivalenza si può rappresentare anche con una doppia freccia. La notazione precisa può variare, purché sia chiaro il significato.

### 13.1 Negazione

La negazione di $p$ si indica con:

$$
\neg p.
$$

Il suo valore di verità è opposto a quello di $p$:

- $\neg p$ è vera quando $p$ è falsa;
- $\neg p$ è falsa quando $p$ è vera.

### 13.2 Congiunzione

La congiunzione si indica con:

$$
p \land q.
$$

È vera quando entrambe le proposizioni sono vere:

$$
p \land q \text{ è vera}
\quad\Longleftrightarrow\quad
p \text{ è vera e } q \text{ è vera}.
$$

### 13.3 Disgiunzione inclusiva

La disgiunzione si indica con:

$$
p \lor q.
$$

È vera quando almeno una delle due proposizioni è vera:

$$
p \lor q \text{ è vera}
\quad\Longleftrightarrow\quad
p \text{ è vera oppure } q \text{ è vera, eventualmente entrambe}.
$$

Questa è una disgiunzione inclusiva.

### Disgiunzione esclusiva

Esiste anche la disgiunzione esclusiva, che non useremo come connettivo principale. È vera quando esattamente una delle due proposizioni è vera.

Per esempio, nell'affermazione:

> Stasera mangio carne o pesce

si potrebbe intendere che si mangia una sola delle due cose, non entrambe. In quel caso servirebbe una disgiunzione esclusiva.

La disgiunzione ordinaria $p\lor q$, invece, permette che siano vere entrambe.

### 13.4 Implicazione

L'[[Implicazione|implicazione]] si indica con:

$$
p \rightarrow q.
$$

La lettura informale è:

> se $p$, allora $q$.

L'implicazione è vera quando, ogni volta che $p$ è vera, anche $q$ è vera.

La condizione essenziale è:

$$
p \text{ vera} \Longrightarrow q \text{ vera}.
$$

Se $p$ è falsa, l'implicazione non viene violata: $q$ può essere vera oppure falsa.

In particolare:

- se $p$ è vera e $q$ è vera, $p\rightarrow q$ è vera;
- se $p$ è vera e $q$ è falsa, $p\rightarrow q$ è falsa;
- se $p$ è falsa, l'implicazione è vera indipendentemente dal valore di $q$.

Le tabelle di verità permetteranno di formalizzare completamente questi casi.

### 13.5 Equivalenza

L'equivalenza si indica con:

$$
p \leftrightarrow q.
$$

La lettura è:

> $p$ se e soltanto se $q$.

L'equivalenza è vera quando $p$ e $q$ hanno lo stesso valore di verità:

- entrambe vere;
- oppure entrambe false.

In particolare:

$$
p \leftrightarrow q
$$

esprime che $p$ è vera se e soltanto se $q$ è vera.

---

## 14. Prosecuzione

Il significato dei connettivi verrà formalizzato con le [[Tavola di verità|tabelle di verità]], che stabiliscono il valore di verità di una proposizione composta in funzione dei valori delle proposizioni che la compongono.
