# بيانات البطاريق Palmer Penguins

<!-- academy-data
{
  "title": "بيانات البطاريق Palmer Penguins",
  "files": [
    {
      "name": "penguins",
      "file": "penguins.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/penguins.csv",
      "legacyPath": "/data/penguins.csv"
    }
  ]
}
-->

**الوصف:** قياسات أنواع البطاريق وأحجامها في أرخبيل Palmer بالقارة القطبية الجنوبية.

**وحدة البيانات والحجم:** بطريق بالغ؛ 344 صفًا و 7 أعمدة في ملف الدورة، مع قياسات مفقودة في بعض الصفوف.

**التفاصيل:**

- درست أبحاث Kristen Gorman وفريق Palmer LTER اختلاف الحجم والغذاء بين الجنسين والأنواع. اختيرت أعشاش قبل وضع البيض، وقيس البالغان عند بلوغ العش مرحلة البيضة الواحدة. استُخدمت القدمة لقياس المنقار، والمسطرة للزعنفة، وموازين زنبركية للكتلة؛ وحدّد الجنس بتحليل جزيئي لعينات الدم. [الدراسة الأصلية وطرائقها](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090081).
- سنوات الدراسة المسجلة في الحزمة: 2007–2009.
- جزر Biscoe وDream وTorgersen في أرخبيل Palmer، القارة القطبية الجنوبية.
- في `species`: النوع، Adelie أو Chinstrap أو Gentoo.
- في `island`: الجزيرة.
- في `sex`: الجنس.
- في `bill_length_mm` و`bill_depth_mm`: طول المنقار وعمقه بالملليمتر.
- في `flipper_length_mm`: طول الزعنفة بالملليمتر.
- في `body_mass_g`: الكتلة بالغرام.
- حزمة palmerpenguins تضم أيضًا عمود `year`.
- ملف الدورة، المنقول عبر seaborn، لا يتضمنه. القياسات مأخوذة في موسم التكاثر، فلا تمثّل الكتلة في كل فصول السنة.

**المصدر:** [توثيق مجموعة Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/reference/penguins.html)، و[الدراسة الأصلية وطرائقها](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090081).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("penguins"))
```

## Download

- [Download penguins.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/penguins.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
