---
document: wiki_decision
päivätty: 2026-08-13
päättäjä: automaattinen päätös (Claude), tilaaja Panu
korvaa: content/gold_review_packet/review_queue.md, content/gold_review_packet/public_candidate_review.md, content/synthesized/admin_deep_analysis/review_queue.md, content/synthesized/public_candidate_review.md
---

# Päätös: mikä menee wikiin, mikä jää elämään Discordiin

Tämä dokumentti korvaa `review_queue.md`- ja `public_candidate_review.md`-tyyppisen loputtoman review-koneiston. Tämän projektin tavoite ei ollut tuottaa täydellistä, 100%-varmaa auditointia RCF:n toiminnasta, vaan louhia yhteisön hiljainen tieto niin, ettei se katoa Discordin viestivirtaan. Sen tavoitteen kannalta lisäkierrokset "onko tämä varmasti vielä voimassa" -kysymyksiä eivät tuota lisäarvoa — ne vain siirtävät päätöksen eteenpäin loputtomiin.

Siksi: alla on suora päätös jokaiselle koostetulle Gold-dokumentille. Ei uutta review-jonoa.

## Periaate, jolla päätettiin

**Wikiin**, jos tieto on:
- pysyvää (ei muutu viikoittain)
- hyödyllistä myös sille, joka ei ollut paikalla kun asia sovittiin
- ei vaadi jatkuvaa ylläpitoa pysyäkseen totena (tai ylläpito on niin kevyt että se kannattaa)

**Jää Discordiin**, jos tieto on:
- aktiivisesti muuttuvaa keskustelua (esim. kesken olevat kausisuunnitelmat)
- prosessin sisäistä kirjanpitoa tästä projektista itsestään, ei RCF:n toiminnasta
- niin tuore/epävarma ehdotus, että sen jäädyttäminen wikiin tekisi siitä virheellisesti "virallisen"
- henkilötieto-, tunniste- tai käyttöoikeussisältöä, joka ei kuulu wikiin ollenkaan

Ei kolmatta laatikkoa "tarvitaan lisää reviewtä ennen kuin voidaan päättää". Jos jokin oli aidosti liian epävarma sisällytettäväksi, se on alla merkitty Discordiin jääväksi eikä sille avata uutta review-kierrosta.

## Wikiin koottu (`content/wiki/`)

| Wiki-kategoria | Dokumentti | Miksi |
|---|---|---|
| YLLÄPITO | [Discordin toimintamalli](../YLLAPITO/discord_operating_model.md) | Pysyvä kuvaus siitä miten palvelin ja onboarding toimivat. Muuttuu harvoin. |
| YLLÄPITO | [Resurssi-inventaario](../YLLAPITO/resource_inventory.md) | Missä työkalut, lomakkeet ja tilaukset sijaitsevat — juuri sitä hiljaista tietoa, joka katoaa kun joku lopettaa aktiivitoiminnan. |
| YLLÄPITO | [Roolit ja vastuut](../YLLAPITO/roles_and_responsibilities.md) | Roolimatriisi selviää, vaikka henkilöt vaihtuisivat. |
| TAPAHTUMAT | [Tapahtumien järjestämismallit](../TAPAHTUMAT/event_organizing_patterns.md) | Yleismalli, joka pätee tapahtumatyypistä riippumatta. |
| TAPAHTUMAT | [Kruunajaiset — tapahtumaplaybook](../TAPAHTUMAT/event_playbook_kruunajaiset.md) | Kolmen vuoden (2024-2026) opit yhdessä paikassa. Korvaa erillisen 2025-pilottidokumentin. |
| TAPAHTUMAT | [RCF Cup ja kilpailutoiminnan prosessi](../TAPAHTUMAT/competition_process_rcf_cup.md) | Erottaa cupin, joukkuekisan, WTRL TTT:n ja TalviCupin toisistaan — tämä sekaannus toistuu joka kaudella jos sitä ei kirjata kerran ylös. |
| TAPAHTUMAT | [RCF-joukkuekisa — playbook](../TAPAHTUMAT/event_playbook_rcf_team_race.md) | Oma formaatti, joka sekoittuu helposti cupiin ilman kirjattua eroa. |
| TAPAHTUMAT | [RCF vs SZR — tapahtumaplaybook](../TAPAHTUMAT/event_playbook_rcf_vs_sz.md) | Ensimmäinen toteutus oli raskas juuri siksi ettei mallia ollut kirjattu. Toinen kerta on helpompi tämän kanssa. |
| JÄSENPOLKU | [Jäsenen FAQ ja onboarding-polku](../JASENPOLKU/member_faq_and_onboarding.md) | Tälle on jatkuva kysyntä help-deskissä — juuri se toistuva kysymys, joka kannattaa kirjoittaa kerran. |
| ORGANIZER_CHECKLISTS | [Checklistit + pääviestipohja](../ORGANIZER_CHECKLISTS/index.md) | Konkreettinen askel-askeleelta-apu järjestäjälle. Nämä olivat jo valmiiksi vähiten "mikkihiirimäisiä" — otettu lähes sellaisenaan. |

Kaikki nämä on merkitty sisäiseksi wikiksi (`internal_only`), paitsi jäsen-FAQ, joka on merkitty julkaisukandidaatiksi — se on ainoa dokumentti, joka kannattaa vielä ennen jäsenille näyttämistä käydä läpi linkkien ja jäsenmaksutiedon osalta, koska ne ovat todella ajan myötä vanhenevia faktoja, ei epävarmaa tulkintaa.

Dokumenteista on poistettu se osa alkuperäistä review-koneistoa, joka toisti saman kysymyksen jokaisen alaotsikon perässä ("Onko tämä edelleen ajan tasalla? Kuka omistaa? Missä sijaitsee?"). Jäljelle on jätetty vain aidosti avoimet, konkreettiset asiat kunkin dokumentin lopussa.

## Jää elämään Discordiin — ei koota wikiin

| Alkuperäinen dokumentti | Miksi jää Discordiin |
|---|---|
| `admin_decisions.md` (päätöskandidaatit: TalviCup 2025-26 linjaus, RCF Cup tammikuun korvaajana, TalviCup 2026-27 -yhteistyö) | Nämä ovat kesken olevaa kausisuunnittelua. Jos ne jäädytetään wikiin nyt, wiki väittää tietävänsä ensi talven ratkaisun jota ei ole vielä tehty. Kausikeskustelu kuuluu admin-kanavalle siihen asti kunnes se on oikeasti päätetty — silloin se on yksi lause tulevaan toimintamalliin, ei oma dokumentti. Vahvistetut, pysyvät faktat (Carl-botti, tervetuloviesti-automaatio) on jo siirretty toimintamalli- ja resurssidokumentteihin. |
| `open_items_and_risks.md` | Tämä on luonteeltaan TODO-lista, ei tietoa. TODO-listat vanhenevat viikossa ja pitää ylläpitää jatkuvasti, mikä on juuri se ylläpitotaakka jota wiki ei kestä. Paremmin paikka tälle on admin-kanavan pinned-viesti tai erillinen ylläpidon tehtävälista, ei wiki-artikkeli. Aidosti pysyvät riskit (esim. massa-pingausoikeudet, palvelinpäivityksen omistajuus) mainitaan lyhyesti toimintamallidokumentissa yhtenä kappaleena, ei omana riskirekisterinä. |
| `pinned_resource_inventory.md` | Toimi hyvin louhintavälineenä, mutta dokumenttina se on lähinnä lista "tarkista tämä" -kysymyksiä. Sen aidosti pysyvät löydökset (help-deskin aloituspolku, matalan kynnyksen kisakonsepti, Kruunajaisten perinne, Moomoo-prosessi, mediaresurssit) on jo poimittu resurssi-inventaarioon, FAQ:hun ja tapahtumaplaybookeihin. Itse inventaariodokumenttia ei tarvita enää erillisenä. |
| `link_registry.md` | Tämä on 699 linkin tilastoyhteenveto, ei artikkeli. Linkkirekisteri on oikea työkalu (taulukko/CSV omistajineen), ei wiki-sivu, ja sen linkkejä ei viedä wikiin ennen kuin joku on käynyt läpi mitkä ovat yhä voimassa. Kunnes niin tehdään, linkit elävät siellä missä ne jo ovat — pinned-viesteissä Discordissa. |
| `followup_channel_scopes.md` | Tämä ei ole RCF:n toimintaa koskevaa tietoa vaan tämän louhintaprojektin oma jatkosuunnitelma. Ei kuulu wikiin ollenkaan, kuuluu tähän repoon. |
| `event_playbook_kruunajaiset_2025.md` | Sisältö on jo yhdistetty monivuotiseen Kruunajaiset-playbookiin. Erillistä 2025-sivua ei tarvita wikiin — se jää tämän repon lähdeaineistoksi. |
| `content/gold_review_packet/*`, `review_queue.md`, `public_candidate_review.md`, `gold_index.md`, kaikki `_generated_gold_synthesis.md` -tiedostot | Tämä on juuri se "mikkihiirikansio". Prosessin oma kirjanpito siitä miten review pitäisi tehdä — ei tietoa RCF:stä. Tämä päätösdokumentti korvaa ne kokonaan. Voit poistaa kansion, jos haluat siistiä repon, mutta mitään ei ole kadonnut: kaikki todellinen sisältö niistä on joko wikissä tai yllä perusteltu miksi ei ole. |

## Mitä tämä käytännössä tarkoittaa

- Ylläpito voi alkaa käyttää `content/wiki/`-kansiota sellaisenaan sisäisenä ohjeistona jo nyt, ilman erillistä hyväksymiskierrosta.
- Jäsen-FAQ (`wiki/JASENPOLKU/member_faq_and_onboarding.md`) on ainoa dokumentti, joka kannattaa vielä silmäillä läpi ennen jäsenille jakamista — lähinnä linkkien ja jäsenmaksun takia, ei sisällön takia.
- TalviCupin ja muun kesken olevan kausisuunnittelun ei tarvitse "valmistua" ennen kuin se kirjataan mihinkään — se saa elää Discordissa niin pitkään kuin se on oikeasti kesken. Kun se on päätetty, yksi lause riittää olemassa olevaan toimintamalli- tai kilpailuprosessidokumenttiin.
