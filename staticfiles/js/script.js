function reveal() {
    var reveals = document.querySelectorAll(".reveal");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }

function boxesReveal() {
  var boxes = document.querySelectorAll(".text_box");

  for (var i = 0; i < boxes.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = boxes[i].getBoundingClientRect().top;
    var elementVisible = 180;

    if (elementTop < windowHeight - elementVisible) {
      boxes[i].classList.add("active");
    } else {
      boxes[i].classList.remove("active");
    }
  }
}
  
  window.addEventListener("scroll", reveal);
  window.addEventListener("scroll", boxesReveal);
  