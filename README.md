# RCF-wiki

Ride Club Finlandin sisäinen tietopankki. Sisältö on tavallista Markdownia
YAML-frontmatterilla `docs/`-kansiossa — ihmiset lukevat sen rakennettuna
sivustona, kielimallit voivat lukea saman lähteen suoraan tästä repositoriosta.

Sisällön alkuperä ja perustelut sille, mikä päätyi wikiin: [`docs/meta/wiki_decision.md`](docs/meta/wiki_decision.md).
Lähde-etsintä ja Discord-louhinta tehtiin erillisessä `RCF_DISCORD_EXPORT`-projektissa.

## Kehitys

```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\mkdocs serve
```

Avaa selaimessa: http://127.0.0.1:8000

## Julkaisu

```powershell
.venv\Scripts\mkdocs build
```

Tulostaa staattisen sivuston `site/`-kansioon. Ei vielä kytketty hostaukseen —
ks. juurikansion päätökset deployn suhteen.

## Sisällön ylläpito

- Uusi sivu: lisää `.md`-tiedosto oikeaan kategoriakansioon `docs/`-alle ja
  listaa se `mkdocs.yml`:n `nav`-osiossa.
- Pidä YAML-frontmatter (`gold_id`, `status`, `last_verified` tms.) mukana,
  se auttaa sekä ihmisiä että kielimalleja arvioimaan sisällön tuoreutta.
