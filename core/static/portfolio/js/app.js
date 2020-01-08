

// iconContent = document.querySelectorAll('#prj-tech-icon')  

noneText = document.querySelectorAll('#skills-list-item')

noneText.forEach(e => {
  if (e.innerHTML == 'None'){
    e.style.display = 'none'
  }
});


var mainListDiv = document.getElementById("mainListDiv"),
  mediaButton = document.getElementById("mediaButton");

mediaButton.onclick = function () {
  "use strict";
  mainListDiv.classList.toggle("show_list");
  mediaButton.classList.toggle("active");
};

window.onscroll = function () {
  this.stickyNav()
};
// Get the navbar
var navbar = document.getElementById("nav");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function stickyNav() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky-nav")
  } else {
    navbar.classList.remove("sticky-nav");
  }
}


const openEls = document.querySelectorAll("[data-open]");
const closeEls = document.querySelectorAll("[data-close]");
const isVisible = "is-visible";

for (const el of openEls) {
  el.addEventListener("click", function() {
    const modalId = this.dataset.open;
    document.getElementById(modalId).classList.add(isVisible);
  });
}

for (const el of closeEls) {
  el.addEventListener("click", function() {
    this.parentElement.parentElement.parentElement.classList.remove(isVisible);
  });
}

document.addEventListener("click", e => {
  if (e.target == document.querySelector(".modal.is-visible")) {
    document.querySelector(".modal.is-visible").classList.remove(isVisible);
  }
});

document.addEventListener("keyup", e => {
  // if we press the ESC
  if (e.key == "Escape" && document.querySelector(".modal.is-visible")) {
    document.querySelector(".modal.is-visible").classList.remove(isVisible);
  }
});

// slick slider Config
jQuery(document).ready(function($) {
  $('.modal-project-img').slick({
    dots: false,
    infinite: true,
    variableWidth: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: true,
    responsive: [{
      breakpoint: 600,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 2
      }
    },
    {
       breakpoint: 400,
       settings: {
          arrows: false,
          slidesToShow: 2,
          slidesToScroll: 1
       }
    }]
});
});

// var icons = [{
//     "name": "js",
//     "icon": "flaticon-ionicons-svg-logo-javascript",
//   },
//   {
//     "name": "hmtl",
//     "icon": "flaticon-html-coding",
//   },
//   {
//     "name": "node",
//     "icon": ".flaticon-download",

//   }
// ];

// var p = {
//   "node": ".flaticon-download",
//   "Hmtl": ".flaticon-html-coding",
//   "js": ".flaticon-ionicons-svg-logo-javascript"
// };

// iconContent.forEach(e => {
//   // console.log(e.innerHTML.toLowerCase());
//     if (e.innerHTML == 'Js') {
//         e.classList.add('flaticon-ionicons-svg-logo-javascript');
//         e.innerHTML = ''
//     }
// })
// iconContent.forEach(e => {
//   // console.log(e.innerHTML.toLowerCase());
//     if (e.innerHTML== 'Html') {
//         e.classList.add('flaticon-html-coding');
//         e.innerHTML = ''
//     }
// })
// iconContent.forEach(e => {
//   // console.log(e.innerHTML.toLowerCase());
//     if (e.innerHTML == 'Node') {
//         e.classList.add('flaticon-python-1');
//         e.innerHTML = ''
//     }
// })