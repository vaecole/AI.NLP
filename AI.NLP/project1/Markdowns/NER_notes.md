## 实体命名识别（NER）
- BIOSE标注体系参考https://ltp.readthedocs.io/zh_CN/latest/appendix.html#id4 ：
    - 命名实体识别标注集
    - NE识别模块的标注结果采用O-S-B-I-E标注形式，其含义为

        | 标记 | 含义 |
        | ---- | ---- |
        | O | 这个词不是NE |
        | S | 这个词单独构成一个NE |
        | B | 这个词为一个NE的开始 |
        | I | 这个词为一个NE的中间 |
        | E | 这个词位一个NE的结尾 |
    - LTP中的NE 模块识别三种NE，分别如下：

        | 标记 | 含义 |
        | --- | --- |
        | Nh | 人名 |
        | Ni | 机构名 |
        | Ns | 地名 |
