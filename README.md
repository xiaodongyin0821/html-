# html小游戏
说明：.py文件用于生成.html文件
- 小游戏合集（主界面）：index.html
- 自动战斗生存：auto_battle_survivor.html
- 五子棋：gomoku.html
- 迷宫：stack_turtles.html
- 贪吃蛇：snake.html
- 叠乌龟（汉诺克）：stack_turtles.html
- 俄罗斯方块：tetris.html

使用浏览器可以直接打开html文件并运行游戏。

# 微信直接启动GitHub小游戏的最简方式
<font color=blue>通过GitHub Pages部署HTML文件，可以让手机微信直接打开并运行游戏，而非仅看到源码。</font>

## 📌 一、为什么直接打开GitHub源码无法运行？
- 原因分析：当访问类似 https://github.com/xiaodongyin0821/html-/blob/main/stack_turtles.html 的链接时，看到的只是源码展示页，不是网页的运行页面。
- 解决方案：使用GitHub Pages托管，让HTML文件以网页形式呈现。

## 🛠️ 二、GitHub Pages部署流程（只需设置一次）

### ✅ 步骤 1：启用 GitHub Pages
1. 打开项目仓库主页：https://github.com/xiaodongyin0821/html-
2. 点击顶部菜单栏的【Settings】
3. 左侧导航栏选择【Pages】（有时在Code and automation下）
4. 在【Build and deployment】部分设置如下：
- **Source**：选择 `main`
- **Folder**：选择 `/ (root)`
- 点击【Save】
5. 稍等片刻，会生成一个访问网址：https://xiaodongyin0821.github.io/html-/
### ✅ 步骤 2：生成HTML页面访问链接
将你的HTML文件名拼接在网址后面：https://xiaodongyin0821.github.io/html-/stack_turtles.html
**这个地址就是可以直接在手机浏览器或微信中打开并运行的游戏网页！**

### ✅ 步骤 3：手机端打开并分享
1. 将链接发到微信群、私聊或生成二维码
2. 微信中点击链接，即可加载并运行游戏

## 🔁 三、如何更新游戏内容？
只需在 GitHub 上更新 stack_turtles.html 文件内容（改完代码、提交），GitHub Pages 会自动刷新内容（1分钟内生效），不需要重复设置。

## 📂 四、支持多页面部署（可选拓展）
如需托管多个HTML游戏或页面，只需将多个.html文件放入同一仓库的根目录或子目录，使用对应的访问路径访问即可：
| 文件名                 | 访问地址                                                        |
| ------------------- | ----------------------------------------------------------- |
| `game11.html`        | `https://xiaodongyin0821.github.io/html-/game11.html`        |
| `game/game22.html` | `https://xiaodongyin0821.github.io/html-/game/game22.html` |
