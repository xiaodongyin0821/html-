<img width="2046" height="624" alt="msedge exe_20250728_104451" src="https://github.com/user-attachments/assets/b8c0af0a-f86f-4a15-b846-527e5563019f" />

# html小游戏
说明：**.py文件用于生成.html文件**

- 小游戏合集（主界面）：index.html
- 自动战斗生存：auto_battle_survivor.html
- 五子棋：gomoku.html
- 迷宫：maze.html
- 贪吃蛇：snake.html
- 叠乌龟（汉诺克）：stack_turtles.html
- 俄罗斯方块：tetris.html
- 水果忍者：fruit_slice.html

备注：**HTML文件可以直接在浏览器中打开并运行。**


# HTML文件 vs Python文件
| 维度   | HTML文件（`.html`）          | Python文件（`.py`）        |
| ---- | ------------------------ | ---------------------- |
| 用途   | 直接在浏览器中打开，运行网页或游戏前端界面    | 用于生成、处理或辅助构建HTML文件     |
| 运行环境 | 浏览器（包括微信浏览器）             | Python解释器（如VSCode、终端等） |
| 文件结构 | HTML/CSS/JS混合，内容即为“网页本体” | 通常包含HTML代码的字符串变量+写入操作等 |
| 用户体验 | 一键打开即用，加载即运行             | 默认仅输出源码或生成HTML文件       |

## ⚠️ 注意：不要直接复制.py文件内容作为HTML源码！
<img width="2046" height="1644" alt="msedge exe_20250728_103828" src="https://github.com/user-attachments/assets/b49c3650-4cb1-484a-bd54-d8b46c77c9cf" />

注意事项：若将py文件强转为html文件，需要去除冗余信息，~~否则手机端界面将直接显示未删除的代码~~ 。
详见如下，除了" 此处是正文... "，其余均需要删除。
```python
# 叠乌龟HTML+JS图形化实现
# 保存为 stack_turtles.html 后用浏览器打开

html_code = """
此处是正文...
"""

if __name__ == "__main__":
    with open("stack_turtles.html", "w", encoding="utf-8") as f:
        f.write(html_code)
    print("已生成 stack_turtles.html，请用浏览器打开体验图形化叠乌龟游戏。")
```



# 微信直接启动GitHub小游戏的最简方式（可选拓展）
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
