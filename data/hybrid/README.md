# بيانات السيارات الهجينة Hybrid Cars

<!-- academy-data
{
  "title": "بيانات السيارات الهجينة Hybrid Cars",
  "files": [
    {
      "name": "hybrid",
      "file": "hybrid.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/hybrid.csv",
      "legacyPath": "/data/hybrid.csv"
    }
  ]
}
-->

**الوصف:** دراسة العلاقات بين السعر وكفاءة الوقود والتسارع في السيارات الهجينة المبيعة في الولايات المتحدة.

**وحدة البيانات والحجم:** سجل طراز وسنة؛ 153 صفًا و 6 أعمدة في الملف، وليس عدد وحدات السيارات المبيعة.

**التفاصيل:**

- يذكر كتاب Computational and Inferential Thinking أن البيانات مقتبسة من أرشيف الأستاذ Larry Winner في جامعة فلوريدا.
- الولايات المتحدة، 1997–2013.
- الأسعار معدّلة إلى دولارات 2013.
- في `vehicle`: الطراز.
- في `year`: سنة الصنع.
- في `class`: فئة السيارة، مثل Compact وSUV.
- في `msrp`: سعر التجزئة المقترح من المصنع.
- في `acceleration`: معدل التسارع بوحدة كيلومتر/ساعة لكل ثانية.
- في `mpg`: كفاءة الوقود بالميل لكل غالون.
- الكتاب يذكر تكييف البيانات من أرشيف Larry Winner بجامعة فلوريدا، لكنه لا يعرض في هذا الفصل بروتوكول اختبار التسارع والوقود أو طريقة اختيار الطرازات.

**المصدر:** [تعريف الأعمدة والوحدات في الكتاب](https://inferentialthinking.com/chapters/15/1/correlation/). عدد السجلات من ملف الدورة.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("hybrid"))
```

## Download

- [Download hybrid.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/hybrid.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
