---
gold_id: resource_inventory
wiki_category: YLLAPITO
related_gold_docs: [discord_operating_model, roles_and_responsibilities]
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-15
---

# Resurssi-inventaario

Mitä työkaluja, lomakkeita, taulukoita, kanavia ja ulkoisia alustoja seuran toiminta nojaa. Tämä on juuri se tieto, joka katoaa ensimmäisenä kun aktiivi lopettaa — siksi se on kirjattu tänne yhteen paikkaan omistajien tarkistettavaksi, ei henkilön muistin varaan.

## Discord ja onboarding

- **Carl-botti**: tervetuloa-automaatio.
- **Tervetuloa-kanavan kysely**: kerää tietoa siitä, miten jäsen löysi seuran ja millaista toimintaa hän toivoo.

## Kalenterit ja tapahtumahallinta

- **Sesh**: Discord-eventtien ja tapahtumakalenterin resurssi, premium-tilaus käytössä. Kuka tahansa jäsen voi luoda Sesh-tapahtuman — ei vaadi admin-oikeuksia. Premium-tilaus on hinnoiteltu joko vuositilauksena (~50$/v) tai kertamaksullisena "lifetime"-lisenssinä (~120$); tilaus kytkeytyy Discord-kirjautumisen kautta yhteen valittuun palvelimeen, joten omistajuuden vaihto (esim. maksavan jäsenen vaihtuessa) vaatii koordinoinnin: uusi omistaja ostaa oman lisenssinsä ja aktivoi sen vasta kun vanha tilaus on deaktivoitu tai vanhentunut — ei automaattista siirtoa.
- **RCF-eventkalenteri**: Google Sheets -pohjainen tapahtumien aikataulunäkymä, sisältää myös "Osallistujat"-välilehden eventtien osallistujamäärien seurantaan. Zwiftiltä voi kuukausittain pyytää raportin, joka näyttää kaikkien RCF:n eventtien osallistujamäärät ja muuta dataa kootusti.

## Lomakkeet ja taulukot

- **Kruunajaisten veikkaus- ja osallistujataulukko**: uusiokäyttökelpoinen pohja tuleville Kruunajaisille.
- **Toiminnan kehittämisen palautekyselyt**: aloittelijoiden huomiointi, naisten mukaan saaminen ym. — toistuva anonyymi Google Forms -kysely, ajoitettu keväällä ennen ulkokauden alkua (ks. [Discordin toimintamalli](discord_operating_model.md#onboarding)).
- **Zwift-eventtien tilaus-Excel** (`Zwift Events.xlsx`): Zwiftin oma Event Request Form, lähetetään liitteenä sähköpostitse events@zwift.com:iin uutta eventtisarjaa tilattaessa. Koko tilausprosessi askel askeleelta: [Zwift-eventin tilaaminen Zwiftiltä](../ORGANIZER_CHECKLISTS/how_to_order_zwift_event.md).
- **Zwift-ajoasun tilausautomaatio**: Google Form + Google Sheet + Apps Script -yhdistelmä (rakennettu tekoälyavusteisesti). Lomake kerää jäsenen Zwift ID:n, skripti tarkistaa tunnisteen muodon ja lähettää joka yö automaattisesti kaikki uudet ID-numerot sähköpostitse Zwiftille kuittauksineen. Ajoasu on tietoisesti rajattu vain Club-jäsenille — sitä ei jaeta ulkopuolisille tilaajan kautta, koska Excel-pohjainen eventtitilaus ei tue rajausta Club-jäseniin. Ajoasu tuli käyttöön Zwift-version 1.98 mukana (2025-09-25).

## Zwift ja ZwiftPower

- **ZwiftPower-tiimikuvaus**: viestintä- ja onboarding-resurssi, auttaa löytämään RCF:n kanavat.
- **Zwift-ajoasun tilauslomake ja automaatio**: Google Form + Sheet + skripti, käsittelee Zwift ID -tunnisteita. Tämä on tili-/tunnisterajapinta, joten sen omistajuus ja käyttöoikeudet pitää olla nimetty ylläpidon toimesta. Ks. tarkempi kuvaus yllä Lomakkeet ja taulukot -kohdassa.
- **ZwiftPowerin League-työkalu**: RCF Cupin pisteytys lasketaan tällä, ei käsin taulukolla. Oikeudet haetaan ZwiftPowerin omalla lomakkeella, eivät RCF:n Discord-roolien kautta — tällä hetkellä yhden henkilön tilin varassa. Käyttöohje ja riski tarkemmin: [RCF Cup ja kilpailutoiminnan prosessi](../TAPAHTUMAT/competition_process_rcf_cup.md#zwiftpowerin-league-tyokalu-pisteytyksen-kaytannon-hallinta).
- **Eventtien muokkaus**: `zwift.com`-sivun "Manage my events" -näkymä on käytännössä toimivampi eventtien muokkaukseen kuin Companion-appi (ei tarvitse näpräillä pienellä ruudulla). Tunnettu rajoitus: Double Draft -asetus ei pysy päällä tallennettaessa (poistui Zwiftistä jo vuosia sitten, mutta Companion-appin käyttöliittymä ei ole päivittynyt vastaamaan tätä) — muut asetukset (esim. Disable Drafting) tallentuvat normaalisti. Eventtien muokkaus on ajoittain ollut kokonaan poikki sekä Companionista että zwift.comista Zwiftin päässä — tällöin ei auta muu kuin odottaa korjausta.

## Seuravaatteet

- **Moomoo-seuravaateprosessi**: toimittajayhteys, designit, samplet, ydintuotevalikoima, hintaneuvottelu, oma seuravaatekanava. Oma prosessinsa, joka kannattaa pitää yhtenäisenä. Toteutunut aikajana: yhteydenotto → ei vastausta viikkoon (viesti oli mennyt roskapostiin, kannattaa varautua tähän ja kysyä perään) → yhteyshenkilö ja hintalista → mallikappaleiden tilaus (n. 50€/setti, sisältää postituksen Suomeen ja 14 vrk palautusajan) → testaus alueellisesti hajautetuilla testaajilla (mitat ja kokemukset kirjattuna) → hintaneuvottelu, jossa alennusporras alkaa n. 50 kpl/tuote. Ydintuotteiksi valittiin ensin rajattu setti (ajopaita ja bibsit kahdessa laatutasossa, takki, liivi, sukat, irtohihat/-lahkeet, lippis) — designien lisääminen on aina lisätyö toimittajan suuntaan, joten laajennetaan valikoimaa vasta myöhemmin. Personointi (nimi rinnassa logon yläpuolella tai kauluksessa) on tarjolla lisäpalveluna.
- **Tunnetut vaihtoehtoiset toimittajat** (selvitetty mutta ei valittu, hyvä lähtökohta jos Moomoo-yhteistyö joskus vaihtuu): owayo (Saksa, ei minimitilausta), Giordana Custom (Italia), CUORE (Saksa/Sveitsi), Q36.5 (Italia, minimi ~10 kpl/tuote), Capo Cycling (Italia), Santini (Italia), Decca (Belgia, minimi 5 kpl). Ei kilpailutettu loppuun asti — päätös oli pitää kilpailutus kevyenä eikä tehdä siitä isoa erillisprojektia.
- **Moomoo-kauppasivu**: `moomoo.cc/ride-club-finland/` — toistuvasti käytetty (viimeksi maaliskuu 2026), näyttää olevan nykyinen tilauskanava erillisen kyselylomakkeen rinnalla.

## Viestintä ja media

Introvideo, Instagram/Facebook/YouTube, kisastreamit, koosteet ja someklipit. Näille kannattaa olla nimetty vastuu (ks. [roolit ja vastuut](roles_and_responsibilities.md)), koska ne ovat julkisen näkyvyyden kannalta seuran kasvot.

- Instagram- ja Facebook-läsnäolo on mainittu toistuvasti, mutta linkkirekisterissä ei ole yhtä pysyvää profiililinkkiä — vain yksittäisiä postaus-/story-linkkejä, jotka vanhenevat. Sivujen omistaja tarkistaa ja lisää kanoniset profiililinkit tähän myöhemmin.
- **Instagram konkreettisesti**: marraskuussa 2025 tili ylitti ensimmäistä kertaa 10 000 näyttökertaa/kk (75 % seuraajilta, 25 % muualta) — RCF vs SZR -tapahtumapostaukset ja uusille jäsenille suunnatut infograafit olivat suosituimpia. Orgaaniset postaukset saavat tyypillisesti 500-700 näyttöä; muutaman euron mainosbudjetti (esim. 3€/pv, 3 päivää) nostaa saman postauksen näytöt nelinumeroisiksi jo vuorokaudessa. Tilien (Instagram + Facebook) yhdistäminen ja adminien lisääminen hoidetaan **Meta Business Suitesta**, kutsu tehdään seuran Facebook-tilin kautta.
- **Aktiiviset kisastriimaajat** (`kisa-streamit-ja-tallenteet`-kanavan viittausmäärien perusteella, ei täydellinen lista): F1RSTlive on selvästi aktiivisin ja toistuvin (Twitch + YouTube, viittauksia yli 40, aikaväli syksy 2024 – kevät 2026). Muita toistuvasti mainittuja: kovaajoa, wattiantti, samituomi, jiiaanii, ToniKauhanen. Nämä ovat yksittäisten jäsenten omia julkisia striimaustilejä, ei RCF:n omistamia kanavia — tarkista ajantasaisuus ennen kuin niitä käytetään viestinnässä kanonisina.
- **Striimivälineistön resursointi**: pitkään yksi vapaaehtoinen striimaaja on kustantanut kaiken oman laitteistonsa itse. Seura on tehnyt tähän ensimmäisen konkreettisen resurssipäätöksen (joulukuu 2025): korvasi noin 350€ edestä laitehankintoja seuran kassasta — hyvä ennakkotapaus sille, että vapaaehtoisen mediaroolin taakse kannattaa saada myös resursseja, ei vain kiitosta.
- **MyWhoosh/SRC-tulosautomaatio**: koodattu työkalu, joka poimii MyWhooshin Sunday Race Club -kisojen tulokset ja julkaisee ne kanavalle automaattisesti tulosten julkistuessa. Jatkokehitysideana automaation laajentaminen suoraan Instagram-julkaisuihin.

## Pysyvät linkit ja tunnisteet

Linkkirekisterin 699 viitteestä suurin osa (noin 85 %) on yksittäisiä kisatallenteita tai kertaluonteisia event-linkkejä, jotka vanhenevat eivätkä kuulu tähän. Näiden joukosta erottuu kuitenkin pieni joukko **toistuvasti käytettyjä, pysyviä** linkkejä — nämä kannattaa pitää ajan tasalla tässä dokumentissa sen sijaan, että niitä etsitään uudestaan joka kerta Discordista:

| Resurssi | Linkki | Huomio |
|---|---|---|
| RCF:n ZwiftPower-tiimi | `zwiftpower.com/team.php?id=20561` | Vakaa, viitattu toistuvasti 2023–2025. |
| RCF Cup -tapahtumatagi | `zwift.com/uk/events/tag/rcfcup` | Pysyvä tagi, näyttää kaikki sarjan eventit — parempi kuin yksittäiset stage-linkit. |
| RCF Kuutar (naisten sarja) -tapahtumatagi | `zwift.com/uk/events/tag/rcfkuutar` | Vastaa [pinned-inventaariossa](#) mainittua naisten kisasarjaa. |
| Category Spotlight -tapahtumatagi | `zwift.com/uk/events/tag/rcfcategoryspotlight` | Viikoittainen matalan kynnyksen kisamalli. |
| RCF Shop | `ride-club-finland.myspreadshop.fi` | Vakaa, viitattu toistuvasti 2025–2026. |
| RCF:n virallinen nettisivu | `rideclub.fi` (mm. `/liity-seuraan`, `/e-pyöräily`) | Käytetään mm. liittymisohjeissa. |
| RCF-materiaalit (logo, kansikuvat, Club ladder -pistelaskuri) | Google Drive -kansio, mainittu infopankissa | `needs_human_review` linkkirekisterissä — tarkista käyttöoikeudet ja ajantasaisuus ennen kuin linkkiä jaetaan laajemmin. |
| Ilmoittautumis-/kisarosteritaulukko | Google Sheets, käytetty 2023–2025 useasta kanavasta | Sisältää osallistujien nimiä — **vain ylläpito-/järjestäjäkäyttöön**, ei jäsenille jaettava linkki. |
| Sesh-kojelauta | `sesh.fyi/dashboard/` | Yleinen Sesh-työkalun kirjautumisosoite. |
| WTRL:n viralliset sivut | `wtrl.racing/zwift-racing-league/` (schedule/rules/registration), `wtrl.racing/login/` | Ulkoisen alustan omat sivut, ei RCF:n ylläpitämiä. |

**Ei vielä ratkaistu:** RCF:n Zwift Club -linkille löytyi linkkirekisteristä **kolme eri club-ID:tä** eri ajankohdilta (heinäkuu 2024, syyskuu 2025, tammikuu 2026). Tämä voi tarkoittaa, että klubi on jossain vaiheessa luotu uudelleen, tai että kyse on eri klubeista. Kunnes joku ylläpidosta vahvistaa nykyisen, oikean linkin, sitä ei ole merkitty tähän eikä jäsen-FAQ:hun — väärän club-linkin jakaminen jäsenille olisi pahempi kuin linkin puuttuminen kokonaan.

Kaksi eri Discord-kutsulinkkiä (`discord.gg/...`) löytyi myös eri ajankohdilta (helmikuu 2024 ja marraskuu 2025) — samasta syystä ei merkitty kanoniseksi ilman vahvistusta.

Erillinen, jo valmiiksi koostettu e-pyöräilyn työkalulinkkien kokoelma (Zwift-analytiikka, reittityökalut, harjoitustyökalut ym.) on siirretty omaksi sivukseen: [E-pyöräilyn työkalulinkit](../JASENPOLKU/e_pyorailyn_tyokalulinkit.md).

## Pinned-viesteistä täydentyneet resurssit

Discordin pinned-viestit paljastivat admin-kanavan lisäksi käytännön arjen resursseja kanavittain:

- **help-desk**: pinned-viesti on jäsenten Zwift-aloituspolku (tilit, ZwiftPower/WTRL-kytkennät) — pohjana [jäsen-FAQ:lle](../JASENPOLKU/member_faq_and_onboarding.md).
- **aloittelijat-ja-vähän-väsähtäneet**: matalan kynnyksen kisakonsepti, oma jäsenpolun kannalta strateginen malli.
- **kisa-streamit-ja-tallenteet / kisojen-selostus**: YouTube-kansipohjat, introasset, ajatus selostuksesta MyWhoosh SRC -kisoihin.
- **rcf-shop / seuravaatteet-moomoo**: seurakauppa ja Moomoo-erikoiserien kyselyprosessi.
- **naiset**: RCF:n ensimmäinen naisten kisasarja, kuukausirytmillä.
- **ulkotapahtumat / saimaa-2027**: fyysisten ulkotapahtumien ilmoitusformaatti ja ajoryhmäsuunnittelu.
- Kisakanavien (Zwift-kisat, RCF Cup, cycling-time-trials-winter, ZRL) pinned-viestit toimivat kisakalenterien ja kausitaulukoiden jakelupaikkana — nämä linkit vanhenevat helposti eivätkä siksi ole tässä dokumentissa, vaan elävät Discordissa kunnes joku ottaa linkkirekisterin omistajuuden (ks. alla).

## Tilit, koodit ja linkit — tietoisesti rajattu pois

Seuraavia ei ole tuotu tähän dokumenttiin, koska ne joko vanhenevat nopeasti tai vaativat käyttöoikeushallintaa:

- yhteiskäyttötilit ja sähköpostit (autentikaatio, palautusoikeudet) — hoidetaan ylläpidon sisäisesti, ei wikissä
- yksittäiset kisatallenteet ja kertaluonteiset event-linkit — linkkirekisterin 699 viitteestä noin 600 on tätä (pääosin YouTube/Twitch-tallenteita `kisa-streamit-ja-tallenteet`- ja `zwift-kilpailut`-kanavilta); käytiin läpi kokonaisuudessaan, eikä näistä löytynyt uusia pysyviä kokoelmia yksittäisten tallenteiden lisäksi — ne jäävät elämään Discordiin
- koodit ja määräaikaiset edut (esim. `kilometrikisa`- ja `kehonhuolto`-kanavien pinned-koodit) — vanhenevat nopeasti, jäävät Discordiin
- vanhat rosterit ja henkilölistat — eivät koskaan wikiin sellaisenaan (ks. yllä ilmoittautumistaulukon rajattu poikkeus)

## Avoinna

- Sesh-premiumin maksutapa ja palautusoikeus.
- Zwift-ajoasulomakkeen ja -skriptin omistaja.
- Linkkirekisterin omistaja (ks. [wiki-päätös](../meta/wiki_decision.md) — linkit itsessään eivät ole wikissä).
- ZwiftPowerin League-työkalun varahenkilö — oikeudet ovat tällä hetkellä yhden tilin varassa.
