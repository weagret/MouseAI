let overviewSection = document.getElementsByTagName("nav")[0].offsetTop;
let teamSection = document.getElementById("team").offsetTop;
let downloadSection = document.getElementById("download").offsetTop;

let NavElements = document.querySelectorAll("nav > ul + ul > li > a");
let defaultNavElementColor = "#777";
let selectedNavElementColor = "#fff";

const changeCss = (num) => {
    NavElements.forEach((e) => {
        e.style.color = defaultNavElementColor;
    });
    NavElements[num].style.color = selectedNavElementColor;
};

window.addEventListener("load", (e) => {
    document.addEventListener("scroll", (e) => {
        let currentScrollTopPos =
            document.documentElement.scrollTop || document.body.scrollTop;

        if (
            currentScrollTopPos >= overviewSection &&
            currentScrollTopPos < teamSection
        ) {
            changeCss(0);
        } else if (
            currentScrollTopPos >= teamSection &&
            currentScrollTopPos < downloadSection - 500
        ) {
            changeCss(1);
        } else {
            changeCss(2);
        }
    });
});
