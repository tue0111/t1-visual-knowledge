# Example 01 — single hero / Sunburst

Route: `single_image` → `gpt-image-2.5-sunburst` → semantic review.

## 母版锁

~~~text
【母版锁】

成年女性肖像，身份、发型、服装结构与右下角极小清晰的“T1 to 9”角标固定；摄影写实，暖灰背景退后，皮肤保留真实微纹理。

~~~

## 分镜

~~~text
【分镜】

半身三分之二侧身，第一视觉落在眼神，第二视觉落在肩线与衣料折痕；只改变主光从左前方移动到左上方，保留脸部身份、裁切、镜头距离与背景角色。

~~~

## 通用负面提示词

~~~text

除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止身份漂移、改变裁切、塑料皮肤、全画面同样清晰。

~~~

Acceptance: identity remains recognizable; light direction changes; no unrelated pose or crop change.
