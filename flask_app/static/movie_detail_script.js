// Targetting the main div on html //
const movieDetail = document.getElementById('details')

// async function to get an API request from approute in controller file //
async function getMovieDetail() {
    const response = await (await fetch('/api/show_detail')).json();
    // const results = response.results //
    //de-structuring technique //
    const movie = response
    let releaseYr = dateToYear(movie.release_date) 
    console.log(response);
    console.log(movie.id);
    movieDetail.innerHTML +=
    // below is the html with JSON values passed in //
    `
    <div class="movieCard d-flex gap-3 m-5 cardHover" style="width: 85vw; padding-bottom: 5px; padding-top: 80px;">
        <div class="leftcol" style="flex: 1;">
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="image of movie title" class="movieTitle"></img>
        </div>

        <div class="midcol" style="flex: 3;">
            <div class="top d-flex justify-content-between">
            <h2 class="text-light text-wrap" style="width: 25rem;">${movie.title}</h2>
            <h4 class="text-light">${releaseYr}</h4>
            <h4 class="text-light">Rating: <span class="text-warning">${movie.vote_average}</span></h4>
        </div>
        <h3 class="text-light mt-3">Overview</h3>
        <p class="text-light">${movie.overview}</p>
        

    </div>
    `
}
getMovieDetail();

// Converting API date index into Month Name + Year //

const monthInd = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',

}
function dateToYear(str){
    let newStr ="";
    let arr = str.split('-');
    console.log(arr);
    newStr += monthInd[String(arr[1])] + " ";   
    newStr += arr[0];
    return newStr    
}


// below is old code to add to fav/queue //

// <div class="rightcol ms-5" style="flex: 1;">

//     <form action="/add_favorite" method="post">
//         <input type="hidden" name="movie_id" value="${movie.id}">
//         <input type="hidden" name="title" value="${movie.title}">
//         <button type="submit" class="btn btn-warning bg-gradient box-shadow3" style="width: 145px" onmouseover="bigButton(this)" onmouseout="normalButton(this)">Add to Favorites</button>
//     </form>

//     <form action="/add_queue" method="post">
//         <input type="hidden" name="movie_id" value="${movie.id}">
//         <input type="hidden" name="title" value="${movie.title}">
//         <button type="submit" class="btn btn-success bg-gradient box-shadow3 mt-3" style="width: 145px" onmouseover="bigButton(this)" onmouseout="normalButton(this)">Add to Queue</button>
//     </form>
// </div>