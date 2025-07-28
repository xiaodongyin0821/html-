html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>叠乌龟游戏</title>
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
            align-items: stretch;
            justify-content: flex-start;
        }
        h1 {
            text-align: center;
            font-size: 2.2em;
            letter-spacing: 0.1em;
            color: #388e3c;
            margin-top: 22px;
            margin-bottom: 10px;
            text-shadow: 0 2px 8px #b2dfdb;
        }
        #top-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 6px;
            margin-bottom: 0;
            gap: 12px;
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
        /* 优化说明文本框样式 */
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
        #controls {
            text-align: center;
            margin-top: 12px;
            font-size: 1em;
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
        #steps {
            text-align: center;
            margin-top: 0;
            margin-bottom: 0;
            font-size: 18px;
            color: #388e3c;
            font-weight: bold;
            letter-spacing: 0.07em;
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
        #reset-btn, #start-btn, #auto-demo-btn {
            margin-left: 8px;
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
        #reset-btn:hover, #start-btn:hover, #auto-demo-btn:hover {
            background: linear-gradient(90deg, #81c784 0%, #b2dfdb 100%);
            box-shadow: 0 4px 12px #26a69a55;
        }
        #input-n {
            width: 40px;
            font-size: 1em;
            border-radius: 5px;
            border: 1.5px solid #b2dfdb;
            padding: 2px 4px;
            margin-right: 2px;
            text-align: center;
        }
        #main-game-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 10px;
            margin-bottom: 0;
            width: 100vw;
            max-width: 100vw;
            box-sizing: border-box;
        }
        #game {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin-top: 0;
            margin-bottom: 6px;
            gap: 0;
            width: 100vw;
            max-width: 100vw;
            box-sizing: border-box;
        }
        .tower {
            /* 宽度和高度由JS动态设置 */
            margin: 0;
            background: linear-gradient(180deg, #e0e0e0 60%, #b2dfdb 100%);
            border-radius: 18px 18px 0 0;
            position: relative;
            display: flex;
            flex-direction: column-reverse;
            align-items: center;
            box-shadow: 0 8px 22px #b2dfdb55;
            border: 2px solid #80cbc4;
            transition: box-shadow 0.2s, height 0.2s, width 0.2s;
        }
        .tower:hover {
            box-shadow: 0 12px 36px #26a69a55;
        }
        .tower-label-row {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            width: 100vw;
            max-width: 100vw;
            margin: 0 auto;
            margin-top: 2px;
            margin-bottom: 0;
            box-sizing: border-box;
            gap: 0;
        }
        .tower-label {
            text-align: center;
            font-weight: bold;
            font-size: 1.5em;
            color: #388e3c;
            letter-spacing: 0.13em;
            text-shadow: 0 1px 4px #b2dfdb88;
            line-height: 1.2;
            min-height: 1.5em;
            user-select: none;
            /* 宽度由JS动态设置 */
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .tower-label-row .tower-label {
            margin-top: 0;
            margin-bottom: 0;
        }
        .turtle {
            /* 尺寸由JS动态设置 */
            border-radius: 14px;
            background: none;
            color: #333;
            text-align: center;
            font-weight: bold;
            box-shadow: 0 3px 10px #b2dfdb88;
            cursor: pointer;
            transition: box-shadow 0.2s, border 0.2s, transform 0.15s;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1;
        }
        .turtle.selected {
            border: 3px solid #1976d2;
            box-shadow: 0 0 18px #1976d2cc, 0 3px 10px #b2dfdb88;
            transform: scale(1.07) translateY(-4px);
        }
        .turtle:hover:not(.selected) {
            box-shadow: 0 0 10px #26a69a99, 0 3px 10px #b2dfdb88;
            transform: scale(1.03);
        }
        .turtle-svg {
            width: 100%;
            height: 100%;
            max-width: 100%;
            max-height: 100%;
            display: block;
            filter: drop-shadow(0 2px 8px #b2dfdb88);
        }
        .turtle-num {
            position: absolute;
            left: 0; right: 0; top: 0; bottom: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #333;
            pointer-events: none;
            text-shadow: 0 1px 4px #fffde7cc, 0 0px 2px #388e3c88;
        }
        #auto-demo-btn { margin-left: 8px; }
        #speed-label { margin-left: 10px; }
        #speed-range {
            width: 90px;
            vertical-align: middle;
            accent-color: #388e3c;
        }
        #fireworks-canvas { display: none !important; }
        #blur-overlay { display: none !important; }
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
        @media (max-width: 900px) {
            .container { max-width: 100vw; }
            #game { max-width: 100vw; }
            .tower-label-row { max-width: 100vw; }
            #signature { font-size: 0.95em; height: 28px; border-radius: 0 0 10px 10px;}
            #instructions { max-width: 96vw; padding: 10px 10px 8px 10px; }
        }
        @media (max-width: 600px) {
            #instructions { padding: 7px 4vw 6px 4vw; font-size: 13px; max-width: 99vw;}
            .container { max-width: 100vw; }
            #main-game-area { margin-top: 4px; }
            #game { max-width: 100vw;}
            .tower-label-row { max-width: 100vw;}
            #steps { font-size: 10px; }
            #game-count { font-size: 10px; }
            #signature { font-size: 0.8em; height: 18px; border-radius: 0 0 6px 6px;}
        }
        @media (max-width: 400px) {
            .tower-label-row { max-width: 100vw;}
            #signature { font-size: 0.7em; height: 14px; border-radius: 0 0 4px 4px;}
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>叠乌龟游戏</h1>
        <div id="top-bar">
            <button id="toggle-instructions-btn">游戏说明</button>
        </div>
        <div id="instructions">
            <b>游戏说明：</b><br>
            叠乌龟是一种经典的益智游戏。目标是将所有乌龟从左侧的乌龟堆（A）移动到右侧的乌龟堆（C），每次只能移动一个乌龟，并且大乌龟不能叠在小乌龟上面。<br>
            <ul>
                <li>点击一个有乌龟的堆选中顶部乌龟，再点击另一个堆完成移动。</li>
                <li>每次只能移动最上面的乌龟。</li>
                <li>不能将大乌龟叠在小乌龟上。</li>
                <li>你可以选择层数，挑战更高难度！</li>
                <li>点击“自动演示”可观看自动解法过程，速度可调。</li>
            </ul>
            <span style="color:#888;">祝你玩得开心！</span>
        </div>
        <div id="controls">
            层数: <input id="input-n" type="number" min="2" max="8" value="3">
            <button id="start-btn">开始游戏</button>
            <button id="reset-btn">重置</button>
            <button id="auto-demo-btn" style="margin-left:8px;">自动演示</button>
            <span id="speed-label">
                速度: 
                <select id="speed-range">
                    <option value="10">极速</option>
                    <option value="100">很快</option>
                    <option value="500" selected>中等</option>
                    <option value="1000">较慢</option>
                    <option value="2000">很慢</option>
                </select>
                <span id="speed-value">中等</span>
            </span>
        </div>
        <div id="main-game-area">
            <div id="game"></div>
            <div class="tower-label-row" id="tower-label-row"></div>
            <div id="steps"></div>
            <div id="game-count"></div>
        </div>
        <div id="message"></div>
    </div>
    <div id="blur-overlay"></div>
    <canvas id="fireworks-canvas"></canvas>
    <div id="signature">胖墩会武术</div>
    <script>
        let towers, n, steps, selectedTower = null;
        let autoDemoRunning = false;
        let autoDemoAbort = false;

        // 游戏次数统计
        let gameCount = 0;
        if (window.localStorage) {
            let gc = localStorage.getItem('stack_turtles_game_count');
            if (gc !== null) {
                gameCount = parseInt(gc) || 0;
            }
        }

        // --- 礼花特效相关（已禁用） ---
        const fireworks = { start() {}, stop() {} };

        // 固定的乌龟和塔尺寸参数
        let fixedTurtleSize = null;

        // 计算最大化填满的乌龟和塔尺寸
        function calcFixedTurtleSize(n) {
            // 计算可用宽度和高度
            let vw = Math.max(window.innerWidth, 320);
            let vh = Math.max(window.innerHeight, 400);

            // 预留顶部/底部空间
            let topSpace = 180; // 控件、标题、说明等
            let bottomSpace = 60; // 步数、签名等
            let availableHeight = vh - topSpace - bottomSpace;
            if (availableHeight < 120) availableHeight = 120;

            // 塔label高度
            let labelHeight = 36;
            if (vw <= 900) labelHeight = 28;
            if (vw <= 600) labelHeight = 18;
            if (vw <= 400) labelHeight = 12;

            // 塔宽度 = 总宽度 / 3
            let towerGap = 0; // 塔之间无间隙
            let towerCount = 3;
            let towerWidth = Math.floor((vw - (towerCount-1)*towerGap) / towerCount);

            // 乌龟宽度最大不能超过塔宽的90%
            let maxTurtleWidth = towerWidth * 0.9;

            // 塔身高度
            let towerHeight = availableHeight;
            // 塔身可放乌龟的高度
            let towerBodyHeight = towerHeight - labelHeight;
            if (towerBodyHeight < 40) towerBodyHeight = 40;

            // 乌龟之间的间隙
            let margin = Math.max(Math.floor(towerBodyHeight * 0.02), 2);

            // 乌龟高度
            let turtleHeight = Math.floor((towerBodyHeight - (n-1)*margin) / n);
            if (turtleHeight < 8) turtleHeight = 8;
            if (turtleHeight > 120) turtleHeight = 120;

            // 乌龟宽度
            let turtleWidth = Math.floor(turtleHeight * 1.8);
            if (turtleWidth > maxTurtleWidth) {
                turtleWidth = Math.floor(maxTurtleWidth);
                turtleHeight = Math.floor(turtleWidth / 1.8);
            }

            // 字体
            let turtleFont = Math.floor(turtleHeight * 0.45 + 6);

            // 塔宽度以乌龟宽度为准
            towerWidth = Math.ceil(turtleWidth / 0.9);

            // 重新计算最大塔宽度，防止超出屏幕
            let totalTowerWidth = towerWidth * towerCount + towerGap * (towerCount-1);
            if (totalTowerWidth > vw) {
                towerWidth = Math.floor((vw - (towerCount-1)*towerGap) / towerCount);
                turtleWidth = Math.floor(towerWidth * 0.9);
                turtleHeight = Math.floor(turtleWidth / 1.8);
                turtleFont = Math.floor(turtleHeight * 0.45 + 6);
            }

            // 塔高度以乌龟高度为准
            towerBodyHeight = n * turtleHeight + (n-1)*margin;
            towerHeight = towerBodyHeight + labelHeight;

            return {
                turtleWidth, turtleHeight, turtleFont, margin, labelHeight, towerHeight, towerWidth
            };
        }

        // 生成初始塔，A柱乌龟有大小区分
        function createTowers(n) {
            towers = { 'A': [], 'B': [], 'C': [] };
            // 让A柱乌龟从大到小，底部最大，顶部最小
            for (let i = n; i >= 1; i--) {
                // 每只乌龟用对象表示，包含编号和大小比例
                let sizeRatio = 0.7 + 0.3 * (i-1)/(n-1); // 最小0.7，最大1.0
                if (n === 1) sizeRatio = 1.0;
                towers['A'].push({num: i, size: sizeRatio});
            }
        }

        // 精致乌龟SVG，支持不同大小
        function getTurtleSVG(turtleObj, color) {
            let shellColor = color || "#8bc34a";
            let bodyColor = "#388e3c";
            // turtleObj.size: 0.7~1.0
            let scale = turtleObj && turtleObj.size ? turtleObj.size : 1;
            return `
            <svg class="turtle-svg" viewBox="0 0 90 54" style="transform:scale(${scale});">
                <ellipse cx="45" cy="48" rx="22" ry="6" fill="#b2dfdb88"/>
                <g>
                    <ellipse cx="18" cy="40" rx="7" ry="4" fill="${bodyColor}" stroke="#2e7d32" stroke-width="2"/>
                    <ellipse cx="72" cy="40" rx="7" ry="4" fill="${bodyColor}" stroke="#2e7d32" stroke-width="2"/>
                    <ellipse cx="24" cy="18" rx="5" ry="2.5" fill="${bodyColor}" stroke="#2e7d32" stroke-width="2"/>
                    <ellipse cx="66" cy="18" rx="5" ry="2.5" fill="${bodyColor}" stroke="#2e7d32" stroke-width="2"/>
                    <ellipse cx="14" cy="44" rx="1.1" ry="2" fill="#795548"/>
                    <ellipse cx="22" cy="44" rx="1.1" ry="2" fill="#795548"/>
                    <ellipse cx="68" cy="44" rx="1.1" ry="2" fill="#795548"/>
                    <ellipse cx="76" cy="44" rx="1.1" ry="2" fill="#795548"/>
                    <ellipse cx="21" cy="21" rx="0.8" ry="1.3" fill="#795548"/>
                    <ellipse cx="27" cy="21" rx="0.8" ry="1.3" fill="#795548"/>
                    <ellipse cx="63" cy="21" rx="0.8" ry="1.3" fill="#795548"/>
                    <ellipse cx="69" cy="21" rx="0.8" ry="1.3" fill="#795548"/>
                </g>
                <ellipse cx="45" cy="28" rx="26" ry="16" fill="url(#shellGrad${turtleObj ? turtleObj.num : ''})" stroke="#333" stroke-width="2.2"/>
                <ellipse cx="45" cy="28" rx="20" ry="12" fill="#fffde7" opacity="0.25"/>
                <ellipse cx="45" cy="28" rx="12" ry="7" fill="#fffde7" opacity="0.18"/>
                <g opacity="0.45">
                    <ellipse cx="45" cy="28" rx="8" ry="4.5" fill="none" stroke="#fffde7" stroke-width="2"/>
                    <ellipse cx="45" cy="28" rx="15" ry="9" fill="none" stroke="#fffde7" stroke-width="1.2"/>
                    <ellipse cx="45" cy="28" rx="22" ry="13" fill="none" stroke="#fffde7" stroke-width="0.8"/>
                </g>
                <ellipse cx="45" cy="10" rx="9" ry="8" fill="${bodyColor}" stroke="#2e7d32" stroke-width="2"/>
                <ellipse cx="42" cy="8.5" rx="1.7" ry="1.7" fill="#222"/>
                <ellipse cx="48" cy="8.5" rx="1.7" ry="1.7" fill="#222"/>
                <ellipse cx="41.5" cy="8" rx="0.5" ry="0.5" fill="#fff"/>
                <ellipse cx="47.5" cy="8" rx="0.5" ry="0.5" fill="#fff"/>
                <ellipse cx="39.5" cy="13" rx="1.2" ry="0.7" fill="#ffb6b6" opacity="0.7"/>
                <ellipse cx="50.5" cy="13" rx="1.2" ry="0.7" fill="#ffb6b6" opacity="0.7"/>
                <path d="M43.5,13 Q45,15 46.5,13" stroke="#ad1457" stroke-width="1.2" fill="none" stroke-linecap="round"/>
                <defs>
                    <radialGradient id="shellGrad${turtleObj ? turtleObj.num : ''}" cx="50%" cy="45%" r="70%">
                        <stop offset="0%" stop-color="#fffde7" stop-opacity="0.7"/>
                        <stop offset="60%" stop-color="${shellColor}" stop-opacity="1"/>
                        <stop offset="100%" stop-color="#5d4037" stop-opacity="0.7"/>
                    </radialGradient>
                </defs>
            </svg>
            `;
        }

        // 设置塔和游戏区尺寸
        function setTowerAndGameHeight(n) {
            let {towerHeight, towerWidth} = fixedTurtleSize;
            document.querySelectorAll('.tower').forEach(t => {
                t.style.height = towerHeight + 'px';
                t.style.width = towerWidth + 'px';
            });
            document.getElementById('game').style.height = towerHeight + 'px';
        }

        // 渲染函数
        function render() {
            const gameDiv = document.getElementById('game');
            gameDiv.innerHTML = '';
            const turtleColors = [
                '#8bc34a', '#4caf50', '#cddc39', '#ffb347', '#ffcc33', '#b388ff', '#40c4ff', '#ffab91',
                '#a5d6a7', '#ffd54f', '#f48fb1', '#90caf9'
            ];
            let {turtleWidth, turtleHeight, turtleFont, margin, labelHeight, towerHeight, towerWidth} = fixedTurtleSize;

            // 渲染塔
            let towerDivs = [];
            ['A', 'B', 'C'].forEach(name => {
                const towerDiv = document.createElement('div');
                towerDiv.className = 'tower';
                towerDiv.dataset.tower = name;
                towerDiv.style.width = towerWidth + 'px';
                towerDiv.style.height = towerHeight + 'px';
                towerDiv.onclick = () => {
                    if (autoDemoRunning) {
                        autoDemoAbort = true;
                        return;
                    }
                    onTowerClick(name);
                };

                // 填充乌龟
                for (let i = 0; i < towers[name].length; i++) {
                    const turtleObj = towers[name][i];
                    const turtleDiv = document.createElement('div');
                    turtleDiv.className = 'turtle';
                    // 让每只乌龟的宽高根据其size缩放
                    let scale = turtleObj && turtleObj.size ? turtleObj.size : 1;
                    turtleDiv.style.width = (turtleWidth * scale) + 'px';
                    turtleDiv.style.height = (turtleHeight * scale) + 'px';
                    turtleDiv.style.fontSize = (turtleFont * scale) + 'px';
                    turtleDiv.style.lineHeight = (turtleHeight * scale) + 'px';
                    turtleDiv.style.marginBottom = (i === towers[name].length - 1 ? "0px" : margin + "px");
                    turtleDiv.style.marginLeft = ((turtleWidth - turtleWidth * scale) / 2) + "px";
                    turtleDiv.style.marginRight = ((turtleWidth - turtleWidth * scale) / 2) + "px";
                    if (selectedTower === name && i === towers[name].length - 1) {
                        turtleDiv.classList.add('selected');
                    }
                    let color = turtleColors[((turtleObj.num ? turtleObj.num : 1)-1)%turtleColors.length];
                    turtleDiv.innerHTML = getTurtleSVG(turtleObj, color) + `<div class="turtle-num" style="font-size:${turtleFont * scale}px;">${turtleObj.num ? turtleObj.num : ''}</div>`;
                    towerDiv.appendChild(turtleDiv);
                }
                // 填充空位
                for (let i = towers[name].length; i < n; i++) {
                    const emptyDiv = document.createElement('div');
                    emptyDiv.className = 'turtle';
                    emptyDiv.style.width = turtleWidth + 'px';
                    emptyDiv.style.height = turtleHeight + 'px';
                    emptyDiv.style.fontSize = turtleFont + 'px';
                    emptyDiv.style.lineHeight = turtleHeight + 'px';
                    emptyDiv.style.opacity = '0';
                    emptyDiv.style.marginBottom = (i === n - 1 ? "0px" : margin + "px");
                    towerDiv.appendChild(emptyDiv);
                }
                towerDivs.push(towerDiv);
                gameDiv.appendChild(towerDiv);
            });

            // 渲染ABC字母
            const labelRow = document.getElementById('tower-label-row');
            labelRow.innerHTML = '';
            document.querySelectorAll('.tower').forEach((towerDiv, idx) => {
                const label = document.createElement('div');
                label.className = 'tower-label';
                label.textContent = ['A', 'B', 'C'][idx];
                label.style.width = towerWidth + 'px';
                labelRow.appendChild(label);
            });

            document.getElementById('steps').textContent = `步数: ${steps}`;
            document.getElementById('game-count').textContent = `游戏次数: ${gameCount}`;
            setTowerAndGameHeight(n);
        }

        function showMessage(msg, color='#d32f2f') {
            const msgDiv = document.getElementById('message');
            msgDiv.textContent = msg;
            msgDiv.style.color = color;
        }

        function onTowerClick(name) {
            if (n === undefined) return;
            if (autoDemoRunning) return;
            if (selectedTower === null) {
                if (towers[name].length === 0) {
                    showMessage(`⚠️ ${name} 没有乌龟可选`);
                    return;
                }
                selectedTower = name;
                showMessage(`已选中 ${name}，请选择目标堆`);
            } else {
                if (selectedTower === name) {
                    selectedTower = null;
                    showMessage('');
                    render();
                    return;
                }
                let source = selectedTower, target = name;
                if (towers[source].length === 0) {
                    showMessage(`⚠️ 源堆 ${source} 没有乌龟！`);
                    selectedTower = null;
                    render();
                    return;
                }
                let turtleObj = towers[source][towers[source].length - 1];
                let turtleNum = turtleObj.num;
                // 判断目标堆顶部乌龟大小
                if (towers[target].length === 0 || towers[target][towers[target].length - 1].num > turtleNum) {
                    towers[source].pop();
                    towers[target].push(turtleObj);
                    steps += 1;
                    showMessage('');
                    if (towers['C'].length === n) {
                        if (window.localStorage) {
                            gameCount += 1;
                            localStorage.setItem('stack_turtles_game_count', gameCount);
                        } else {
                            gameCount += 1;
                        }
                        render();
                        showMessage(`🎉 恭喜！你用了 ${steps} 步完成叠乌龟！`, '#388e3c');
                        n = undefined;
                        return;
                    }
                } else {
                    showMessage(`⚠️ 无法移动：目标堆 ${target} 的顶部乌龟比当前小！`);
                }
                selectedTower = null;
            }
            render();
        }

        function startGame() {
            n = parseInt(document.getElementById('input-n').value) || 3;
            if (n < 2) n = 2;
            if (n > 8) n = 8;
            steps = 0;
            selectedTower = null;
            createTowers(n);
            fixedTurtleSize = calcFixedTurtleSize(n);
            showMessage('');
            render();
            fireworks.stop();
            autoDemoAbort = true;
            autoDemoRunning = false;
            document.getElementById('auto-demo-btn').textContent = "自动演示";
        }

        function hanoiMoves(num, from, via, to, moves) {
            if (num === 0) return;
            hanoiMoves(num-1, from, to, via, moves);
            moves.push([from, to]);
            hanoiMoves(num-1, via, from, to, moves);
        }

        async function autoDemo() {
            if (autoDemoRunning) {
                autoDemoAbort = true;
                return;
            }
            startGame();
            autoDemoRunning = true;
            autoDemoAbort = false;
            document.getElementById('auto-demo-btn').textContent = "停止演示";
            selectedTower = null;
            render();

            let speedSelect = document.getElementById('speed-range');
            let speed = parseInt(speedSelect.value) || 500;
            let moves = [];
            hanoiMoves(n, 'A', 'B', 'C', moves);

            for (let i = 0; i < moves.length; i++) {
                if (autoDemoAbort) break;
                let [from, to] = moves[i];
                selectedTower = from;
                render();
                await new Promise(r => setTimeout(r, Math.max(5, speed/2)));
                let turtleObj = towers[from][towers[from].length - 1];
                towers[from].pop();
                towers[to].push(turtleObj);
                steps += 1;
                selectedTower = null;
                render();
                await new Promise(r => setTimeout(r, speed));
            }
            selectedTower = null;
            render();
            if (!autoDemoAbort && towers['C'].length === n) {
                if (window.localStorage) {
                    gameCount += 1;
                    localStorage.setItem('stack_turtles_game_count', gameCount);
                } else {
                    gameCount += 1;
                }
                render();
                showMessage(`🎉 自动演示完成！共 ${steps} 步。`, '#388e3c');
            }
            autoDemoRunning = false;
            autoDemoAbort = false;
            document.getElementById('auto-demo-btn').textContent = "自动演示";
        }

        // 速度档位显示
        document.addEventListener('DOMContentLoaded', function() {
            let speedSelect = document.getElementById('speed-range');
            let speedValue = document.getElementById('speed-value');
            function updateSpeedLabel() {
                let label = speedSelect.options[speedSelect.selectedIndex].text;
                speedValue.textContent = label;
            }
            speedSelect.onchange = updateSpeedLabel;
            // 默认选中“中等”
            speedSelect.value = "500";
            updateSpeedLabel();

            // 说明按钮折叠
            const btn = document.getElementById('toggle-instructions-btn');
            const inst = document.getElementById('instructions');
            btn.onclick = function() {
                if (inst.style.display === 'none' || inst.style.display === '') {
                    inst.style.display = 'block';
                    btn.textContent = '收起说明';
                } else {
                    inst.style.display = 'none';
                    btn.textContent = '游戏说明';
                }
            };
        });

        // 层数输入同步调整塔高度
        document.getElementById('input-n').addEventListener('input', function() {
            let val = parseInt(this.value) || 3;
            if (val < 2) val = 2;
            if (val > 8) val = 8;
            fixedTurtleSize = calcFixedTurtleSize(val);
            render();
        });

        document.getElementById('start-btn').onclick = startGame;
        document.getElementById('reset-btn').onclick = startGame;
        document.getElementById('auto-demo-btn').onclick = autoDemo;

        // 初始化
        startGame();
        // 首次设置高度
        setTowerAndGameHeight(parseInt(document.getElementById('input-n').value) || 3);
        // 首次显示游戏次数
        if (document.getElementById('game-count')) {
            document.getElementById('game-count').textContent = `游戏次数: ${gameCount}`;
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    with open("stack_turtles.html", "w", encoding="utf-8") as f:
        f.write(html_code)
    print("已生成 stack_turtles.html，请用浏览器打开体验图形化叠乌龟游戏。")
