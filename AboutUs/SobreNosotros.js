const image = document.querySelector("img");
const modal = document.querySelector(".modal");
const modalImage = document.querySelector(".modal img");

image.addEventListener("click", function() {
  modal.style.display = "block";
  modalImage.src = this.src;
});

modal.addEventListener("click", function() {
  modal.style.display = "none";
});