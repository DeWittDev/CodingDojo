var search = ''


function count1() {
    var clicks = document.getElementById("Tart").innerHTML;
    clicks++;
    document.getElementById("Tart").innerHTML = clicks;
}

function count2() {
    var clicks = document.getElementById("Macrons").innerHTML;
    clicks++;
    document.getElementById("Macrons").innerHTML = clicks;
}

function count3() {
    var clicks = document.getElementById("Creme").innerHTML;
    clicks++;
    document.getElementById("Creme").innerHTML = clicks;
}

function hide() {
    document.getElementById("join").remove()
}

function searching(element) {
    var search = document.querySelector(".search")
    console.log(search)
    return search;
}

function searched() {
    alert("You are searching for " + search)
}