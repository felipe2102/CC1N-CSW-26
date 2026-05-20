for(let i=0; i<=10; i++) {
    if(i%2 == 0) {
        console.log(i);
    }
}
var i = 0;
while (i <= 10) {
    if (i%2 != 0) {
        console.log(i);
    }
    i++;
}


function get_age() {
    let nome = document.getElementById("input").value;

    document.getElementById("title").innerHTML = "Você"

}