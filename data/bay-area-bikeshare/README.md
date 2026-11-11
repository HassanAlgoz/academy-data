# بيانات رحلات الدراجات Bay Area Bike Share

<!-- academy-data
{
  "title": "بيانات رحلات الدراجات Bay Area Bike Share",
  "files": [
    {
      "name": "bay-area-bikeshare/stations",
      "file": "station.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/bay_area_bikeshare/station.csv",
      "legacyPath": "/data/bay_area_bikeshare/station.csv"
    },
    {
      "name": "bay-area-bikeshare/trips",
      "file": "trip.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/bay_area_bikeshare/trip.csv",
      "legacyPath": "/data/bay_area_bikeshare/trip.csv"
    }
  ]
}
-->

**الوصف:** سجلات تشغيل خدمة مشاركة الدراجات، لدراسة الاستخدام والمدة وحركة الرحلات بين المحطات.

**وحدة البيانات والحجم:** `trip.csv`: رحلة، 354,152 صفًا و 11 عمودًا؛ `station.csv`: محطة، 70 صفًا و 7 أعمدة. عدد الرحلات ليس عدد راكبين مختلفين.

**التفاصيل:**

- ملفا الدورة نسخة تاريخية للفترة 2014–2015 ، يصفها مرجع الكتاب المرتبط أدناه.
- بدايات الرحلات في الملف من 1 سبتمبر 2014 إلى 31 أغسطس 2015.
- محطات في San Francisco وSan Jose وMountain View وPalo Alto وRedwood City.
- المعرّف، المدة بالثواني، وقتا البداية والنهاية، اسما المحطتين ورمزاهما، رقم الدراجة، نوع الاشتراك والرمز البريدي.
- المعرّف والاسم، خطا العرض والطول، عدد مواضع الإرساء، المدينة `landmark`، وتاريخ التركيب `installation`.
- سجلات تأجير نشرها المشغّل.
- توثيق الكتاب يطابق عدد رحلات النسخة وفترتها. لا يشرح الكتاب أجهزة تسجيل العمليات أو كل قواعد استبعاد الرحلات.

**المصدر:** [توثيق النسخة التاريخية في كتاب Berkeley](https://inferentialthinking.com/chapters/08/5/bike-sharing-in-the-bay-area/index.html)، و[صفحة المشغّل الحالية](https://lyftbikes.com/system-data). مواقع المحطات وحدود التواريخ الدقيقة من الملفين.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("bay-area-bikeshare/stations"))
data = pd.read_csv(academy.get_data_url("bay-area-bikeshare/trips"))
```

## Download

- [Download station.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/station.csv)
- [Download trip.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/trip.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
