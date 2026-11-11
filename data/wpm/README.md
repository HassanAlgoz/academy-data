# سرعة الكتابة WPM

<!-- academy-data
{
  "title": "سرعة الكتابة WPM",
  "files": [
    {
      "name": "wpm",
      "file": "wpm.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/wpm.csv",
      "legacyPath": "/data/wpm.csv"
    }
  ]
}
-->

**الوصف:** مثال يربط سرعة الكتابة بوجود الإضاءة.

**وحدة البيانات والحجم:** قياس مسجّل؛ 26 صفًا وعمودان. لا يوجد معرّف يثبت أنه شخص مختلف في كل صف.

**التفاصيل:**

- في `wpm`: كلمات في الدقيقة.
- في `light`: وجود الإضاءة، بقيمتي True وFalse.
- لا يوجد في مواد الدورة بروتوكول اختبار أو توزيع عشوائي للإضاءة أو بيانات مشاركين أو تاريخ ومكان.
- لا ننسب الملف إلى تجربة منشورة.

**المصدر:** درس القراءة والكتابة. مثال تعليمي من مواد الدورة، بلا مصدر خارجي موثّق.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("wpm"))
```

## Download

- [Download wpm.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/wpm.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
