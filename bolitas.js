function setup() {
	createCanvas(windowWidth, windowHeight);
	background(67, 163, 224);

}

function draw() {
	radio = 20;
	fill(random(0, 255), random(0, 255), random(0, 255));
	ellipse(mouseX, mouseY, radio, radio);
}
