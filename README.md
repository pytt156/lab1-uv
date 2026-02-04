# L1 (Miljöverifiering)

## Övergripande angreppssätt

Uppgiftens syfte var att verifiera en **reproducerbar ML-miljö**,
fokus har därför legat på **tydlighet och minsta möjliga komplexitet**.

Alla val är gjorda för att:
- minska risken för miljöberoende fel
- tydligt visa *vad* som verifieras och *varför*

.. framför onödig komplexibilitet/avancerad nivå.

---

## Miljö och beroendehantering

- Projektet är initierat med `uv init`
- Alla beroenden hanteras via `uv add`
- Exakta versioner i `uv.lock` för reproducerbarhet

`Python 3.12` används.
Projektet är konfigurerat för Python `>=3.10,<3.13` i pyproject.toml, vilket är kompatibelt med samtliga använda beroenden.

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
3. Kontroll av tillgänglig beräknings-backend via PyTorch
    - CUDA (NVIDIA)
    - MPS (Apple Silicon)
    - CPU (fallback)
4. Enkel tensoroperation på vald device

Tensorberäkningen är minimal och syftar endast till att visa att:
- tensors kan allokeras på korrekt device
- beräkningar kan utföras utan fel

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
- eventuellt verifierat CUDA-version och drivrutin mer detaljerat
- lagt till CI för att köra scriptet på push