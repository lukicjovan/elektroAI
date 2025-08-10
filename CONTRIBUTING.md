# Contributing (elektroAI)

## Branch strategija
- `main`: stabilne verzije (release-ovi)
- `dev`: integracija novih funkcija
- `feature/*`: pojedinačne funkcionalnosti
- `hotfix/*`: brze ispravke za produkciju

## Konvencija commit poruka (Conventional Commits)
- `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
Primer: `feat(ocr): dodata PaddleOCR integracija`

## PR pravila
- Mali, fokusirani PR-ovi
- Opis šta i zašto je menjano
- Proći CI (flake8, black, isort, pytest)