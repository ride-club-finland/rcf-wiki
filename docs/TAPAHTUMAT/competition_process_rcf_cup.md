---
gold_id: competition_process_rcf_cup
wiki_category: TAPAHTUMAT
related_gold_docs:
  - event_playbook_rcf_team_race
  - how_to_run_rcf_cup
  - how_to_run_wtrl_ttt
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-15
---

# RCF Cup ja kilpailutoiminnan prosessi

RCF:n kilpailutoiminta jakautuu useaan formaattiin, jotka sekoittuvat helposti keskenään jos niitä ei erota selvästi:

- **RCF Cup** — RCF:n oma sarja-/cup-muotoinen kilpailu
- **RCF-joukkuekisa** — RCF:n sisäinen joukkueformaatti, ks. [oma playbook](event_playbook_rcf_team_race.md)
- **WTRL TTT** — ulkoisen alustan tiimikisa, jossa RCF vain kokoaa joukkueen
- **TalviCup ja muut ulkoiset sarjat** — RCF ei omista sarjan virallista tietoa

## RCF Cup

Tammikuun 2026 malli on käyttökelpoinen sarjapohja:

- viiden viikon Zwift-kisasarja, voi ajaa yksittäisiä kisoja tai koko cupin
- loppupisteisiin lasketaan neljä parasta tulosta
- DNF/DNS = nolla pistettä, kaikki maaliin tulleet saavat pisteitä
- tulokset ZwiftPowerissa ja Discordissa, tasapisteille erillinen ratkaisutapa

Suositus: käytä pistepohjaista kokonaiskilpailua jos halutaan sallia yhden osakilpailun väliin jättäminen; päätä etukäteen lasketaanko kategoriat yhdessä vai erikseen; kirjaa pisteasteikko ja tasapistesäännöt pääilmoitukseen; julkaise tulospaikka ennen ensimmäistä osakilpailua. Ks. valmis [pääviestipohja](../ORGANIZER_CHECKLISTS/templates/rcf_cup_announcement_template.md).

Stage-linkit ovat väliaikainen tiedotusratkaisu, ei pysyvä dokumentointi — yksittäiset linkit saavat olla Discordissa, mutta niitä ei viedä tähän dokumenttiin.

Zwiftissä on kuitenkin yksi pysyvä, uudelleenkäytettävä linkkityyppi: **tapahtumatagi**. RCF Cupin eventit on merkitty tagilla `rcfcup`, jolloin `zwift.com/uk/events/tag/rcfcup` näyttää aina kaikki sarjan tulevat eventit yhdellä pysyvällä linkillä — ei tarvitse jakaa yksittäisiä stage-linkkejä uudelleen joka viikko. Sama malli on käytössä myös muissa toistuvissa RCF-sarjoissa: `tag/rcfkuutar` (naisten kisasarja) ja `tag/rcfcategoryspotlight` (viikoittainen matalan kynnyksen kisa). Ks. [resurssi-inventaario](../YLLAPITO/resource_inventory.md#pysyvat-linkit-ja-tunnisteet).

### ZwiftPowerin League-työkalu — pisteytyksen käytännön hallinta

RCF Cupin pisteytystä ei lasketa käsin taulukkoon, vaan ZwiftPowerin **League**-työkalulla:

- Työkalulla luodaan liiga (osoitteessa `zwiftpower.com/league.php?id=...`), johon osakilpailujen tulokset kootaan automaattisesti ZwiftPowerin kisatuloksista valitun pistemallin mukaan.
- Liiganäkymä päivittyy, kun järjestäjä vahvistaa kunkin osakilpailun (stagen) jälkeen — tammikuun 2026 RCF Cupissa pistetilanne julkaistiin `rcf-cup`-kanavalle samalla liigalinkillä jokaisen stagen jälkeen.
- Työkalulla voi myös poistaa yksittäisiä tuloksia tuloslistalta manuaalisesti, jos virhe tai väärinkäytös pitää korjata.

**Miten oikeudet saadaan:** League-työkalu ei ole automaattisesti kaikkien käytössä. Oikeudet myöntää ZwiftPower itse omalla League-pyyntölomakkeellaan (täytetään suoraan ZwiftPowerin sivulla) — pyyntö ei kulje RCF:n Discord-roolien tai -adminoikeuksien kautta, vaan on kokonaan ZwiftPoweriin sidottu, henkilökohtainen tilioikeus. Nykyinen RCF Cupin liiga-admin haki ja sai oikeutensa elokuussa 2025 tätä lomaketta kautta.

**Riski:** oikeudet ovat juuri nyt yhden henkilön ZwiftPower-tilin varassa, ei jaettu roolina eikä varahenkilölle. Jos tili menetetään tai henkilö lopettaa aktiivitoiminnan, joku toinen joutuu hakemaan League-oikeudet uudestaan samalla lomakkeella omalle tililleen ennen kuin seuraavan Cupin pisteytystä voi jatkaa samalla tavalla. Ks. [roolit ja vastuut](../YLLAPITO/roles_and_responsibilities.md) ja [resurssi-inventaario](../YLLAPITO/resource_inventory.md).

## RCF-joukkuekisat

Ero RCF Cupiin: joukkuekisassa osallistujat jaetaan järjestäjän toimesta kahteen tasaväkiseen joukkueeseen, ja pisteet lasketaan maaliintulojärjestyksestä — ei yksilön sarjasijoituksesta. Voi ajaa yksittäisenä iltana ilman sarjarakennetta.

Järjestämisvaiheet: sovi päivä ja kellonaika, valitse rata, luo RCF Club -event, avaa keskusteluthread, kerää osallistujien vauhtikategoria ja tarvittavat kilpailupisteet, jaa joukkueet tasaväkisesti, tarvittaessa luo yksityiset taktiikkakanavat, sovi ajopaidat ja radiokanavat, laske pisteet sovitulla laskurilla.

Tietosuoja: ZRS-pisteitä, privaattikanavia, taktisia keskusteluja ja henkilökohtaisia osallistumistietoja ei nosteta julkaistaviin dokumentteihin — vain prosessi ja roolit. Täysi playbook: [event_playbook_rcf_team_race.md](event_playbook_rcf_team_race.md).

## WTRL TTT

RCF kokoaa joukkueita WTRL:n omiin tapahtumiin — tämä ei ole sama prosessi kuin RCF:n oma club-event.

Pysyvät elementit: joukkueen koko 3-8 ajajaa, Race Pass ilmoittautumislinkkinä (ei viedä Goldiin/wikiin), joukkue voi olla sekajoukkue, Coffee Class määräytyy WTRL:n logiikalla, kokoonpano voi vaihtua viikoittain.

**Konkreettinen sääntö, joka on toistuvasti aiheuttanut kysymyksiä**: joukkueen aika lasketaan tietyn kuskin maalintulosta — jos joukkueessa on 5-8 ajajaa, ajaksi lasketaan neljännen maaliin tulleen aika; jos 3-4 ajajaa, kolmannen aika. Sekajoukkueessa saa olla korkeintaan 3 A-, B- tai C-kategorian ajajaa; D-kategorian ajajien määrää ei ole rajattu. Joukkueen lopullinen Coffee Class -luokka (esim. Frappe) määräytyy automaattisesti kisan jälkeen korkeimman mukana olleen kategorian perusteella, ei ilmoittautumisvaiheen arviosta — tämä on hämmentänyt järjestäjiäkin ("en mä mitään ymmärrä, toivottavasti joku tästä jotain tietää"), joten se kannattaa selittää osallistujille etukäteen sen sijaan että selvitetään kisan jälkeen. Käytännössä ajopaidaksi on vakiintunut Zwiftin Basic3, ja ilmoittautuminen hoidetaan reagoimalla kanavan Sesh-tapahtumaan ja sen jälkeen leimaamalla RacePass ennen kisan alkua.

Käytännön ohje: [how_to_run_wtrl_ttt.md](../ORGANIZER_CHECKLISTS/how_to_run_wtrl_ttt.md).

## TalviCup ja ulkoiset sarjat

TalviCup-kanavissa RCF ei omista sarjan virallista tietoa — kanavat ovat tiedonvälitys- ja keskustelupaikka, viralliset tiedot ovat ulkoisilla lähteillä. Älä kopioi ulkoista sarjadokumentaatiota pysyväksi RCF-ohjeeksi. Kausikanavat arkistoidaan historiallisina kun ne eivät enää ohjaa aktiivista toimintaa.

TalviCupin *tuleva* muoto (esim. talvikausi 2026-2027 -yhteistyö muiden seurojen kanssa) on tällä hetkellä kesken oleva keskustelu — se jää tarkoituksella Discordiin kunnes se on oikeasti päätetty, ks. [wiki-päätös](../meta/wiki_decision.md).

## Historialliset rosterit ja taulukot

Vanhoja pinned-taulukoita voi käyttää prosessihistorian ymmärtämiseen, mutta niitä ei julkaista sellaisenaan. Henkilölistat pysyvät admin-review-tasolla; taulukoista nostetaan tähän vain prosessirakenne (kalenteri, osakilpailut, kategoriat, ilmoittautumistapa).

## Esimerkkipolku: tammikuun 2026 Cup

Konkreettinen läpivienti yhdestä toteutuneesta sarjasta, jotta "päätä pisteytys, DNF/DNS-sääntö, tasapistesääntö" -ohje muuttuu kokemukseksi eikä pelkäksi checklist-riviksi:

- **3.12.2025 (n. 4 viikkoa ennen)**: pääviesti julkaistiin heti täydellisenä — sarjan kesto (5 osakilpailua, lauantaisin 3.1.-31.1.2026), pisteytysmalli (4 parasta 5:stä lasketaan loppupisteisiin), DNF/DNS = 0 pistettä, sekä koko pisteasteikko (1. = 50, 2. = 46, 3. = 43 … sija 20 = 7, sijat 21-40 = 5, 41+ = 3) ja tasapistesääntö (paras yksittäinen sijoitus ratkaisee, sitten seuraavaksi paras, viimeisenä viimeisen kisan tulos). Tämä sama pisteasteikko on käytössä myös Kruunajaisten etappiformaatissa (ks. [Kruunajaiset-playbook](event_playbook_kruunajaiset.md)) — kannattaa pitää yhtenä vakiotaulukkona koko RCF:n kisatoiminnassa.
- **Osallistujamäärän kasvu viikon sisällä**: ensimmäistä stagea edeltävänä päivänä ilmoittautuneita oli 58; järjestäjä arvioi määrän nousevan yli sadan seuraavaan aamuun mennessä, koska osa osallistujista on "drop-on"-kuskeja, jotka ajavat vain yhden osakilpailun täydestä sarjasta huolimatta.
- **Kategoriasääntö, joka kannattaa kertoa etukäteen**: jos osallistuja vaihtaa kategoriaa kesken sarjan, kertyneet pisteet **eivät** siirry mukana — ne nollautuvat ja alkavat kasvamaan alusta uudessa kategoriassa. Tämä on tullut esiin osallistujakysymyksenä joka kaudella, joten se kannattaa mainita jo pääviestissä.
- **Pistetilanne julkaistiin ZwiftPowerin League-linkillä** jokaisen stagen jälkeen samalla kanavalla (ks. [League-työkalu](#zwiftpowerin-league-tyokalu-pisteytyksen-kaytannon-hallinta)) — ei erillistä taulukkoa käsin ylläpidettynä.
- **Yksi tekninen keskeytys**: yhden osallistujan kisa keskeytyi kesken stagen laitevian takia (traineri rikkoutui kesken ajon) — tämä käsiteltiin tavallisena DNF:nä ilman erillistä poikkeusta, koska sääntö oli jo etukäteen selkeä.
- **Sarjan päätös**: tulokset viimeisen stagen jälkeen julkaistiin samalla League-linkillä, ja kanavalle jäi kiitosviesti sekä lyhyt yhteenveto osallistujilta — ei erillistä koostedokumenttia, koska League-näkymä toimii sellaisenaan lopullisena arkistona niin kauan kuin liiga pysyy ZwiftPowerissa.

## Osallistujamäärä ja ajoitus

Toistuva riski: omat viikkokisat ja RCF Cup jäävät osallistujamääriltään pieniksi jos ajoitus kilpailee muiden sarjojen (ZRL, laddereiden) tai arjen kanssa. Testaa aikaikkuna ennen uuden cupin käynnistämistä (esim. Sesh-äänestyksellä), ja suunnittele sarja niin ettei yksi väliin jäänyt osakilpailu poista motivaatiota.

## Yhteinen kilpailuprosessin runko

Kaikille RCF:n omille kilpailuille sama perusrunko: 1) päätä tavoite (cup / yksittäinen kisa / joukkuekilpailu / ulkoinen sarja) 2) päätä omistaja 3) päätä formaatti 4) päätä aikataulu 5) päätä ilmoittautuminen 6) päätä tulospaikka 7) päätä tietosuojarajaus 8) julkaise ja pidä pääviesti ajan tasalla 9) arkistoi linkit, tulokset ja opit sarjan jälkeen.
