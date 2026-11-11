# بيانات طلبات المطعم Chipotle

<!-- academy-data
{
  "title": "بيانات طلبات المطعم Chipotle",
  "files": [
    {
      "name": "chipotle",
      "file": "chipotle.tsv",
      "delimiter": "\t",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/chipotle.tsv",
      "legacyPath": "/data/chipotle.tsv"
    }
  ]
}
-->

**الوصف:** بيانات مقال The Upshot عن الأصناف التي يطلبها زبائن Chipotle فعليًا.

**وحدة البيانات والحجم:** بند في طلب؛ 4,622 صفًا و 5 أعمدة، تمثّل 1,834 معرّف طلب مختلفًا. قد يضم الطلب عدة بنود، وقد تزيد كمية البند على واحد.

**التفاصيل:**

- حُفظت نسخة الدورة من مستودع Kevin Markham؛ يربط مستودعه بمصدر The Upshot الأصلي.
- في `order_id`: معرّف الطلب.
- في `quantity`: الكمية.
- في `item_name`: الصنف.
- في `choice_description`: الاختيارات والإضافات.
- في `item_price`: السعر المسجّل للبند.
- نص مفصول بعلامة الجدولة.
- السعر مخزّن مع علامة الدولار، والاختيارات نصوص وليست أعمدة مستقلة لكل إضافة.
- المقال مؤرخ في 17 فبراير 2015 ، لكن ملف البيانات لا يحتوي تواريخ طلبات أو مواقع فروع. README لا يشرح آلية الحصول على الطلبات أو اختيارها.
- تاريخ المقال ليس فترة الرصد.

**المصدر:** [مستودع The Upshot](https://github.com/TheUpshot/chipotle)، و[المقال المرتبط به](https://www.nytimes.com/interactive/2015/02/17/upshot/what-do-people-actually-order-at-chipotle.html).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("chipotle"), sep='\t')
```

## Download

- [Download chipotle.tsv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/chipotle.tsv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
