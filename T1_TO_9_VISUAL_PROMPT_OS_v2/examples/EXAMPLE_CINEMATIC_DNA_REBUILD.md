# Example — cinematic DNA rebuild casebook

Label: `AUTHORED_FIXTURE`. Not a live chat transcript and not a rendered-image claim.

Route: on-demand `cinematic_rebuild` → `library/20` + formation `CINEMATIC_VISUAL_STORYTELLING_KB.md`.
Input image for A–C: wooden loft still (`IMAGE_OBSERVED` in the originating run). Temp paths are not runtime dependencies.

Baseline locks from the user's original prompt, until a later request opens them: high-angle through wood, figure looking up, Chinese interior, pale traditional dress, quiet photographic still. Case B is allowed to move the camera because the authored user line opens angle and layout.

Difference rule: a rebuild must change relation, action, space, or station. Recolor is not a rebuild.

---

## Case A — interrupted task, high angle kept

Request: keep the original high-angle wood threshold; add a beat.

Evidence: `IMAGE_OBSERVED`. Identity lock. Camera lock kept.

DNA keep: adult woman, pale cloth on dark wood, threshold observation, quiet register, upward gaze.
Translate: center standing → weight at the table, one hand closing a book, head still lifting.
Drop: empty center pose.

Ledger: staging/action change; station unchanged.

Cost: book or sleeve may hide the hands.

```
母版锁
单幅竖构图写实摄影静帧。参考图只用于保持同一位明确成年东亚女性的面部辨识度、浅色层叠中式服装、深色木构与安静克制气质。保留高机位、近处木栏遮挡与人物向上看向镜头的观看关系。不出现文字、标志或水印。

分镜
镜头仍在上层，穿过近处深色木栏向下看。木栏占画面上沿与下沿两侧，中间留出通向室内的开口；栏杆不得切掉眼睛。
人物从画面正中移到左侧桌边。身体仍朝向桌上的书，重心在靠近桌子的腿上；一只手正把一本厚书合到一半，袖口因这个动作自然下垂。头已经抬起，视线穿过栏杆空隙看向镜头，嘴唇放松，像被一声轻响打断，而不是摆拍。
桌面只保留合上的书、一只小香炉与一束素花。暖灯在左上角局部发光，不把整张脸染成橙色。近处木栏略柔，人物面部与合书的手同在可读区域。

通用负面提示词
禁止改成平视或门口构图；禁止回到正中站姿却只在手里加一本书；禁止夸张惊吓、统一橙色滤镜、文字、标志与水印。禁止拼图或多画面。
```

Expected failures: book floating; hands cropped by the railing; face-first so hard the closing book disappears.

---

## Case B — doorway encounter (authored dialogue + no-logo prompt)

User fixture: “Giữ người, chất gỗ và cảm giác kín đáo. Được đổi góc và bố cục. Cùng bàn trước, chưa viết prompt.”

Bot fixture, substance: keep the woman, pale cloth on dark wood, and a threshold that separates the viewer. High angle is open. A keeps the loft and adds an interrupted task. B drops to a corridor and looks through a half-open door. C puts the meeting in a mismatched reflection if impossibility is wanted. Lean B because it changes distance while keeping quiet. Ask whether the meeting should feel closer or still wary.

User fixture: “B, dè chừng nhẹ thôi, viết prompt, không logo.”

Bot compiles B. No second choice question. No logo. Independent prompt (no “or A/B/C”).

Evaluation: station high → same floor; blocking center stand → stop at a threshold; viewer-through-railing → viewer-through-door; gaze/body relation changes; near occlusion remains as a door leaf. Identity/world/mood kept. Camera numbers omitted because spatial consequence is enough.

```
母版锁
单幅竖构图写实摄影静帧。参考图用于保持同一位明确成年东亚女性的面部辨识度、浅色层叠中式服装、深色木构空间与安静克制的气质；不复制原图的高机位、中央站姿或栏杆布局。皮肤、头发、织物与旧木材保持可信的摄影质感。画面不出现文字、标志或水印。

分镜
镜头位于同一层回廊内，接近人物眼睛的高度，从一扇半开的深色木门后斜看向相邻房间。近处门扇仅在画面左侧形成宽而柔焦的竖向遮挡，右侧保留通向房内的完整视线；门框不得截断人物的眼睛或手。
人物处于中景右侧，刚在门槛处停下，身体仍朝向离开的走廊，头部轻轻转向镜头所在的门缝；视线落在门缝内，嘴唇自然放松，神情仅有很轻的迟疑。重心仍落在后脚，前脚停在门槛旁，一只手搭在门框上，袖口因抬手自然下垂；动作像被一次短暂的注意打断，而不是为镜头摆姿。
人物身后可读的木地板与侧墙向房间深处延伸，远处桌面只保留一盏小灯与合上的书，细节安静。画外侧窗的柔和日光从房内侧面照到她的眼周、面颊和衣褶，靠近镜头的门廊较暗；远处灯光只形成局部暖色，不把整张脸染橙。眼神与搭门框的手构成同一可读区域，前门柔焦，室内逐渐减弱细节；保留她与门、门槛及后方房间的空间关系。整体克制，近处的遮挡带来距离感，停顿与视线带来轻微戒备。

通用负面提示词
禁止回到原图的高机位俯拍或中央正面站姿；禁止把人物移到门板后而遮住眼睛与手；禁止僵硬对称摆拍、夸张恐惧、统一橙色滤镜、无来源的强轮廓光、全景同等锐利、现代家具、身份漂移、文字、标志与水印。禁止拼图或多画面。
```

Gaze-revision turn (authored): user later says the eyes should not meet the gap so directly. Bot updates only gaze/head in the shot, bumps `decision_revision`, does not reopen identity or restage the door.

---

## Case C — reflection mismatch (surreal, only if user wants impossibility)

Request: quiet interior, interrupted encounter, but eye contact happens in a narrow mirror before the real head turns.

DNA keep: quiet wood, restrained palette, adult identity.
Translate: threshold into a screen + mirror pair.
Authored exception: reflection looks at the viewer; real head has not finished turning. Do not “correct” the mirror.

Ledger: gaze location changes; two readable heads (real + reflection) required.

Cost: double person or illegal extra mismatch.

```
母版锁
单幅竖构图写实摄影静帧，同一位成年东亚女性，浅色中式层叠服装，安静木构室内。唯一被允许的不可能是：窄镜中的面容已经抬眼看向观者，而真实的头仍未转完。不要把镜面改回同步反射。不出现文字、标志或水印。

分镜
镜头在室内同一层，平视略偏。真实人物位于中景，侧身正在合上一扇木屏风，真实的头仍朝向屏风，眼睛尚未找到镜头。画面右侧一块窄长的旧镜里，同一张脸已经抬眼看向观者。必须同时看见真人、镜子、以及头向的差异；景深足够让两者都可读，镜子不是贴图。近处屏风边缘形成竖向遮挡，但不切掉真实的眼睛。光线仍是室内侧窗柔光，镜子只是更亮一点。

通用负面提示词
禁止复制出两个完整的人在房间里；禁止镜面与真人姿势完全同步；禁止在许可范围之外再加错位的手脚；禁止恐怖夸张、文字、标志与水印。禁止拼图或多画面。
```

---

## Case E — mechanism-first mixed media (chopsticks kitchen)

Request: keep the chopsticks-as-window and planar kitchen. Do not restate “cook hands a bowl across.” New causal event: a real tea-candle already sits on the live table outside the chopsticks; the drawn cook reaches a drawn lid across the chopstick edge and covers that real flame, putting it out.

`first_read_owner`: mechanism / crossing (lid meeting flame).
Real: chopsticks, table, tea-candle, smoke after the cover.
Flat: kitchen interior, drawn cook, drawn lid.
Law kept: chopsticks are physical; kitchen is graphic.
Law broken: a drawn lid may occlude and extinguish a real flame.
Proof: the lid is interrupted by a real chopstick; the candle wick is under the lid; a thin real smoke thread is on the table side, not inside the drawing.

No extra human invented to “make it cinematic.” Face is not the sharpest plane.

```
母版锁
单幅横构图。一对真实筷子在近景构成稳定三角；三角内部是多层平面绘制的小厨房，不是微型三维模型。真实桌面上、筷缘之外已有一只点燃的茶烛。平面厨师被允许把一只平面锅盖越过筷缘盖到这团真实火焰上，把它熄灭。真实桌面、筷缘与蜡烛保持摄影材质；厨房与锅盖保持平涂分层。第一视觉是锅盖压住烛火的越界，不是人脸，也不是递碗。不出现文字、标志或水印。

分镜
真实筷子从画面两侧伸入，交叉成一个可读的三角窗。窗内平面厨房有灶与蒸气剪影，前后层靠遮挡和大小分，不靠厚重体积。平面厨师侧身伸臂，双手把一只扁的平面锅盖送到筷缘之外；锅盖的一部分已被真实筷身挡住，盖面正好压在真实茶烛的火苗上，烛芯被盖住，桌面一侧升起极淡的真实烟气。不要把厨师画成三维小人，不要改成递碗。若有真人只出现在远景或画面一角，略柔，不做最清晰面。颜色克制：木筷、白瓷、烛火一点暖色。

通用负面提示词
禁止把整间厨房做成精致微缩模型；禁止取消筷缘越界；禁止改回递碗而没有灭烛；禁止让真人脸成为最清晰主体；禁止到处补厚度和投影来“修平涂”；禁止文字、标志与水印。禁止拼图或多画面。
```

---

## Case F — local edit, prompt-only, and no-figure still

F1 local edit: change only the coat to dusty blue. Keep staging, camera, identity, action.

```
只把外层长衫从浅米改成灰蓝，其余完全保持：同一位成年女性、同一高机位、同一木栏遮挡、同一向上注视、同一双手位置与同一室内陈设。不要重排人物，不要改镜头高度，不要新增故事。不出现文字、标志或水印。
```

F2 prompt-only (no image): user pastes a text brief about an empty clock workshop at noon and asks to discuss, not write a prompt. Bot marks `PROMPT_ONLY`. Must not say “I see in the image.” Stop after DNA + one question. No person is required: first read is the stopped clock and a shaft of daylight on brass dust. Contemplative, not a thriller.

Non-figure cinematic still (compile only after the user asks to write):

```
母版锁
单幅横构图写实静帧，无人物。一座停止的钟表工房在正午侧窗光里。第一视觉是一只打开后盖、指针停在某一刻的座钟；第二视觉是工作台上被光切过的铜屑。空间靠前后遮挡和桌面纵深阅读，不靠全背景虚化，也不靠阴郁滤镜。不出现文字、标志或水印。

分镜
相机在工作台高度，略侧。近处一只木凳靠在桌沿形成遮挡，但不挡住座钟打开的后盖。座钟与一排未装上的齿轮都保持可读：这是深焦、日光、日常，不是夜戏。灰尘只在光束里显现。没有人的手。

通用负面提示词
禁止添加人物或面孔；禁止把车间改成废墟惊悚；禁止全背景大虚化、青绿分色、文字、标志与水印。禁止拼图或多画面。
```

---

Dialogue chain (authored, one sitting): discussion → DNA + three directions → user picks B and no-logo → prompt B → user revises gaze → bot updates only the gaze clause and revision. Expected: no tool call before compile; no re-asking after “B, write”; identity lock survives the gaze patch.

The copy-ready three-section block below is Case D with the project default brand (daylight / deep focus / two adults). It is a different task from no-logo Case B.

## 母版锁

~~~text
【母版锁】

单幅横构图写实摄影静帧，日光，深焦。两位明确成年东亚女性在同一庭院里完成一次可见的交接：近处一人递出合上的书，远处一人伸手要接。身份、年龄与浅色常服结构固定；画面右下角仅允许一个极小清晰的衬线体品牌角标“T1 to 9”。不是夜戏，不是青橙分色，不是全身虚化的情绪肖像。

~~~

## 分镜

~~~text
【分镜】

相机在略高的游廊口，但仍是庭院这一层的高度，不是原木栏俯拍。前景只有一根暗色柱子切掉左边一小条，柱后整条庭院保持清晰：石板地面、两个人的手脚、远处要接书的手都必须可读。近处女子身体仍朝向房间，头和伸出的书朝向远处；远处女子前脚刚踏进光里，手掌张开，脸不必最大最锐。阳光从画面右侧进入，阴影短而清楚，没有烟雾。第一视觉是两只手与那本书之间的空隙，不是任何一张脸的特写。

~~~

## 通用负面提示词

~~~text
禁止把远处人物虚化到不可读；禁止改成夜景、青橙滤镜、泪水或追逐；禁止身份漂移、儿童化、拼图或多画面。除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印。

~~~
