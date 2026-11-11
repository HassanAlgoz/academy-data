# بيانات Tips

<!-- academy-data
{
  "title": "بيانات Tips",
  "files": [
    {
      "name": "tips",
      "file": "tips.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/tips.csv",
      "legacyPath": "/data/tips.csv"
    }
  ]
}
-->

**الوصف**: سجّل مدير مطعم بيانات الزبائن الذين خدمهم خلال شهرين ونصف.

**وحدة البيانات والحجم:** فاتورة مجموعة زبائن مع الإكرامية؛ 244 صفًا و7 أعمدة.

**التفاصيل:**

- في `total_bill`: مبلغ الفاتورة للطعام والشراب، بالدولار الأمريكي.
- في `tip`: مبلغ الإكرامية بالدولار الأمريكي.
- في `sex`: جنس الزبون المسجّل، `Male` أو `Female`.
- في `smoker`: حالة التدخين المسجّلة، `Yes` أو `No`.
- في `day`: يوم الأسبوع.
- في `time`: الوجبة، `Lunch` للغداء أو `Dinner` للعشاء.
- في `size`: عدد أفراد مجموعة الزبائن.

**المصدر:** Bryant, P. G. and Smith, M. (1995), *Practical Data Analysis: Case Studies in Business Statistics*. Homewood, IL: Richard D. Irwin Publishing. [نسخة CSV في مستودع بيانات Seaborn](https://github.com/mwaskom/seaborn-data/blob/master/tips.csv).



تتوفر المجموعة أيضًا عبر [Seaborn](https://seaborn.pydata.org/generated/seaborn.load_dataset.html) باستخدام `sns.load_dataset("tips")`.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("tips"))
```

## Download

- [Download tips.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/tips.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
