function setup() {
	createCanvas(windowWidth, windowHeight);
	x = 250;
	y = 250;
	vx = 5;
	vy = -5;
	ancho = 50;
}

function dibuja_bolita(x, y, radio) {
	noStroke();
	fill(232, 81, 81);
	ellipse(x, y, radio, radio);
}

function dibuja_barrita(ancho) {
	stroke(22, 44, 66);
	strokeWeight(10);
	line(mouseX-ancho, windowHeight-50, mouseX+ancho, windowHeight-50);
}

function mueve_bolita(x, y, vx, vy) {
	x = x + vx;
	y = y + vy;
	return [x, y];
}

function draw() {
	background(133, 182, 242);
	[x, y] = mueve_bolita(x, y, vx, vy);
	dibuja_bolita(x, y, 10);
	dibuja_barrita(ancho);

	if (x > (windowWidth-10) || x < 10) {
		vx = -vx;
	}
	if (y < 10) {
		vy = -vy;
	}
	if (y > (windowHeight-60) && x > (mouseX-ancho) && x < (mouseX+ancho) && y < (windowHeight-40)){
		vy = -vy;
	}
}
