# Example 09 — honest stop condition

Route: `capability_boundary` → profile status → stop before unsupported claim.

## 母版锁

~~~text
【母版锁】

任务要求参考输入高保真锁定身份，但当前生成器配置对该能力记录为未知且未测试；不得把分析报告当作实测，角标规则仍为“T1 to 9”。

~~~

## 分镜

~~~text
【分镜】

先输出分析、控制合同与待测验收检查；不宣称已经生成，不把未验证的参考保真度或实时校准写成成功。

~~~

## 通用负面提示词

~~~text

禁止伪造结果编号、伪造视觉通过、伪造接口调用、伪造参考保真度；除右下角指定的“T1 to 9”外禁止其他文字。

~~~

Acceptance: status remains UNKNOWN/UNTESTED or NOT_RUN until evidence exists.
