# بيانات مزيج الكهرباء Our World in Data

<!-- academy-data
{
  "title": "بيانات مزيج الكهرباء Our World in Data",
  "files": [
    {
      "name": "electricity-mix-2024",
      "file": "electricity-mix-2024.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/electricity-mix-2024.csv",
      "legacyPath": "/data/electricity-mix-2024.csv"
    }
  ]
}
-->

**الوصف:** مقارنة مساهمة مصادر الطاقة في توليد الكهرباء، لا في مجمل استهلاك الطاقة.

**وحدة البيانات والحجم:** دولة أو إقليم في 2024 ؛ 191 صفًا و 6 أعمدة في مستخلص الدورة.

**التفاصيل:**

- مستخلص تعليمي لعام 2024 ، يجمع مؤشرات الكهرباء من Our World in Data مع رموز القارات من [Country Codes](https://github.com/datasets/country-codes). توثّق [ملاحظات إعداد الملف](./electricity-mix-2024.sources.md) مصادره وخطوات اختياره.
- في `country`: الدولة أو الإقليم.
- في `continent`: رمز القارة.
- في `solar_pct` و`wind_pct` و`hydro_pct` و`renewables_pct`: نسب توليد الكهرباء من الشمس والرياح والمياه وجميع المتجددة.
- يجمع OWID مؤشرات من Ember وEnergy Institute. ويجمع Ember بدوره إحصاءات دولية ووطنية.
- ليست قياسات أخذها مؤلف الدورة مباشرة من محطات الكهرباء.
- اختيار 2024 ورموز ISO ذات ثلاثة أحرف، واستبعاد التجمعات الإقليمية والصفوف التي ينقصها أحد المؤشرات الأربعة، ثم إلحاق القارة وإعادة تسمية الأعمدة.
- النسب من إجمالي الكهرباء المولّدة محليًا.
- المتجددة تشمل مصادر إضافية غير الشمس والرياح والمياه. `NA` رمز أمريكا الشمالية.
- متوسط الدول غير الموزون ليس حصة القارة من التوليد.

**المصدر:** [قاموس مؤشرات OWID](https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-codebook.csv)، و[مصادر Ember ومنهجيته](https://ember-energy.org/data/yearly-electricity-data/)، و[إعداد نسخة الدورة](./electricity-mix-2024.sources.md).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("electricity-mix-2024"))
```

## Download

- [Download electricity-mix-2024.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/electricity-mix-2024.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
