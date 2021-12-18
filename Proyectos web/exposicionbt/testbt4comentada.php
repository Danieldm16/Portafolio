<!DOCTYPE html>
<html>
    <head>
        <title>Test Bootstrap 4</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <!-- Estas lineas son las que nos permiten usar Bootstrap -->
    
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        
    </head>
<body class="bg-warning">

<!-- Esta linea es la presentación de la pagina, el titulo -->

    <div class="container-fluid text-black text-center">
        <h1 class="display-1 font-weight-bold">Criticas Chafas<small><img src="logo.png" class="rounded-circle" width="120px" alt="logo de criticas chafas"></small></h1>
    </div>

<!-- Aquí se da una pequeña descripción de la pagina. -->

    <div class="container-fluid text-black text-center">
        <p class="font-weight-bold">Bienvenido a criticas chafas, una pagina donde encontraras
            criticas "chafas" de las series y peliculas más actuales, y de vez en cuando también
            recomendaciones.
        </p>
    </div>

<!-- Esto solo indica la sección donde estarán las criticas -->

    <div class="container-fluid bg-dark text-white text-center">
        <h1>Criticas</h1>
    </div>

<!-- Aquí se da la imagen, una pequeña primera reacción y el enlace a la critica -->

    <div class="card-deck">

        <div class="card bg-dark">
            <img class="card-img-top img-fluid" src="rapidosyfuriosos.jpg" alt="Rapidos y furiosos 9">
            <div class="card-body text-white text-center">
                <h4 class="card-title">Rapidos y furiosos 9</h4>
                <p class="card-text">Esto es tan sorprendente que por más exagerado que sea ya quiero ver cómo termina la saga.</p>
                <a href="https://www.facebook.com/Chafacritics/photos/a.1914587048649845/3805857682856096/" class="btn btn-primary stretched-link">Ver critica</a>
            </div>
        </div>

        <div class="card bg-dark">
            <img class="card-img-top img-fluid" src="durodecuidar.jpg" alt="Duro de cuidar 2">
            <div class="card-body text-white text-center">
                <h4 class="card-title">Duro de cuidar 2</h4>
                <p class="card-text">Ver actores muy famosos en películas ridículas de acción/comedia es extrañamente disfrutable.</p>
                <a href="https://www.facebook.com/Chafacritics/photos/a.1914587048649845/3795002070608324/" class="btn btn-primary stretched-link">Ver critica</a>
            </div>
        </div>

        <div class="card bg-dark">
            <img class="card-img-top img-fluid" src="enelbarrio.jpg" alt="En el barrio">
            <div class="card-body text-white text-center">
                <h4 class="card-title">En el barrio</h4>
                <p class="card-text">Hay historias que tienen que contarse, y un musical es una gran manera para hacerlo.</p>
                <a href="https://www.facebook.com/Chafacritics/photos/a.1914587048649845/3789484124493452/" class="btn btn-primary stretched-link">Ver critica</a>
            </div>
        </div>

    </div>

    <br>

<!-- Aquí solo se indica la sección de las recomendaciones -->

    <div class="container-fluid bg-dark text-white text-center">
        <h1>Recomendaciones</h1>
    </div>

<!-- En esta sección es una muestra de series/peliculas que se recomiendan -->

    <div id="demo" class="carousel slide" data-ride="carousel">

        <ul class="carousel-indicators">
            <li data-target="#demo" data-slide-to="0" class="active"></li>
            <li data-target="#demo" data-slide-to="1"></li>
            <li data-target="#demo" data-slide-to="2"></li>
        </ul>
        
        <div class="carousel-inner">

            <div class="carousel-item active">
                <img src="centauria.jpg" width="100%" height="450px" alt="Centauria">
                    <div class="carousel-caption">
                        <h3>Centauria</h3>
                    </div>
            </div>

            <div class="carousel-item">
                <img src="manifiesto.jpeg" width="100%" height="450px" alt="Manifiesto">
                    <div class="carousel-caption">
                        <h3>Manifest</h3>
                    </div>
            </div>

            <div class="carousel-item">
                <img src="tokyorevengers.jpg" width="100%" height="450px" alt="Tokyo Revengers">
                    <div class="carousel-caption">
                        <h3>Tokyo Revengers</h3>
                    </div>
            </div>
        </div>

    </div>-->

    <br>

<!-- Aquí se muestran las redes sociales de criticas chafas -->


    <div class="container-fluid text-white bg-dark">
        <div class="row">
            <div class="col text-center">
                <h2>-</h2>
                <h2>Redes sociales -></h2>
                <h2>-</h2>
            </div>

            <div class="col" >
                <a href="https://www.instagram.com/daniel.dm.16/" class="list-group-item list-group-item-action text-white bg-dark text-center">Instagram</a>
                <a href="https://www.facebook.com/Chafacritics" class="list-group-item list-group-item-action text-white bg-dark text-center">Facebook</a>
                <a href="https://peoople.app/influencers/criticaschafas/recomendaciones" class="list-group-item list-group-item-action text-white bg-dark text-center">Peoople</a>
            </div>
        </div>
    </div>

</body>
</html>