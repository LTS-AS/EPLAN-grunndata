# Installasjon av EPLAN ELECTRIC P8

## Introduksjon
Denne rutinen beskriver installasjon av EPLAN electric P8 på en windows-maskin med 64-biters operativsystem. Vi har ofte behov for å ta med PCen ut til kunder. Derfor velger vi å ha databasene i MS-Access filer.

## Programvare
- EPLAN Electric P8 Professional Version 2.7
- 64-bit Windows 7 Pro
- 64-bit MS office 2010, 2013, 2016 --ELLER-- (64-bit MS office 365 og 64-bit MS Acces Runtime 2016)
- <B>EPLAN 2.7 klarer ikke</B> å kjøre MS-access filer hvis det er installert 32-bit office på maskinen.
- Filer er plassert på en filserver med navn ws1.

## Installasjon
- \\ws1\data\software\EPLAN\Electric P8 2.7.3.11418\setup.exe
- Velg Electric P8 (x64), klikk neste
- Aksepter lisensen, klikk neste
- Klikk Default
- Velg Company code. OBS! vanskelig å gjøre om senere. En del mapper i mappestrukturen vil få dette navnet. Feltet bør ikke stå tomt. Hør med en kollega om du er usikker.
- Velg mm, klikk neste, klikk neste

### Gratulerer! du har installert EPLAN lokalt. Dtte har blitt installert på maskinen
Mappe | Beskrivelse
--- | --- 
C:\Program Files\EPLAN | EPLAN applikasjoner
C:\ProgramData\EPLAN\O_Data\Platform Data | Originale grunndata for EPLAN platformen
C:\ProgramData\EPLAN\O_Data\Electric P8 Data | Originale grunndata for EPLAN Electric P8
C:\Users\Public\EPLAN\Settings | 
C:\Users\Public\EPLAN\Settings | 
C:\Users\Public\EPLAN\Settings | 
C:\Users\Public\EPLAN\Data | Arbeidsmapper

Legg merke til at alle mapper er plasert på maskinens fellesområde. Det vil si at alle brukere av maskinen har tilgang.

## Tilpassinger for arbeid mot ny filserver
- Monter nettverkspartisjon
```cmd
NET USE L: \\ws1\data
```
- Kopier arbeidsmappe fra C:\Users\Public\EPLAN\Data til L:\EPLAN\Data
- Hent scheme....

## Gratulerer! du jobber nå mot en filserver
Nå kan flere jobbe mot samme grunndata, og dra nytte av hverandres forbedringer. Flere brukere kan til til og med åpne samme prosjekt samtidig.

## Arbeid i felt
- Ta en sikkerhetskopi av C:\Users\Public\EPLAN\Data
- Slett C:\Users\Public\EPLAN\Data
- Kopier L:\EPLAN\Data til C:\Users\Public\EPLAN\Data
