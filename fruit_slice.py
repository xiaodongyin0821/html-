html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>水果忍者</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <link href="https://fonts.googleapis.com/css2?family=Luckiest+Guy&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        html, body {
            height: 100%;
            width: 100%;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Luckiest Guy', 'Orbitron', Arial, sans-serif;
            background: radial-gradient(ellipse at 60% 40%, #fffbe7 0%, #ffe082 60%, #ffd54f 100%), 
                        linear-gradient(135deg, #ffecb3 0%, #ff9800 100%);
            min-height: 100vh;
            min-width: 100vw;
            display: flex;
            flex-direction: column;
            align-items: stretch;
            animation: bgmove 12s linear infinite alternate;
        }
        @keyframes bgmove {
            0% { background-position: 0% 0%, 100% 100%; }
            100% { background-position: 100% 100%, 0% 0%; }
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
            color: #fff;
            margin-top: 22px;
            margin-bottom: 8px;
            text-shadow: 0 8px 32px #ff9800, 0 2px 0 #fff, 0 0 16px #ffd54f, 0 0 40px #ff5722;
            font-family: 'Orbitron', 'Luckiest Guy', cursive, sans-serif;
            user-select: none;
            background: linear-gradient(90deg, #ff9800 10%, #ffd600 50%, #ff4081 90%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 12px #ffb30088);
        }
        #top-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 10px;
            gap: 18px;
        }
        #toggle-instructions-btn, #mode-btn, #option-btn, #music-btn, #start-btn {
            background: linear-gradient(90deg, #ffd600 0%, #ff9800 100%);
            border: none;
            border-radius: 14px;
            padding: 9px 22px;
            font-size: 1em;
            font-weight: bold;
            color: #222;
            box-shadow: 0 2px 12px #ffecb355;
            cursor: pointer;
            margin-left: 10px;
        }
        #music-btn {
            font-size: 1.3em;
            padding: 9px 14px;
            border-radius: 50%;
            background: #fffde7;
            color: #ffb300;
            border: 2px solid #ffd600;
            margin-left: 0;
            box-shadow: 0 2px 8px #ffd60055;
        }
        #music-btn.on {
            background: #ffd600;
            color: #d32f2f;
        }
        #instructions {
            max-width: 540px;
            width: 98vw;
            min-width: 200px;
            margin: 18px auto 0 auto;
            background: rgba(255,255,255,0.98);
            border: 3px solid #ffd600;
            border-radius: 22px;
            padding: 20px 28px 18px 28px;
            font-size: 16px;
            color: #333;
            line-height: 1.7;
            box-shadow: 0 4px 32px #ffd54f55;
            display: none;
            position: relative;
            z-index: 10;
        }
        #controls {
            text-align: center;
            margin-top: 16px;
        }
        #message {
            text-align: center;
            color: #d32f2f;
            font-size: 20px;
            min-height: 32px;
            margin-top: 14px;
            font-weight: bold;
            letter-spacing: 0.09em;
            text-shadow: 0 2px 12px #fff3e0;
        }
        #score, #combo, #mode, #lives, #highscore {
            text-align: center;
            margin: 0;
            font-size: 18px;
            color: #e65100;
            font-weight: bold;
            letter-spacing: 0.11em;
            user-select: none;
            display: inline-block;
            margin-right: 12px;
            text-shadow: 0 2px 8px #fffbe7;
        }
        #highscore {
            color: #1976d2;
            font-size: 16px;
            margin-right: 0;
        }
        #combo {
            color: #ff4081;
            font-size: 16px;
            margin-left: 0;
            margin-right: 12px;
        }
        #mode {
            color: #1976d2;
            font-size: 16px;
            margin-left: 0;
            margin-right: 12px;
        }
        #lives {
            color: #d32f2f;
            font-size: 16px;
            margin-right: 0;
        }
        #game-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100vw;
            max-width: 100vw;
            box-sizing: border-box;
        }
        #game-canvas {
            background: repeating-linear-gradient(135deg, #fffde7 0 40px, #ffe082 40px 80px, #ffd54f 80px 120px, #fffde7 120px 160px);
            border-radius: 32px;
            box-shadow: 0 12px 48px #ffecb355, 0 0px 0px #fff;
            border: 4px solid #ffd600;
            margin: 0 auto;
            display: block;
            touch-action: none;
            margin-top: 18px;
        }
        #game-canvas.frozen {
            box-shadow: 0 0 40px #1976d2cc, 0 12px 48px #ffecb355;
            filter: blur(2px) grayscale(0.6) brightness(1.1);
        }
        #status-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 12px;
            gap: 12px;
        }
        #signature {
            width: 100vw;
            max-width: 100vw;
            margin: 0 auto 0 auto;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Orbitron', 'Luckiest Guy', Arial, sans-serif;
            font-size: 1em;
            color: #fff;
            letter-spacing: 0.18em;
            font-weight: bold;
            opacity: 0.92;
            background: linear-gradient(90deg, #ffd600 0%, #ff9800 100%);
            border-radius: 0 0 32px 32px;
            box-shadow: 0 -2px 24px #ffe08255;
            margin-top: 16px;
            height: 36px;
            text-shadow: 0 2px 8px #ffb300, 0 0 8px #fffde7;
        }
        .particle {
            position: absolute;
            pointer-events: none;
            border-radius: 50%;
            opacity: 0.8;
            z-index: 1000;
            box-shadow: 0 0 16px #ffd60088, 0 0 4px #fff;
            animation: particle-float 0.8s linear;
        }
        @keyframes particle-float {
            0% { opacity: 0.8; }
            100% { opacity: 0; }
        }
        .fruit-half {
            position: absolute;
            pointer-events: none;
            z-index: 900;
            will-change: transform, opacity;
            transition: transform 0.7s cubic-bezier(.4,2,.6,1), opacity 0.7s;
            filter: drop-shadow(0 0 8px #ffd60088);
        }
        .score-float {
            position: absolute;
            pointer-events: none;
            font-weight: bold;
            font-family: 'Orbitron', 'Luckiest Guy', Arial, sans-serif;
            z-index: 1200;
            font-size: 1.1em;
            text-shadow: 0 2px 12px #fffbe7, 0 0 8px #ffd54f;
            opacity: 0.97;
            transition: transform 0.8s cubic-bezier(.4,2,.6,1), opacity 0.8s;
            will-change: transform, opacity;
        }
        #countdown {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%,-50%);
            font-size: 3em;
            color: #ff5722;
            font-family: 'Orbitron', 'Luckiest Guy', cursive, sans-serif;
            text-shadow: 0 4px 32px #fff3e0, 0 2px 0 #fff, 0 0 16px #ffd54f;
            z-index: 2000;
            pointer-events: none;
            display: none;
            letter-spacing: 0.18em;
        }
        .frozen {
            filter: blur(2px) grayscale(0.6) brightness(1.1);
            transition: filter 0.3s;
        }
        body.psy, #game-canvas.psy {
            filter: invert(1) hue-rotate(180deg) contrast(1.1) !important;
            transition: filter 0.5s;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>水果忍者</h1>
        <div id="top-bar">
            <button id="toggle-instructions-btn">玩法说明</button>
            <button id="mode-btn">玩法：经典</button>
            <button id="option-btn">选项：经典</button>
            <button id="music-btn" title="音乐开关">🎵</button>
        </div>
        <div id="instructions">
            <b>玩法说明：</b>
            <ol>
                <li><b>经典：</b>常规切水果，切到炸弹有惩罚。</li>
                <li><b>特效：</b>每个水果都带有独特特效。</li>
            </ol>
            <b>操作：</b>
            <ul>
                <li>用鼠标或手指在画布上划线切水果。</li>
                <li>切中水果得分，连续切中有连击加成。</li>
                <li>切到炸弹有惩罚。</li>
                <li>点击“玩法”切换，点击“选项”切换模式，点击🎵切换音乐。</li>
            </ul>
            <span style="color:#888;">祝你玩得开心！</span>
        </div>
        <div id="controls">
            <button id="start-btn">开始游戏</button>
        </div>
        <div id="status-bar">
            <div id="mode">玩法: 经典 | 选项: 经典</div>
            <div id="score">分数: 0</div>
            <div id="highscore">最高: 0</div>
            <div id="combo">连击: 0</div>
            <div id="lives">生命: 3</div>
        </div>
        <div id="game-area" style="position:relative;">
            <canvas id="game-canvas" width="340" height="420"></canvas>
            <div id="countdown"></div>
        </div>
        <div id="message"></div>
    </div>
    <div id="signature">Fruit Ninja X</div>
    <audio id="bgm" src="https://cdn.jsdelivr.net/gh/zh-lx/picx@main/fruit_bgm.mp3" loop preload="auto"></audio>
    <audio id="cut-sound" src="https://cdn.jsdelivr.net/gh/zh-lx/picx@main/fruit_cut.mp3" preload="auto"></audio>
    <audio id="combo-sound" src="https://cdn.jsdelivr.net/gh/zh-lx/picx@main/fruit_combo.mp3" preload="auto"></audio>
    <audio id="bomb-sound" src="https://cdn.jsdelivr.net/gh/zh-lx/picx@main/fruit_bomb.mp3" preload="auto"></audio>
    <audio id="golden-sound" src="https://cdn.jsdelivr.net/gh/zh-lx/picx@main/fruit_golden.mp3" preload="auto"></audio>
    <audio id="freeze-sound" src="https://cdn.jsdelivr.net/gh/zh-lx/picx@main/fruit_freeze.mp3" preload="auto"></audio>
    <audio id="heal-sound" src="https://cdn.jsdelivr.net/gh/zh-lx/picx@main/fruit_heal.mp3" preload="auto"></audio>
    <script>
        // --- 配置 ---
        const PLAY_MODES = [
            {name: "经典", desc: "常规切水果，炸弹有惩罚", effect: false},
            {name: "特效", desc: "每个水果都带有独特特效", effect: true}
        ];
        const GAME_OPTIONS = [
            {name: "经典", desc: "漏掉水果扣命，切炸弹直接结束", time: null, endless: false, bombEnd: true, bombPenalty: 0},
            {name: "限时", desc: "60秒内尽量多得分，炸弹扣5分", time: 60, endless: false, bombEnd: false, bombPenalty: 5},
            {name: "无尽", desc: "无限生命，炸弹扣3分", time: null, endless: true, bombEnd: false, bombPenalty: 3}
        ];
        const FRUITS = [
            {name: "西瓜", emoji: "🍉", radius: 36, special: null, score: 3},
            {name: "苹果", emoji: "🍎", radius: 24, special: null, score: 2},
            {name: "橙子", emoji: "🍊", radius: 24, special: null, score: 2},
            {name: "柠檬", emoji: "🍋", radius: 20, special: null, score: 1},
            {name: "猕猴桃", emoji: "🥝", radius: 20, special: null, score: 1},
            {name: "香蕉", emoji: "🍌", radius: 22, special: null, score: 1},
            {name: "葡萄", emoji: "🍇", radius: 18, special: null, score: 1},
            {name: "草莓", emoji: "🍓", radius: 16, special: null, score: 1},
            {name: "蓝莓", emoji: "🫐", radius: 14, special: null, score: 1},
            {name: "樱桃", emoji: "🍒", radius: 14, special: null, score: 1},
            // 特效水果
            {name: "冰冻果", emoji: "🧊", radius: 18, special: "freeze", score: 2},
            {name: "回血果", emoji: "💖", radius: 18, special: "heal", score: 1},
            {name: "全屏切割", emoji: "🧃", radius: 16, special: "sliceall", score: 1},
            {name: "黄金果", emoji: "🥇", radius: 18, special: "golden", score: 10},
            {name: "大满贯", emoji: "🎉", radius: 22, special: "grand", score: 0},
            {name: "迷幻果", emoji: "🍄", radius: 18, special: "psy", score: 2},
            {name: "巧克力", emoji: "🍫", radius: 18, special: "choco", score: 2},
            {name: "随机果", emoji: "🧬", radius: 18, special: "random", score: 2},
            {name: "幸运果", emoji: "🍀", radius: 18, special: "lucky", score: 2},
            {name: "蜂蜜果", emoji: "🍯", radius: 18, special: "honey", score: 2}
        ];
        const BOMB = {name: "炸弹", emoji: "💣", radius: 18, special: "bomb", score: -5};
        const FRUIT_PROB = [0.90, 0.85, 0.88];
        const SPECIAL_PROB = [0.13, 0.15, 0.13];
        const GRAVITY = 0.32;
        const LAUNCH_INTERVAL = [320, 700];
        const FRUIT_SPEED = [7, 13];
        let MAX_LIVES = 3;
        let MAX_LIVES_LIMIT = 5;

        // --- 状态 ---
        let fruits = [];
        let trails = [];
        let score = 0;
        let highscore = 0;
        let lives = MAX_LIVES;
        let running = false;
        let lastLaunch = 0;
        let launchTimer = null;
        let animFrame = null;
        let canvas, ctx;
        let width = 340, height = 420;
        let isDrawing = false;
        let lastPoint = null;
        let gameOver = false;
        let combo = 0;
        let comboTimer = null;
        let playModeIdx = 0;
        let optionIdx = 0;
        let playMode = PLAY_MODES[0];
        let option = GAME_OPTIONS[0];
        let timeLeft = null;
        let timerInterval = null;
        let musicOn = true;
        let activeTouches = {};
        let holding = false;
        let frozen = false;
        let freezeTimer = null;
        let grandActive = false;
        let luckyActive = false;
        let chocoActive = false;
        let honeyActive = false;
        let psyActive = false;

        // --- 音效 ---
        function playSound(id) {
            let el = document.getElementById(id);
            if (!el) return;
            el.currentTime = 0;
            el.volume = 0.7;
            el.play();
        }
        function playBGM(on) {
            let bgm = document.getElementById('bgm');
            if (!bgm) return;
            if (on) {
                bgm.volume = 0.45;
                bgm.play().catch(()=>{});
            } else {
                bgm.pause();
            }
        }

        // --- 工具 ---
        function rand(a, b) {
            return Math.random() * (b - a) + a;
        }
        function pickFruit() {
            let bombProb = FRUIT_PROB[optionIdx] || 0.9;
            if (Math.random() > bombProb) {
                return {...BOMB};
            }
            let specialProb = SPECIAL_PROB[optionIdx] || 0.12;
            if (playMode.effect && Math.random() < specialProb) {
                let specials = FRUITS.filter(f=>f.special);
                if (specials.length) return {...specials[Math.floor(Math.random()*specials.length)]};
            }
            let normals = FRUITS.filter(f=>!f.special);
            return {...normals[Math.floor(Math.random()*normals.length)]};
        }

        // --- 初始化 ---
        function resizeCanvas() {
            let dpr = window.devicePixelRatio || 1;
            let w = Math.min(window.innerWidth * 0.98, 340);
            let h = Math.min(window.innerHeight * 0.60, 420);
            if (w < 180) w = 180;
            if (h < 220) h = 220;
            canvas.width = w * dpr;
            canvas.height = h * dpr;
            canvas.style.width = w + "px";
            canvas.style.height = h + "px";
            width = w;
            height = h;
            ctx.setTransform(1,0,0,1,0,0);
            ctx.scale(dpr, dpr);
        }

        function loadHighscore() {
            let key = `fruit_highscore_${playModeIdx}_${optionIdx}`;
            let val = localStorage.getItem(key);
            highscore = val ? parseInt(val) : 0;
            document.getElementById('highscore').textContent = "最高: " + highscore;
        }
        function saveHighscore() {
            let key = `fruit_highscore_${playModeIdx}_${optionIdx}`;
            if (score > highscore) {
                highscore = score;
                localStorage.setItem(key, highscore);
                document.getElementById('highscore').textContent = "最高: " + highscore;
            }
        }

        function resetGame() {
            fruits = [];
            trails = [];
            score = 0;
            lives = MAX_LIVES;
            running = false;
            lastLaunch = 0;
            gameOver = false;
            combo = 0;
            frozen = false;
            grandActive = false;
            luckyActive = false;
            chocoActive = false;
            honeyActive = false;
            psyActive = false;
            clearTimeout(freezeTimer);
            clearTimeout(comboTimer);
            document.getElementById('score').textContent = "分数: 0";
            document.getElementById('lives').textContent = "生命: " + MAX_LIVES;
            document.getElementById('combo').textContent = "连击: 0";
            document.getElementById('message').textContent = "";
            document.getElementById('game-canvas').classList.remove('frozen');
            document.getElementById('game-canvas').classList.remove('psy');
            document.body.classList.remove('psy');
            cancelAnimationFrame(animFrame);
            clearTimeout(launchTimer);
            clearInterval(timerInterval);
            ctx.clearRect(0,0,width,height);
            document.querySelectorAll('.fruit-half').forEach(e=>e.remove());
            document.querySelectorAll('.score-float').forEach(e=>e.remove());
            if (option.time) {
                timeLeft = option.time;
                document.getElementById('mode').textContent = `玩法: ${playMode.name} | 选项: ${option.name} (${timeLeft}s)`;
            } else {
                document.getElementById('mode').textContent = `玩法: ${playMode.name} | 选项: ${option.name}`;
            }
            loadHighscore();
        }

        // --- 分数飘字 ---
        function createScoreFloat(x, y, value, color, fruit) {
            let rect = canvas.getBoundingClientRect();
            let px = rect.left + (x / width) * rect.width;
            let py = rect.top + (y / height) * rect.height;
            let el = document.createElement('div');
            el.className = 'score-float';
            el.textContent = (value > 0 ? "+" : "") + value;
            el.style.left = (px - 18) + "px";
            el.style.top = (py - 18) + "px";
            el.style.color = color || (value > 0 ? "#e65100" : "#d32f2f");
            el.style.fontSize = Math.max(18, Math.floor((fruit ? fruit.radius : 18) * 1.2)) + "px";
            document.body.appendChild(el);
            setTimeout(()=>{
                el.style.transform = "translateY(-48px) scale(1.25)";
                el.style.opacity = 0;
            }, 10);
            setTimeout(()=>{el.remove();}, 950);
        }

        // --- 倒计时 ---
        function showCountdown(cb) {
            let cd = document.getElementById('countdown');
            cd.style.display = 'block';
            let arr = ['3','2','1','Go!'];
            let idx = 0;
            function next() {
                cd.textContent = arr[idx];
                if (idx < arr.length-1) {
                    setTimeout(()=>{ idx++; next(); }, 600);
                } else {
                    setTimeout(()=>{
                        cd.style.display = 'none';
                        cb && cb();
                    }, 600);
                }
            }
            next();
        }

        function startGame() {
            resetGame();
            showCountdown(()=>{
                running = true;
                if (option.time) {
                    timeLeft = option.time;
                    document.getElementById('mode').textContent = `玩法: ${playMode.name} | 选项: ${option.name} (${timeLeft}s)`;
                    timerInterval = setInterval(()=>{
                        if (!running) return;
                        timeLeft--;
                        document.getElementById('mode').textContent = `玩法: ${playMode.name} | 选项: ${option.name} (${timeLeft}s)`;
                        if (timeLeft <= 0) {
                            endGame("⏰ 时间到！分数: " + score);
                        }
                    }, 1000);
                }
                launchFruit();
                animFrame = requestAnimationFrame(gameLoop);
            });
        }

        // --- 生成水果 ---
        function launchFruit() {
            if (!running) return;
            let count = (grandActive ? 8 : (Math.random() < 0.22 ? 2 : 1));
            for (let i = 0; i < count; i++) {
                let fruit = pickFruit();
                let x = rand(width * 0.25, width * 0.75);
                let y = height - rand(60, 90);
                let vx = rand(-2.2, 2.2) * (honeyActive ? 0.6 : 1);
                let vy = -rand(FRUIT_SPEED[0], FRUIT_SPEED[1]) * (honeyActive ? 0.6 : 1);
                vx = Math.max(-5, Math.min(5, vx));
                vy = Math.max(-20, Math.min(-5, vy));
                fruits.push({
                    ...fruit,
                    x, y, vx, vy, cut: false, falling: false, cutTime: null, halves: null
                });
            }
            let next = rand(LAUNCH_INTERVAL[0], LAUNCH_INTERVAL[1]);
            if (grandActive) {
                grandActive = false;
            }
            launchTimer = setTimeout(launchFruit, next);
        }

        // --- 粒子特效 ---
        function createParticles(x, y, color, emoji, type) {
            let n = 8;
            for (let i=0; i<n; i++) {
                let p = document.createElement('div');
                p.className = 'particle';
                let size = rand(10, 18);
                let rect = canvas.getBoundingClientRect();
                let px = rect.left + (x / width) * rect.width;
                let py = rect.top + (y / height) * rect.height;
                p.style.width = size+'px';
                p.style.height = size+'px';
                p.style.left = (px - size/2) + 'px';
                p.style.top = (py - size/2) + 'px';
                p.style.background = color || 'rgba(255,200,0,0.7)';
                p.style.opacity = 0.8;
                p.style.fontSize = Math.floor(size*0.9)+'px';
                p.style.textAlign = 'center';
                p.style.lineHeight = size+'px';
                p.style.userSelect = 'none';
                if (emoji) p.textContent = emoji;
                document.body.appendChild(p);
                let dx = rand(-2,2), dy = rand(-2,2);
                setTimeout(()=>{
                    p.style.transition = 'all 0.7s cubic-bezier(.4,2,.6,1)';
                    p.style.transform = `translate(${dx*36}px,${dy*36}px) scale(0.18)`;
                    p.style.opacity = 0;
                }, 10);
                setTimeout(()=>{p.remove();}, 850);
            }
        }

        // --- 切割特效：水果切半 ---
        function createFruitHalves(fruit, cutLine) {
            let emoji = fruit.emoji;
            let size = fruit.radius * 2;
            let rect = canvas.getBoundingClientRect();
            function clamp(val, min, max) { return Math.max(min, Math.min(max, val)); }
            let fx = fruit.x, fy = fruit.y;
            let x1 = cutLine.x1, y1 = cutLine.y1, x2 = cutLine.x2, y2 = cutLine.y2;
            let dx = x2 - x1, dy = y2 - y1;
            let len2 = dx*dx + dy*dy;
            let t = len2 === 0 ? 0 : ((fx - x1) * dx + (fy - y1) * dy) / len2;
            t = clamp(t, 0, 1);
            let cx = x1 + t * dx;
            let cy = y1 + t * dy;
            let px = rect.left + (cx / width) * rect.width;
            let py = rect.top + (cy / height) * rect.height;
            let angle = Math.atan2(y2 - y1, x2 - x1);
            let deg = angle*180/Math.PI;
            let left = px - size/2;
            let top = py - size/2;

            let half1 = document.createElement('div');
            half1.className = 'fruit-half';
            half1.style.width = size + 'px';
            half1.style.height = size + 'px';
            half1.style.left = left + 'px';
            half1.style.top = top + 'px';
            half1.style.fontSize = (size*0.9) + 'px';
            half1.style.lineHeight = size + 'px';
            half1.style.textAlign = 'center';
            half1.style.userSelect = 'none';
            half1.style.overflow = 'hidden';
            half1.style.clipPath = 'polygon(0 0, 50% 0, 50% 100%, 0 100%)';
            half1.textContent = emoji;
            half1.style.transform = `rotate(${deg}deg)`;

            let half2 = document.createElement('div');
            half2.className = 'fruit-half';
            half2.style.width = size + 'px';
            half2.style.height = size + 'px';
            half2.style.left = left + 'px';
            half2.style.top = top + 'px';
            half2.style.fontSize = (size*0.9) + 'px';
            half2.style.lineHeight = size + 'px';
            half2.style.textAlign = 'center';
            half2.style.userSelect = 'none';
            half2.style.overflow = 'hidden';
            half2.style.clipPath = 'polygon(50% 0, 100% 0, 100% 100%, 50% 100%)';
            half2.textContent = emoji;
            half2.style.transform = `rotate(${deg}deg)`;

            document.body.appendChild(half1);
            document.body.appendChild(half2);

            setTimeout(()=>{
                let dx = Math.cos(angle), dy = Math.sin(angle);
                half1.style.transform = `rotate(${deg-18}deg) translate(${-36*dx-12*dy}px, ${-22*dy+12*dx}px) scale(0.7)`;
                half1.style.opacity = 0;
                half2.style.transform = `rotate(${deg+18}deg) translate(${36*dx+12*dy}px, ${22*dy-12*dx}px) scale(0.7)`;
                half2.style.opacity = 0;
            }, 10);
            setTimeout(()=>{
                half1.remove();
                half2.remove();
            }, 900);
        }

        // --- 绘制 ---
        function draw() {
            ctx.clearRect(0,0,width,height);
            for (let fruit of fruits) {
                if (fruit.cut) continue;
                ctx.save();
                ctx.font = `${Math.floor(fruit.radius*1.7)}px serif`;
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";
                ctx.shadowColor = "#fffde7";
                ctx.shadowBlur = 10;
                ctx.globalAlpha = 1;
                ctx.fillText(fruit.emoji, fruit.x, fruit.y);
                ctx.restore();
            }
            let now = Date.now();
            for (let t of trails) {
                if (!t.length) continue;
                if (now - t[0].time > 300) continue;
                ctx.save();
                let grad = ctx.createLinearGradient(t[0].x, t[0].y, t[t.length-1].x, t[t.length-1].y);
                grad.addColorStop(0, "#fffbe7");
                grad.addColorStop(0.5, "#ff4081");
                grad.addColorStop(1, "#ffd600");
                ctx.strokeStyle = grad;
                ctx.lineWidth = 10;
                ctx.globalAlpha = 0.65;
                ctx.lineCap = "round";
                ctx.beginPath();
                for (let i = 0; i < t.length; i++) {
                    let p = t[i];
                    if (i === 0) ctx.moveTo(p.x, p.y);
                    else ctx.lineTo(p.x, p.y);
                }
                ctx.stroke();
                ctx.restore();
            }
        }

        // --- 物理与碰撞 ---
        function update() {
            if (frozen) return;
            for (let fruit of fruits) {
                if (fruit.cut) continue;
                fruit.x += fruit.vx;
                fruit.y += fruit.vy;
                fruit.vy += GRAVITY;
            }
            for (let i = fruits.length-1; i >= 0; i--) {
                let fruit = fruits[i];
                if (fruit.cut) {
                    fruits.splice(i,1);
                    continue;
                }
                if (fruit.y - fruit.radius > height+8) {
                    if (fruit.name !== "炸弹" && !option.endless && !grandActive) {
                        lives -= 1;
                        if (lives < 0) lives = 0;
                        document.getElementById('lives').textContent = "生命: " + lives;
                        if (lives <= 0) {
                            endGame("游戏结束！分数: " + score);
                        }
                    }
                    fruits.splice(i,1);
                }
            }
            let tnow = Date.now();
            trails = trails.filter(t=>t.length && tnow-t[0].time<=300);
        }

        // --- 检查切割 ---
        function checkCut(x1, y1, x2, y2) {
            let hit = false;
            let hitFruits = [];
            for (let fruit of fruits) {
                if (fruit.cut) continue;
                let dx = fruit.x - x1;
                let dy = fruit.y - y1;
                let fx = x2 - x1;
                let fy = y2 - y1;
                let t = ((dx*fx)+(dy*fy))/(fx*fx+fy*fy);
                t = Math.max(0, Math.min(1, t));
                let cx = x1 + t*fx;
                let cy = y1 + t*fy;
                let dist = Math.hypot(fruit.x-cx, fruit.y-cy);
                if (dist < fruit.radius+5) {
                    fruit.cut = true;
                    fruit.cutTime = Date.now();
                    createParticles(fruit.x, fruit.y, null, fruit.emoji, fruit.special);
                    createFruitHalves(fruit, {x1, y1, x2, y2});
                    hit = true;
                    hitFruits.push(fruit);
                }
            }
            if (hitFruits.length) {
                playSound('cut-sound');
                combo += hitFruits.length;
                document.getElementById('combo').textContent = "连击: " + combo;
                if (combo >= 2) playSound('combo-sound');
                if (comboTimer) clearTimeout(comboTimer);
                comboTimer = setTimeout(()=>{
                    combo = 0;
                    document.getElementById('combo').textContent = "连击: 0";
                }, 800);

                for (let fruit of hitFruits) {
                    let addScore = fruit.score || 1;
                    let showColor = "#e65100";
                    if (fruit.name === "炸弹") {
                        playSound('bomb-sound');
                        if (option.bombEnd) {
                            createScoreFloat(fruit.x, fruit.y, fruit.score, "#d32f2f", fruit);
                            endGame("💣 切到炸弹，游戏结束！分数: " + score);
                            return true;
                        } else {
                            addScore = fruit.score || -2;
                            score += addScore;
                            if (score<0) score=0;
                            createScoreFloat(fruit.x, fruit.y, addScore, "#d32f2f", fruit);
                        }
                    } else {
                        addScore = (fruit.score || 1);
                        score += addScore;
                        createScoreFloat(fruit.x, fruit.y, addScore, showColor, fruit);
                    }
                }
                if (hitFruits.length >= 2) {
                    let bonus = hitFruits.length-1;
                    let bonusScore = bonus;
                    score += bonusScore;
                }
                if (score < 0) score = 0;
                document.getElementById('score').textContent = "分数: " + score;
                saveHighscore();
            }
            return hit;
        }

        function showMsg(msg, color) {
            let el = document.getElementById('message');
            el.textContent = msg;
            el.style.color = color || "#d32f2f";
            setTimeout(()=>{el.textContent="";}, 950);
        }

        // --- 游戏主循环 ---
        function gameLoop() {
            if (!running) return;
            update();
            draw();
            animFrame = requestAnimationFrame(gameLoop);
        }

        function endGame(msg) {
            running = false;
            gameOver = true;
            document.getElementById('message').textContent = msg;
            clearTimeout(launchTimer);
            clearInterval(timerInterval);
            saveHighscore();
        }

        // --- 事件 ---
        function getPos(e, idx=0) {
            let rect = canvas.getBoundingClientRect();
            if (e.touches && e.touches.length) {
                let t = e.touches[idx] || e.changedTouches[idx] || e.touches[0];
                let x = (t.clientX - rect.left) * (width / rect.width);
                let y = (t.clientY - rect.top) * (height / rect.height);
                if (psyActive) {
                    x = width - x;
                    y = height - y;
                }
                return {x, y};
            } else {
                let x = (e.clientX - rect.left) * (width / rect.width);
                let y = (e.clientY - rect.top) * (height / rect.height);
                if (psyActive) {
                    x = width - x;
                    y = height - y;
                }
                return {x, y};
            }
        }

        // --- 切割事件 ---
        function onPointerDown(e) {
            if (!running) return;
            holding = true;
            if (e.touches && e.touches.length) {
                for (let i=0; i<e.touches.length; i++) {
                    let id = e.touches[i].identifier;
                    let pos = getPos(e, i);
                    activeTouches[id] = {last: pos};
                    let t = [{x: pos.x, y: pos.y, time: Date.now()}];
                    trails.push(t);
                    if (trails.length > 12) trails.shift();
                }
            } else {
                isDrawing = true;
                let pos = getPos(e);
                lastPoint = pos;
                let t = [{x: pos.x, y: pos.y, time: Date.now()}];
                trails.push(t);
                if (trails.length > 12) trails.shift();
            }
        }
        function onPointerMove(e) {
            if (!running) return;
            if (e.touches && e.touches.length) {
                for (let i=0; i<e.touches.length; i++) {
                    let id = e.touches[i].identifier;
                    let pos = getPos(e, i);
                    let trail = trails[trails.length-1];
                    if (!activeTouches[id]) continue;
                    let prev = activeTouches[id].last;
                    if (Math.hypot(pos.x-prev.x, pos.y-prev.y) > 3) {
                        let t = [{x: prev.x, y: prev.y, time: Date.now()}, {x: pos.x, y: pos.y, time: Date.now()}];
                        trails.push(t);
                        if (trails.length > 12) trails.shift();
                        checkCut(prev.x, prev.y, pos.x, pos.y);
                        activeTouches[id].last = pos;
                    }
                }
            } else if (isDrawing) {
                let pos = getPos(e);
                let trail = trails[trails.length-1];
                if (trail.length > 0) {
                    let prev = trail[trail.length-1];
                    if (Math.hypot(pos.x-prev.x, pos.y-prev.y) > 3) {
                        trail.push({x: pos.x, y: pos.y, time: Date.now()});
                        checkCut(prev.x, prev.y, pos.x, pos.y);
                        lastPoint = pos;
                    }
                }
            }
        }
        function onPointerUp(e) {
            holding = false;
            if (e.changedTouches && e.changedTouches.length) {
                for (let i=0; i<e.changedTouches.length; i++) {
                    let id = e.changedTouches[i].identifier;
                    delete activeTouches[id];
                }
            } else {
                isDrawing = false;
                lastPoint = null;
            }
        }

        // --- 说明按钮/玩法/选项/音乐 ---
        document.addEventListener('DOMContentLoaded', function() {
            canvas = document.getElementById('game-canvas');
            ctx = canvas.getContext('2d');
            resizeCanvas();
            window.addEventListener('resize', resizeCanvas);

            // 说明按钮折叠
            const btn = document.getElementById('toggle-instructions-btn');
            const inst = document.getElementById('instructions');
            btn.onclick = function() {
                if (inst.style.display === 'none' || inst.style.display === '') {
                    inst.style.display = 'block';
                    btn.textContent = '收起说明';
                } else {
                    inst.style.display = 'none';
                    btn.textContent = '玩法说明';
                }
            };

            // 玩法切换
            const modeBtn = document.getElementById('mode-btn');
            modeBtn.onclick = function() {
                playModeIdx = (playModeIdx+1)%PLAY_MODES.length;
                playMode = PLAY_MODES[playModeIdx];
                modeBtn.textContent = "玩法：" + playMode.name;
                document.getElementById('mode').textContent = `玩法: ${playMode.name} | 选项: ${option.name}`;
                resetGame();
            };

            // 选项切换
            const optionBtn = document.getElementById('option-btn');
            optionBtn.onclick = function() {
                optionIdx = (optionIdx+1)%GAME_OPTIONS.length;
                option = GAME_OPTIONS[optionIdx];
                optionBtn.textContent = "选项：" + option.name;
                document.getElementById('mode').textContent = `玩法: ${playMode.name} | 选项: ${option.name}`;
                resetGame();
            };

            // 音乐按钮
            const musicBtn = document.getElementById('music-btn');
            function setMusicBtnState() {
                if (musicOn) {
                    musicBtn.classList.add('on');
                } else {
                    musicBtn.classList.remove('on');
                }
            }
            musicBtn.onclick = function() {
                musicOn = !musicOn;
                setMusicBtnState();
                playBGM(musicOn);
            };
            setMusicBtnState();
            setTimeout(()=>{ playBGM(musicOn); }, 300);

            // 事件绑定
            canvas.addEventListener('mousedown', onPointerDown);
            canvas.addEventListener('mousemove', onPointerMove);
            canvas.addEventListener('mouseup', onPointerUp);
            canvas.addEventListener('mouseleave', onPointerUp);

            canvas.addEventListener('touchstart', function(e){onPointerDown(e); e.preventDefault();});
            canvas.addEventListener('touchmove', function(e){onPointerMove(e); e.preventDefault();});
            canvas.addEventListener('touchend', function(e){onPointerUp(e); e.preventDefault();});
            canvas.addEventListener('touchcancel', function(e){onPointerUp(e); e.preventDefault();});

            document.getElementById('start-btn').onclick = startGame;

            resetGame();
        });

        document.addEventListener('visibilitychange', function() {
            if (document.hidden) {
                playBGM(false);
            } else if (musicOn) {
                playBGM(true);
            }
        });
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    with open("fruit_slice.html", "w", encoding="utf-8") as f:
        f.write(html_code)
    print("已生成 fruit_slice.html，请用浏览器打开体验水果忍者！")
