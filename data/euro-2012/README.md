# بيانات بطولة أوروبا Euro 2012

<!-- academy-data
{
  "title": "بيانات بطولة أوروبا Euro 2012",
  "files": [
    {
      "name": "euro-2012",
      "file": "Euro_2012_stats_TEAM.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/exercises/03/02_filtering_and_sorting/Euro_2012_stats_TEAM.csv",
      "legacyPath": "/notebook/exercises/03/02_filtering_and_sorting/Euro_2012_stats_TEAM.csv"
    }
  ]
}
-->

**الوصف:** إحصاءات مجمّعة لأداء الفرق في Euro2012 ؛ الصف يصف فريقًا على مستوى البطولة، لا مباراة أو لاعبًا.

**وحدة البيانات والحجم:** فريق؛ 16 صفًا و 35 عمودًا في نسخة الدورة.

**التفاصيل:**

- تتوفر نسخة الملف في مستودع تمارين pandas، دون بطاقة وصف للمجموعة أو إسناد موثّق إلى ناشر الإحصاءات الأصلي.
- الأهداف والتسديدات ودقتها، ضرب القائم، أهداف الجزاء والرأس.
- منها `Goals` و`Shots on target` و`Shooting Accuracy`.
- التمريرات والمكتملة ودقتها، اللمسات والعرضيات والمراوغات والركنيات، الافتكاك والإبعاد والاعتراض والتصديات والأهداف المستقبلة.
- الأخطاء والتسلل والبطاقات الصفراء والحمراء والتبديلات وعدد اللاعبين المستخدمين.
- اسم الملف يحدد البطولة والسنة.
- نسخة المستودع لا توثّق مزوّد الأحداث، أو قواعد ترميز كل إحصاء، أو مواعيد تسجيله. هذه المعلومات غير متحققة لهذا الملف.

**المصدر:** [ملف تمارين pandas](https://github.com/guipsamora/pandas_exercises/blob/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv). أسماء المتغيرات والحجم مأخوذة من ملف الدورة نفسه.

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("euro-2012"))
```

## Download

- [Download Euro_2012_stats_TEAM.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/Euro_2012_stats_TEAM.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
