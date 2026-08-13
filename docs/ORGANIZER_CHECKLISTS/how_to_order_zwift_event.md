---
gold_id: how_to_order_zwift_event
wiki_category: ORGANIZER_CHECKLISTS
related_gold_docs:
  - how_to_run_rcf_cup
  - competition_process_rcf_cup
  - event_organizing_patterns
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-13
source: sähköpostikirjeenvaihto events@zwift.com, elo-lokakuu 2025 (Ride Club Finland: Nordic Pace)
---

# Zwift-eventin tilaaminen Zwiftiltä

Miten RCF tilaa uuden julkisen Zwift-ryhmäajon tai -eventtisarjan suoraan Zwiftin tapahtumatiimiltä. Tämä on ollut avoin kysymys useassa muussa dokumentissa ("nykyinen tekninen tapa luoda/tilata Zwift-eventit") — tässä on todellinen, toteutunut prosessi yhdestä päästä toiseen.

## Kanava

Kaikki tilaukset, muutokset ja poistot hoidetaan sähköpostitse osoitteeseen **events@zwift.com**. Ei erillistä nettilomaketta tai itsepalveluportaalia julkisille eventeille — pyyntö on tavallinen sähköposti, jonka Zwift reitittää sisäisesti oikealle henkilölle.

Vastaaja vaihtuu vaiheen mukaan: ensimmäinen viesti on usein pelkkä kuittaus ("välitän tämän oikealle tiimille"), varsinaisen aikataulutuksen tekee eri henkilö, ja poistopyyntöön voi vastata vielä kolmas. Tämä on normaalia — vastaa aina samaan sähköpostiketjuun, ei uuteen viestiin.

## 1. Lähetä tilauspyyntö

Sähköposti osoitteeseen events@zwift.com, jossa kerrotaan vähintään:

- **Series Name** — sarjan nimi sellaisena kuin sen halutaan näkyvän Zwiftissä (esim. "Ride Club Finland: Nordic Pace")
- **Format** — toistuvuus ja viikonpäivä (esim. "Weekly Saturday group rides")
- **Duration** — aikaväli ja eventtien kokonaismäärä (esim. "September 2025 - March 2026, 30 events total")
- **Target Audience** — kenelle ajo on suunnattu (esim. W/kg-haarukka, kesto, taso)
- **Key Feature** — erityisasetukset, esim. Double Draft päällä/pois

Liitteeksi tarvitaan Zwiftin oma **Event Request Form** -Excel-lomake (esiintyi tiedostonimellä `Zwift Events.xlsx`). Tämä on sama lomake, joka on mainittu [resurssi-inventaariossa](../YLLAPITO/resource_inventory.md) kilpailutoiminnan tilaus-Excelinä — ilman täytettyä lomaketta tilausta ei käsitellä.

## 2. Odota ja vastaa ajankohtakeskusteluun

Vastaanotto vahvistetaan yleensä saman tai seuraavan päivän aikana, mutta varsinainen aikataulutus voi kestää päivän tai pari.

Jos pyydetty kellonaika ei ole vapaana julkisessa kalenterissa, Zwift ehdottaa lähimpiä vapaita aikoja (esimerkkitapauksessa pyydetty la 7:00 UTC ei ollut vapaana → tarjolla 6:30 tai 7:45 UTC). Vaihtoehtona Zwift tarjosi myös alkuperäisen ajan **club-eventtinä** julkisen sijaan, jos kellonaika on tärkeämpi kuin julkinen näkyvyys.

## 3. Vahvista aika ja kysy toistuvuudesta

Kun aika sovitaan, kysy samalla suoraan: tilataanko jokainen kerta erikseen, vai luodaanko yksi toistuva pohja? Kannattaa kysyä heti — RCF:n tapauksessa vastaus oli, että **yksi tilaus riittää koko sarjalle**, joten toistuvia eventtejä ei tarvitse tilata uudestaan viikoittain.

## 4. Näin toistuvuus toimii käytännössä

Zwift lähettää linkin ensimmäiseen eventtiin (`zwift.com/events/view/...`). Sen jälkeen:

- Event **julkaisee itsensä automaattisesti seuraavalle viikolle 24 tuntia sen jälkeen, kun edellinen kerta on ajettu**.
- Reitin ja muut muokattavat asetukset voi itse vaihtaa jokaista tulevaa kertaa varten **Companion Appin** kautta.
- Jos jokin muutos ei onnistu itse Companion Appista, se pyydetään erikseen sähköpostilla events@zwift.com:iin.

## 5. Eventin tai koko sarjan lopettaminen

Jos osallistujia on liian vähän tai sarja halutaan lopettaa:

1. Lähetä sähköposti events@zwift.com:iin ja pyydä **sekä** eventin poistoa **että** sen toistumisen lopettamista nimenomaisesti. Pelkkä poistopyyntö ei riitä, jos toistuva julkaisumekanismi (kohta 4) on päällä.
2. Zwift pyytää varmistamaan oikean eventin tunnisteen/linkin ennen poistoa, koska **poisto on peruuttamaton**.
3. Vahvista oikea event-linkki. Zwift poistaa eventin ja vahvistaa poiston sähköpostitse.

## Avoinna

- Kuinka pitkälle etukäteen uusi sarja kannattaa tilata Zwiftiltä (toteutuneessa tapauksessa pyyntö lähti n. 2 viikkoa ennen ensimmäistä ajoa).
- Onko `Zwift Events.xlsx` -lomakkeen nykyinen versio tallessa ja kenellä on siihen pääsy — ks. [resurssi-inventaario](../YLLAPITO/resource_inventory.md).
- Kuka RCF:ssä saa lähettää tilaus-/poistopyyntöjä events@zwift.com:iin — tähän asti prosessi on kulkenut yhden henkilön sähköpostin kautta, ei jaetun/roolipohjaisen osoitteen.
- Toimiiko sama prosessi myös RCF Club -eventeille (esim. joukkuekisat), vai onko niillä oma, kevyempi tilaustapa suoraan Zwift Club -hallintapaneelin kautta.
