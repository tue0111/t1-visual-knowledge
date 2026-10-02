# Example 02 — reference-guided material edit

Route: `reference_guided` → `CARRY identity` + `REPAIR material` → `control_contract`.

## 母版锁

~~~text
【母版锁】

保留参考图中同一个成年人物的脸部辨识度、身体比例、服装轮廓与镜头角度；材质改为半透明石蜡，右下角仅保留准确的“T1 to 9”角标。

~~~

## 分镜

~~~text
【分镜】

只改变袖口与肩部的材质：出现薄层透光、边缘吸收暖光、褶皱保持原有方向；身份、姿态、构图、背景与文字位置不变。

~~~

## 通用负面提示词

~~~text

除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止换脸、改姿势、改镜头、塑料透明、无厚度材质。

~~~

Acceptance: material change visible; identity and composition preserved.
