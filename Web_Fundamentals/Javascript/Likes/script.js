function increment(i) {
    var value = document.querySelectorAll(".count")[i];
    count = value.innerHTML;
    count++

    value.innerHTML = count;
}
