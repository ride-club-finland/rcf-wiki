---
gold_id: roles_and_responsibilities
wiki_category: YLLAPITO
related_gold_docs: [discord_operating_model, resource_inventory]
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-15
---

# Roolit ja vastuut

Roolipohjainen kuvaus seuran ylläpidon vastuualueista. Ei henkilönimiä eikä tarkkoja käyttöoikeuslistoja — tarkoitus on, että vastuualue pysyy näkyvissä vaikka henkilö vaihtuisi.

## Roolimatriisi

| Rooli | Vastuualue | Keskeiset resurssit | Sensitiivisyys |
|---|---|---|---|
| Discord-ylläpito ja bot-vastuu | Botit, tervetuloviestit, kanavat, oikeudet, palvelimen peruskonfiguraatio | Carl-botti, tervetuloa-automaatio, Discord-kanavat | private |
| Sesh- ja tapahtumakalenterivastuu | Sesh-premium, tapahtumasarjat, eventit, ilmoittautumisroolit | Sesh, eventkalenteri, Discord-eventit | private |
| Discord- ja alustaoikeuksien hallinta | Admin-, ban-, Zwift Club owner-, ZwiftPower admin- ja muut alustaoikeudet | Discord, Zwift Club, ZwiftPower, domainit | private |
| Kilpailujärjestäjä | Ilmoittautumiset, säännöt, reitit, kilpailutilaukset, tulokset | Zwift-eventit, ZwiftPower, taulukot | internal |
| Viestintä- ja somevastuu | Jäsenhankinta, some, uutiskirjeet, kanavakuvaukset, ulkoinen näkyvyys | Instagram, Facebook, YouTube, ZwiftPower-kuvaus | internal |
| Striimi- ja mediaresurssien vastuu | Kisastreamit, koosteet, someklipit, tallenteet | streamit, tallenteet, somekanavat | internal |
| Seuravaatekoordinaatio | Toimittajayhteys, designit, samplet, tuotteet, tilausohjeet | Moomoo, tilauslomakkeet, designit | internal |
| Tili- ja automaatio-omistajuus | Yhteiskäyttötilit, palautusoikeudet, lomakkeet, skriptit | sähköpostit, Google Forms, Sheets, automaatiot | private |

Sama henkilö voi hoitaa useita rooleja pienessä seurassa, mutta vastuu kannattaa silti kuvata roolitasolla — se tekee näkyväksi, missä yhden henkilön poissaolo on riski.

## Käytännön huomiot rooleittain

- **Discord-ylläpito**: kattaa myös sen, kuka tarkistaa massa-pingausoikeudet ja hyväksyy kanavarakenteen muutokset. Konkreettinen tilanne (2025-11): kaikilla jäsenillä on tällä hetkellä oikeus massapingaukseen — ei ole vielä kenenkään korjaama, ks. [Discordin toimintamalli](discord_operating_model.md#ilmoitukset-ja-pingaukset). Rooliin on kuulunut myös botin (Carl-bot) alkuperäinen käyttöönotto ja tervetuloviestin automatisointi.
- **Sesh-vastuu**: kattaa premium-maksutavan ja sen, kuka saa luoda Sesh-eventtejä (käytännössä kuka tahansa jäsen, ei vain admin). Premium-tilaus on sidottu yhteen Discord-tiliin ja palvelimeen kirjautumisen kautta, joten maksavan jäsenen vaihtuessa uusi tilaus pitää hankkia ja aktivoida koordinoidusti ennen kuin vanha tilaus vanhenee — ei automaattista siirtoa (ks. [resurssi-inventaario](resource_inventory.md#kalenterit-ja-tapahtumahallinta)).
- **Alustaoikeuksien hallinta**: kriittisimmät oikeudet tarvitsevat varahenkilön, ja niille pitää olla poistoprosessi kun henkilö jää pois aktiivitoiminnasta. Havaittu käytäntö, joka on toiminut hyvin: admin-oikeuksia (esim. Zwift Club moderator -status) on tietoisesti jaettu useammalle aktiiviselle jäsenelle sen sijaan että ne pidettäisiin harvoilla — perusteluna, ettei kaiken toiminnan (esim. Club-eventtien luominen) tarvitse olla kiinni vain admineista.
- **Kilpailujärjestäjä**: ei ole vain eventin tilaaja — rooliin kuuluu myös säännöt, kategoriat, tulokset, vastapuolten kontaktointi ja jälkidokumentointi. Tähän kuuluu myös ZwiftPowerin League-työkalu, jolla RCF Cupin pisteytys hoidetaan — oikeudet siihen ovat tällä hetkellä yhden henkilön tilin varassa, ei jaettu roolina (ks. [kilpailutoiminnan prosessi](../TAPAHTUMAT/competition_process_rcf_cup.md#zwiftpowerin-league-tyokalu-pisteytyksen-kaytannon-hallinta)). Kansainvälisen haastekisan (RCF vs SZR) jälkeen tunnistettiin konkreettinen tarve pilkkoa tämä rooli useammaksi nimetyksi osaksi seuraavalla kerralla: omien osallistujien organisointi, yhdyshenkilö vastapuolen joukkueeseen, Zwift-eventtien tekninen tilaus, sekä striimin/somenäkyvyyden synkkaus tapahtuman kanssa — yhden henkilön varassa koko prosessi on raskas ja altis unohduksille.
- **Viestintävastuu**: kattaa myös sen, ettei jäsenpolku jää liian kilpailukeskeiseksi — aloittelija- ja matalan kynnyksen viestintä kuuluu tähän rooliin. Käytännössä rooliin on kuulunut myös maksetun somenäkyvyyden hallinta (esim. Instagram-mainosbudjetin siirto vastuuhenkilön "lompakkoon" ja kuittien kerääminen kirjanpitoa varten) sekä Meta Business Suiten kautta tehtävä tilien admin-hallinta.
- **Striimi- ja mediaresurssien vastuu**: usein pitkään täysin vapaaehtoispohjainen ja omakustanteinen rooli. Konkreettinen ennakkotapaus resursoinnista: seura korvasi vapaaehtoisen striimaajan laitehankintoja n. 350€ edestä (2025-12) — hyvä malli sille, että roolia kannattaa tukea rahallisesti, ei vain kiittää siitä.

## Seuraava askel

`content/catalog/people_roles.md` täydennetään näillä roolinimillä, kun ylläpito nimeää omistajat ja varahenkilöt. Julkaistaviin dokumentteihin viedään aina roolinimi, ei henkilönimeä.
