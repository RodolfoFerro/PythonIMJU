function setup() {
	createCanvas(windowWidth, windowHeight);
	x = 250;
	y = 250;
	vx = 3;
	vy = -3;
}

function dibuja_bolita(x, y, radio) {
	noStroke();
	fill(153, 102, 255);
	ellipse(x, y, radio, radio);
}

function mueve_bolita(x, y, vx, vy) {
	x = x + vx;
	y = y + vy;
	return [x, y];
}

function draw() {
	background(67, 163, 224);
	[x, y] = mueve_bolita(x, y, vx, vy);
	dibuja_bolita(x, y, 10);

	if (x > (windowWidth-10) || x < 10) {
		vx = -vx;
	}
	if (y > (windowHeight-10) || y < 10) {
		vy = -vy;
	}
}
