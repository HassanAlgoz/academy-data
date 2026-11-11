# بيانات الألماس Diamonds

<!-- academy-data
{
  "title": "بيانات الألماس Diamonds",
  "files": [
    {
      "name": "diamonds",
      "file": "diamonds.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/diamonds.csv",
      "legacyPath": "/data/diamonds.csv"
    }
  ]
}
-->

**الوصف:** وصف أسعار ألماس ذي قطع دائري وخصائصه، ودراسة علاقتها بالسعر.

**وحدة البيانات والحجم:** سجل ألماسة؛ 53,940 صفًا و 10 أعمدة.

**التفاصيل:**

- في `price`: السعر بالدولار الأمريكي.
- في `carat`: الكتلة بالقيراط.
- في `cut`: جودة القطع من Fair إلى Ideal.
- في `color`: اللون من D الأفضل إلى J الأسوأ.
- في `clarity`: درجة النقاء من I1 إلى IF.
- في `x` و`y` و`z`: الطول والعرض والعمق بالملليمتر.
- في `depth`: نسبة العمق الكلي.
- في `table`: عرض السطح العلوي نسبةً إلى أوسع جزء.
- توثيق ggplot2 يعرّف المتغيرات ونطاقاتها، لكنه لا يبيّن في هذه الصفحة متجر الجمع أو تاريخه أو أجهزة القياس أو ما إذا كان السعر سعر عرض أم بيع فعلي.
- نطاقات التوثيق تتضمن أبعادًا تساوي صفرًا.
- وجود قيمة في الملف لا يجعلها قياسًا صالحًا تلقائيًا.

**المصدر:** [قاموس diamonds ووحداته ونطاقاته](https://ggplot2.tidyverse.org/reference/diamonds.html).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("diamonds"))
```

## Download

- [Download diamonds.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/diamonds.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
