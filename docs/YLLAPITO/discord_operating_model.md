---
gold_id: discord_operating_model
wiki_category: YLLAPITO
related_gold_docs: [resource_inventory, roles_and_responsibilities]
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-15
---

# Discordin toimintamalli

Discord on RCF:n käytännön toimintaympäristö: jäsenet otetaan vastaan, tapahtumia suunnitellaan, kisoja koordinoidaan, resursseja jaetaan ja yhteisöllisyyttä rakennetaan.

## Onboarding

Uuden jäsenen polku nojaa kolmeen osaan:

- automatisoitu tervetuloviesti (Carl-botti)
- tervetuloa-kanavan kysely (miten jäsen löysi seuran, millaista toimintaa hän toivoo)
- esittelyt-kanavan aktiivinen follow-up

Katso jäsenelle näkyvä versio: [Jäsenen FAQ ja onboarding-polku](../JASENPOLKU/member_faq_and_onboarding.md).

**Konkreettinen tervetuloviestin rakenne** (Carl-bot, automatisoitu heti liittymisen yhteydessä): 1) ohjaa lukemaan infopankki-kanavan ohjeet, 2) ohjaa seuraamaan tapahtumakalenterikanavaa, 3) ohjaa liittymään seuraavaan yhteislenkkiin suoraan tapahtumalistauksesta, 4) kannustaa (vapaaehtoisesti) esittelemään itsensä esittelyt-kanavalla. Viestissä on lisäksi tilaa yhdelle ajankohtaiselle nostolle (esim. tulevan kilpailukauden alkamisesta). Tämä neliosainen rakenne on toiminut sellaisenaan vuodesta 2024 asti eikä sitä ole tarvinnut muuttaa.

**Kertaluonteinen kysymys, joka toistuu**: tervetuloviestin rekrytointikampanjoista (esim. "kutsu tapaamasi suomalainen Zwift-ajaja mukaan") on kokeiltu, mutta yhteisö päätyi siihen, että kynnys kontaktoida tuntemattomia on korkea molemmin puolin — toimivammaksi malliksi osoittautui kevyempi tiedotus (infoviesti tapahtumakalenterikanavalla + vapaamuotoinen keskustelu yleiskanavalla) ilman erillistä kampanjarakennetta.

**Toistuva kevätrytmi**: ennen kuin aktiivisuus laskee ulkokauden alkaessa (maalis-huhtikuu), on vakiintunut tapa julkaista anonyymi kehityskysely e-pyöräilytoiminnasta yleiskanavalla — kerää toiveita, syitä olla osallistumatta ja halukkuutta ottaa isompaa roolia. Kyselyyn kannattaa jättää avoin vapaatekstikenttä kiinteiden kysymysten lisäksi, ja se kannattaa ajoittaa juuri ennen kauden vaihtumista, ei sen jälkeen.

## Kanavien elinkaari

Discordissa on käytännössä neljä kanavatyyppiä:

- pysyvät toimintakanavat
- tapahtumien väliaikaiset kanavat (voidaan avata yksityisenä suunnittelukanavana ennen julkista avaamista)
- admin- tai suunnitteluvaiheen yksityiset kanavat
- arkistoitavat tai myöhemmin poistettavat tapahtumakanavat

Väliaikaiselle tapahtumakanavalle kannattaa aina olla selvä elinkaari: kuka avaa sen, milloin se avataan jäsenille, milloin pinned-viestit/resurssit otetaan talteen ennen arkistointia, ja kuka päättää arkistoinnista.

**Konkreettinen esimerkki toteutuneesta elinkaaresta**: Kruunajaisten vuosittainen kanava on avattu ensin vain admin-tasolla (muille piilossa) muutaman viikon ajaksi valmistelua varten, ja avattu kaikille vasta kun sisältö (pääilmoitus, veikkaustaulukko) on ollut valmis — tyypillisesti noin viikko ennen tapahtumaa. Joukkuekisojen taktiikkakanavat ("a-tiimi"/"b-tiimi", ks. [RCF-joukkuekisa-playbook](../TAPAHTUMAT/event_playbook_rcf_team_race.md)) taas poistetaan ja luodaan tyhjinä uudestaan joka kisakertaa varten — keskusteluhistoria on niissä tarkoituksella katoavaa. Kevään 2026 aikana on myös perustettu pysyviä paikkakuntakanavia (esim. alueellisille yhteislenkeille) oman kategoriansa alle, ja hiljaisia kanavia on siirretty arkistoon säännöllisin väliajoin sen sijaan että ne jäisivät roikkumaan aktiivisten joukkoon.

## Ylläpitoroolit

Discordiin ja siihen liittyviin alustoihin liittyy useita oikeuksia (Discord-admin, ban/poisto, Zwift Club owner, ZwiftPower admin, domain- ja verkkopalveluoikeudet, bottien ja automaatioiden hallinta). Näitä ei julkaista henkilötasoisena listana — roolikuvaukset ovat [roolit ja vastuut -dokumentissa](roles_and_responsibilities.md).

## Botit ja automaatiot

- **Carl-botti** hoitaa tervetuloa-automaation.
- **Sesh** on Discord-eventtien ja tapahtumakalenterin resurssi (premium-tilaus käytössä). Premiumissa on ominaisuus, jolla osallistujille voi jakaa tapahtumakohtaisen, tapahtuman jälkeen poistuvan roolin — sen avulla voi pingata vain kyseiseen tapahtumaan ilmoittautuneet (esim. `@WTRL` vain WTRL TTT -ilmoittautuneille) ilman laajempaa massapingausta.
- Google Forms / Google Sheets -pohjaisia kyselyjä ja lomakkeita käytetään mm. Zwift-ajoasun tilaamiseen — ks. [resurssi-inventaario](resource_inventory.md#lomakkeet-ja-taulukot) konkreettisesta toteutuksesta.

Tarkempi listaus: [resurssi-inventaario](resource_inventory.md).

## Ilmoitukset ja pingaukset

Yksittäisen kanavan pakotettu mykistys ei ole suoraviivainen — jäsenten pitää pääosin hallita ilmoituksia itse. Massa-pingausoikeudet (`@everyone`, `@here`, roolipingit) kannattaa pitää rajattuina admineille tai erilliselle viestintäroolille, jotta oikeus ei ole tarpeettoman monella. **Tämä ei ole vielä korjattu**: läpikäynnissä (2025-11) havaittiin, että kaikilla jäsenillä on tällä hetkellä oikeus käyttää massa-pingauksia — korjaus on joko rajata oikeus rooleittain, tai käyttää yllä mainittua Sesh-tapahtumaroolia kohdennettuun pingaukseen aina kun pingaus koskee vain tiettyä tapahtumaa eikä koko palvelinta.

## Puhekanavat

Puhekanavia käytetään PK-ajoihin, yhteislenkkeihin, kisojen aikaiseen keskusteluun, treeneihin ja yleiseen yhteisölliseen läsnäoloon. Mahdollinen jatkokehitys: nimetty puhekanavamalli, jossa kanavan nimi kertoo käyttötarkoituksen (esim. tasavauhti, PK-jurraus, kisaradio, yhteislenkki).

**Kaksi konkreettista mallia, jotka ovat toimineet hyvin**:
- **"Kisakoulutus"**: kokenut kisaaja on radiossa mukana, kun aloitteleva kuski ajaa oman ensimmäisen tai varhaisen kisansa, ja neuvoo reaaliajassa sijoittumista, lepäämistä ja tehojen jaksottamista. Kokemus on ollut poikkeuksellisen hyvä ("tuli yhtä paljon oivallusta kuin koko edellisenä vuonna yhteensä") — kynnys sekä pyytää että tarjota tätä on kuitenkin ollut korkea, joten sitä kannattaa aktiivisesti tarjota, ei jäädä odottamaan pyyntöjä.
- **Epämuodollinen arki-ilta-slotti**: kiinteä Sesh-tapahtumasarja arki-iltoina (esim. klo 17-19), johon kannustetaan liittymään puhekanavalle oman PK-treenin ajaksi ilman erillistä ohjelmaa — madaltaa kynnystä käyttää puhekanavia myös kisojen ulkopuolella.

## Kansainvälinen onboarding

Julkiset Zwift-eventit ja Club-jäsenmäärän kasvu voivat tuoda palvelimelle muunkielisiä jäseniä. Ideana on ollut englanninkielinen kanava tai tervetuloviestin englanninkielinen osio — tätä ei ole vielä vahvistettu toimintamalliksi, ja se kannattaa suunnitella rajatusti ettei se hajauta nykyistä kanavarakennetta.

Konkreettinen tunnistettu tarve: kansainvälisiä osallistujia tulee erityisesti MyWhoosh/Sunday Race Club -tyyppisten kisojen kautta, jotka eivät ymmärrä suomea eivätkä tarvitse näkyviin suomenkielisiä kanavia. Ehdotettu ratkaisu on sitoa tämä Discordin **Community Server** -tilaan siirtymiseen (ks. Palvelinpäivitys alla): uuden jäsenen alkukysely voisi ohjata ulkomaiset osallistujat automaattisesti vain heille relevanttien (esim. MyWhoosh-) kanavien pariin roolituksen kautta, ilman että se sotkee suomenkielistä pääkanavarakennetta.

## Palvelinpäivitys

Discord-palvelimen kanavarakenteen päivittäminen liittyy sisarprojektiin `palvelin_nostatus`. Päivityksessä huomioitava: kanavien todellinen käyttötarkoitus, pinned-viestit ja pysyvät resurssit, admin-/yksityissisällön rajaus, tapahtumakanavien arkistointi, matalasignaali-kanavien käsittely, roolit ja oikeudet, ilmoitus- ja pingauskäytännöt.

**Konkreettinen, jo puntaroitu iso päätös**: siirtyminen tavallisesta palvelimesta Discordin viralliseksi **Community Server** -tilaksi. Hyötynä automaattinen, kyselypohjainen roolitus uusille jäsenille (kanavien näkyvyys kiinnostuksen mukaan ilman ylläpidon käsityötä), Server Insights -analytiikka (mitkä kanavat aktiivisia, mistä uudet jäsenet tulevat) ja viralliset tiedotuskanavat. Ainoa mainittu haittapuoli: viestien lähettäminen vaatii jäseneltä vahvistetun sähköpostiosoitteen, mikä on pieni lisäkynnys. Keskustelussa painotus oli, että hyödyt voittavat selvästi — päätöstä ei ollut vielä viety loppuun asti, joten tarkista tilanne ennen kuin oletat sen olevan käytössä.

**Server boost -taso konkreettisesti**: palvelin on saavuttanut tason 1 kolmella jäsenen omalla Nitro-boostilla; tason 2 saavuttaminen vaatisi vielä yhden lisäboostin. Boostien tuomat ominaisuudet (mm. pidemmät viestit, suuremmat tiedostokoot, parempi näytönjakolaatu) kannattaa tarkistaa suoraan Discordista, koska ne muuttuvat Discordin puolelta ajoittain.

## Avoinna

- Massa-pingausoikeuksien rajaaminen — tunnistettu avoimeksi 2025-11, ei vielä korjattu.
- Palvelinpäivityksen omistaja pitää nimetä ennen kuin `palvelin_nostatus`-projektia viedään eteenpäin.
- Community Server -siirtymän lopullinen päätös ja ajoitus.
- Neljäs Server Boost tason 2 saavuttamiseksi, jos ominaisuuksille on tarvetta.
