---
gold_id: how_to_run_rcf_team_race
wiki_category: ORGANIZER_CHECKLISTS
related_gold_docs: [event_playbook_rcf_team_race, competition_process_rcf_cup]
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-15
---

# RCF-joukkuekisan järjestäjäohje

Käytännön versio [RCF-joukkuekisa-playbookista](../TAPAHTUMAT/event_playbook_rcf_team_race.md).

## Ennen

1. Päätä että järjestetään RCF:n sisäinen joukkuekisa.
2. Varmista alustava osallistujamäärä (tavoite yli kymmenen, pienempikin käy jos joukkueet tasataan järkevästi). **Nyrkkisääntö**: 2 joukkuetta toimii pienemmällä porukalla, mutta noin 20 varman osallistujan jälkeen kannattaa harkita 3 joukkuetta — muuten yksi joukkue kasvaa liian isoksi ja tasoerot sen sisällä kasvavat.
3. Avaa ajankohta-äänestys [Sesh Time Finderilla](https://www.sesh.fyi/dashboard) RCF:n palvelimelle — kuka tahansa voi luoda äänestyksen, ei vaadi admin-oikeuksia.
4. Valitse rata, joka sopii joukkuekilpailun ideaan.
5. Päätä pisteytys (perusmalli: maaliintulojärjestys, ks. valmis Google Sheets -laskuri linkkirekisterissä).
6. Päätä kuka luo/tilaa eventin, kuka tekee joukkuejaon, kuka laskee tulokset.

## Julkaisu

1. Luo RCF Club -tapahtuma (admin luo Companionissa) ja lisää se ZwiftPoweriin RCF:n private-event-työkalulla, jotta tulokset rekisteröityvät. Jaa event-linkki kanavalle.
2. Avaa Discord-thread ja kerro siinä: päivä, kellonaika, rata, ilmoittautumistapa, tarvittavat tiedot, joukkuejaon periaate, pisteiden laskentatapa. Pyydä osallistujia ilmoittamaan oma ZRS-piste ja vauhtikategoria threadissä — sama paikka sopii myös vastustajan nokitteluun ilman että se sotkee pääkanavaa.
3. Pyydä osallistujilta vain joukkuejaon kannalta välttämättömät tiedot — ei henkilöpohjaisia rosteririvejä pysyvään dokumenttiin.

## Viimeinen viikko

1. Kerää osallistujatiedot, tarkista vauhtitasot vain järjestelykäyttöön. Määritä ilmoittautumiselle takaraja, esim. kisaa edeltävä torstai-ilta, jotta joukkuejako ehditään tehdä ja vielä säätää perjantaihin mennessä.
2. Jaa osallistujat tasaväkisiin joukkueisiin ZRS-pisteiden ja vauhtikategorian perusteella (tekoälyavusteinen ehdotus + käsin tarkistus toimii hyvin, ks. [playbook](../TAPAHTUMAT/event_playbook_rcf_team_race.md#vakiintuneet-nimeamiskaytannot-ja-tyokalut)), päätä parittoman määrän tasaus. Lukitse jako nopealla äänestyksellä kanavalla.
3. Luo yksityiset taktiikkakanavat nimillä **a-tiimi** / **b-tiimi** (kolmannelle joukkueelle vastaava malli). Kerro ajopaidat (vakiokäytäntö: joukkue A = Zwiftin Basic1, joukkue B = Basic2, kolmas joukkue = Basic3 — vaihto _ennen_ eventtiin liittymistä, muuten muut eivät näe sitä) ja radiokanavat (kaava `kat-a-kisaradio` / `kat-b-kisaradio`).
4. Tarkista event-linkki ja tulosten laskentapohja.

## Tapahtumapäivä

1. Muistuta ajopaidasta ennen eventtiin liittymistä, ohjaa joukkueet puhekanaville.
2. Varmista että kaikki tietävät joukkueensa ja pisteytyksen periaatteen.
3. Anna hetki taktiikan sopimiseen, aja kisa, kerää tulokset heti maalin jälkeen.

## Tulokset

1. Laske pisteet maaliintulojärjestyksestä Google Sheets -laskurilla (ZwiftPowerin tulokset pohjana), tarkista mahdolliset poikkeukset. Odota tarvittaessa muutama minuutti - tunti, että ZwiftPower päivittyy täydellisesti.
2. Julkaise tulokset Discordissa ilman tarpeetonta henkilötietojen toistoa, kerro voittajajoukkue ja opit.
3. Vie linkit ja laskentapohjat linkkirekisteriin.

## Jälkihoito

1. Poista tai luo uudelleen tyhjinä väliaikaiset taktiset kanavat (a-tiimi/b-tiimi) — keskusteluhistoria on tarkoituksella katoavaa jokaisen kisan jälkeen.
2. Kirjaa toimiko joukkuejako ja pisteytys, oliko osallistujamäärä riittävä.
3. Kirjaa mitä muuttaa seuraavaan kertaan (rata, ajankohta, joukkuejako). Päivitä tätä checklistiä.

## Avoinna

- Kuka saa luoda RCF Club -eventtejä.
- Joukkuejaon laskentaskriptin/taulukon sijainti.
- Minimi osallistujamäärä, jolla kisa vielä kannattaa järjestää.
