# L1 (Miljöverifiering)

## Övergripande angreppssätt

Uppgiftens syfte: att verifiera en **reproducerbar ML-miljö**,
fokus har därför legat på **tydlighet och minsta möjliga komplexitet**.

Alla val är gjorda för att:
- vara lätta att granska vid rättning
- minska risken för miljöberoende fel
- tydligt visa *vad* som verifieras och *varför*

---

## Miljö och beroendehantering

- Projektet är initierat med `uv init`
- Alla beroenden hanteras via `uv add`
- Exakta versioner i `uv.lock` för reproducerbarhet

`Python 3.12` används då den är tillräckligt etablerad för de valda beroendena och fungerar stabilt i den aktuella miljön. Har även specifierat i ***pyproject.toml*** att allt lägre än python 3.13 men högre än 3.10 fungerar, och att den skall installera de andra paketen baserat på detta.

---

## Tillagda paket

- **PyTorch** för att verifiera tensorberäkningar och GPU-stöd
- **Pandas** och **Scikit-learn** lades till eftersom de är standard i ML-pipelines
- **ipykernel** används som verifiering av Jupyter-stöd (som uppgiften krävde)

`ipykernel` verifieras här istället för ett Jupyter-UI, eftersom det är kärnan som faktiskt kör notebooks.

---

## check_env.py

Skriptet är avsiktligt skrivet utan hjälpfunktioner eller abstraktioner.

Verifieringen sker i fyra steg:
1. Python-version för att säkerställa rätt interpreter
2. Versionsnummer för adderade paket
3. Kontroll av CUDA-tillgänglighet via `PyTorch`
4. Enkel tensoroperation på vald device (GPU eller CPU)

Tensorberäkningen är minimal och syftar endast till att visa att:
- tensors kan allokeras på korrekt device
- beräkningar kan utföras utan fel

Ingen prestandamätning, eftersom det inte var relevant för uppgiften.

---

## Felhantering

- Skriptet förutsätter att beroenden finns installerade via `uv`
- CPU används som fallback om CUDA saknas
- Ingen try/except används, eftersom ett fel i detta läge ska indikera att miljön är fel uppsatt

---

## Reflektion och förbättringar

För ett större projekt hade jag antagligen:
- separerat verifieringslogik i funktioner
- lagt till tydligare exit-koder
- eventuellt verifierat CUDA-version och drivrutin mer detaljerat och gjort det mer reproducerbart på andra maskiner