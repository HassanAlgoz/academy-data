# بيانات الولايات US States Data

<!-- academy-data
{
  "title": "بيانات الولايات US States Data",
  "files": [
    {
      "name": "us-states/abbreviations",
      "file": "state-abbrevs.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/state-abbrevs.csv",
      "legacyPath": "/data/state-abbrevs.csv"
    },
    {
      "name": "us-states/areas",
      "file": "state-areas.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/state-areas.csv",
      "legacyPath": "/data/state-areas.csv"
    },
    {
      "name": "us-states/population",
      "file": "state-population.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/state-population.csv",
      "legacyPath": "/data/state-population.csv"
    }
  ]
}
-->

**الوصف:** جداول أعدها Jake VanderPlas لعرض الدمج وتنظيف البيانات؛ جمعها من مكتب الإحصاء الأمريكي وWikipedia.

**وحدة البيانات والحجم:** السكان: 2,544 صفًا و 4 أعمدة؛ اختصارات الولايات: 51 صفًا وعمودان؛ المساحات: 52 صفًا وعمودان. تختلف تغطية الجداول، فلا نفترض تطابق مفاتيحها جميعًا.

**التفاصيل:**

- بيانات السكان في الملف تمتد من 1990 إلى 2013 ، وتشمل رموز ولايات ومناطق ومجموع الولايات المتحدة. ملف المساحة لا يحمل سنة قياس.
- في `state/region`: رمز المنطقة.
- في `ages`: جميع الأعمار `total` أو أقل من 18 سنة `under18`.
- في `year`: السنة.
- في `population`: عدد السكان.
- في `state` و`abbreviation`: الاسم والاختصار.
- في `area (sq. mi)`: المساحة بالميل المربع.
- المستودع يذكر استخلاص البيانات من الموقعين، لكنه لا يسرد لكل قيمة إصدار المصدر وتاريخ استخلاصها. صفوف مجموع الأعمار وصفوف أقل من 18 ليست مجموعات منفصلة قابلة للجمع معًا.

**المصدر:** [مستودع ناشر الجداول](https://github.com/jakevdp/data-USstates). الأعداد ونطاق السنوات من ملفات الدورة.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("us-states/abbreviations"))
data = pd.read_csv(academy.get_data_url("us-states/areas"))
data = pd.read_csv(academy.get_data_url("us-states/population"))
```

## Download

- [Download state-abbrevs.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/state-abbrevs.csv)
- [Download state-areas.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/state-areas.csv)
- [Download state-population.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/state-population.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
