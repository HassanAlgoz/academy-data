# بيانات الزهور Iris

<!-- academy-data
{
  "title": "بيانات الزهور Iris",
  "files": [
    {
      "name": "iris",
      "file": "iris.csv",
      "delimiter": ",",
      "hasHeader": false,
      "legacySource": "/notebooks/ds-202-data-analysis/data/iris.csv",
      "legacyPath": "/data/iris.csv",
      "columns": [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "class"
      ]
    }
  ]
}
-->

**الوصف:** تصنيف نباتات Iris من القياسات؛ مجموعة مرتبطة بعمل Fisher سنة 1936. سنة إيداعها لدى UCI، 1988 ، ليست سنة جمع القياسات.

**وحدة البيانات والحجم:** عينة نبات؛ 150 سجلًا، 50 لكل نوع، وأربعة قياسات مع عمود التصنيف. الملف بلا صف أسماء للأعمدة؛ السطر الفارغ الأخير ليس ملاحظة.

**التفاصيل:**

- طول السبلة وعرضها، وطول البتلة وعرضها، جميعها بالسنتيمتر.
- أسماء الدورة: `sepal_length` و`sepal_width` و`petal_length` و`petal_width`.
- في `class`: ‏Iris-setosa أو Iris-versicolor أو Iris-virginica.
- بطاقة UCI توثّق القياسات ووحداتها، لكنها لا تفصّل في البطاقة بروتوكول القياس الميداني أو موقع جمع كل عينة.
- لا توجد قيم مفقودة حسب UCI.
- وتنبّه البطاقة إلى اختلافات في عينتين بين البيانات المنشورة ومقال Fisher.

**المصدر:** [بطاقة UCI وقاموس المتغيرات والتنبيه على العينات](https://archive.ics.uci.edu/dataset/53/iris).

## Usage

```python
import academy
import pandas as pd

data = pd.read_csv(academy.get_data_url("iris"), header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
```

## Download

- [Download iris.csv](https://github.com/HassanAlgoz/academy-data/releases/download/v1/iris.csv)

## Attribution and redistribution

The source and adaptations are described above. Original datasets retain their upstream terms; inclusion here does not grant a new license over third-party data. No additional redistribution license is asserted where the original course materials did not document one.
