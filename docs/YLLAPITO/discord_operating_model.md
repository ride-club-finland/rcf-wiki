---
gold_id: discord_operating_model
wiki_category: YLLAPITO
related_gold_docs: [resource_inventory, roles_and_responsibilities]
publishability: internal_only
status: koostettu_wikiin
last_verified: 2026-08-13
---

# Discordin toimintamalli

Discord on RCF:n käytännön toimintaympäristö: jäsenet otetaan vastaan, tapahtumia suunnitellaan, kisoja koordinoidaan, resursseja jaetaan ja yhteisöllisyyttä rakennetaan.

## Onboarding

Uuden jäsenen polku nojaa kolmeen osaan:

- automatisoitu tervetuloviesti (Carl-botti)
- tervetuloa-kanavan kysely (miten jäsen löysi seuran, millaista toimintaa hän toivoo)
- esittelyt-kanavan aktiivinen follow-up

Katso jäsenelle näkyvä versio: [Jäsenen FAQ ja onboarding-polku](../JASENPOLKU/member_faq_and_onboarding.md).

## Kanavien elinkaari

Discordissa on käytännössä neljä kanavatyyppiä:

- pysyvät toimintakanavat
- tapahtumien väliaikaiset kanavat (voidaan avata yksityisenä suunnittelukanavana ennen julkista avaamista)
- admin- tai suunnitteluvaiheen yksityiset kanavat
- arkistoitavat tai myöhemmin poistettavat tapahtumakanavat

Väliaikaiselle tapahtumakanavalle kannattaa aina olla selvä elinkaari: kuka avaa sen, milloin se avataan jäsenille, milloin pinned-viestit/resurssit otetaan talteen ennen arkistointia, ja kuka päättää arkistoinnista.

## Ylläpitoroolit

Discordiin ja siihen liittyviin alustoihin liittyy useita oikeuksia (Discord-admin, ban/poisto, Zwift Club owner, ZwiftPower admin, domain- ja verkkopalveluoikeudet, bottien ja automaatioiden hallinta). Näitä ei julkaista henkilötasoisena listana — roolikuvaukset ovat [roolit ja vastuut -dokumentissa](roles_and_responsibilities.md).

## Botit ja automaatiot

- **Carl-botti** hoitaa tervetuloa-automaation.
- **Sesh** on Discord-eventtien ja tapahtumakalenterin resurssi (premium-tilaus käytössä).
- Google Forms / Google Sheets -pohjaisia kyselyjä ja lomakkeita käytetään mm. Zwift-ajoasun tilaamiseen.

Tarkempi listaus: [resurssi-inventaario](resource_inventory.md).

## Ilmoitukset ja pingaukset

Yksittäisen kanavan pakotettu mykistys ei ole suoraviivainen — jäsenten pitää pääosin hallita ilmoituksia itse. Massa-pingausoikeudet (`@everyone`, `@here`, roolipingit) kannattaa pitää rajattuina admineille tai erilliselle viestintäroolille, jotta oikeus ei ole tarpeettoman monella.

## Puhekanavat

Puhekanavia käytetään PK-ajoihin, yhteislenkkeihin, kisojen aikaiseen keskusteluun, treeneihin ja yleiseen yhteisölliseen läsnäoloon. Mahdollinen jatkokehitys: nimetty puhekanavamalli, jossa kanavan nimi kertoo käyttötarkoituksen (esim. tasavauhti, PK-jurraus, kisaradio, yhteislenkki).

## Kansainvälinen onboarding

Julkiset Zwift-eventit ja Club-jäsenmäärän kasvu voivat tuoda palvelimelle muunkielisiä jäseniä. Ideana on ollut englanninkielinen kanava tai tervetuloviestin englanninkielinen osio — tätä ei ole vielä vahvistettu toimintamalliksi, ja se kannattaa suunnitella rajatusti ettei se hajauta nykyistä kanavarakennetta.

## Palvelinpäivitys

Discord-palvelimen kanavarakenteen päivittäminen liittyy sisarprojektiin `palvelin_nostatus`. Päivityksessä huomioitava: kanavien todellinen käyttötarkoitus, pinned-viestit ja pysyvät resurssit, admin-/yksityissisällön rajaus, tapahtumakanavien arkistointi, matalasignaali-kanavien käsittely, roolit ja oikeudet, ilmoitus- ja pingauskäytännöt.

## Avoinna

- Massa-pingausoikeuksien nykytila kannattaa tarkistaa suoraan Discordin roolikonfiguraatiosta.
- Palvelinpäivityksen omistaja pitää nimetä ennen kuin `palvelin_nostatus`-projektia viedään eteenpäin.
- Server boost -taso ja sen vaikutus ominaisuuksiin kannattaa tarkistaa suoraan Discordista tarvittaessa.
