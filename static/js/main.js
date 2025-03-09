// عند النقر على زر الهامبرغر
const menuBtn = document.getElementById("menu-btn");
const menu = document.getElementById("menu-links");

menuBtn.addEventListener("click", () => {
    // Toggle (إظهار أو إخفاء) القائمة
    menu.classList.toggle("hidden");
});
