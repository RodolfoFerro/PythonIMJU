function setup() {
	createCanvas(windowWidth, windowHeight);
	background(67, 163, 224);
	noStroke();

	// Rostro:
	fill(255, 204, 204);
	ellipse(100, 100, 50, 60);

	// Ojos:
	fill(255);
	ellipse(90, 95, 10, 6);
	ellipse(110, 95, 10, 6);

	// Pupilas:
	fill(0);
	ellipse(90, 95, 3, 3);
	ellipse(110, 95, 3, 3);

	// Boca:
	fill(255, 0, 0);
	ellipse(100, 115, 15, 15);
	fill(0);
	ellipse(100, 115, 13, 13);
}

function draw() {

}
