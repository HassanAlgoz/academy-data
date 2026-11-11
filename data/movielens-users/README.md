# بيانات المستخدمين MovieLens

<!-- academy-data
{
  "title": "بيانات المستخدمين MovieLens",
  "files": [
    {
      "name": "movielens-users",
      "file": "users.csv",
      "delimiter": "|",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/users.csv",
      "legacyPath": "/data/users.csv"
    }
  ]
}
-->

**الوصف:** مجموعة بحثية لأنظمة توصية الأفلام؛ بيانات المستخدمين جزء من MovieLens 100K الذي يضم 100,000 تقييم لـ 1,682 فيلمًا.

**وحدة البيانات والحجم:** مستخدم؛ 943 صفًا و 5 أعمدة في ملف الدورة. لا يحتوي هذا الملف تقييمات الأفلام نفسها.

**التفاصيل:**

- يستخدم الملف بيانات المستخدمين `u.user` من MovieLens 100K، مع رأس للأعمدة وفاصل `|`؛ الوصف من توثيق GroupLens في جامعة مينيسوتا.
- جُمعت المجموعة عبر موقع MovieLens من 19 سبتمبر 1997 إلى 22 أبريل 1998.
- في `user_id`: معرّف المستخدم.
- في `age`: العمر.
- في `gender`: الجنس.
- في `occupation`: المهنة.
- في `zip_code`: الرمز البريدي، وينبغي الاحتفاظ به نصًا لحماية الأصفار البادئة.
- جمعها مشروع GroupLens بجامعة مينيسوتا عبر الموقع.
- استُبعد من له أقل من 20 تقييمًا أو معلومات ديموغرافية غير مكتملة. ليست عينة عشوائية من عموم السكان.
- يوجد رمز بريدي، لكن README لا يحدّد إطار معاينة جغرافيًا نعتبره بلد إقامة لكل مستخدم.

**المصدر:** [README الأصلي، شروط الاختيار ووصف الملفات](https://files.grouplens.org/datasets/movielens/ml-100k/README).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("movielens-users"), sep='|')
```

## Download

- [Download users.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/users.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
