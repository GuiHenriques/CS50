const mario = document.querySelector(".mario");
const pipe = document.querySelector(".pipe");
const cloud = document.querySelector(".clouds");

const jump = () => {
    mario.classList.add("jump")
    setTimeout(() => {
        mario.classList.remove("jump")
    }, 700)
};

let scoreCounter = 0;
let score = document.querySelector(".score");

const scoreLoop = setInterval(() => {
    scoreCounter++;
    score.innerHTML = "Score: " + scoreCounter
    console.log(scoreCounter);
}, 2000)
 
const loop = setInterval(() => {

    const pipePosition = pipe.offsetLeft;
    const marioHeight = +window.getComputedStyle(mario).bottom.replace("px", "")
    const cloudPosition = cloud.offsetLeft;

        if (pipePosition <= 130 && marioHeight <= 100 && pipePosition > 0) {
            //When mario hits pipe:        
            pipe.style.animation = "none";
            pipe.style.left = `${pipePosition}px`
            
            mario.style.animation = 'none'
            mario.style.bottom = `${marioHeight}px`
            mario.src = "imgs/game-over.png"
            mario.style.width = "80px"
            mario.style.marginLeft = "50px"
            
            cloud.style.animation = 'none'
            cloud.style.left = `${cloudPosition}px`;
            
            clearInterval(loop)
            clearInterval(scoreLoop)

            setTimeout(() => {
                location.reload()
            }, 300)
        }
}, 10)

document.addEventListener("keydown", jump);