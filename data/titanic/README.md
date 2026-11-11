# بيانات تيتانيك Titanic

<!-- academy-data
{
  "title": "بيانات تيتانيك Titanic",
  "files": [
    {
      "name": "titanic",
      "file": "titanic.csv",
      "delimiter": ",",
      "hasHeader": true,
      "legacySource": "/notebooks/ds-202-data-analysis/data/titanic.csv",
      "legacyPath": "/data/titanic.csv"
    }
  ]
}
-->

**الوصف:** بيانات ركاب ونتائج نجاة، تُستخدم لدراسة علاقة خصائص الراكب بالنجاة في كارثة تيتانيك.

**وحدة البيانات والحجم:** راكب؛ 891 صفًا و 12 عمودًا في ملف الدورة. العدد يخص هذا الملف، وليس جميع من كانوا على السفينة.

**التفاصيل:**

- مصدر الملف المحفوظ هو مستودع pandas؛ يشرح توثيقه الأعمدة، ويربط بملف البيانات نفسه.
- رحلة تيتانيك سنة 1912.
- يتضمن `Embarked` رمز ميناء الصعود، وليس موقع الراكب وقت الغرق.
- في `Survived`: النجاة، 0 أو 1.
- في `Pclass`: فئة التذكرة، 1 أو 2 أو 3.
- في `PassengerId` و`Name`: معرّف الراكب واسمه.
- في `Sex`: الجنس.
- في `Age`: العمر بالسنوات.
- في `SibSp`: عدد الإخوة أو الأزواج المرافقين.
- في `Parch`: عدد الوالدين أو الأبناء المرافقين.
- في `Ticket`: التذكرة.
- في `Fare`: الأجرة.
- في `Cabin`: المقصورة.
- في `Embarked`: ميناء الصعود. توجد قيم مفقودة، ومنها العمر والمقصورة.
- pandas يوزّع الملف ويوثّق الأعمدة، لكنه لا يشرح في هذه الصفحة كيفية إعادة بناء سجلات الركاب التاريخية. لا نستنتج منها بروتوكول جمع أولي.

**المصدر:** [قاموس الأعمدة ونسخة pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)، و[بطاقة مسابقة Titanic](https://www.kaggle.com/competitions/titanic/data).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("titanic"))
```

## Download

- [Download titanic.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/titanic.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
