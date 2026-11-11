# جدول الأعداد ABC

<!-- academy-data
{
  "title": "جدول الأعداد ABC",
  "files": [
    {
      "name": "abc",
      "file": "abc.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/abc.csv",
      "legacyPath": "/data/abc.csv"
    }
  ]
}
-->

**الوصف:** جدول أعداد أُنشئ في الصف للتدرّب على قراءة البيانات ومعالجتها وحفظها.

**وحدة البيانات والحجم:** صف من الأعداد؛ صفّان وثلاثة أعمدة: `a` و`b` و`c`.

**التفاصيل:**

- يحتوي الجدول على الأعداد من 1 إلى 6، مفصولة بفواصل، مع سطر أول لأسماء الأعمدة.
- هذه أعداد تعليمية أُنشئت في الصف، وليست قياسات لدراسة.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("abc"))
```

## Download

- [Download abc.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/abc.csv)
