# بيانات استهلاك الوقود Auto MPG

<!-- academy-data
{
  "title": "بيانات استهلاك الوقود Auto MPG",
  "files": [
    {
      "name": "auto-mpg/mpg",
      "file": "mpg.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/mpg.csv",
      "legacyPath": "/data/mpg.csv"
    },
    {
      "name": "auto-mpg/cars1",
      "file": "cars1.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/exercises/04/02_merge/cars1.csv",
      "legacyPath": "/notebook/exercises/04/02_merge/cars1.csv"
    },
    {
      "name": "auto-mpg/cars2",
      "file": "cars2.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/exercises/04/02_merge/cars2.csv",
      "legacyPath": "/notebook/exercises/04/02_merge/cars2.csv"
    }
  ]
}
-->

**الوصف:** دراسة استهلاك الوقود في دورة قيادة داخل المدينة، والتنبؤ بـ `mpg` من خصائص السيارة.

**وحدة البيانات والحجم:** سجل سيارة؛ 398 صفًا و 9 أعمدة في `mpg.csv`. ملفا الدمج يحتويان 198 و 200 صف على الترتيب؛ في `cars1.csv` أيضًا خمسة أعمدة بلا أسماء.

**التفاصيل:**

- `mpg.csv` نسخة seaborn من Auto MPG؛ يستخدم تمرين الدمج الملفين `cars1.csv` و`cars2.csv` بأعمدة السيارات نفسها. هذه ليست مجموعة `mpg` المختلفة التي توزّعها ggplot2.
- سنوات الطراز 1970–1982 في الملف.
- `origin` يميز الولايات المتحدة وأوروبا واليابان، ولا يحدد مكان اختبار السيارة.
- في `mpg`: كفاءة الوقود بالميل لكل غالون.
- في `cylinders`: الأسطوانات.
- في `displacement`: إزاحة المحرك.
- في `horsepower`: القدرة.
- في `weight`: الوزن.
- في `acceleration`: متغير التسارع.
- في `model_year`: سنة الطراز.
- في `origin`: المنشأ.
- في `name`: الاسم.
- انتقلت المجموعة من مكتبة StatLib بجامعة Carnegie Mellon.
- استُبعدت 8 حالات لا تتوفر لها قيمة `mpg`. توجد قيم مفقودة للقدرة.
- بطاقة UCI لا تفصّل أجهزة القياس أو بروتوكول دورة القيادة أو وحدات جميع الحقول.
- لا نفترض أن `acceleration` له تعريف متغير التسارع في بيانات السيارات الهجينة.

**المصدر:** [بطاقة Auto MPG ومعلومات إعدادها](https://archive.ics.uci.edu/dataset/9/auto+mpg). سنوات الطراز وتوزيع ملفات الدمج متحقق منها في ملفات الدورة.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("auto-mpg/mpg"))
data = pd.read_csv(academy.get_data_url("auto-mpg/cars1"))
data = pd.read_csv(academy.get_data_url("auto-mpg/cars2"))
```

## Download

- [Download mpg.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/mpg.csv)
- [Download cars1.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/cars1.csv)
- [Download cars2.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/cars2.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
