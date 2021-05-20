[![Integration Test](https://github.com/zyeloni/ti-projekt/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/zyeloni/ti-projekt/actions/workflows/main.yml)

# RANKED.IO-APP

Celem programu jest utworzenie rozwiązania chmurowego odpowiedzialnego za gromadzenie danych z serwera do gry minecraft. Dane przechowywane będa w bazie mysql (w przyszłości może postgresql).
Całość projektu będzie rozłożona ma mikroserwisy. Specyfikacja mikroserwisów zostanie udostępniona za niegługo (powodem jest czesta zmiana koncepcji oraz usprawnienia, które mocno zmieniją całe podejście).

## Instalacja

Ranked.io wymaga [DOCKER](https://www.docker.com/).

```sh
docker-compose up
```
To wszystko docker zrobi za Ciebie resztę

## Autorzy

| Lp | Imię i Nazwisko |
| ------ | ------ |
| 1. | Kacper Łukasik |
| 2. | Michał Mulik |
| 3. | Sebastian Komuda |

## Wykorzystane technologię

- ngnix
- php
- js (vue.js + node)
- java

## Wykorzystane obrazy

Lista wykorzystanych obrazów z DOCKER HUB

| NAZWA | LINK |
| ------ | ------ |
| mysql | [https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql) |
| itzg/minecraft-server | [https://hub.docker.com/r/itzg/minecraft-server](https://hub.docker.com/r/itzg/minecraft-server) |

## Struktura folderów

| FOLDER | OPIS |
| ------ | ------ |
| /backend | folder z aplikacją backendową |
| /frontend | folder z aplikacją frontendową |
| /minecraft-server | folder z serwerem do gry minecraft |
| /sql-data | folder danych bazy sql |
| /ranked-io-plugin | folder z kodem źródłowym pluginu do serwera minecraft |


## Licencja

MIT
