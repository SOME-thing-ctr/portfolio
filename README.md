# 丁飞 · 作品集

一个极简风格的单页作品集，**HTML + CSS + 极少量原生 JavaScript**（仅用于视频灯箱的自动播放与暂停），无框架、无构建步骤。
所有图片与视频均来自上级素材文件夹，已做压缩与重命名处理。

## 目录结构

```
portfolio/
├── index.html              # 页面结构与文案
├── styles.css              # 全部样式、动效、响应式
├── assets/
│   ├── images/             # 压缩后的图片（约 2.1 MB）
│   │   ├── badge-cover.jpg
│   │   ├── art-therapy.jpg
│   │   ├── td-mandala.jpg         # 1.png，曼陀罗封面与视频 poster
│   │   ├── xiyouji-poster.jpg     # 西游记·菩提渡 海报（源：海报西游记.png）
│   │   ├── poster-1mov.jpg        # 1.MOV 第一帧
│   │   ├── poster-putidu.jpg      # 菩提渡第 4 秒片头（播放器封面）
│   │   ├── poster-youyuan.jpg     # 游园惊梦第一帧
│   │   ├── poster-demo.jpg        # 效果演示第一帧
│   │   ├── poster-flow.jpg        # 粒子动效·湍流第一帧
│   │   ├── poster-glow.jpg        # 粒子动效·光轨第一帧
│   │   └── portrait.jpg
│   └── videos/             # 按需加载的视频（约 262 MB）
│       ├── youyuan-jingmeng.mp4   # 游园惊梦（源：游园惊梦.mp4）
│       ├── demo.mp4               # 效果演示（源：效果演示.mp4）
│       ├── td-mandala.mp4         # 曼陀罗动态影像（源：TD/1.mp4）
│       ├── particles-flow.mp4     # 粒子动效·湍流（源：TD/2.mp4）
│       ├── particles-glow.mp4     # 粒子动效·光轨（源：TD/3.mp4）
│       ├── putidu.mp4             # 菩提渡（源：菩提渡.mp4，529 MB → 68 MB）
│       └── aigc-1.mp4             # AIGC 实验影像（源：1.MOV，HEVC → H.264）
├── tools/
│   ├── build_assets.py     # 图片压缩 / 视频复制（不改动源文件）
│   └── make_qr.py          # 生成访问二维码
└── README.md
```

## 本次使用的技能与工具

| 类型 | 名称 | 用途 |
| --- | --- | --- |
| 技能 | find-skills | 检索 / 安装可复用技能 |
| 技能 | Web Deploy GitHub Pages | 静态站初始化与 Pages 部署流程 |
| 技能 | GitHub | 通过连接器检索仓库（本机未安装 `oo`，改用 GitHub REST API） |
| 工具 | Python 3.12 + Pillow | 图片压缩、二维码绘制 |
| 工具 | qrcode[pil] | 生成容错等级 H 的二维码 |
| 工具 | Playwright + 系统 Edge | 桌面 / 平板 / 移动端截图验收、播放行为测试 |
| 工具 | imageio-ffmpeg（ffmpeg 9.0） | 视频首帧截取、HEVC / 大码率视频转码 |
| 工具 | CloudBase CLI 3.9 | 腾讯云静态网站托管部署（登录、上传、环境管理） |
| 工具 | GitHub REST API | 按 topic / stars 检索参考仓库 |

## 本地预览

在 `portfolio` 目录执行：

```bash
python -m http.server 8000
```

浏览器打开 <http://localhost:8000>。手机与电脑连同一 Wi-Fi 时，可用
`http://电脑局域网IP:8000` 在手机上预览。

## 页面功能

- **首屏**：大字号标题、个人介绍、徽章主视觉、关键词跑马灯
- **作品**：7 个作品，非对称栅格；悬停时图片缩放、出现「查看项目」按钮、标题变色；关闭灯箱停留在原位置，不跳转
- **粒子动效**：TD/2.mp4（湍流）与 TD/3.mp4（光轨）两段实时粒子作品；点击曼陀罗图片会直接进入其动态影像（TD/1.mp4）
- **视频封面**：游园惊梦、效果演示、湍流、光轨均取视频第一帧作为卡片封面与灯箱 poster；曼陀罗例外，使用 `1.png`（即 `td-mandala.jpg`）
- **AIGC 专栏**：深色独立区块，收录「西游记 · 菩提渡」动态海报与「实验影像 · 1.0」；点击海报直接进入 `菩提渡.mp4` 并自动播放（有声），关闭或切换作品时立即暂停，声音同步中断
- **灯箱**：纯 CSS `:target` 负责显隐，视频自动播放 / 暂停由约 20 行原生 JS 控制；视频 `preload="none"` 不占首屏带宽
- **移动端入场**：AIGC 专栏在 ≤860px 时启用滚动驱动的标题字距展开 + 卡片错峰上浮（缩放、模糊消散），尊重 `prefers-reduced-motion`
- **关于**：个人照、创作自述、能力 / 工具标签、时间线
- **联系**：深色收尾区块、邮箱与社交链接
- **动效**：首屏分层入场、滚动驱动入场（`animation-timeline: view()`，不支持的浏览器自动降级）、平滑滚动
- **响应式**：1024 / 860 / 560 三档断点，移动端单列
- **无障碍**：跳转链接、焦点样式、`prefers-reduced-motion` 降级

## 需要替换的内容

| 位置 | 说明 |
| --- | --- |
| `index.html` 中邮箱（已设置为 `feiding76@gmail.com`，出现 2 处） | 如需更换直接搜索替换 |
| `index.html` 中社交链接 `https://github.com/` 等 | 换成你的主页地址 |
| 「关于我」时间线 | 按真实经历调整 |
| 作品标题 / 描述 | 依据实际项目命名修改 |
| 姓名 `丁飞` | 如需要可全局替换 |

## 素材说明

- 图片压缩：ART THERAPY 展板 21.3 MB → 0.7 MB，西游记海报 8.4 MB → 0.65 MB，徽章图 0.28 MB，曼陀罗 1 MB → 92 KB，照片 0.17 MB。
- 视频转码（`imageio-ffmpeg` 自带 ffmpeg）：
  - `1.MOV`：HEVC 2560×1440 / 60fps / 388.6 MB → H.264 1080p / 30fps / 64 MB（`aigc-1.mp4`），HEVC 在 Chrome / Edge 中无法播放，必须转码。
  - `菩提渡.mp4`：H.264 1080p60 / 528.7 MB → 1080p30 / 68 MB（`putidu.mp4`），仍在 GitHub 100 MB 单文件限制内。
  - 命令示例（`$FF` 为 ffmpeg 路径）：

```bash
ffmpeg -y -i "1.MOV" -vf "scale=-2:1080" -r 30 -c:v libx264 -preset veryfast \
  -b:v 4000k -maxrate 5000k -bufsize 8000k -pix_fmt yuv420p \
  -c:a aac -b:a 128k -movflags +faststart "assets/videos/aigc-1.mp4"
```

- 未纳入：`1月30日.mp4`（449 MB）与 `TD/1.0.mov`（31 MB，.mov 容器兼容性差）。
- 视频均按需加载，首屏体积仍约 1 MB；仓库总量约 264 MB，最大单文件 68 MB。
- 若仓库体积仍偏大，可用 Git LFS 或把视频传到对象存储后改 `src`。

## 部署到 GitHub Pages

### 方式 A：网页操作（最简单）

1. 登录 GitHub，新建仓库，例如 `portfolio`（公开）。
2. 上传 `portfolio` 目录内的全部文件（保持 `index.html` 在仓库根目录）。
3. 进入 **Settings → Pages**，Source 选择 **Deploy from a branch**，
   Branch 选 `main`、目录选 `/ (root)`，保存。
4. 等待 1–3 分钟，访问：
   `https://<你的用户名>.github.io/portfolio/`

> 如果仓库名直接叫 `<你的用户名>.github.io`，访问地址就是
> `https://<你的用户名>.github.io/`，更适合作为个人主页。

### 方式 B：命令行

```bash
cd portfolio
git init
git add .
git commit -m "feat: personal portfolio"
git branch -M main
git remote add origin https://github.com/<你的用户名>/portfolio.git
git push -u origin main
```

推送后按方式 A 的第 3 步开启 Pages。

### 方式 C：GitHub Actions（可选）

若希望每次 push 自动发布，把 Pages 的 Source 改为 **GitHub Actions**，
并添加 `.github/workflows/deploy.yml`：

```yaml
name: Deploy static site to Pages
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deployment
        uses: actions/deploy-pages@v4
```

## 部署到腾讯云 CloudBase 静态网站托管（COS + CDN）

当前站点同时部署在腾讯云 CloudBase 静态网站上：

- 环境：`convinced-bonobo-d4e16yc0ceabb37`（ap-shanghai，体验版，有效期至 2027-05-17）
- 访问地址：<https://convinced-bonobo-d4e16yc0ceabb37-1534696201.tcloudbaseapp.com/>
- 部署命令：

```bash
npm i -g @cloudbase/cli
tcb login        # 浏览器设备码授权，或 tcb login --apiKeyId <id> --apiKey <key>
tcb hosting deploy index.html  ""       -e convinced-bonobo-d4e16yc0ceabb37
tcb hosting deploy styles.css  ""       -e convinced-bonobo-d4e16yc0ceabb37
tcb hosting deploy assets      assets   -e convinced-bonobo-d4e16yc0ceabb37
```

> 注意：上传目录时第二个参数（云端前缀）必须写 `assets`，否则目录内容会散落到根路径。
> 部署完成后全部资源返回 200（7 个视频，最大 68 MB）。

> 限制：默认测试域名 `*.tcloudbaseapp.com` 首次访问会显示腾讯云「页面访问提示」，
> 需等 10 秒后点「继续访问」；绑定已备案的自定义域名后该提示才会消失。
> 因此对外分享（二维码、名片）优先用 GitHub Pages 地址，CloudBase 地址作为镜像备用。

## 生成访问二维码

部署完成、拿到正式地址后执行：

```bash
python -m pip install "qrcode[pil]"
python tools/make_qr.py "https://<你的用户名>.github.io/portfolio/"
```

默认输出 `assets/images/qr.png`（深墨 / 米白配色，容错等级 H，适合印刷或投屏），
可用 `--out` 指定输出文件名。当前仓库内：

- `assets/images/qr.png` → GitHub Pages 地址
- `assets/images/qr-cloudbase.png` → CloudBase 静态托管地址

在手机相机中扫描即可访问。

> 仓库内已附 `assets/images/qr-local.png`，内容为本次预览用的局域网地址
> `http://172.20.10.2:8000/`。只有在本地服务器运行、且手机与电脑处于同一 Wi-Fi 时有效；
> 正式上线后请用上面的命令重新生成 `qr.png`，不要把局域网二维码用于印刷或发布。

如需把二维码放进页面，在 `index.html` 联系区加入：

```html
<figure class="contact__qr">
  <img src="assets/images/qr.png" alt="扫码访问作品集" width="160" height="160">
  <figcaption>扫码在手机查看</figcaption>
</figure>
```

> 提示：二维码内容就是网址本身，换域名或仓库名后需重新生成。
> 也可用在线工具（如 qr.io、草料二维码）生成，但本地脚本可复现、无水印。

## 参考案例清单（GitHub 检索）

| 仓库 | Stars | 技术栈 | 适用理由 |
| --- | --- | --- | --- |
| [codewithsadee/vcard-personal-portfolio](https://github.com/codewithsadee/vcard-personal-portfolio) | 8.2k | HTML / CSS / JS | 单页 vCard 结构，深色极简、响应式完整，最接近本项目形态，可直接对照改文案 |
| [bchiang7/v4](https://github.com/bchiang7/v4) | 8.3k | Gatsby / React | 极简排版与克制动效的标杆，适合参考字号层级、留白与配色 |
| [soumyajit4419/Portfolio](https://github.com/soumyajit4419/Portfolio) | 6.5k | React | 作品卡片与项目详情的组织方式清晰，适合扩展多项目结构 |
| [RyanFitzgerald/devportfolio](https://github.com/RyanFitzgerald/devportfolio) | 5.0k | Astro / Tailwind | 现代极简模板，信息架构（Hero / About / Projects / Contact）可直接借鉴 |
| [rammcodes/Dopefolio](https://github.com/rammcodes/Dopefolio) | 3.8k | HTML / CSS / JS | 动效丰富但不过度，适合参考悬停与入场节奏 |
| [smaranjitghose/awesome-portfolio-websites](https://github.com/smaranjitghose/awesome-portfolio-websites) | 2.8k | HTML / CSS | 开源作品集模板合集，适合继续找不同风格与组件 |
| [nisarhassan12/portfolio-template](https://github.com/nisarhassan12/portfolio-template) | 731 | HTML / CSS | 主打 minimal + accessible，可参考语义化与键盘可访问性写法 |
| [CommunityPro/portfolio-html](https://github.com/CommunityPro/portfolio-html) | 672 | 原生 HTML / CSS / JS | 零构建、零依赖，与当前项目技术路线一致，便于按需搬运组件 |
| [varadbhogayata/varadbhogayata.github.io](https://github.com/varadbhogayata/varadbhogayata.github.io) | 1.5k | HTML / CSS / JS | 真实 GitHub Pages 个人站，可参考仓库组织与部署方式 |

> Stars 为 2026-11 检索结果，仅作热度参考；选用前请确认各仓库 License。
