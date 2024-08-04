# Super irriterende reminder script
Hvis du har brug et (super) irriterende script med et pop-up vindue til at minde dig om et eller andet, så er håbet, at dette script kunne hjælpe dig med det.

## Forudsætninger for at bruge scriptet
For at kunne bruge scriptet er der følgende 2 forudsætninger, som hver beskrives og gennemgås i nedenstående:
1. Have Python installeret
2. Have Python pakken "pyAutoGUI" installeret

### Python
For at kunne bruge scriptet forudsættes det først og fremmest, at du har Python installeret.

Har du ikke Python installeret, så download det her: https://www.python.org/ 

### PyAutoGUI
Derudover forudsætter brugen af scriptet, at man med Pythons package manager, "pip", har installeret Python pakken kaldet "[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)".

Har man ikke det, så kan man køre følgende kommando for at installere "PyAutoGUI" vhja. af filen "requirements.txt" som dette repo indeholder:

```bash
pip install -r requirements.txt
```

Når begge dele er installeret vil du kunne bruge scriptet.

## Om brugen af scriptet
Hvis du fx gerne vil minde dig selv om at tage din medicin, så ville du blot kører scriptet med følgende kommando:

```python
python3 script.py "tage medicin"
```

Ved kørsel af scriptet vil et pop-up vindue som dette således komme frem på skærmen.

<img width="512" alt="reminder_script" src="https://github.com/user-attachments/assets/51b7b12d-5f23-435f-bb29-dd330780b0d9">

Med vinduet vil man således kunne trykke på enten "Ja" eller "Nej" knappen.

Trykker man på "Ja" knappen, så vil scriptet gemme dags dato i en tekstfil, således at gentagne kørsler - fx via "crontab" på Mac eller "Task Scheduler" på Windows - ikke vil få pop-up vinduet til at vise sig (da man jo i så fald har husket at tage sin medicin som i dette eksempel). Sættes scriptet således til at køre automatisk fx hver dag, så vil vindue altså først vises næste gang, hvor dags dato ikke er lig med den dato som er gemt i tekstfilen.

Trykker man på "Nej" knappen, så vil pop-up vinduet fremkommer hver gang det køres.

## Om automatiseret kørsel af scriptet
På nuværende er tidspunkt er en automatiseret kørsel af scriptet kun testet på Mac.

Hvis man på en Mac vil køre scriptet automatisk - fx hver dag på et givent tidspunkt - så skal det køres vhja. af "sub.py" filen, da brugen af pyautogui ellers ikke virker.

I crontab (eller hvordan man nu siger det) ville et eksempel på automatisk kørsel af scriptet således være at sætte det op som følger (udskift her frasen "<path-to-script>" med stien til mappen med scriptet):

```bash
10 8-12 * * * cd <path-to-script> && /usr/bin/python3 sub.py "tage medicin"
```

### Hvordan man kører scripts automatisk via 'crontab' på Mac
Google fx frasen "how to schedule tasks with crontab" for at finde ud af, hvordan man automatisk kører scripts på en Mac.

### Hvordan man kører scripts automatisk via 'Task Scheduler' på Windows
Google fx frasen "how to schedule tasks in task scheduler" for at finde ud af, hvordan man automatisk kører scripts på Windows.
