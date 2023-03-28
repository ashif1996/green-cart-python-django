
var slideImg = document.getElementById("slideImg");

var images = new Array(
    "static/images/footer.jpg",
    "static/images/bg4.jpg",
    "static/images/bg2.jpg"
    );

var len = images.length;
var i = 0;
function slider(){
    if(i > len-1){
        i = 0;
    }
    slideImg.src = images[i];
    i++;
    setTimeout('slider()',3000);
}

const menuBtn = document.querySelector('.menu-btn')
const navlinks = document.querySelector('.nav-links')

menuBtn.addEventListener('click',()=>{
    navlinks.classList.toggle('mobile-menu')
})
