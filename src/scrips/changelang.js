let buttons = document.getElementsByTagName("button");
let engButton = buttons[0];
let rusButton = buttons[1];

let documentation = document.getElementsByTagName("zero-md")[0];
let engDocumentationPlaced = "./../../documentation/HOW_TO_INSTALL_eng.md";
let rusDocumentationPlaced = "./../../documentation/HOW_TO_INSTALL_rus.md";

window.addEventListener("load", (e) => {
    engButton.addEventListener("click", (e) => {
        if (documentation.getAttribute("src") == rusDocumentationPlaced) {
            documentation.setAttribute("src", engDocumentationPlaced);
        }
    });
    rusButton.addEventListener("click", (e) => {
        if (documentation.getAttribute("src") == engDocumentationPlaced) {
            documentation.setAttribute("src", rusDocumentationPlaced);
        }
    });
});
