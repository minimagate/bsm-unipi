---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-09-19'
title: Pensiero computazionale, algoritmi e modelli di calcolo
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-09-19 - Pensiero computazionale, algoritmi e modelli di calcolo.md
vault_hash: 26676b8729cb8c0d3f595e4e7858b1637d811684c6810298b118ae222766be36
---

## 1. Obiettivi e percorso del corso

Il corso introduce alcuni concetti fondamentali dell'informatica per sviluppare il [[Pensiero computazionale|pensiero computazionale]], cioè la capacità di:

- formulare i problemi in modo preciso;
- individuare soluzioni algoritmiche;
- descrivere e verificare programmi con rigore.

Il percorso parte dai concetti introduttivi, poi passa alla logica proposizionale e del primo ordine, ai principi della programmazione imperativa e alla programmazione in **C**. Più avanti si vedranno i costrutti di base del linguaggio, la programmazione modulare e ricorsiva, i puntatori, l'allocazione dinamica e strutture dati come liste concatenate e alberi binari.

## 2. Pensiero computazionale

Il **pensiero computazionale** è un modo di affrontare i problemi che li rende descrivibili, risolvibili e verificabili da un esecutore. Si basa su quattro componenti principali:

1. **Astrazione**: isolare gli aspetti rilevanti e ignorare i dettagli non essenziali.
2. **Scomposizione**: dividere un problema complesso in sottoproblemi più semplici.
3. **Riconoscimento di schemi**: individuare regolarità ricorrenti nei dati e nei problemi.
4. **Algoritmo e automazione**: descrivere una procedura eseguibile e verificarne l'effetto.

Con questo punto di vista si passa un passo alla volta da un problema informale a una specifica, poi a un algoritmo e infine a un programma.

## 3. Che cos'è l'informatica

L'informatica non coincide con:

- la scienza e la tecnica dei calcolatori;
- lo studio delle applicazioni dei calcolatori e del software;
- il semplice imparare a scrivere programmi.

La definizione proposta dall'**ACM** la presenta invece come lo studio sistematico degli algoritmi che descrivono e trasformano l'informazione, con la loro teoria, analisi, progetto, efficienza, realizzazione e applicazione.

Il centro dell'informatica è quindi l'**algoritmo**, non la macchina particolare che lo esegue.

## 4. Algoritmi: idea e origini

Un [[Algoritmo|algoritmo]] è una sequenza di passi che, se eseguita da un opportuno esecutore, porta ai risultati attesi a partire dai dati forniti. Gli algoritmi non sono roba solo da informatici: compaiono anche nelle istruzioni di montaggio, nell'uso di una lavastoviglie o nel prelievo da uno sportello automatico.

Una volta descritto un algoritmo, il procedimento corrispondente può essere automatizzato.

Il termine *algoritmo* deriva dalla latinizzazione del nome del matematico persiano **Abū Jaʿfar Muḥammad ibn Mūsā al-Khwārizmī** (circa 780-850), le cui opere contribuirono a diffondere in Europa la numerazione posizionale con lo zero.

### 4.1 La moltiplicazione egizia

Il papiro di Ahmes, o papiro di Rhind, risale circa al 1650 a.C. ed è copia di un testo ancora più antico. Contiene uno dei primi algoritmi documentati: la moltiplicazione di $A$ per $B$ viene ricondotta a raddoppi, dimezzamenti e addizioni:

$$
\begin{aligned}
A = 1 &\implies A \cdot B = B, \\
A \text{ pari} &\implies A \cdot B = \frac{A}{2} \cdot (2B), \\
A \text{ dispari} &\implies A \cdot B = (A-1) \cdot B + B.
\end{aligned}
$$

I passi per i casi pari e dispari si ripetono finché $A$ diventa $1$.

> [!example] Esempio
> Calcoliamo $6 \cdot 7$. Poiché $6$ è pari, $6 \cdot 7 = 3 \cdot 14$. Ora $3$ è dispari, quindi $3 \cdot 14 = 2 \cdot 14 + 14$, e $2 \cdot 14 = 1 \cdot 28 = 28$. Il risultato è $28 + 14 = 42$.

### 4.2 L'algoritmo di Euclide per il MCD

Per calcolare il [[Massimo comun divisore|massimo comune divisore]] di $x$ e $y$ non serve elencare tutti i divisori. Si possono sfruttare queste proprietà (è l'[[Algoritmo di Euclide|algoritmo di Euclide]]):

$$
\begin{aligned}
\operatorname{MCD}(x,x) &= x, \\
\operatorname{MCD}(x,y) &= \operatorname{MCD}(x-y,y) && \text{se } x>y, \\
\operatorname{MCD}(x,y) &= \operatorname{MCD}(x,y-x) && \text{se } x<y.
\end{aligned}
$$

Con sottrazioni successive il problema iniziale si trasforma in problemi sempre più semplici.

> [!example] Esempio
> $\operatorname{MCD}(12,8) = \operatorname{MCD}(4,8) = \operatorname{MCD}(4,4) = 4$.

## 5. Calcolabilità e modelli di calcolo

Solo a partire dagli anni Trenta del Novecento si è cercato di formalizzare la nozione intuitiva di **procedura effettiva**. Le domande fondamentali sono:

- che cosa significa che un problema è effettivamente calcolabile?
- quali problemi ammettono una soluzione algoritmica?
- esistono problemi per i quali nessun algoritmo può risolvere tutti i casi?

La risposta all'ultima domanda è sì: esistono problemi **indecidibili**.

### 5.1 Macchina di Turing

La [[Macchina di Turing|macchina di Turing]], introdotta da Alan Turing, è un modello astratto di calcolo. Il calcolo è visto come manipolazione di insiemi finiti e discreti di simboli secondo un insieme finito di regole.

Turing mostrò anche l'esistenza di una **macchina di Turing universale** (MTU), capace di ricevere la descrizione di una macchina di Turing insieme al suo input e di simularne il comportamento. La MTU è quindi un modello teorico di computer a programma memorizzato.

### 5.2 $\lambda$-calcolo e tesi di Church-Turing

Negli stessi anni Alonzo Church introdusse il **$\lambda$-calcolo**, un formalismo basato sulle funzioni e molto diverso dalla macchina di Turing. Nonostante la differenza di impostazione, i due modelli descrivono la stessa classe di funzioni effettivamente calcolabili.

La [[Tesi di Church-Turing|tesi di Church-Turing]] afferma che le macchine di Turing sono in grado di risolvere tutti i problemi effettivamente risolubili. È una tesi universalmente accettata, ma non un teorema dimostrabile: mette in relazione un modello formale con la nozione intuitiva, e quindi non formalizzata, di risolubilità effettiva.

Tra gli altri modelli di calcolo citati ci sono i sistemi di Post, le funzioni ricorsive di Kleene, il calcolo quantistico e il DNA computing. Nella presentazione del corso sono tutti considerati Turing-equivalenti rispetto a ciò che è calcolabile.

### 5.3 Modello di von Neumann

Il [[Modello di von Neumann|modello di von Neumann]], introdotto intorno al 1945, è un modello concreto di architettura alla base dei calcolatori attuali. Quanto a capacità di calcolo è equivalente alla macchina di Turing; la sua generalità deriva dal **programma memorizzato**, che permette alla stessa macchina di eseguire calcoli diversi.

## 6. Linguaggi e paradigmi di programmazione

Un calcolatore è **programmabile**: la funzione che svolge dipende dal programma che gli dice quali azioni compiere. Un **linguaggio di programmazione** permette di descrivere gli algoritmi in una forma che il calcolatore può capire ed eseguire.

I linguaggi si classificano in base al loro **paradigma di programmazione**, cioè lo stile e gli strumenti concettuali con cui rappresentano la computazione.

| Paradigma | Idea centrale | Esempi citati |
|---|---|---|
| Imperativo | Sequenza di comandi che modifica lo stato o l'ordine di esecuzione | Assembly, FORTRAN, C, COBOL, Pascal |
| Funzionale | Computazione espressa tramite funzioni | ML, Haskell, Scheme |
| Orientato agli oggetti | Organizzazione tramite oggetti | Java, Smalltalk, Eiffel |
| Logico | Computazione tramite relazioni e inferenza logica | PROLOG |
| Concorrente | Processi che evolvono e interagiscono | CCS, CSP |

Il corso adotta il **paradigma imperativo** e, nella seconda parte, il linguaggio C.

## 7. Le quattro fasi della programmazione

La **programmazione** è il procedimento che porta a definire programmi adatti a risolvere problemi. A un primo livello di astrazione si articola in quattro fasi:

$$
\text{specifica} \longrightarrow \text{algoritmo} \longrightarrow \text{codifica} \longrightarrow \text{esecuzione}.
$$

### 7.1 Specifica

La [[Specifica di un problema|specifica]] consiste nel capire e definire il problema. Può essere più o meno rigorosa, a seconda del formalismo usato, e deve descrivere:

- lo [[Stato|stato]] iniziale, cioè i dati in ingresso (*input*);
- lo **stato finale atteso**, cioè i risultati in uscita (*output*).

La forma concreta degli stati dipende dal problema e dagli oggetti considerati.

Esempi di specifiche informali:

1. dati due numeri, trovare il maggiore;
2. dato un elenco telefonico e un nome, trovare il numero corrispondente;
3. dati una rete stradale e i flussi dei veicoli, trovare il percorso più veloce tra due punti;
4. trovare numeri pari maggiori di $2$ che non siano somma di due numeri primi, come richiesto dalla congettura di Goldbach;
5. decidere, per ogni programma e ogni input, se il programma termina su quell'input (**problema dell'arresto**).

Questi esempi mostrano limiti diversi:

- una specifica non fornisce necessariamente il metodo risolutivo;
- può essere ambigua o imprecisa, per esempio se più persone hanno lo stesso nome;
- per alcuni problemi non è noto alcun metodo risolutivo;
- per altri, come il problema dell'arresto, è stato dimostrato che un metodo risolutivo generale non può esistere.

Nel corso si considerano problemi per i quali si sa che esiste un metodo risolutivo, cioè problemi **decidibili**.

### 7.2 Algoritmo

Dopo aver specificato il problema, si cerca un procedimento risolutivo. Per essere un algoritmo, il procedimento deve rispettare almeno tre requisiti:

- **finitezza**: è composto da una sequenza finita di passi elementari;
- **non ambiguità**: ogni azione è interpretata in modo univoco dall'esecutore;
- **eseguibilità**: l'esecutore può completare ogni azione in tempo finito con le risorse disponibili.

Indicazioni come «aggiungere sale quanto basta» non rispettano la non ambiguità per un esecutore automatico.

#### Efficienza e ricerca binaria

Algoritmi diversi possono risolvere lo stesso problema con efficienza diversa. Per cercare un nome in un elenco ordinato, la **ricerca binaria** procede così:

1. apre l'elenco a metà e legge il nome trovato;
2. termina se il nome coincide con quello cercato;
3. continua nella prima metà se il nome cercato viene prima in ordine lessicografico;
4. altrimenti continua nella seconda metà;
5. ripete finché trova il nome o conclude che non è presente.

A ogni passo si scarta metà dello spazio di ricerca, invece di confrontare tutti i nomi uno dopo l'altro.

### 7.3 Codifica

La **codifica** richiede di scegliere:

- una rappresentazione degli oggetti rilevanti;
- una descrizione dell'algoritmo in un linguaggio noto all'esecutore.

Quando l'esecutore è un calcolatore, l'algoritmo viene tradotto in un linguaggio di programmazione e diventa un programma eseguibile. Più il linguaggio usato per descrivere l'algoritmo è vicino al linguaggio di programmazione scelto, più la traduzione è semplice.

Il linguaggio deve permettere di rappresentare:

| Elemento concettuale | Nel programma |
|---|---|
| algoritmo | programma |
| informazioni iniziali | dati in ingresso |
| informazioni usate durante l'elaborazione | dati ausiliari |
| informazioni finali | dati in uscita |

### 7.4 Esecuzione e messa a punto

L'ultima fase è l'**esecuzione** del programma. Può far emergere errori nati nella specifica, nell'algoritmo o nella codifica, e quindi portare a rivedere una o più fasi.

I **debugger** sono strumenti che aiutano a trovare gli errori e a mettere a punto il programma.

## 8. Quadro d'insieme

L'intero processo si può leggere come una catena di raffinamenti:

$$
\text{problema informale}
\longrightarrow
\text{specifica precisa}
\longrightarrow
\text{procedimento risolutivo}
\longrightarrow
\text{programma}
\longrightarrow
\text{esecuzione verificata}.
$$

L'astrazione chiarisce che cosa conta, l'algoritmo stabilisce come procedere, il linguaggio rende la procedura eseguibile e la verifica controlla che il risultato ottenuto corrisponda allo stato finale richiesto.

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 1, a.a. 2026/2027. La slide di apertura del PDF non riporta una data di lezione.
