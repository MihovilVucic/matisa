// Sakrivanje/pokazivanje side nava u mobilnom načinu
function showNav() {
	sideNav = document.getElementById("secondary-navigation");
	/*const currentDisplay = sideNav.style.display;

	if (currentDisplay === "none") {
		sideNav.style.display = "block";
	} 
	else {
		sideNav.style.display = "none";
	}*/
	sideNav.classList.toggle("appear");
}
// Sakrivanje/pokazivanje glavnog nava u mobilnom načinu
function showNavHeader() {
	nav = document.getElementById("primary-navigation");
	//const currentDisplay = nav.style.display;
	glavni = document.getElementById("glavni");
	x = document.getElementsByTagName('main')[0];
	/*if (currentDisplay === "none") {
		nav.style.display = "block";
		glavni.style.filter = "brightness(50%)";
	} 
	else {
		nav.style.display = "none";
		glavni.style.filter = "brightness(100%)"
	}*/
	nav.classList.toggle("appear");
	if (x.style.filter == "brightness(30%)") {
		//glavni.style.filter = "brightness(100%)";
		x.style.filter = "brightness(100%)";

	}
	else {
		//glavni.style.filter = "brightness(70%)";
		x.style.filter = "brightness(30%)";
	}
}
// Proširivanje i smanjivanje side nava po potpoglavljima
function toggle() {
	const clickedElement = event.currentTarget;
	const parentDiv = clickedElement.parentElement;
	const upArrow = parentDiv.querySelector('.up-arrow');
	const downArrow = parentDiv.querySelector('.down-arrow');
	const sibling = parentDiv.querySelector('.dropdown-content');
	//const currentDisplay = sibling.style.display;
	
	/*if (sibling && sibling.classList.contains('dropdown-content')) {
		if (currentDisplay === "none") {
			sibling.style.display = "block";
			downArrow.style.display = "none";
			upArrow.style.display = "inline";
			
		} 
		else {
			sibling.style.display = "none";
			downArrow.style.display = "inline";
			upArrow.style.display = "none";
		}
	}*/
	
	sibling.classList.toggle("appear");
	upArrow.classList.toggle("appear");
	downArrow.classList.toggle("remove");
}

// Avatar border
function selectAvatar(img) {
  const avatarOptions = document.querySelectorAll('.avatar');
  
  avatarOptions.forEach(option => {
    option.classList.remove('selected');
  });
  
  img.classList.add('selected');
}

//Bolji show hide - za zadatke, pa primijeniti na side-nav i nav
function s_h() {
	const clickedElement = event.currentTarget;
	const parentDiv = clickedElement.parentElement;
	const sibling = parentDiv.querySelector(".solution");
	/*console.log(clickedElement);
	console.log(parentDiv);
	console.log(sibling);*/
	sibling.classList.toggle("show");
}

// Sakrivanje/pokazivanje zadataka po temama
function showExercise() {
	const clickedElement = event.currentTarget;
	const parentDiv = clickedElement.parentElement;
	const grandpaDiv = parentDiv.parentElement;
	const upArrow = parentDiv.querySelector('.up-arrow');
	const downArrow = parentDiv.querySelector('.down-arrow');
	const sibling = grandpaDiv.querySelector('.exercise-dropdown');
	
	sibling.classList.toggle("appear-block");
	upArrow.classList.toggle("appear");
	downArrow.classList.toggle("remove");
}












