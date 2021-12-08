// listen for a scroll event and then execuate the function
// myFunction()
window.onscroll = function() {
    myFunction();
}

// grab the navbar

const navbar = document.querySelector(".navbar");

// get the offset postion of the navbar

const sticky = navbar.offsetTop;

const hero = document.querySelector('#hero');

function myFunction(){
    if(window.pageYOffset >= sticky){
        navbar.classList.add('sticky')
    }else{
        navbar.classList.remove('sticky')
    }
}

// grab the content of the body for modification following the 
// change in postion of the navabr



/**
   * Back to top button
   */
 let backtotop = select('.back-to-top')
 if (backtotop) {
   const toggleBacktotop = () => {
     if (window.scrollY > 100) {
       backtotop.classList.add('active')
     } else {
       backtotop.classList.remove('active')
     }
   }
   window.addEventListener('load', toggleBacktotop)
   onscroll(document, toggleBacktotop)
 }