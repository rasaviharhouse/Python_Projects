function navigateToSearch() {
    document.getElementById("homePage").style.display = "none";
    document.getElementById("searchPage").style.display = "block";
    document.getElementById("detailsPage").style.display = "none";
}

function navigateToHome() {
    document.getElementById("homePage").style.display = "block";
    document.getElementById("searchPage").style.display = "none";
    document.getElementById("detailsPage").style.display = "none";
}

function navigateToSearchResults() {
    document.getElementById("homePage").style.display = "none";
    document.getElementById("searchPage").style.display = "none";
    document.getElementById("detailsPage").style.display = "block";
}

function searchCountry() {
    const searchInput = document.getElementById("name").value.toLowerCase();
    const selectedCountry = document.getElementById("country").value;

    if (selectedCountry === "US") {
        // Simulating details for USA
        showCountryDetails("USA", "Population: 331 million, Capital: Washington D.C., Currency: US Dollar", "usa.jpeg");
    } else if (selectedCountry === "IN") {
        // Simulating details for India
        showCountryDetails("India", "Population: 1.3 billion, Capital: New Delhi, Currency: Indian Rupee", "india.jpeg");
    } else {
        alert("Country details not available for the selected criteria.");
    }
}

function showCountryDetails(country, details, img_url) {
    // Display country details
    const detailsContainer = document.getElementById("countryDetails");
    detailsContainer.innerHTML = `<h3>${country}</h3><p>${details}</p> <img src=${img_url} style="width: 100%; height: auto;">`;

    // Navigate to the details page
    document.getElementById("homePage").style.display = "none";
    document.getElementById("searchPage").style.display = "none";
    document.getElementById("detailsPage").style.display = "block";
}

var ageSlider = document.getElementById("ageSlider");
var ageOutput = document.getElementById("age");
ageOutput.innerHTML = ageSlider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
ageSlider.oninput = function() {
    ageOutput.innerHTML = this.value;
}

var ratingSlider = document.getElementById("ratingSlider");
var ratingOutput = document.getElementById("rating");
ratingOutput.innerHTML = ratingSlider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
ratingSlider.oninput = function() {
    ratingOutput.innerHTML = this.value;
}