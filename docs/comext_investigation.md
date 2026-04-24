# Eurostat COMEXT Dataset Investigation

## Dataset Identification

**Dataset Code:** `ext_go_detail`  
**Full Name:** International Trade in Goods — Detailed Data  
**Official Metadata Page:** https://ec.europa.eu/eurostat/cache/metadata/en/ext_go_detail_sims.htm

---

## What the Data Shows

**Austria (AT) exporting to Andorra (AD) in February 2024**, at the most granular level possible — 8-digit Combined Nomenclature product codes, with values in EUR, kilograms, and supplementary units.

### Sample Data

```csv
REPORTER,PARTNER,TRADE_TYPE,PRODUCT_NC,PRODUCT_SITC,PRODUCT_CPA21,PRODUCT_CPA22,PRODUCT_BEC,PRODUCT_BEC5,PRODUCT_SECTION,FLOW,STAT_PROCEDURE,SUPPL_UNIT,PERIOD,VALUE_EUR,VALUE_NAC,QUANTITY_KG,QUANTITY_SUPPL_UNIT
AT,AD,E,35069190,59229,2052,2059,220,311210,06,2,1,NO_SU,202402,65,65,3,0
AT,AD,E,38089490,59140,2020,2020,630,313101,06,2,1,NO_SU,202402,2700,2700,136,0
AT,AD,E,38249996,59899,2059,2059,220,211220,06,2,1,NO_SU,202402,156,156,6,0
AT,AD,E,39161000,58310,2221,2221,220,211210,07,2,1,NO_SU,202402,2870,2870,141,0
AT,AD,E,39201089,58221,2221,2221,220,311220,07,2,1,NO_SU,202402,45,45,1,0
AT,AD,E,39204910,58224,2221,2221,220,311220,07,2,1,NO_SU,202402,43,43,4,0
AT,AD,E,39205100,58225,2221,2221,220,311220,07,2,1,NO_SU,202402,15,15,0,0
AT,AD,E,39219041,58299,2221,2221,220,311210,07,2,1,NO_SU,202402,3,3,0,0
AT,AD,E,39269097,89399,2229,2226,620,314200,07,2,1,NO_SU,202402,76,76,0,0
AT,AD,E,39XXXXXX,582XX,XXXX,XXXX,700,31XXXX,07,2,1,NO_SU,202402,89,89,0,0
AT,AD,E,40129090,62594,2211,2211,530,511210,07,2,1,NO_SU,202402,9,9,0,0
AT,AD,E,40169300,62999,2219,2212,630,311210,07,2,1,NO_SU,202402,36,36,0,0
AT,AD,E,40169991,62999,2219,2212,630,211210,07,2,1,NO_SU,202402,1606,1606,89,0
```

---

## Column Breakdown

| Column | Meaning | Values in sample |
|---|---|---|
| `REPORTER` | Reporting EU country | `AT` = Austria |
| `PARTNER` | Trade partner | `AD` = Andorra |
| `TRADE_TYPE` | Intra/Extra-EU | `E` = Extra-EU |
| `PRODUCT_NC` | 8-digit CN product code | e.g. `35069190` = adhesives |
| `PRODUCT_SITC` | SITC classification code | — |
| `PRODUCT_CPA21` | CPA 2.1 product classification | — |
| `PRODUCT_CPA22` | CPA 2.2 product classification | — |
| `PRODUCT_BEC` | Broad Economic Categories (rev. 4) | — |
| `PRODUCT_BEC5` | Broad Economic Categories (rev. 5) | — |
| `PRODUCT_SECTION` | HS section number | `06` = chemicals, `07` = plastics |
| `FLOW` | Trade direction | `2` = exports (`1` = imports) |
| `STAT_PROCEDURE` | Statistical procedure | `1` = normal trade |
| `SUPPL_UNIT` | Supplementary unit type | `NO_SU` = none defined |
| `PERIOD` | Reference period (`YYYYMM`) | `202402` = February 2024 |
| `VALUE_EUR` | Trade value in euros | — |
| `VALUE_NAC` | Trade value in national currency | Same as EUR for Austria |
| `QUANTITY_KG` | Weight in kilograms | — |
| `QUANTITY_SUPPL_UNIT` | Supplementary quantity | `0` when no unit defined |

---

## Official Resources

| Resource | URL |
|---|---|
| **Metadata / SIMS page** | https://ec.europa.eu/eurostat/cache/metadata/en/ext_go_detail_sims.htm |
| **Dataset in Data Browser** | https://ec.europa.eu/eurostat/web/international-trade-in-goods/database |
| **Easy Comext (query UI)** | https://ec.europa.eu/eurostat/comext/newxtweb/ |
| **API guide for COMEXT datasets** | https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started/comext-database |
