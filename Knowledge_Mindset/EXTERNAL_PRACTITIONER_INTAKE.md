# EXTERNAL PRACTITIONER INTAKE — HÀNG ĐỢI TIẾP NHẬN

Đăng ký các nguồn thực hành bên ngoài đang chờ dung nạp. Nguyên tắc áp dụng đúng như lần hợp nhất phương pháp外部 trước đây (CHANGELOG 2.4.0): **hút cơ chế có ghi nguồn, không sao chép nguyên văn**, và mọi kiến thức đi vào đúng phạm vi bằng chứng của nó (`00_FORMATION_ROUTER.md` epistemic order).

## 1. Nguồn đã đăng ký

| Handle | Tên hiển thị | Nền tảng | Trạng thái | Bài thu được |
|---|---|---|---|---|
| @xiaoxiaodong01 | 小小东 | X Articles | **CAPTURED** | 7/7 |
| @liyue_ai | 李岳 | X Articles | **CAPTURED** | 24/24 |
| @nanyuan0412 | 南鸢 nuyoah | X Articles | **CAPTURED** | 15/15 |
| @VoxcatAI | VoxCat | X Articles | **CAPTURED** | 11/11 |
| vibeshot.club/forum | Vibe Shot Club | Forum | **CAPTURED** | 48 threads |

Đợt kéo 2026-08-25 bằng Grok browser session (X /articles tab login-gated; article bodies lấy từ public article payload fxtwitter + Playwright crawl). Chi tiết: `_external_sources/CAPTURE_LOG.md`. Kiểm định mẫu 4 bài: frontmatter đủ, nội dung nguyên văn tiếng Trung, ảnh đính kèm tải kèm và liệt kê trong `## attached_images`. Lưu ý chất lượng: file vibeshot còn lẫn UI noise đầu trang (menu forum) — không ảnh hưởng phần nội dung chính.

## 2. Cách đưa nguyên liệu vào (chọn một)

1. **Copy-paste**: mở từng bài article trên X → chọn toàn bộ → lưu thành `.md` hoặc `.txt` (mỗi bài một file) vào `_external_sources/<handle>/`.
2. **HTML**: lưu trang bài viết thành `.html` (Save Page As) rồi thả vào cùng thư mục.
3. **Ảnh chụp màn hình**: `.png` từng bài cũng đọc được, nhưng mất chất lượng text khi trích dẫn.
4. Dán trực tiếp vào chat khi làm việc cũng được — sẽ được ghi lại thành file đúng quy trình.

Tên file khuyến nghị: `<handle>_<tiêu đề rút gọn>_<ngày>.md`.

## 3. Giao thức hấp thụ (khi nguyên liệu về)

Mỗi bài đi qua bốn bước:

1. **Trích xuất cơ chế** — tách quan sát (prompt nào cho ra hiệu ứng gì) khỏi tuyên bố (tác giả giải thích tại sao). Chỉ cơ chế mới có thể thăng cấp.
2. **Phân loại phạm vi bằng chứng** — hành vi riêng của một generator → `Portable_Agent_OS/FIELD_NOTES.md`; thủ thuật craft lặp lại được → thư viện/core sau khi chứng minh phổ quát; thẩm mỹ gắn một style cụ thể → casebook chờ charter theo core/07; chưa kiểm chứng được → ghi chú pending kèm điều kiện kiểm chứng.
3. **Ghi nguồn bắt buộc** — handle, ngày đăng, URL, ngày nạp; giữ nguyên tác giả trong mọi trích dẫn.
4. **Quyền sử dụng** — kỹ thuật và cơ chế hấp thụ tự do có attribution; không sao chép prompt hoàn chỉnh của họ vào canonical/examples khi chưa có sự đồng ý; ảnh của họ không nạp vào Visual_Resource_Library nếu rights không rõ.

## 4. Trạng thái hấp thụ

### Đợt 1 — 2026-08-25 (10 bài đọc kỹ, 95 bài phân loại theo tiêu đề)

**Bài đã đọc kỹ — biên bản cơ chế:**

| # | Bài (nguồn · ngày) | Cơ chế trích xuất | Phạm vi bằng chứng | Đích đề xuất |
|---|---|---|---|---|
| 1 | 李岳《GPT Image 2 安全审查真相》05-22 | An toàn GPT Image 2 = hệ thống **dự đoán rủi ro bức tranh** từ hướng ngữ nghĩa toàn cục prompt, KHÔNG phải lọc từ khóa. Chiến lược ổn định: đóng khung thương mại/ngữ cảnh (Lookbook), mô tả cấu trúc quần áo thay vì thân thể, kết thúc bằng chuỗi「避免…」tường minh | Generator-scoped · GPT Image 2 · chưa tự calibration | `FIELD_NOTES.md` — bằng chứng ngoài củng cố nhóm five-ban-triggers hiện có |
| 2 | 李岳《你缺的不是GPT提示词，而是一套能复用的出图流程》06-25 | Pipeline 9 bước: idea→可行性→需求拆解→模板设计→参数组合→prompt→测试→复盘→迭代; chốt trước: chủ đề gì / không muốn gì / trọng tâm / có phải series / chỗ nào khóa / chỗ nào cho biến | Workflow-level · kinh nghiệm một tác giả | Không thăng cấp — canonical `core/02` + TEMPLATE_CREATIVE_BRIEF + GENERATION_LOG đã phủ đầy đủ; dùng làm đối chiếu |
| 3 | vibeshot·南鸢《AIGC系列写真机位公式拆解》 | Series cảm giác thật đến từ **đổi vị trí máy**, không đổi cảnh. Công thức 7 biến: 机位位置×相机高度×拍摄距离×方向×景别×前景关系×人物占比; viết máy quan hệ không gian cụ thể («摄影机站在楼梯最上方，向下俯拍，人物只占画面15%») | Studio heuristic · có ảnh chứng minh trong bài | Ứng viên distill vào `library/11_CAMERA_LIGHT_OPTICS.md` sau khi test 3 ảnh locally; trực tiếp củng cố luật «系列变化来自轴线轮换» |
| 4 | vibeshot·南鸢《斜向硬光带重塑人像光影结构》 | Sửa sáng = sửa cấu trúc qua 6 thành phần: 光源(遮光板切硬光)/形状(斜向窄光带)/落点(单眼半鼻颧骨唇缘一手)/边界(截断突然禁渐变)/高光(推近白允许丢细节)/阴影(加深不补光) | Studio heuristic · before/after 2 ảnh | Ứng viên `library/11` — ngôn ngữ cơ chế khớp Luật 3 (ánh sáng là quan hệ); cần test trước khi thăng cấp |
| 5 | vibeshot·南鸢《用具体事件驱动角色动作表情》 | Thay vì liệt kê pose, dùng **sự kiện cụ thể** làm động lực (接雨， 触碰水珠) để sinh动作+表情 tự nhiên | Heuristic nhỏ · 3 ảnh minh họa | Ghép vào casebook; khớp doctrine «Motivated, not arbitrary» |
| 6 | vibeshot·迪丽热翼《人像提示词构架思路》 | Prompt chân dung theo kiến trúc khóa trước, hoán đổi phần tử: 拍摄风格/人物/衣服风格/(构图)/身材侧写 | Studio heuristic · nói rõ phụ thuộc context hội thoại | Đối chiếu với carry/lock/repair/open của Gate A; không mới về cấu trúc |
| 7 | 小小东《不会构图，有这篇够用》05-25 | Trỏ tới repo mở **100-layout-compositions** (GitHub: nevertoday) — thư viện bố cục tham chiếu dạng ảnh | Resource pointer · rights: open-source | Đăng ký vào `Visual_Resource_Library/source_registry.json` nếu muốn tra cứu; không phải luật |
| 8 | 小小东《中国传统配色742种开源》06-05 | Repo mở **zhongguo-traditional-colors**: 742 màu truyền thống Trung Hoa kèm gợi ý phối + kiến thức màu | Resource pointer · rights: open-source | ⭐ Ứng viên mạnh: bổ sung nguồn vào Visual_Resource_Library phục vụ palette trung hoa cho các family xianxia/deco |
| 9 | vibeshot《【教程】用Codex自动探索风格》 | (chưa đọc kỹ — tiêu đề chỉ ra quy trình khám phá style tự động) | — | Hàng đợi ưu tiên, liên quan route new_family_or_fusion |
| 10 | 小小东/Li岳 các bài DeepSeek Harness, skills军队 | Công cụ agent/AI tooling — ngoài phạm vi tri thức hình ảnh | OUT OF SCOPE | Lưu trữ, không hấp thụ |

**Phân loại 95 bài còn lại theo tiêu đề (chưa đọc):**

- 🔴 **Ưu tiên đọc kế tiếp** (khả năng cao chứa cơ chế hình ảnh): 南鸢《跑了上千张写真图片后总结了一套方法论》《构图是语法，故事是语义：双层视觉导演法（上）》《为什么加了真实皮肤还是塑料感》《image-2人像怎么做才好看（短词篇）》《港风写真该怎么写提示词》； VoxCat《你的提示词为什么一百个词模型只听进去三个》《AI摄影的空气感是呼吸》《AI角色设定卡锁一张脸》《只写风格词＋角色名为什么还能出神图》《施工图vs创意简报：跨模型迁移》《🍌Nano Banana Pro：视觉渲染与构图》； 李岳《借助AI写出高质量提示词：生图技巧》《99%的人都写错了…性感》《东方仙界Skill》
- 🟡 Trung bình: các bài写真/GPT showcase vibeshot còn lại (~35 thread), 杂志感封面， 手搓高达
- ⚪ Out-of-scope: OpenClaw/Hermes/Codex/公众号爆文/PPT (~30 bài Li岳 + vài bài khác) — công cụ vận hành, không phải tri thức thị giác

### Đợt 2 — 2026-08-25 (12 bài đọc kỹ bổ sung)

**Tích hợp canonical (`library/11` §11 mới):** công thức máy quay 7 biến cho series · cấu trúc sửa dải sáng cứng 6 thành phần · doctrine逆光勾边+柔光补强+Soft Bloom · tách 5 biến da thật. Tất cả có attribution và exception boundary, theo tiền lệ 2.4.0.

**Ghi FIELD_NOTES (generator/method scope):** thí nghiệm style-word kích hoạt cả hệ thị giác (VoxCat, control experiment 2 nhân vật) · chế độ khám phá short-word không nhãn (南鸢) · identity anchor sheet 骨相钉死 cho video consistency (VoxCat) · 4 nguyên nhân fail khi迁移 prompt cross-model · pointer repo `xianxia-visual-director` làm external grammar reference cho hướng megastructure chưa calibration.

**Biên bản rút gọn từng bài:**

| Bài | Kết luận |
|---|---|
| 南鸢《跑了上千张写真…方法论》 | Prompt写真 = 「拍摄小抄」cho một đội sản xuất; viết từ「这张图的成立点」; mật độ道具 cụ thể tạo không gian đã từng có người sống; câu「镜头像藏在果树枝叶之间」ép foreground遮挡 → khớp Law 3/anchor; casebook |
| 南鸢《构图是语法，故事是语义（上）》 | 构图决定先看哪里，故事决定看到了什么; 元素≠关系（火车票只说明桌上有票）; World Press Photo chấm vòng 1 visual quality rồi mới story → củng cố Law 16 + message-first; casebook |
| 南鸢《为什么加了真实皮肤还是塑料感》 | 「真实皮肤」token quá thô → beauty-filter default; tách 5 biến (纹理/高光位置/质感基调/轻微不完美/光线) → **đã tích hợp library/11** |
| 南鸢《image-2人像短词篇》 | Bỏ nhãn phân loại ở pha khám phá để từ ngữ tự tái tổ hợp; giữ nhãn khi cần ổn định → FIELD_NOTES |
| 南鸢《港风写真该怎么写提示词》 | Hệ style港风 đầy đủ 5 hệ (妆发/服装/配饰/场景/摄影语言) + negative + 3 tiêu chí phán đoán; «红唇卷发≠港风» → **ứng viên family/instance charter** theo core/07, đang nằm casebook chờ falsifier |
| VoxCat《一百个词模型只听三个》 | 高信号词 vs 语义泡沫; prompt = hợp đồng với anchor cứng; test «đây là constraint hay noise?» → khớp doctrine mechanism-not-label; casebook |
| VoxCat《空气感是呼吸》 | 逆光勾边(骨架)+柔光补强(呼吸)+Soft Bloom tại điểm sáng nhất+palette tiết chế → **đã tích hợp library/11** |
| VoxCat《AI角色设定卡锁一张脸》 | Sheet = khóa một gương mặt; 骨相钉死 từng feature; layout 左大右小; 6 close-up đúng góc drift; cấm chữ trên sheet → FIELD_NOTES (video consistency) |
| VoxCat《施工图vs创意简报》 | Fail khi迁移 do 4 nguyên nhân (nhiều chủ ngữ cùng dimension / pseudo-parameter / negative vô quan / quá nhiều yêu cầu cùng lúc); clean baseline + single-change → xác nhận độc lập Luật 15 |
| VoxCat《只写风格词＋角色名出神图》 | Style word = key kích hoạt cả hệ thị giác (cảnh/trang/light/medium/narrative), có thể tự chọn medium render → FIELD_NOTES, generator-scoped image2 |
| 李岳《东方仙界Skill》 | Rule-routing skill architecture (khớp thiết kế .kimi-code/skills của mình); repo mở xianxia-visual-director = external grammar cho megastructure chưa calibration |
| 李岳《借助AI写出高质量提示词》《99%都写错了性感》 | Chưa đọc kỹ — giữ trong hàng đợi; chủ đề trùng cơ chế safety đã hấp thụ đợt 2.4.0 |



Mọi cơ chế ở cột "Đích đề xuất" đều **chưa được thăng cấp** — chỉ khi qua test local (3 ảnh fresh-seed, single-axis) mới được ghi vào canonical/field notes theo đúng luật promotion.


### Đợt 3 — 2026-09-20…23 (EggOS lab craft + reverse loop)

**Nguồn / tool (distill, không dump prompt nguyên văn):**

| Nguồn | Cơ chế giữ lại | Phạm vi | Đích |
|---|---|---|---|
| TideKnight/voxcat-chatgpt-prompt-eagle-exporter @ adea5c3 | Base→Generated→Revision causal freeze; User Reference ≠ Generated/Edited | workflow · ChatGPT image chains | `VOXCAT_CREATIVE_CHAIN.md` + skill `voxcat-creative-chain` |
| reverse-image-prompt-loop (Codex A/B → EggOS slim) | A=Director Final · B=Analyst REVERSE_LOOP; max 3 mặc định; no full pack in reverse mode | lab process · EggOS | `REVERSE_IMAGE_PROMPT_LOOP_SLIM.md` |
| nuyoah-meizi-pose / nuyoah-image-reverse-prompt / vibeshot-premium-4 | pose 美姿; one-shot reverse; carrier+light+optics | craft optional · named by Change next | local `knowledge/` + Grok skills (Drive: pointer in changelog) |

**Token policy (lab):** reverse mode không chồng VISUAL_CONTEXT_PACK + FINAL_CHECK + REVERSE_LOOP cùng vòng.
