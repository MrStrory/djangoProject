var elems = [];
var rightArrow = document.getElementById("rightArrow");
var leftArrow = document.getElementById("leftArrow");
for (var i = 0; i < 3; i++){
    elems[i] = document.getElementById("elem"+[i]);
}

var i = 0;

rightArrow.addEventListener("click", function (){
    elems[i].classList.toggle("carousel-hidden");
    (i < 2) ? i++ : i = 0;
    elems[i].classList.toggle("carousel-hidden");
});

leftArrow.addEventListener("click", function (){
    elems[i].classList.toggle("carousel-hidden");
    (i > 0) ? i-- : i = 2;
    elems[i].classList.toggle("carousel-hidden");
});



