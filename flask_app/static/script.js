
// Targetting the main div on html //
const movieList = document.getElementById('movieCards')

// async function to get an API request from approute in controller file //
async function getAMovie() {
    const response = await (await fetch('/api/show_movie')).json();
    // const results = response.results //
    //de-structuring technique //
    const {results} = response
    for(const movie of results) {
        console.log(movie.id);
        movieList.innerHTML +=
        // below is the html with JSON values passed in //
        `
        <div class="movieCard d-flex gap-3 m-5 cardHover" style="width: 85vw; padding-bottom: 5px;">
            <div class="leftcol" style="flex: 1;">
                <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="image of movie title" class="movieTitle"></img>
            </div>

            <div class="midcol" style="flex: 3;">
                <div class="top d-flex justify-content-between">
                <h2 class="text-light text-wrap" style="width: 25rem;">${movie.title}</h2>
                <h4 class="text-light">${movie.release_date}</h4>
                <h4 class="text-light">Rating: <span class="text-warning">${movie.vote_average}</span></h4>
            </div>
            <h3 class="text-light mt-3">Overview</h3>
            <p class="text-light">${movie.overview}</p>
            

        </div>
            <div class="rightcol ms-5" style="flex: 1;">

                <form action="/add_favorite" method="post">
                    <input type="hidden" name="movie_id" value="${movie.id}">
                    <input type="hidden" name="title" value="${movie.title}">
                    <button type="submit" class="btn btn-outline-warning bg-gradient box-shadow3 cardHover" style="width: 145px">Add to Favorites</button>
                </form>

                <form action="/add_queue" method="post">
                    <input type="hidden" name="movie_id" value="${movie.id}">
                    <input type="hidden" name="title" value="${movie.title}">
                    <button type="submit" class="btn btn-outline-success bg-gradient box-shadow3 mt-3 cardHover" style="width: 145px">Add to Queue</button>
                </form>
            </div>
        `
    }
}
getAMovie();



//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}