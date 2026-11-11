# بيانات السكان حسب العمر والجنس U.S. Census

<!-- academy-data
{
  "title": "بيانات السكان حسب العمر والجنس U.S. Census",
  "files": [
    {
      "name": "us-census",
      "file": "nc-est2019-agesex-res.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/nc-est2019-agesex-res.csv",
      "legacyPath": "/data/nc-est2019-agesex-res.csv"
    }
  ]
}
-->

**الوصف:** تقدير أعداد السكان المقيمين حسب العمر والجنس، ومتابعة تغيرها بين السنوات.

**وحدة البيانات والحجم:** فئة عمر وجنس؛ 306 صفوف و 14 عمودًا. الصف ليس شخصًا؛ بعض الصفوف مجاميع تتداخل مع الصفوف التفصيلية.

**التفاصيل:**

- يتناول توثيق مكتب الإحصاء هذا الملف بعينه، للفترة من 1 أبريل 2010 إلى 1 يوليو 2019.
- الولايات المتحدة.
- تعداد وأساس تقدير في 1 أبريل 2010 ، وتقديرات في 1 يوليو لكل سنة من 2010 إلى 2019.
- نشر الملف في أبريل 2020.
- في `SEX`: الرمز 0 للمجموع، و 1 للذكور، و 2 للإناث.
- في `AGE`: الأعمار 0–99 ، و 100 لفئة 100 سنة فأكثر، و 999 لمجموع الأعمار.
- في `CENSUS2010POP`: تعداد 2010.
- في `ESTIMATESBASE2010`: أساس التقديرات.
- في `POPESTIMATE2010` إلى `POPESTIMATE2019`: التقدير السنوي.
- تقديرات مكتب الإحصاء مبنية على تعداد 2010 ، مع تعديلات برنامج مراجعة نتائج التعداد.
- ليست إعادة عدّ ميداني شامل كل سنة.

**المصدر:** [تعريف حقول الملف](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nc-est2019-agesex-res.pdf)، و[منهجيات التقديرات السكانية](https://www.census.gov/programs-surveys/popest/technical-documentation/methodology.html).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("us-census"))
```

## Download

- [Download nc-est2019-agesex-res.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/nc-est2019-agesex-res.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
