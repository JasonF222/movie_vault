// 3 functions - Login, Registration, Back //
// Login Button - Hides Self, Registration Button, Populates Login Div //
// Registration Button - Hides Self, Login Button, Populates Registration Div //
// Back Button - Attached to both Forms, returns to Initial 2 Button Look //

const divGrab = document.getElementById('transitionBox')

function loginTransition() {
    divGrab.innerHTML = 
    `

    <div class="registration boxGrow p-3" style="width: 400px;">

        <form action="/login" method="post" class="form-group background p-3">
            <label for="email" class="mb-2">Email: </label>
            <input type="text" name="email" id="email" class="form-control border border-3 border-dark inputF">

            <label for="pw" class="mt-2 mb-2">Password: </label>
            <input type="password" name="pw" id="pw" class="form-control border border-3 border-dark inputF">

            <!-- <button type="submit" class="mt-3 loginbtn">Login</button> -->
            <input type="submit" value="Login" class="mt-3 mb-3 loginbtn"> <br>
            <a class="mt-3 loginbtn" style="cursor: pointer;" onclick="goBack()"> Back </a>
        </form>

    </div>
    `
}

function goBack() {
    divGrab.innerHTML = 
    `
    <button class=" loginBig" onclick="loginTransition()" style="cursor: pointer;">Login</button> <br>
    <button class=" regBig" onclick="regTransition()" style="cursor: pointer;">Register</button> <br>
    `
}

function regTransition() {
    divGrab.innerHTML = 
    `

    <div class="login p-3 mt-4 mb-3" style="width: 400px;">

    <!-- Registration Form -->
    <form action="/register" method="post" class="form-group background p-3">
        <label for="first_name" class="mb-2">First Name: </label>
        <input type="text" name="first_name" id="first_name" class="form-control border border-3 border-dark inputF">

        <label for="last_name" class="mt-2 mb-2">Last Name: </label>
        <input type="text" name="last_name" id="last_name" class="form-control border border-3 border-dark inputF">

        <label for="email" class="mt-2 mb-2">Email: </label>
        <input type="text" name="email" id="email" class="form-control border border-3 border-dark inputF">

        <label for="pw" class="mt-2 mb-2">Password: </label>
        <input type="password" name="pw" id="pw" class="form-control border border-3 border-dark inputF">

        <label for="pw1" class="mt-2 mb-2">Confirm Password: </label>
        <input type="password" name="pw1" id="pw1" class="form-control border border-3 border-dark inputF">

        <!-- <button type="submit" class="mt-3 registerbtn">Register</button> -->
        <input type="submit" value="Register" class="mt-3 mb-3 registerbtn"> <br>
        <a class="mt-3 loginbtn" style="cursor: pointer;" onclick="goBack()"> Back </a>
    </form>

</div>
    `
}