---
gold_id: event_playbook_rcf_team_race
wiki_category: TAPAHTUMAT
related_gold_docs:
  - competition_process_rcf_cup
  - how_to_run_rcf_team_race
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-15
---

# RCF-joukkuekisa — tasajoukkueiden sisäinen playbook

Oma formaatti — ei RCF Cup, ei WTRL TTT, ei seurojen välinen RCF vs SZR -haaste. RCF:n omat osallistujat jaetaan mahdollisimman tasavahvoihin joukkueisiin, ja joukkueet ajavat toisiaan vastaan yhdessä Zwift-kisassa.

## Konsepti

Kerää riittävä määrä osallistujia, jaa kahteen suunnilleen tasavahvaan joukkueeseen, aja kisa. Voittaja ratkeaa maaliintulojärjestykseen perustuvilla pisteillä. Formaatti on kevyt ja yhteisöllinen verrattuna cupiin — ei vaadi monen viikon sarjaa, ulkoista vastustajaa tai laajaa pistetaulukkoa. Arvo syntyy tasaisesta joukkuejaosta, taktiikasta ja siitä, että eri tasoiset kuskit voivat vaikuttaa saman joukkueen tulokseen.

## Perusformaatti

- yksi RCF:n sisäinen Zwift-kisa, kaksi tasavahvaa joukkuetta
- osallistujia mieluiten yli kymmenen, pienempikin määrä käy jos joukkueet saadaan tasattua mielekkäästi
- yksi yhteinen reitti, pisteet maaliintulojärjestyksestä
- pariton osallistujamäärä ratkaistaan vahvuuksien, pisteytyksen tai järjestäjän päätöksen mukaan
- joukkueiden ei tarvitse olla pysyviä — formaatti voidaan toistaa eri kokoonpanoilla

## Joukkuejako

Apuna: osallistujien ilmoittamat vauhtikategoriat, Racing Score-/ZRS-tieto, aiempi osallistumishistoria, järjestäjän arvio. Henkilökohtaisia tasotietoja ei julkaista — ne ovat lyhytikäistä järjestelydataa.

1. Kerää osallistujat ja tasotiedot.
2. Järjestä kuskit alustavasti vahvuuden mukaan.
3. Jaa kahteen joukkueeseen niin että arvioitu kokonaisvahvuus on lähellä toisiaan.
4. Tarkista, ettei toinen joukkue saa kaikkia saman ajotyypin vahvuuksia (kirimiehet, mäkikuskit).
5. Päätä parittoman osallistujamäärän käsittely ennen julkaisua.
6. Julkaise joukkueet vain siinä kanavassa/threadissa missä niitä tarvitaan.

## Pisteytys

Perusmalli: ensimmäinen saa eniten pisteitä, pisteet laskevat sijoitus sijoitukselta, jokainen maaliin ajanut tuo joukkueelleen pisteitä, joukkueen kokonaispisteet ratkaisevat. Jos osallistujia on pariton määrä tai joukkue menettää kuskin ennen starttia, järjestäjä päättää ennen lähtöä: lasketaanko kaikki, rajataanko pisteyttävien määrä, vai käytetäänkö muuta tasoitusta.

## Taktinen elementti

Toimii parhaiten kun joukkueilla on oma neuvottelupaikka (puhekanava, ajopaidat, tms). Taktiset kanavat ovat operatiivista, lyhytikäistä sisältöä eikä niiden sisältöä tuoda tähän dokumenttiin — kisan jälkeen ne poistetaan tai arkistoidaan sovitun toimintamallin mukaan.

## Järjestämisprosessi

1. Päätä että ajetaan joukkuekisa, ei cup-formaatti.
2. Varmista alustava osallistujamäärä.
3. Sovi päivä ja kellonaika.
4. Valitse reitti, joka tukee joukkuetaktiikkaa.
5. Päätä pisteytys ja parittoman määrän käsittely.
6. Luo tai tilaa RCF Club -event.
7. Avaa Discord-thread.
8. Kerää osallistujien tasotiedot.
9. Tee joukkuejako, tarkista tasaisuus.
10. Julkaise joukkueet, ajopaidat, puhekanavat, pisteytys.
11. Aja kisa, kerää tulokset.
12. Laske joukkuepisteet, julkaise voittajajoukkue.
13. Kirjaa opit seuraavaa kertaa varten.

Askel-askeleelta-versio: [how_to_run_rcf_team_race.md](../ORGANIZER_CHECKLISTS/how_to_run_rcf_team_race.md).

## Vakiintuneet nimeämiskäytännöt ja työkalut

Nämä ovat toistuneet samanlaisina useammassa toteutuksessa, joten kannattaa käyttää samaa mallia jatkossakin sen sijaan että keksitään uudestaan joka kerta:

- **Ajankohta**: Sesh-äänestys (Time Finder) RCF:n palvelimella — kuka tahansa voi luoda äänestyksen, ei vaadi admin-oikeuksia.
- **Ilmoittautuminen**: Zwift-eventin oma osallistujalista (companion-appista tai zwift.comista), ei erillinen lomake.
- **Joukkuekanavat**: yksityiset Discord-kanavat nimillä **"a-tiimi"** ja **"b-tiimi"** taktiikan suunnitteluun. Vanha kanava poistetaan ja luodaan uudestaan tyhjänä joka kisakertaa varten — keskusteluhistoria on siis tarkoituksella katoavaa, ei arkistoitavaa.
- **Paidat**: joukkue A käyttää Zwiftin Basic1-paitaa, joukkue B Basic2-paitaa (kolmannelle joukkueelle on käytetty Basic3:a). Paita vaihdetaan _ennen_ eventtiin liittymistä — muuten vaihto ei näy muille osallistujille (tunnettu Zwift-bugi).
- **Radiokanavat**: joukkueen omat äänikanavat, nimetty kaavalla `kat-a-kisaradio` / `kat-b-kisaradio`.
- **Joukkuejako**: tasataan ZRS-pisteiden ja vauhtikategorian mukaan. Käytännössä jako on tehty tekoälyavusteisesti (esim. pyytämällä kielimallilta ehdotus annetulla osallistujalistalla ja ZRS-pisteillä), minkä jälkeen ehdotusta on vielä säädetty käsin muutaman kuskin verran, jos ajotyyli (esim. montako saman kategorian mäkikuskia samassa joukkueessa) sitä vaatii. Pelkkä ZRS ei aina anna oikeaa kuvaa yksittäisestä kuskista, joten viimeinen tasapainotus kannattaa tehdä ihmisarviolla.
- **Pisteiden laskenta**: kisapäivän tulos lasketaan valmiilla Google Sheets -laskurilla (maaliintulojärjestys → pisteet, käyttöohje laskurin sisällä). Sama pohja soveltuu myös taktiikan ennakkosuunnitteluun ennen kisaa.
- **Kausittainen pistelista**: yksittäisten kisojen lisäksi on pidetty yllä kevyttä, hauskuuteen tähtäävää kausipistelistaa (Sheets), johon on jaettu myös "erikoispisteitä" hyvistä suorituksista kisan ulkopuolella (esim. hauska keskeytys) — tarkoituksella ei täysin ennustettava, jotta hupi säilyy.

## Esimerkkipolku: viikoittainen sarja (loka-marraskuu 2025)

Näin yksi konkreettinen kolmen viikon sarja eteni käytännössä — hyvä referenssi sille, missä tahdissa asiat oikeasti tapahtuvat:

- **Maanantai/tiistai**: Sesh-äänestys avataan seuraavien 1-2 viikonlopun ajoista. Ensimmäisellä kerralla kaksi vaihtoehtoista päivää testattiin rinnakkain, koska äänet jakautuivat.
- **Ilmoittautumisen kertymä**: osallistujamäärä kasvoi tasaisesti läpi viikon — 14 hlöä keskiviikkona, 17 perjantaina, ja lopullinen määrä vasta lauantaiaamuna kun viime hetken ilmoittautumisia ja perumisia vielä tuli. Tästä syntyi käytännön nyrkkisääntö osallistujamäärän kasvaessa: **noin 20 varmaa osallistujaa on raja, jonka jälkeen kannattaa harkita kahden joukkueen sijaan kolmea** — alle sen 3 joukkuetta johtaa liian suuriin tasoeroihin joukkueiden sisällä, ja 2 joukkuetta antaa selkeämmän taktisen asetelman.
- **Joukkueiden lukitseminen**: jako julkaistiin ja lukittiin torstai-iltana (2-3 päivää ennen kisaa), mutta jätettiin tarkoituksella vielä muutettavaksi perjantaihin asti epävarmojen ilmoittautumisten takia. Käytännössä lukitseminen vahvistettiin nopealla emoji-äänestyksellä kanavalla.
- **Kisapäivä**: paidat ja puhekanava sovittiin viestillä juuri ennen lähtöä ("Basic 1 päälle", "kympiltä startti"), koska tarkkaa erillistä pääviestipohjaa ei ole — tämä on yksi asia, jonka voisi jatkossa vakioida.
- **Tulos**: julkaistiin heti kisan jälkeen laskurin ja ZwiftPower-tulosten pohjalta, tarkennettuna kun ZwiftPower päivittyi (viive muutamia minuutteja - tunteja).
- **Formaatin elää mukana**: kolmannella viikolla osa osallistujista muodosti orgaanisesti oman kolmannen "alueellisen" joukkueen suurten osallistujamäärien takia — järjestäjä hyväksyi tämän kevyesti sen sijaan että pakotti alkuperäiseen kaksijakoon, ja teki jaon molemmilla vaihtoehdoilla (2 vs. 3 joukkuetta) nähtäväksi ennen lopullista päätöstä.

## Roolit

Tapahtumaomistaja, eventtivastaava, joukkuejakovastaava, viestintävastaava, taktiikkakanavavastaava, tulosvastaava. Pienessä kisassa sama henkilö voi hoitaa useita, mutta joukkuejako ja pisteytys kannattaa nimetä eksplisiittisesti.

## Tietosuoja

Tähän dokumenttiin ei nosteta osallistujien henkilökohtaisia tasopisteitä, rosteririvejä, taktisten kanavien sisältöä, vanhoja event-linkkejä eikä yksityisten kanavien nimiä. Joukkuejaon laskentataulukko käsitellään linkkirekisterissä, ei tässä.

## Avoinna

- Vahvistettu minimiosallistujamäärä, jolla kisa kannattaa ajaa.
- Käytetäänkö pisteytyksessä aina kaikkia maaliintulijoita vai rajattua määrää per joukkue.
- Kuka saa luoda RCF Club -eventtejä.
- Voidaanko tästä myöhemmin tehdä jäsenille näkyvä kevennetty ohje.
