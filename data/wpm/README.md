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

**الوصف:** بيانات جُمعت في الصف من اختبار سرعة الكتابة في حالتين: إطفاء الإضاءة وتشغيلها، لاستكشاف قدرة الطلاب على الكتابة دون النظر إلى لوحة المفاتيح.

**وحدة البيانات والحجم:** نتيجة اختبار لطالب واحد؛ 26 صفًا وعمودان. يمثّل كل صف طالبًا مختلفًا.

**التفاصيل:**

- `wpm`: سرعة الكتابة بالكلمات في الدقيقة.
- `light`: حالة الإضاءة أثناء الاختبار؛ `True` تعني أن الإضاءة مشغّلة، و`False` تعني أنها مطفأة.
- أجرى الطلاب الاختبار تحت إحدى حالتي الإضاءة، بهدف استكشاف من يستطيع الكتابة دون النظر إلى لوحة المفاتيح.
- لا تمثّل الصفوف قياسين متكرّرين للطالب نفسه؛ كل نتيجة تخصّ طالبًا مختلفًا.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("wpm"))
```

## Download

- [Download wpm.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/wpm.csv)
