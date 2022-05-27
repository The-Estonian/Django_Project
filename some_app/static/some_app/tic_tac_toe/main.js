console.log("Django Connected!");
let boxOne = document.querySelector('#one');
let boxTwo = document.querySelector('#two');
let boxThree = document.querySelector('#three');

let boxFour = document.querySelector('#four');
let boxFive = document.querySelector('#five');
let boxSix = document.querySelector('#six');

let boxSeven = document.querySelector('#seven');
let boxEight = document.querySelector('#eight');
let boxNine = document.querySelector('#nine');

let playerXWin = document.querySelector('.playerX');
let playerOWin = document.querySelector('.playerO');

const buttons = [
  boxOne,
  boxTwo,
  boxThree,
  boxFour,
  boxFive,
  boxSix,
  boxSeven,
  boxEight,
  boxNine,
];

const defaultCounter = 0;
let counter = defaultCounter;
let playerX = [];
let playerO = [];

const first = ['one', 'two', 'three'];
const second = ['four', 'five', 'six'];
const third = ['seven', 'eight', 'nine'];
const fourth = ['one', 'four', 'seven'];
const fifth = ['two', 'five', 'eight'];
const sixth = ['three', 'six', 'nine'];
const seventh = ['one', 'five', 'nine'];
const eight = ['seven', 'five', 'three'];

const winList = [first, second, third, fourth, fifth, sixth, seventh, eight];

const rotate = (event, player) => {
  if (player == playerX) {
    event.style.transition = '3s';
    event.style.transform = 'rotate(180deg)';
    playerXWin.style.visibility = 'visible';
    playerXWin.style.opacity = '1';
    playerXWin.style.left = '1%';
    playerXWin.style.top = '75%';
    playerXWin.style.transform = 'rotate(0deg)';
    playerXWin.style.fontSize = '7rem';
  } else if ((player = playerO)) {
    event.style.transition = '1s';
    event.style.opacity = '0.3';
    playerOWin.style.visibility = 'visible';
    playerOWin.style.opacity = '1';
    playerOWin.style.left = '1%';
    playerOWin.style.top = '75%';
    playerOWin.style.transform = 'rotate(0deg)';
    playerOWin.style.fontSize = '7rem';
    event.addEventListener('transitionend', () => {
      event.style.opacity = '1';
    });
  }
};

const winCheck = (winList, player, buttons) => {
  if (winList.every((number) => player.includes(number))) {
    for (let i = 0; i < buttons.length; i++) {
      if (winList.includes(buttons[i].id)) {
        rotate(buttons[i], player);
      }
    }
  }
};

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    if (counter % 2 == 0) {
      if (buttons[i].style.clipPath == '') {
        buttons[i].style.clipPath =
          'polygon(20% 0%, 0% 20%, 30% 50%, 0% 80%, 20% 100%, 50% 70%, 80% 100%, 100% 80%, 70% 50%, 100% 20%, 80% 0%, 50% 30%)';
        playerX.push(buttons[i].id);
        console.log('Player X: ' + playerX);
        counter++;
      } else {
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].firstChild.style.transition = '2s';
          if (buttons[i].style.clipPath == '') {
            buttons[i].firstChild.style.visibility = 'visible';
            buttons[i].firstChild.style.opacity = '100%';
            buttons[i].firstChild.style.transform = 'rotate(405deg)';
            buttons[i].addEventListener('transitionend', function () {
              buttons[i].firstChild.style.opacity = '0%';
              buttons[i].firstChild.style.visibility = 'hidden';
              buttons[i].firstChild.style.transform = 'rotate(300deg)';
            });
          }
        }
      }
      for (let i = 0; i < winList.length; i++) {
        winCheck(winList[i], playerX, buttons);
      }
    } else {
      if (buttons[i].style.clipPath == '') {
        buttons[i].style.clipPath = 'url(#doughnut-path)';
        buttons[i].style.position = 'relative';
        buttons[i].style.left = '1.1rem';
        buttons[i].style.top = '1rem';
        playerO.push(buttons[i].id);
        console.log('Player O: ' + playerO);
        counter++;
      } else {
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].firstChild.style.transition = '2s';
          if (buttons[i].style.clipPath == '') {
            buttons[i].firstChild.style.visibility = 'visible';
            buttons[i].firstChild.style.opacity = '100%';
            buttons[i].firstChild.style.transform = 'rotate(405deg)';
            buttons[i].addEventListener('transitionend', function () {
              buttons[i].firstChild.style.opacity = '0%';
              buttons[i].firstChild.style.visibility = 'hidden';
              buttons[i].firstChild.style.transform = 'rotate(300deg)';
            });
          }
        }
      }
      for (let i = 0; i < winList.length; i++) {
        winCheck(winList[i], playerO, buttons);
      }
    }
  });
}
