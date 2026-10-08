---
gold_id: tietosuojaseloste
wiki_category: JASENPOLKU
related_gold_docs: [member_faq_and_onboarding, discord_operating_model]
publishability: public_candidate
status: luonnos
last_verified: 2026-10-08
---

# Tietosuojaseloste: Discord-yhteisö, viestintä ja automaatiot

Tämä seloste kertoo, miten Ride Club Finland käsittelee henkilötietoja Discord-yhteisössään, Instagramissa ja seuran viestinnässä, ja mihin tekoälyä käytetään. Seloste perustuu EU:n tietosuoja-asetuksen (GDPR) artikloihin 13 ja 14.

Päivitetty 8.10.2026.

## Rekisterinpitäjä ja yhteystiedot

- **Rekisterinpitäjä:** [seuran virallinen nimi ja Y-tunnus]
- **Yhteyshenkilö tietosuoja-asioissa:** [nimi tai rooli, sähköpostiosoite]
- Discordissa voit ottaa yhteyttä myös ylläpitoon yksityisviestillä.

## Lyhyesti

- Seura kokoaa Discordin yhteisökanavien keskusteluista viikoittain **nimettömiä koosteita** tekoälyn avulla, jotta voimme kertoa tapahtumista ja osallistumisesta täsmällisemmin. Nimet ja maininnat poistetaan ennen tekoälykäsittelyä, ja viestit poistetaan heti käsittelyn jälkeen.
- Seuran Discord-botti laskee yhteisön tilastoja, hoitaa joukkuejaon ja tehtävätaulun ja välittää seuran Instagram-julkaisut Discordiin.
- Seura käyttää julkisia kisatuloksia tulospostauksissa ja kuukausittaisessa e-pyöräilyn katsauksessa.
- **Voit kieltäytyä** koosteista ja tulosnostoista milloin tahansa ilman perusteluja. Ks. kohta *Oikeutesi*.

## Mitä tietoja käsitellään ja miksi

| Käsittely | Tiedot | Tarkoitus | Missä tulos näkyy |
|---|---|---|---|
| **Viikkokoosteet** | Yhteisökanavien viestit, kirjoittajan näyttönimi ja Discord-tunniste, reaktiot. Nimet, maininnat, linkit ja yhteystiedot poistetaan ennen tekoälyä | Nimettömät kuvaukset siitä, mistä yhteisössä puhuttiin ja mitä on tulossa | Seuran WhatsApp-kanava ja kuukausipostaus #ilmoitukset-kanavalla, ihmisen hyväksynnän jälkeen. Koosteet säilytetään seuran yksityisessä arkistossa |
| **Yhteisön tilastot** (seuran pulssi, kuukausikooste) | Viestien, kirjoittajien ja jäsenten määrät kanavittain | Seuran toiminnan seuranta. Raporteissa ei ole nimiä eikä jäsenkohtaisia lukuja | Ylläpidon kanava #yhteisöpulssi |
| **Viikon parhaat palat** | Viikon eniten reaktioita saanut yhteisöviesti, sen kuva ja saman kanavan viikon keskustelu nimimerkkeineen | Ehdotus somevastaavalle Instagram-tarinaksi. Julkaistaan vain kirjoittajan luvalla | Ylläpidon kanava #some-materiaali |
| **Aktiiviehdokkaat** | Kahdeksan viikon aikana tasaisesti kirjoittaneet jäsenet, joilla ei ole aktiiviroolia | Henkilökohtainen kysymys vapaaehtoistehtävästä. Ei automaattisia päätöksiä | Yksityinen kanava #admin (enintään 15 ylläpitäjää) |
| **Tehtävätaulu** | #aktiiviksi-kanavan viestit, jotka alkavat sanalla `tehtävä:`, kirjoittajan nimi ja tunniste, tehtävien tekijät | Seuran tehtävien ja tekijöiden ylläpito | #aktiiviksi; kuukausikooste muutoksista #ilmoitukset-kanavalla hyväksynnän jälkeen |
| **Joukkuejako** | Viikkoviestin reaktiot ja joukkueroolit | Joukkuekisojen joukkueet. Joukkuekanavien viestit poistetaan viikoittain | #rcf-joukkuekisat ja joukkuekanavat |
| **Instagram-välitys ja tilastot** | Seuran omat julkaisut ja tarinat, julkisten tilien merkinnät seuran tilille (käyttäjänimi), tilin tilastot | Seuran julkaisut jäsenten nähtäville; seuran näkyvyyden seuranta | #somefeedi, #yhteisöpulssi |
| **Kisatulokset** | Julkiset MyWhoosh- ja Zwift-tulokset: nimi, sijoitus, aika, teho ja teho-painosuhde, joukkue, palkinnot. Sykettä, painoa ja ikää ei käytetä | Tulospostaukset, seuran tulostilastot ja kuukausittainen e-pyöräilyn katsaus Suomen Pyöräilyn sivuille | Seuran Instagram ja Discord; katsauksen pohjatiedot lähetetään Suomen Pyöräilyn somevastaavalle |

**Oikeusperuste** kaikissa käsittelyissä on seuran **oikeutettu etu** (GDPR 6 artiklan 1 kohdan f alakohta): seuran toiminnasta viestiminen, yhteisön kehittäminen ja kisatoiminnan esille tuominen. Arvioimme, että käsittely on jäsenten kannalta odotettavaa ja vähäistä, koska tiedot ovat jo seuran kanavilla tai julkisissa tuloslistoissa, nimet poistetaan ennen tekoälykäsittelyä ja jokaisesta käsittelystä voi kieltäytyä.

**Tietolähteet:** seuran Discord-palvelin (Ride Club Finland), seuran Instagram-tili ja MyWhooshin ja Zwiftin julkiset tulospalvelut. Kisatuloksissa voi olla myös muiden seurojen suomalaisia ajajia; heidän tietonsa tulevat julkisista tuloslistoista.

## Tekoälyn käyttö

- **Mihin:** viikkokoosteet, viikon parhaiden palojen tarinaehdotus, tehtävätaulun päivitys `tehtävä:`-viesteistä ja tehtävätaulun kuukausikooste, sekä MyWhooshin ja Zwiftin julkisten tiedotteiden tiivistelmät.
- **Palvelu:** OpenRouter, joka välittää pyynnön kielimallille (Anthropic Claude).
- **Mitä palveluun lähtee:** viikkokoosteissa yhteisökanavien viestit ilman nimiä, mainintoja, linkkejä ja yhteystietoja. Parhaissa paloissa ja tehtävätaulussa valitut viestit nimimerkkeineen.
- **Ihminen tarkistaa** jokaisen tekoälyn kirjoittaman tekstin ennen kuin se julkaistaan missään. Tekoäly ei tee päätöksiä kenestäkään.

## Vastaanottajat ja siirrot EU:n ulkopuolelle

| Palvelu | Rooli | Sijainti |
|---|---|---|
| Discord | Yhteisön alusta | Yhdysvallat |
| GitHub (Microsoft) | Automaatioiden ajo ja seuran yksityiset arkistot | Yhdysvallat |
| OpenRouter ja Anthropic | Tekoälykäsittely | Yhdysvallat |
| Meta (Instagram) | Seuran Instagram-tili | Yhdysvallat |
| WhatsApp (Meta) | Seuran jäsenten WhatsApp-kanava | Yhdysvallat |
| Suomen Pyöräily | Saa kuukausittain suomalaisten kisatulosten pohjatiedot katsausta varten ja päättää itse julkaisustaan | Suomi |

Siirrot Yhdysvaltoihin perustuvat palveluntarjoajien tietojenkäsittelyehtoihin (EU:n vakiosopimuslausekkeet tai EU–Yhdysvallat-tietosuojakehys).

Tietoja ei myydä eikä luovuteta markkinointiin, eikä niitä käytetä tekoälymallien kouluttamiseen.

## Säilytysajat

| Tieto | Säilytys |
|---|---|
| Viikkokoosteita varten haetut viestit | Poistetaan heti käsittelyn jälkeen. Niitä ei tallenneta |
| Nimettömät havainnot ja viikkokoosteet | Seuran yksityisessä arkistossa toistaiseksi. Poistetaan pyynnöstä |
| Yhteisön tilastot | Raportit Discordissa; jäsenmäärien historia 12 viikkoa |
| Tehtävätaulun muutosloki | Seuran yksityisessä arkistossa toistaiseksi |
| Aktiiviehdokaslistat | Botin viestit #admin-kanavalla; botti lukee niistä 26 viikkoa taaksepäin |
| Joukkuekanavien viestit | Poistetaan viikoittain |
| Kisatulosten pohjatiedot | Kuukausittainen tiedosto somevastaavan yksityisviesteissä |

Säilytysajat, joissa lukee "toistaiseksi", tarkistetaan vuosittain.

## Oikeutesi

- **Kieltäytyminen (vastustamisoikeus):** voit pyytää, ettei viestejäsi käytetä koosteisiin, ettei nimeäsi nosteta tuloksissa tai ettei sinua oteta aktiiviehdokaslistalle. Perusteluja ei tarvita. Pyyntö toteutetaan seuraavasta ajosta alkaen, ja jo tehdyt koosteet päivitetään ilman sinua.
- **Tarkastus, oikaisu ja poisto:** voit pyytää tiedot siitä, mitä sinusta on tallennettu, ja niiden korjaamista tai poistamista.
- **Käsittelyn rajoittaminen:** voit pyytää käsittelyn rajoittamista selvityksen ajaksi.
- **Valitus:** voit tehdä valituksen tietosuojavaltuutetulle ([tietosuoja.fi](https://tietosuoja.fi)).

Pyynnöt: kohdan *Rekisterinpitäjä ja yhteystiedot* yhteyshenkilölle tai ylläpidolle Discordissa.

## Tietoturva

- Seuran arkistot ovat yksityisiä, ja niihin pääsee vain ylläpito.
- Automaatioiden tunnukset ovat salattuina palvelussa, eivät koodissa.
- Koosteisiin päätyvä teksti tarkistetaan ohjelmallisesti nimien ja tunnisteiden varalta ennen tallennusta.
- Viikkokoosteiden viestit käsitellään kertakäyttöisellä palvelimella, joka tuhotaan käsittelyn jälkeen.

## Muutokset

Selostetta päivitetään, kun käsittely muuttuu. Päivityspäivä on sivun alussa.
