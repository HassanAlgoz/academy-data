# بيانات الدخل Adult

<!-- academy-data
{
  "title": "بيانات الدخل Adult",
  "files": [
    {
      "name": "adult",
      "file": "adult.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/adult.csv",
      "legacyPath": "/data/adult.csv"
    }
  ]
}
-->

**الوصف:** تصنيف ما إذا كان دخل الفرد السنوي يتجاوز 50,000 دولار اعتمادًا على خصائص ديموغرافية واقتصادية.

**وحدة البيانات والحجم:** سجل فرد؛ المجموعة الأصلية 48,842 سجلًا و 14 متغيرًا تفسيريًا؛ نسخة الدورة 32,561 صفًا و 15 عمودًا، وهي حجم مجموعة التدريب.

**التفاصيل:**

- استخراج من قاعدة تعداد 1994.
- إيداعها في UCI سنة 1996 ليس تاريخ جمع الأفراد.
- استخرجها Barry Becker، بشروط: `AAGE > 16`، و`AGI > 100`، و`AFNLWGT > 1`، و`HRSWK > 0`. توجد قيم مفقودة.
- العمر، قطاع العمل، الوزن السكاني `fnlwgt`، التعليم ومستواه العددي، الحالة الزوجية، المهنة، العلاقة الأسرية، العرق، الجنس، مكاسب رأس المال وخسائره، ساعات العمل الأسبوعية وبلد الميلاد.
- في `income`: ‏`<=50K` أو `>50K`.
- في `native-country`: بلد الميلاد، فلا نقرأه بوصفه موقع المقابلة أو الإقامة.

**المصدر:** [بطاقة Adult وشروط الاستخراج وقاموس المتغيرات](https://archive.ics.uci.edu/dataset/2/adult). حجم نسخة الدورة متحقق منه في الملف.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("adult"))
```

## Download

- [Download adult.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/adult.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
