html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>迷宫游戏</title>
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
            background: linear-gradient(135deg, #e0f7fa 0%, #fffde7 100%);
            min-height: 100vh;
            min-width: 100vw;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: stretch;
        }
        .container {
            width: 100vw;
            max-width: 100vw;
            margin: 0 auto;
            flex: 1 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
        }
        h1 {
            text-align: center;
            font-size: 2.2em;
            letter-spacing: 0.1em;
            color: #388e3c;
            margin-top: 32px;
            margin-bottom: 18px;
            text-shadow: 0 2px 8px #b2dfdb;
        }
        #maze-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 24px;
        }
        #maze-canvas {
            background: #222;
            border-radius: 10px;
            box-shadow: 0 8px 22px #b2dfdb55;
            border: 2px solid #bfa06a;
            display: block;
            margin-bottom: 18px;
        }
        #maze-controls {
            margin-top: 10px;
            display: flex;
            flex-direction: row;
            gap: 10px;
            align-items: center;
            justify-content: center;
        }
        #maze-controls button {
            background: linear-gradient(90deg, #b2dfdb 0%, #81c784 100%);
            border: none;
            border-radius: 8px;
            padding: 8px 24px;
            font-size: 1em;
            font-weight: bold;
            color: #222;
            box-shadow: 0 2px 6px #b2dfdb55;
            cursor: pointer;
            transition: background 0.2s, box-shadow 0.2s;
        }
        #maze-controls button:hover {
            background: linear-gradient(90deg, #81c784 0%, #b2dfdb 100%);
            box-shadow: 0 4px 12px #26a69a55;
        }
        #level-select {
            margin-left: 10px;
            font-size: 1em;
            border-radius: 6px;
            padding: 6px 10px;
            border: 1px solid #b2dfdb;
            background: #fff;
        }
        #timer, #score, #level-label {
            font-size: 1.1em;
            color: #1976d2;
            margin: 0 8px;
            font-weight: bold;
        }
        #instructions {
            max-width: 420px;
            width: 92vw;
            min-width: 220px;
            box-sizing: border-box;
            margin: 18px auto 0 auto;
            background: rgba(255,255,255,0.98);
            border: 1.5px solid #b2dfdb;
            border-radius: 12px;
            padding: 14px 22px 12px 22px;
            font-size: 15px;
            color: #444;
            line-height: 1.7;
            box-shadow: 0 2px 12px #b2dfdb33;
            display: none;
            transition: all 0.2s;
            position: relative;
            z-index: 10;
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
            margin-top: 10px;
        }
        #toggle-instructions-btn:hover {
            background: linear-gradient(90deg, #81c784 0%, #b2dfdb 100%);
            box-shadow: 0 4px 12px #26a69a55;
        }
        #signature {
            text-align: center;
            color: #888;
            font-size: 1em;
            margin-top: 40px;
            margin-bottom: 18px;
            letter-spacing: 0.12em;
            user-select: none;
        }
        @media (max-width: 700px) {
            #maze-canvas { width: 90vw !important; height: 90vw !important; max-width: 360px !important; max-height: 360px !important;}
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>迷宫游戏</h1>
        <div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:8px;">
            <span id="level-label">难度：</span>
            <select id="level-select">
                <option value="1">简单</option>
                <option value="2">普通</option>
                <option value="3">困难</option>
            </select>
            <span id="timer">用时: 0.00s</span>
            <span id="score">评分: 0</span>
        </div>
        <button id="toggle-instructions-btn">游戏说明</button>
        <div id="instructions">
            <b>游戏说明：</b><br>
            迷宫游戏是一款经典的益智游戏。你需要通过键盘方向键或按钮操作小球，从起点走到终点。<br>
            <ul>
                <li>方向键 ← ↑ → ↓ 控制小球移动</li>
                <li>点击“重置迷宫”可生成新迷宫</li>
                <li>到达右下角终点即胜利</li>
                <li>每一关有怪物巡逻，碰到怪物会失败</li>
                <li>用时越短，评分越高</li>
                <li>可选择不同难度，难度越高迷宫越大、怪物越多</li>
            </ul>
            <span style="color:#888;">祝你玩得开心！</span>
        </div>
        <div id="maze-area">
            <canvas id="maze-canvas" width="420" height="420" tabindex="0"></canvas>
            <div id="maze-controls">
                <button id="reset-btn">重置迷宫</button>
            </div>
        </div>
        <div id="signature">胖墩会武术</div>
    </div>
    <script>
    // --- 迷宫生成与游戏逻辑 ---
    // 难度参数
    const LEVELS = [
        {rows: 11, cols: 11, monsters: 1}, // 简单
        {rows: 17, cols: 17, monsters: 2}, // 普通
        {rows: 23, cols: 23, monsters: 3}  // 困难
    ];
    let level = 1; // 1:简单 2:普通 3:困难
    let ROWS = LEVELS[level-1].rows, COLS = LEVELS[level-1].cols;
    let MONSTER_COUNT = LEVELS[level-1].monsters;
    let CELL = Math.floor(420 / Math.max(ROWS, COLS));
    const canvas = document.getElementById('maze-canvas');
    const ctx = canvas.getContext('2d');
    let maze = [];
    let visited = [];
    let player = {x: 0, y: 0};
    let monsters = [];
    let gameWon = false;
    let gameLost = false;
    let timer = 0;
    let timerInterval = null;
    let startTime = null;
    let score = 0;

    // 迷宫生成算法：Prim算法，保证有更多分支和死路
    function initMaze() {
        maze = [];
        visited = [];
        for (let y = 0; y < ROWS; y++) {
            let row = [];
            let vrow = [];
            for (let x = 0; x < COLS; x++) {
                row.push({top: true, right: true, bottom: true, left: true});
                vrow.push(false);
            }
            maze.push(row);
            visited.push(vrow);
        }
        generateMazePrim();
    }

    function generateMazePrim() {
        // Prim算法生成迷宫，分支更多
        let wallList = [];
        let inMaze = [];
        for (let y = 0; y < ROWS; y++) {
            inMaze.push(Array(COLS).fill(false));
        }
        let sx = 0, sy = 0;
        inMaze[sy][sx] = true;
        let addWalls = (x, y) => {
            if (x > 0) wallList.push({x, y, nx: x-1, ny: y, dir: 'left', opp: 'right'});
            if (x < COLS-1) wallList.push({x, y, nx: x+1, ny: y, dir: 'right', opp: 'left'});
            if (y > 0) wallList.push({x, y, nx: x, ny: y-1, dir: 'top', opp: 'bottom'});
            if (y < ROWS-1) wallList.push({x, y, nx: x, ny: y+1, dir: 'bottom', opp: 'top'});
        };
        addWalls(sx, sy);
        while (wallList.length > 0) {
            let idx = Math.floor(Math.random() * wallList.length);
            let wall = wallList.splice(idx, 1)[0];
            let {x, y, nx, ny, dir, opp} = wall;
            if (nx < 0 || nx >= COLS || ny < 0 || ny >= ROWS) continue;
            if (!inMaze[ny][nx]) {
                maze[y][x][dir] = false;
                maze[ny][nx][opp] = false;
                inMaze[ny][nx] = true;
                addWalls(nx, ny);
            }
        }
    }

    function drawMaze() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.strokeStyle = "#bfa06a";
        ctx.lineWidth = 3;
        for (let y = 0; y < ROWS; y++) {
            for (let x = 0; x < COLS; x++) {
                const cell = maze[y][x];
                const px = x * CELL, py = y * CELL;
                if (cell.top) {
                    ctx.beginPath();
                    ctx.moveTo(px, py);
                    ctx.lineTo(px + CELL, py);
                    ctx.stroke();
                }
                if (cell.right) {
                    ctx.beginPath();
                    ctx.moveTo(px + CELL, py);
                    ctx.lineTo(px + CELL, py + CELL);
                    ctx.stroke();
                }
                if (cell.bottom) {
                    ctx.beginPath();
                    ctx.moveTo(px, py + CELL);
                    ctx.lineTo(px + CELL, py + CELL);
                    ctx.stroke();
                }
                if (cell.left) {
                    ctx.beginPath();
                    ctx.moveTo(px, py);
                    ctx.lineTo(px, py + CELL);
                    ctx.stroke();
                }
            }
        }
        // 绘制起点和终点
        ctx.fillStyle = "#81c784";
        ctx.fillRect(4, 4, CELL-8, CELL-8);
        ctx.fillStyle = "#ffb300";
        ctx.fillRect((COLS-1)*CELL+4, (ROWS-1)*CELL+4, CELL-8, CELL-8);
        // 绘制怪物
        for (let m of monsters) {
            ctx.beginPath();
            ctx.arc(m.x*CELL + CELL/2, m.y*CELL + CELL/2, CELL/2-8, 0, 2*Math.PI);
            ctx.fillStyle = "#e53935";
            ctx.shadowColor = "#e53935";
            ctx.shadowBlur = 8;
            ctx.fill();
            ctx.shadowBlur = 0;
            // 怪物眼睛
            ctx.beginPath();
            ctx.arc(m.x*CELL + CELL/2-4, m.y*CELL + CELL/2-2, 2, 0, 2*Math.PI);
            ctx.arc(m.x*CELL + CELL/2+4, m.y*CELL + CELL/2-2, 2, 0, 2*Math.PI);
            ctx.fillStyle = "#fff";
            ctx.fill();
        }
        // 绘制玩家
        ctx.beginPath();
        ctx.arc(player.x*CELL + CELL/2, player.y*CELL + CELL/2, CELL/2-6, 0, 2*Math.PI);
        ctx.fillStyle = "#1976d2";
        ctx.shadowColor = "#1976d2";
        ctx.shadowBlur = 8;
        ctx.fill();
        ctx.shadowBlur = 0;
        ctx.restore();
        if (gameWon) {
            ctx.save();
            ctx.globalAlpha = 0.8;
            ctx.fillStyle = "#fff";
            ctx.fillRect(0,canvas.height/2-40,canvas.width,80);
            ctx.globalAlpha = 1;
            ctx.fillStyle = "#388e3c";
            ctx.font = "bold 2em Arial";
            ctx.textAlign = "center";
            ctx.fillText("恭喜通关！",canvas.width/2,canvas.height/2-10);
            ctx.font = "1.2em Arial";
            ctx.fillStyle = "#1976d2";
            ctx.fillText("用时: " + timer.toFixed(2) + "s  评分: " + score, canvas.width/2, canvas.height/2+30);
            ctx.restore();
        }
        if (gameLost) {
            ctx.save();
            ctx.globalAlpha = 0.8;
            ctx.fillStyle = "#fff";
            ctx.fillRect(0,canvas.height/2-40,canvas.width,80);
            ctx.globalAlpha = 1;
            ctx.fillStyle = "#e53935";
            ctx.font = "bold 2em Arial";
            ctx.textAlign = "center";
            ctx.fillText("被怪物抓住了！",canvas.width/2,canvas.height/2+10);
            ctx.restore();
        }
    }

    function resetGame() {
        // 重新设置参数
        ROWS = LEVELS[level-1].rows;
        COLS = LEVELS[level-1].cols;
        MONSTER_COUNT = LEVELS[level-1].monsters;
        CELL = Math.floor(420 / Math.max(ROWS, COLS));
        canvas.width = CELL * COLS;
        canvas.height = CELL * ROWS;
        player = {x: 0, y: 0};
        gameWon = false;
        gameLost = false;
        score = 0;
        timer = 0;
        document.getElementById('timer').textContent = "用时: 0.00s";
        document.getElementById('score').textContent = "评分: 0";
        clearInterval(timerInterval);
        startTime = null;
        initMaze();
        placeMonsters();
        drawMaze();
        canvas.focus();
    }

    function placeMonsters() {
        monsters = [];
        let placed = 0;
        let forbidden = [{x:0,y:0},{x:COLS-1,y:ROWS-1}];
        while (placed < MONSTER_COUNT) {
            let mx = Math.floor(Math.random() * COLS);
            let my = Math.floor(Math.random() * ROWS);
            // 不放在起点终点和玩家身上
            if (forbidden.some(p=>p.x===mx&&p.y===my)) continue;
            if (monsters.some(m=>m.x===mx&&m.y===my)) continue;
            monsters.push({x: mx, y: my, lastDir: null});
            placed++;
        }
    }

    function movePlayer(dx, dy) {
        if (gameWon || gameLost) return;
        const nx = player.x + dx, ny = player.y + dy;
        if (nx < 0 || nx >= COLS || ny < 0 || ny >= ROWS) return;
        const cell = maze[player.y][player.x];
        if (dx === -1 && !cell.left) player.x--;
        else if (dx === 1 && !cell.right) player.x++;
        else if (dy === -1 && !cell.top) player.y--;
        else if (dy === 1 && !cell.bottom) player.y++;
        // 怪物移动
        moveMonsters();
        // 检查碰撞
        checkGameState();
        drawMaze();
        // 计时
        if (!startTime) {
            startTime = Date.now();
            timerInterval = setInterval(updateTimer, 50);
        }
    }

    function moveMonsters() {
        // 简单AI：怪物向玩家靠近，遇墙随机拐弯
        for (let m of monsters) {
            let dirs = [];
            const cell = maze[m.y][m.x];
            if (!cell.left) dirs.push({dx:-1,dy:0,dir:'left'});
            if (!cell.right) dirs.push({dx:1,dy:0,dir:'right'});
            if (!cell.top) dirs.push({dx:0,dy:-1,dir:'top'});
            if (!cell.bottom) dirs.push({dx:0,dy:1,dir:'bottom'});
            // 怪物优先向玩家靠近
            dirs.sort((a,b)=>{
                let da = Math.abs((m.x+a.dx)-player.x)+Math.abs((m.y+a.dy)-player.y);
                let db = Math.abs((m.x+b.dx)-player.x)+Math.abs((m.y+b.dy)-player.y);
                return da-db;
            });
            // 避免原地打转
            if (m.lastDir) {
                dirs = dirs.filter(d=>!(d.dx===-m.lastDir.dx&&d.dy===-m.lastDir.dy));
                if (dirs.length===0) dirs = [{dx:-m.lastDir.dx,dy:-m.lastDir.dy}];
            }
            // 20%概率随机走
            let move;
            if (Math.random()<0.2) move = dirs[Math.floor(Math.random()*dirs.length)];
            else move = dirs[0];
            m.x += move.dx;
            m.y += move.dy;
            m.lastDir = move;
        }
    }

    function checkGameState() {
        // 检查是否被怪物抓住
        for (let m of monsters) {
            if (m.x === player.x && m.y === player.y) {
                gameLost = true;
                clearInterval(timerInterval);
                drawMaze();
                return;
            }
        }
        // 检查是否到达终点
        if (player.x === COLS-1 && player.y === ROWS-1) {
            gameWon = true;
            clearInterval(timerInterval);
            updateTimer();
            calcScore();
            drawMaze();
        }
    }

    function updateTimer() {
        if (!startTime) return;
        timer = (Date.now() - startTime) / 1000;
        document.getElementById('timer').textContent = "用时: " + timer.toFixed(2) + "s";
    }

    function calcScore() {
        // 评分：基础分+难度+速度
        let base = 1000;
        let diff = level * 500;
        let timeScore = Math.max(0, 1000 - Math.floor(timer*50));
        score = base + diff + timeScore;
        document.getElementById('score').textContent = "评分: " + score;
    }

    document.getElementById('reset-btn').onclick = resetGame;

    document.getElementById('level-select').onchange = function() {
        level = parseInt(this.value);
        resetGame();
    };

    document.addEventListener('keydown', function(e){
        if(document.activeElement!==canvas) return;
        if (gameWon || gameLost) return;
        if (e.key === "ArrowLeft") movePlayer(-1,0);
        else if (e.key === "ArrowRight") movePlayer(1,0);
        else if (e.key === "ArrowUp") movePlayer(0,-1);
        else if (e.key === "ArrowDown") movePlayer(0,1);
    });

    // 说明按钮
    document.getElementById('toggle-instructions-btn').onclick = function() {
        let inst = document.getElementById('instructions');
        if(inst.style.display==="none"||inst.style.display==="") {
            inst.style.display = "block";
            this.textContent = "收起说明";
        } else {
            inst.style.display = "none";
            this.textContent = "游戏说明";
        }
    };

    // 初始化
    resetGame();
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    with open("maze.html", "w", encoding="utf-8") as f:
        f.write(html_code)
    print("已生成 maze.html，请用浏览器打开体验迷宫游戏。")
