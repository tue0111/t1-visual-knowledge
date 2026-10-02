# W2 — VÍ DỤ ĐẦY ĐỦ (có chú thích trục)

status: v0.1 CANDIDATE · author: Claude · date: 2026-10-02
Các prompt dưới đây **chưa chạy thử**; chúng minh hoạ cách phân cấp trục, không phải bằng chứng. Chú thích `[K…·chính/phụ]` chỉ để học — **xoá khi dùng thật**.
Brand rule và câu negative brand chép từ `core/00_PROJECT_CONTRACT.md`.

---

## Ví dụ 1 — Cinema: thiếu nữ thắp đèn lồng trên lầu tuyết

Bảng quyết định (M1): cinema · xem lâu · đọc: mặt ấm → ánh nhìn ra ngoài khung → sân tuyết lạnh · **chính K1** · phụ K7, K6 · bảo vệ K7 (nhìn ống kính), K1 (tia sáng vô cớ).

```text
【母版锁 · 雪楼灯影】

单张电影剧照质感的写实画面，观众像在场景中旁观一个正在发生的瞬间，而不是被画中人注视。
画面中所有光线都有合理来源：画内的灯笼，或夜空与雪地的微弱冷色环境光；不使用无来源的轮廓光或补光。
【固定品牌角标】
画面右下角仅允许出现一个极小、克制、清晰的衬线体品牌角标“T1 to 9”。文字必须逐字准确，大小写与空格完全一致。角标使用与画面协调的低亮度暖白色、古金色或冷灰色，不发光、不加边框、不遮挡主体、不抢夺视觉焦点。除此之外禁止任何其他文字、标志、签名和水印。
每次只生成一张指定画面，不生成拼图、九宫格或多个备选。

【分镜 · 点灯】

横幅 2.39:1。相机位于二楼回廊内侧，前景一根木柱遮住画面左边约四分之一并轻微虚化，人物位于画面右三分之一，中景，平视。
[K1·chính] 她手中刚点亮的纸灯笼是画面中唯一的暖光源，从左下方照亮她的侧脸、下巴和袖口，脸上明暗分明但暗部保留细节；木栏杆在灯笼光下向右投出长影，光照范围之外迅速衰减成深暗。
[K7·phụ] 她刚放下火折子，另一只手仍提着灯笼的竹柄，视线落向画外左下方的庭院，嘴唇微启。
[K6·phụ] 夜雪细细落下，靠近灯笼的雪花被照成暖色小点，远处庭院在雪中变淡，保持冷蓝阴影。

【通用负面提示词】

人物直视镜头，画面中出现多个暖色光源，体积光光束，全画面同样清晰，蜡质皮肤，手指畸形或多指，现代物品。
除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止角标拼写错误、大小写错误、空格错误、缺字、多字、重复或乱码。
```

Ghi chú:
- K1 có 3 bằng chứng (mặt, bóng lan can, vùng tối ngoài tầm), có mức sàn (暗部保留细节).
- K7, K6 mỗi trục **một câu**.
- Câu K1 đứng trước câu K7 dù `core/03` §2 xếp ánh sáng sau tư thế: đây là **ngoại lệ có chủ ý** (W1 §4) — khi trục chính nằm ở khối sau, được kéo lên đầu 分镜 sau câu khung/máy.
- "Không nhìn ống kính" chỉ ghi ở 母版锁 (người xem là kẻ đứng ngoài) + câu đích ánh nhìn + negative; không lặp thêm (`core/03` §7).
- K2 không phải trục, nhưng câu máy có vật tiền cảnh vì cinema cần "máy trong không gian" (M2 §3) — đây là khoá chế độ, không phải trục chính.
- "体积光光束" trong negative: điều kiện tia sáng không đủ (thiếu khe), nên chặn (K6 §2.3).

## Ví dụ 2 — Poster: thiếu nữ và cửu vĩ hồ băng

Bảng: poster · vài giây · đọc: đầu cáo khổng lồ + mặt người → hai ánh nhìn → đuôi xoè · **chính K2 + K3** (cùng một hiệu ứng tỷ lệ + ánh nhìn) · phụ K4, K5 · bảo vệ K1 (không bóng → ghép).

```text
【母版锁 · 冰狐】

写实摄影质感的角色主视觉海报，单一主体组合：白发巫女与巨大的九尾冰狐。
配色角色：人物服装取自冰狐的配色——冰白、雾蓝与少量银色；背景为大片平整的暖杏色傍晚天空，与主体形成冷暖互补。
冰狐保持原有的轮廓与毛色分区，只增加真实的毛发与湿润眼睛的细节。
【固定品牌角标】
画面右下角仅允许出现一个极小、克制、清晰的衬线体品牌角标“T1 to 9”。文字必须逐字准确，大小写与空格完全一致。角标使用与画面协调的低亮度暖白色、古金色或冷灰色，不发光、不加边框、不遮挡主体、不抢夺视觉焦点。除此之外禁止任何其他文字、标志、签名和水印。
每次只生成一张指定画面，不生成拼图、九宫格或多个备选。

【分镜 · 仰视】

竖幅 3:4。
[K2·chính] 相机贴近雪地向上仰拍，距离冰狐头部很近，狐鼻吻在画面下方占据约三分之一，明显大于人物上半身；人物站在狐头后方中景，双腿被拉长但五官比例正常；地平线压到画面下五分之一，天空占据大部分画面。
[K3·chính] 人物与冰狐同时直视镜头，形成两个并列的焦点；九条狐尾在人物身后呈扇形张开，构成背景光环；人物面部为主体中最亮处。
[K5·phụ] 狐毛尖端透光，鼻头湿润，眼睛有清晰的环境反射。
[K1·bảo vệ] 傍晚低角度阳光从人物右后方照来，人物与冰狐在雪地上投下指向镜头的清晰长影，冰狐脚下有接触阴影，人物面部保留细节。

【通用负面提示词】

人物与狐狸像拼贴，没有接触阴影，狐狸失去原有轮廓或配色，红色圆盘或红日，背景元素与人物、冰狐争夺焦点，蜡质皮肤，手指畸形或多指，广角导致的人脸变形。
除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止角标拼写错误、大小写错误、空格错误、缺字、多字、重复或乱码。
```

Ghi chú:
- K4 nằm ở 母版锁 vì là vai màu ổn định (W1 §3).
- K1 không phải trục chính nhưng có câu riêng vì attractor "ghép" (M1 B6).
- Nếu làm series, đổi ≥ 2/4 trục casebook C01 (khoảng cách, góc máy, hành động, chủ tiêu điểm) mỗi ảnh — ví dụ ảnh 2 dùng máy ngang ngực, khoảng cách xa.
- Hình học bóng: mặt trời ở phía sau-phải nhân vật, cáo ở gần máy → bóng đổ **về phía máy**, không thể đổ lên chân người. Bầu trời màu mơ ấm → mặt trời thấp (傍晚), không phải buổi chiều cao. Mặt người ngược sáng không thể sáng hơn bầu trời → "chủ thể sáng nhất trong các chủ thể".

## Ví dụ 3 — Candid: ông lão xe bánh mì qua cầu

Bảng: candid nghiêng cinema · đọc: ông lão + xe → cây cầu, dòng sông → bánh mì trên xe · **chính K7** · phụ K8, K1 · bảo vệ K2 (attractor A1: máy trên mặt cầu).

```text
【母版锁 · 桥头早市】

写实纪实摄影，像路人用普通相机随手拍下的清晨街景，人物不知道镜头存在。
越南城市清晨的日常生活，所有物件与服装符合当地当代的真实使用状态，不美化。
【固定品牌角标】
画面右下角仅允许出现一个极小、克制、清晰的衬线体品牌角标“T1 to 9”。文字必须逐字准确，大小写与空格完全一致。角标使用与画面协调的低亮度暖白色、古金色或冷灰色，不发光、不加边框、不遮挡主体、不抢夺视觉焦点。除此之外禁止任何其他文字、标志、签名和水印。
每次只生成一张指定画面，不生成拼图、九宫格或多个备选。

【分镜 · 过桥】

横幅 3:2。相机在河岸一侧的人行道上，高度与人物胸口齐平，相机不在桥面上；桥身从画面右侧斜向延伸，只露出一侧栏杆。
[K7·chính] 老人推着装满法棍的玻璃柜小推车，刚踏上桥头的坡道，身体前倾，重心落在前脚，双手握住推车把手，手臂因用力而微微绷紧；他低头看着脚下的路面，不看镜头。
[K8·phụ] 推车玻璃柜一角盖着褪色的蓝色塑料布，车把缠着磨旧的布条。
[K1·phụ] 清晨低角度的阳光从画面左侧照来，老人和推车在路面投下长长的影子，河面泛着淡金色。

【通用负面提示词】

相机站在桥面中央形成对称透视通道，人物摆拍或直视镜头，蜡质皮肤，手指畸形或多指，推车结构不合理，现代广告牌，乱码文字。
除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止角标拼写错误、大小写错误、空格错误、缺字、多字、重复或乱码。
```

Ghi chú:
- Câu máy dùng **điểm tham chiếu** (河岸人行道) + phủ định (相机不在桥面上) + kết quả (只露出一侧栏杆) — K2 §6.
- Bản nháp đầu dùng "手写价格纸" (giấy giá viết tay) — đó là **chữ trong ảnh**, mâu thuẫn với luật brand "không chữ nào khác" và với negative "乱码文字". Đã đổi sang vật không chữ (褪色的蓝色塑料布). Bài học: dấu vết K8 hay kéo theo chữ (biển, nhãn, giá); kiểm mâu thuẫn dương–âm (`core/03` §10).

## Phản ví dụ — viết đều tay (cùng brief ví dụ 1)

```text
【分镜 · 点灯】
电影感，美丽的少女站在雪中的古楼上，手提灯笼，暖色调，柔和光线，景深，细节丰富，高品质，8K，大师作品，氛围感，雪花飘落，古风建筑，精致服装，完美的脸。
```

Vì sao yếu: không biết trục chính; "暖色调, 柔和光线" không có nguồn và bằng chứng; không có ánh nhìn có đích (model sẽ cho nhìn ống kính); "细节丰富" kéo nét đều khắp khung (lỗi cinema); tính từ đánh giá ("高品质, 大师作品") không mang quyết định nào (`core/03` §7).

## OPEN
- **O1** Chạy 3 ví dụ trên GPT Image + một generator khác, mỗi cái 4 mẫu; chấm "thứ đầu tiên thấy" có khớp bảng quyết định không.
- **O2** So ví dụ 1 với phản ví dụ — đo tỷ lệ nhìn ống kính, tỷ lệ nét đều.
