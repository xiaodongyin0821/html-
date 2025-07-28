html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>五子棋</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <style>
        html, body {
            height: 100%;
            width: 100%;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'HarmonyOS Sans', '微软雅黑', Arial, sans-serif;
            background: linear-gradient(120deg, #e3f2fd 0%, #fffde7 100%);
            min-height: 100vh;
            min-width: 100vw;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
        }
        .container {
            width: 100%;
            max-width: 520px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: stretch;
            background: rgba(255,255,255,0.98);
            border-radius: 18px;
            box-shadow: 0 4px 32px #b2dfdb33;
            padding: 18px 10px 10px 10px;
            margin-top: 18px;
        }
        h1 {
            text-align: center;
            font-size: 2.3em;
            letter-spacing: 0.1em;
            color: #1976d2;
            margin-top: 0;
            margin-bottom: 10px;
            text-shadow: 0 2px 8px #b2dfdb;
        }
        #top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 0 0 8px 0;
            gap: 10px;
        }
        #toggle-instructions-btn {
            background: linear-gradient(90deg, #b2dfdb 0%, #81c784 100%);
            border: none;
            border-radius: 8px;
            padding: 7px 18px;
            font-size: 1em;
            font-weight: bold;
            color: #222;
            box-shadow: 0 2px 6px #b2dfdb55;
            cursor: pointer;
            transition: background 0.2s, box-shadow 0.2s;
        }
        #toggle-instructions-btn:hover {
            background: linear-gradient(90deg, #81c784 0%, #b2dfdb 100%);
            box-shadow: 0 4px 12px #26a69a55;
        }
        #instructions {
            max-width: 480px;
            width: 98%;
            min-width: 220px;
            margin: 12px auto 0 auto;
            background: #f9fbe7;
            border: 1.5px solid #b2dfdb;
            border-radius: 12px;
            padding: 14px 18px 12px 18px;
            font-size: 15px;
            color: #444;
            line-height: 1.7;
            box-shadow: 0 2px 12px #b2dfdb33;
            display: none;
            transition: all 0.2s;
            position: relative;
            z-index: 10;
        }
        #instructions ul {
            margin: 10px 0 0 22px;
            padding-left: 0;
        }
        #instructions b {
            font-size: 1.08em;
            color: #388e3c;
        }
        #instructions span {
            display: block;
            margin-top: 8px;
            text-align: right;
            font-size: 0.98em;
        }
        #mode-detail {
            margin: 10px 0 0 0;
            padding: 10px 12px 8px 12px;
            background: #e3f2fd;
            border-radius: 8px;
            border: 1px solid #b2dfdb;
            font-size: 14px;
            color: #1976d2;
            line-height: 1.6;
            display: none;
        }
        #controls {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
            margin-bottom: 6px;
        }
        #message {
            text-align: center;
            color: #d32f2f;
            font-size: 18px;
            min-height: 24px;
            margin-top: 6px;
            font-weight: bold;
            letter-spacing: 0.05em;
        }
        #game-count {
            text-align: center;
            margin-top: 0;
            margin-bottom: 0;
            font-size: 16px;
            color: #1976d2;
            font-weight: bold;
            letter-spacing: 0.07em;
            user-select: none;
        }
        .btn {
            background: linear-gradient(90deg, #b2dfdb 0%, #81c784 100%);
            border: none;
            border-radius: 8px;
            padding: 6px 14px;
            font-size: 1em;
            font-weight: bold;
            color: #222;
            box-shadow: 0 2px 6px #b2dfdb55;
            cursor: pointer;
            transition: background 0.2s, box-shadow 0.2s;
        }
        .btn:hover {
            background: linear-gradient(90deg, #81c784 0%, #b2dfdb 100%);
            box-shadow: 0 4px 12px #26a69a55;
        }
        #board-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 10px;
            margin-bottom: 0;
            width: 100%;
            box-sizing: border-box;
        }
        #gomoku-board {
            display: grid;
            grid-template-columns: repeat(var(--size), var(--cell-size));
            grid-template-rows: repeat(var(--size), var(--cell-size));
            gap: 0;
            background: #f5f5dc;
            border: 3px solid #388e3c;
            border-radius: 10px;
            margin: 0 auto;
            box-shadow: 0 8px 22px #b2dfdb55;
            user-select: none;
            position: relative;
            width: max-content;
        }
        .cell {
            width: var(--cell-size);
            height: var(--cell-size);
            border: 1px solid #bdb76b;
            box-sizing: border-box;
            background: none;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            position: relative;
        }
        .cell:hover {
            background: #e0f7fa88;
        }
        .piece {
            width: calc(var(--cell-size) * 0.7);
            height: calc(var(--cell-size) * 0.7);
            border-radius: 50%;
            box-shadow: 0 2px 8px #b2dfdb88;
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }
        .piece.black {
            background: radial-gradient(circle at 30% 30%, #444 80%, #222 100%);
            border: 2px solid #111;
        }
        .piece.white {
            background: radial-gradient(circle at 30% 30%, #fff 80%, #eee 100%);
            border: 2px solid #bbb;
        }
        .last-move {
            box-shadow: 0 0 0 3px #ff9800cc, 0 2px 8px #b2dfdb88;
            z-index: 2;
        }
        #signature {
            width: 100vw;
            max-width: 100vw;
            margin: 0 auto 0 auto;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            bottom: 0;
            left: 0;
            right: 0;
            font-family: 'HarmonyOS Sans', '微软雅黑', Arial, sans-serif;
            font-size: 1.1em;
            color: #388e3c;
            letter-spacing: 0.12em;
            font-weight: bold;
            opacity: 0.85;
            background: rgba(255,255,255,0.7);
            border-radius: 0 0 18px 18px;
            box-shadow: 0 -2px 12px #b2dfdb33;
            margin-top: 10px;
            margin-bottom: 0;
            height: 38px;
        }
        .select-group {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .select-group label {
            font-size: 1em;
            color: #1976d2;
            font-weight: bold;
        }
        select {
            font-size: 1em;
            border-radius: 6px;
            border: 1px solid #b2dfdb;
            padding: 3px 8px;
            background: #f5f5dc;
        }
        @media (max-width: 700px) {
            .container { max-width: 99vw; }
            #gomoku-board { --cell-size: 22px; }
            #signature { font-size: 0.95em; height: 28px; border-radius: 0 0 10px 10px;}
            #instructions { max-width: 99vw; padding: 10px 10px 8px 10px; }
        }
        @media (max-width: 500px) {
            #instructions { padding: 7px 2vw 6px 2vw; font-size: 13px; max-width: 99vw;}
            .container { max-width: 100vw; }
            #board-area { margin-top: 4px; }
            #gomoku-board { --cell-size: 14px; }
            #signature { font-size: 0.8em; height: 18px; border-radius: 0 0 6px 6px;}
        }
        @media (max-width: 400px) {
            #signature { font-size: 0.7em; height: 14px; border-radius: 0 0 4px 4px;}
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>五子棋</h1>
        <div id="top-bar">
            <div class="select-group">
                <label for="mode-select">玩法:</label>
                <select id="mode-select">
                    <option value="gomoku">标准五子棋</option>
                    <option value="renju">连珠禁手</option>
                    <option value="swap2">SWAP2换先</option>
                    <option value="freestyle">自由五子棋</option>
                </select>
            </div>
            <div class="select-group">
                <label for="level-select">难度:</label>
                <select id="level-select">
                    <option value="easy">简单</option>
                    <option value="normal" selected>普通</option>
                    <option value="hard">困难</option>
                </select>
            </div>
            <button id="toggle-instructions-btn" class="btn">游戏说明</button>
        </div>
        <div id="instructions">
            <b>游戏说明：</b><br>
            五子棋是一种两人对弈的棋类游戏。你将与AI对战，先手执黑。<br>
            <ul>
                <li>点击棋盘空白处下子，黑子为玩家，白子为AI。</li>
                <li>先连成五子者获胜。</li>
                <li>可选择不同玩法和AI难度。</li>
                <li>SWAP2模式支持换先，连珠模式有禁手规则。</li>
                <li>点击“重新开始”可重置棋盘。</li>
            </ul>
            <span style="color:#888;">祝你玩得开心！</span>
            <div id="mode-detail"></div>
        </div>
        <div id="controls">
            <button id="start-btn" class="btn">重新开始</button>
            <button id="undo-btn" class="btn">悔棋</button>
            <button id="swap-btn" class="btn" style="display:none;">换先</button>
        </div>
        <div id="board-area">
            <div id="gomoku-board"></div>
        </div>
        <div id="message"></div>
        <div id="game-count"></div>
    </div>
    <div id="signature">五子棋AI by 胖墩会武术</div>
    <script>
        // --- 五子棋核心逻辑 ---
        let SIZE = 15;
        let board = [];
        let currentPlayer = 1; // 1: 玩家(黑), 2: AI(白)
        let gameOver = false;
        let lastMove = null;
        let moveHistory = [];
        let gameCount = 0;
        let mode = "gomoku";
        let aiLevel = "normal";
        let swapAvailable = false;
        let swapUsed = false;

        // 玩法详细说明
        const modeDetails = {
            "gomoku": `<b>标准五子棋：</b><br>
                <ul>
                    <li>棋盘为15×15。</li>
                    <li>黑白双方轮流下子，先连成5子者获胜。</li>
                    <li>无禁手，黑白规则完全对等。</li>
                </ul>`,
            "renju": `<b>连珠禁手：</b><br>
                <ul>
                    <li>棋盘为15×15。</li>
                    <li>黑方（玩家）先手，但有禁手限制：</li>
                    <li>黑方不能通过长连（6子及以上）、三三、四四等禁手获胜。</li>
                    <li>白方（AI）无禁手限制。</li>
                </ul>`,
            "swap2": `<b>SWAP2换先：</b><br>
                <ul>
                    <li>棋盘为15×15。</li>
                    <li>开局黑方先下3子（2黑1白），然后白方可选择换先。</li>
                    <li>换先后身份互换，AI继续落子。</li>
                    <li>无禁手，适合平衡先手优势。</li>
                </ul>`,
            "freestyle": `<b>自由五子棋：</b><br>
                <ul>
                    <li>棋盘为19×19。</li>
                    <li>黑白双方轮流下子，先连成5子者获胜。</li>
                    <li>无禁手，规则最自由，适合娱乐。</li>
                </ul>`
        };

        // 动态设置棋盘大小
        function setBoardSize(size) {
            SIZE = size;
            document.documentElement.style.setProperty('--size', size);
            document.documentElement.style.setProperty('--cell-size', '32px');
        }
        setBoardSize(15);

        if (window.localStorage) {
            let gc = localStorage.getItem('gomoku_game_count');
            if (gc !== null) {
                gameCount = parseInt(gc) || 0;
            }
        }

        function initBoard() {
            board = [];
            for (let i = 0; i < SIZE; i++) {
                let row = [];
                for (let j = 0; j < SIZE; j++) row.push(0);
                board.push(row);
            }
            currentPlayer = 1;
            gameOver = false;
            lastMove = null;
            moveHistory = [];
            swapAvailable = (mode === "swap2");
            swapUsed = false;
            document.getElementById('swap-btn').style.display = swapAvailable ? "inline-block" : "none";
            render();
            showMessage("你执黑先手。");
        }

        function render() {
            const boardDiv = document.getElementById('gomoku-board');
            boardDiv.innerHTML = '';
            for (let i = 0; i < SIZE; i++) {
                for (let j = 0; j < SIZE; j++) {
                    const cell = document.createElement('div');
                    cell.className = 'cell';
                    cell.dataset.x = i;
                    cell.dataset.y = j;
                    cell.onclick = () => onCellClick(i, j);
                    if (board[i][j] !== 0) {
                        const piece = document.createElement('div');
                        piece.className = 'piece ' + (board[i][j] === 1 ? 'black' : 'white');
                        if (lastMove && lastMove[0] === i && lastMove[1] === j) {
                            piece.classList.add('last-move');
                        }
                        cell.appendChild(piece);
                    }
                    boardDiv.appendChild(cell);
                }
            }
            if (document.getElementById('game-count')) {
                document.getElementById('game-count').textContent = `对局数: ${gameCount}`;
            }
        }

        function showMessage(msg, color='#d32f2f') {
            const msgDiv = document.getElementById('message');
            msgDiv.textContent = msg;
            msgDiv.style.color = color;
        }

        function onCellClick(x, y) {
            if (gameOver) return;
            if (currentPlayer !== 1) return;
            if (board[x][y] !== 0) {
                showMessage("此处已有棋子！");
                return;
            }
            board[x][y] = 1;
            lastMove = [x, y];
            moveHistory.push({x, y, player: 1});
            render();
            if (checkWin(x, y, 1)) {
                gameOver = true;
                if (window.localStorage) {
                    gameCount += 1;
                    localStorage.setItem('gomoku_game_count', gameCount);
                } else {
                    gameCount += 1;
                }
                render();
                showMessage("🎉 恭喜你获胜！", "#388e3c");
                return;
            }
            if (isFull()) {
                gameOver = true;
                showMessage("平局！");
                return;
            }
            currentPlayer = 2;
            showMessage("AI思考中...", "#1976d2");
            setTimeout(aiMove, aiLevel === "easy" ? 200 : aiLevel === "hard" ? 600 : 350);
        }

        function isFull() {
            for (let i = 0; i < SIZE; i++)
                for (let j = 0; j < SIZE; j++)
                    if (board[i][j] === 0) return false;
            return true;
        }

        function checkWin(x, y, player) {
            const dirs = [
                [1, 0], [0, 1], [1, 1], [1, -1]
            ];
            for (let [dx, dy] of dirs) {
                let cnt = 1;
                for (let d = 1; d < 5; d++) {
                    let nx = x + dx * d, ny = y + dy * d;
                    if (nx < 0 || nx >= SIZE || ny < 0 || ny >= SIZE) break;
                    if (board[nx][ny] === player) cnt++;
                    else break;
                }
                for (let d = 1; d < 5; d++) {
                    let nx = x - dx * d, ny = y - dy * d;
                    if (nx < 0 || nx >= SIZE || ny < 0 || ny >= SIZE) break;
                    if (board[nx][ny] === player) cnt++;
                    else break;
                }
                // 禁手规则
                if (mode === "renju" && player === 1) {
                    if (cnt >= 6) return false; // 黑子长连禁手
                }
                if (cnt >= 5) return true;
            }
            return false;
        }

        // AI主逻辑
        function aiMove() {
            if (gameOver) return;
            let move = null;
            // 1. AI能赢直接下
            move = findBestMove(2);
            if (!move) {
                // 2. 玩家能赢堵住
                move = findBestMove(1);
            }
            if (!move) {
                // 3. 难度分级
                if (aiLevel === "easy") {
                    move = randomMove();
                } else if (aiLevel === "hard") {
                    move = heuristicMove(true);
                } else {
                    move = heuristicMove(false);
                }
            }
            if (!move) {
                move = randomMove();
            }
            if (move) {
                board[move[0]][move[1]] = 2;
                lastMove = [move[0], move[1]];
                moveHistory.push({x: move[0], y: move[1], player: 2});
                render();
                if (checkWin(move[0], move[1], 2)) {
                    gameOver = true;
                    if (window.localStorage) {
                        gameCount += 1;
                        localStorage.setItem('gomoku_game_count', gameCount);
                    } else {
                        gameCount += 1;
                    }
                    render();
                    showMessage("😎 AI 获胜！", "#1976d2");
                    return;
                }
                if (isFull()) {
                    gameOver = true;
                    showMessage("平局！");
                    return;
                }
                currentPlayer = 1;
                showMessage("轮到你下棋。", "#388e3c");
            }
        }

        // 查找能直接获胜的落子
        function findBestMove(player) {
            for (let i = 0; i < SIZE; i++) {
                for (let j = 0; j < SIZE; j++) {
                    if (board[i][j] === 0) {
                        board[i][j] = player;
                        let win = checkWin(i, j, player);
                        board[i][j] = 0;
                        if (win) return [i, j];
                    }
                }
            }
            return null;
        }

        // 随机落子
        function randomMove() {
            let empties = [];
            for (let i = 0; i < SIZE; i++)
                for (let j = 0; j < SIZE; j++)
                    if (board[i][j] === 0) empties.push([i, j]);
            if (empties.length === 0) return null;
            return empties[Math.floor(Math.random() * empties.length)];
        }

        // 评分函数，hard模式更注重防守
        function heuristicMove(hard=false) {
            let maxScore = -1, best = null;
            for (let i = 0; i < SIZE; i++) {
                for (let j = 0; j < SIZE; j++) {
                    if (board[i][j] === 0) {
                        let score = evaluatePoint(i, j, 2) + 0.8 * evaluatePoint(i, j, 1);
                        if (hard) score += 0.5 * evaluatePoint(i, j, 2) * evaluatePoint(i, j, 1);
                        if (score > maxScore) {
                            maxScore = score;
                            best = [i, j];
                        }
                    }
                }
            }
            return best;
        }

        // 评分：本方连子数+阻断对方
        function evaluatePoint(x, y, player) {
            let score = 0;
            const dirs = [
                [1, 0], [0, 1], [1, 1], [1, -1]
            ];
            for (let [dx, dy] of dirs) {
                let cnt = 1, block = 0;
                for (let d = 1; d < 5; d++) {
                    let nx = x + dx * d, ny = y + dy * d;
                    if (nx < 0 || nx >= SIZE || ny < 0 || ny >= SIZE) { block++; break; }
                    if (board[nx][ny] === player) cnt++;
                    else if (board[nx][ny] !== 0) { block++; break; }
                    else break;
                }
                for (let d = 1; d < 5; d++) {
                    let nx = x - dx * d, ny = y - dy * d;
                    if (nx < 0 || nx >= SIZE || ny < 0 || ny >= SIZE) { block++; break; }
                    if (board[nx][ny] === player) cnt++;
                    else if (board[nx][ny] !== 0) { block++; break; }
                    else break;
                }
                if (cnt >= 5) score += 10000;
                else if (cnt === 4 && block === 0) score += 1000;
                else if (cnt === 4 && block === 1) score += 200;
                else if (cnt === 3 && block === 0) score += 100;
                else if (cnt === 3 && block === 1) score += 30;
                else if (cnt === 2 && block === 0) score += 10;
                else if (cnt === 2 && block === 1) score += 3;
            }
            return score;
        }

        // 悔棋
        document.getElementById('undo-btn').onclick = function() {
            if (moveHistory.length < 2 || gameOver) return;
            // 撤销AI和玩家各一步
            for (let k = 0; k < 2; k++) {
                let last = moveHistory.pop();
                if (last) {
                    board[last.x][last.y] = 0;
                    lastMove = moveHistory.length ? [moveHistory[moveHistory.length-1].x, moveHistory[moveHistory.length-1].y] : null;
                }
            }
            gameOver = false;
            currentPlayer = 1;
            render();
            showMessage("悔棋成功，轮到你下棋。", "#388e3c");
        };

        // 换先（SWAP2模式）
        document.getElementById('swap-btn').onclick = function() {
            if (!swapAvailable || swapUsed || moveHistory.length < 3) return;
            // 交换玩家和AI身份
            currentPlayer = 2;
            swapUsed = true;
            swapAvailable = false;
            showMessage("已换先，AI继续。", "#1976d2");
            setTimeout(aiMove, 400);
            this.style.display = "none";
        };

        document.getElementById('start-btn').onclick = initBoard;

        // 说明按钮折叠
        document.addEventListener('DOMContentLoaded', function() {
            const btn = document.getElementById('toggle-instructions-btn');
            const inst = document.getElementById('instructions');
            btn.onclick = function() {
                if (inst.style.display === 'none' || inst.style.display === '') {
                    inst.style.display = 'block';
                    btn.textContent = '收起说明';
                    // 显示当前玩法详细说明
                    showModeDetail();
                } else {
                    inst.style.display = 'none';
                    btn.textContent = '游戏说明';
                }
            };
            // 页面初始时显示当前玩法说明
            showModeDetail();
        });

        // 玩法切换
        document.getElementById('mode-select').onchange = function() {
            mode = this.value;
            // 切换玩法时合理化界面
            if (mode === "freestyle") setBoardSize(19);
            else setBoardSize(15);
            // 切换玩法时关闭说明面板
            document.getElementById('instructions').style.display = 'none';
            document.getElementById('toggle-instructions-btn').textContent = '游戏说明';
            // 切换玩法时刷新玩法详细说明
            showModeDetail();
            initBoard();
        };
        // 难度切换
        document.getElementById('level-select').onchange = function() {
            aiLevel = this.value;
            showMessage("难度已切换为：" + (aiLevel === "easy" ? "简单" : aiLevel === "hard" ? "困难" : "普通"), "#1976d2");
        };

        // 显示当前玩法详细说明
        function showModeDetail() {
            const modeSel = document.getElementById('mode-select');
            const modeVal = modeSel ? modeSel.value : mode;
            const detailDiv = document.getElementById('mode-detail');
            if (detailDiv) {
                detailDiv.innerHTML = modeDetails[modeVal] || "";
                detailDiv.style.display = "block";
            }
        }

        // 初始化
        initBoard();
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    with open("gomoku.html", "w", encoding="utf-8") as f:
        f.write(html_code)
    print("已生成 gomoku.html，请用浏览器打开体验五子棋。")
