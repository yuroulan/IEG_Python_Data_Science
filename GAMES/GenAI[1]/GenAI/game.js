const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let jetfighter = {
    x: canvas.width / 2 - 15,
    y: canvas.height - 30,
    width: 30,
    height: 30,
    dx: 0,
    dy: 0
};

let bullets = [];
let meteors = [];
let score = 0;
let gameOver = false;

let jetfighterImage = new Image();
jetfighterImage.src = './Jet.png';

let meteorImage = new Image();
meteorImage.src = './Meteor.png';

let shootSound = new Audio('./Automatic Machine Gun.mp3');
let explosionSound = new Audio('./Bomb.mp3');

function drawJetfighter() {
    ctx.drawImage(jetfighterImage, jetfighter.x, jetfighter.y, jetfighter.width, jetfighter.height);
}

function drawBullets() {
    ctx.fillStyle = 'yellow';
    bullets.forEach(bullet => {
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    });
}

function drawMeteors() {
    meteors.forEach(meteor => {
        ctx.drawImage(meteorImage, meteor.x, meteor.y, meteor.width, meteor.height);
    });
}

function updateBullets() {
    bullets.forEach((bullet, index) => {
        bullet.y -= 5;
        if (bullet.y + bullet.height < 0) {
            bullets.splice(index, 1);
        }
    });
}

function updateMeteors() {
    meteors.forEach((meteor, index) => {
        meteor.y += 2;
        if (meteor.y + meteor.height > canvas.height) {
            gameOver = true;
        }
        bullets.forEach((bullet, bulletIndex) => {
            if (bullet.x < meteor.x + meteor.width &&
                bullet.x + bullet.width > meteor.x &&
                bullet.y < meteor.y + meteor.height &&
                bullet.y + bullet.height > meteor.y) {
                explosionSound.play();
                meteors.splice(index, 1);
                bullets.splice(bulletIndex, 1);
                score++;
            }
        });
    });
}

function createMeteor() {
    let meteor = {
        x: Math.random() * (canvas.width - 20),
        y: -20,
        width: 20,
        height: 20
    };
    meteors.push(meteor);
}

function updateJetfighter() {
    jetfighter.x += jetfighter.dx;
    jetfighter.y += jetfighter.dy;
    if (jetfighter.x < 0) jetfighter.x = 0;
    if (jetfighter.x + jetfighter.width > canvas.width) jetfighter.x = canvas.width - jetfighter.width;
    if (jetfighter.y < 0) jetfighter.y = 0;
    if (jetfighter.y + jetfighter.height > canvas.height) jetfighter.y = canvas.height - jetfighter.height;
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function drawScore() {
    ctx.fillStyle = 'white';
    ctx.font = '16px Arial';
    ctx.fillText('Score: ' + score, 8, 20);
}

function gameLoop() {
    if (gameOver) {
        alert('Game Over! Your score: ' + score);
        document.location.reload();
        return;
    }
    clearCanvas();
    drawJetfighter();
    drawBullets();
    drawMeteors();
    drawScore();
    updateJetfighter();
    updateBullets();
    updateMeteors();
    requestAnimationFrame(gameLoop);
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') jetfighter.dx = -5;
    if (e.key === 'ArrowRight') jetfighter.dx = 5;
    if (e.key === 'ArrowUp') jetfighter.dy = -5;
    if (e.key === 'ArrowDown') jetfighter.dy = 5;
    if (e.key === ' ') {
        let bullet = {
            x: jetfighter.x + jetfighter.width / 2 - 2.5,
            y: jetfighter.y,
            width: 5,
            height: 10
        };
        bullets.push(bullet);
        shootSound.play();
    }
});

document.addEventListener('keyup', (e) => {
    if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') jetfighter.dx = 0;
    if (e.key === 'ArrowUp' || e.key === 'ArrowDown') jetfighter.dy = 0;
});

setInterval(createMeteor, 2000);
gameLoop();
