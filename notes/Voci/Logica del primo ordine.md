---
title: Logica del primo ordine
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine
alias:
- LPO
- logica dei predicati
sintesi: Estensione del calcolo proposizionale con termini, predicati e quantificatori, per parlare di individui, proprietà e relazioni.
---

La **logica del primo ordine** (LPO) estende il [[Calcolo proposizionale|calcolo proposizionale]] per poter parlare di individui, delle loro proprietà e delle relazioni tra loro, e di "tutti" o "qualche" individuo.

## Definizione

Oltre ai connettivi, il linguaggio ha:

- **termini**, che denotano gli individui (costanti, variabili, applicazioni di simboli di funzione);
- **predicati**, che esprimono proprietà e relazioni e trasformano termini in formule;
- [[Quantificatore|quantificatori]]: universale $\forall$ ed esistenziale $\exists$.

Una formula assume un valore di verità rispetto a un'[[Interpretazione|interpretazione]] (un dominio più il significato dei simboli) e a un assegnamento delle variabili. Le formule vere in ogni interpretazione sono dette **valide**, l'analogo delle tautologie.

## Intuizione

Il calcolo proposizionale tratta «Antonio va al cinema» come un blocco indivisibile; la LPO guarda dentro e vede il predicato "va al cinema" applicato all'individuo Antonio. Il prezzo è che non esistono tavole di verità finite per decidere la validità: bisogna dimostrare, e non sempre si riesce.

## Esempi

«Tutti i numeri pari maggiori di due non sono primi»:

$$
\forall x.\bigl((\operatorname{pari}(x)\land x>2)\Rightarrow\neg\operatorname{primo}(x)\bigr).
$$

«Esiste un numero maggiore di due che non è primo»: $\exists x.\bigl((x>2)\land\neg\operatorname{primo}(x)\bigr)$.

## Vedi anche

- [[Formula ben formata]]
- [[Variabile libera e legata]]
- [[Quantificatore]]
- [[Calcolo proposizionale]]
