# بيانات الطول والوزن SOCR

<!-- academy-data
{
  "title": "بيانات الطول والوزن SOCR",
  "files": [
    {
      "name": "socr-height-weight/original",
      "file": "SOCR-HeightWeight.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/SOCR-HeightWeight.csv",
      "legacyPath": "/data/SOCR-HeightWeight.csv"
    },
    {
      "name": "socr-height-weight/modified",
      "file": "SOCR-HeightWeight_modified.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/SOCR-HeightWeight_modified.csv",
      "legacyPath": "/data/SOCR-HeightWeight_modified.csv"
    }
  ]
}
-->

**الوصف:** بيانات تعليمية مولّدة لمحاكاة العلاقة بين الطول والوزن عند عمر 18 سنة؛ ليست 25,000 قياس ميداني مباشر.

**وحدة البيانات والحجم:** سجل محاكاة؛ 25,000 صف في كل نسخة؛ الأصل 3 أعمدة، والمعدّل 5 أعمدة.

**التفاصيل:**

- يصف SOCR البيانات بأنها مولّدة بالمحاكاة. الملف الذي ينتهي اسمه بـ `_modified` نسخة معدّلة داخل مواد الدورة.
- يذكر SOCR أن المحاكاة مبنية على مسح نمو بهونغ كونغ سنة 1993 شمل أطفالًا من الميلاد حتى 18 سنة، جُنّدوا عبر مراكز صحة الأم والطفل والمدارس.
- في `Index`: رقم السجل.
- في `Height(Inches)`: الطول بالبوصة.
- في `Weight(Pounds)`: الوزن بالرطل.
- في `Height(m)` و`Weight(kg)`: الطول بالمتر والوزن بالكيلوغرام.
- في `BMI`: مؤشر كتلة الجسم.
- في `classification`: فئة مشتقة. هذه الإضافات تخص النسخة المعدّلة، ولا تصف قياسات جمعها SOCR مستقلة.
- هونغ كونغ و 1993 يخصان المسح الذي استندت إليه المحاكاة.
- لا توجد تواريخ أو أماكن رصد مستقلة لسجلات المحاكاة.

**المصدر:** [شرح SOCR لأصل المحاكاة ووحدات القياس](https://wiki.socr.umich.edu/index.php/SOCR_Data_Dinov_020108_HeightsWeights). الأعمدة الإضافية متحقق منها في ملف الدورة المعدّل.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("socr-height-weight/original"))
data = pd.read_csv(academy.get_data_url("socr-height-weight/modified"))
```

## Download

- [Download SOCR-HeightWeight.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/SOCR-HeightWeight.csv)
- [Download SOCR-HeightWeight_modified.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/SOCR-HeightWeight_modified.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
