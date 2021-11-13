import cgi
import cgitb

cgitb.enable()


print("Content-Type: text/html")

html = """
<!DOCTYPE html>

<html lang="fr">
    <head>
        <title>Warna38 - Projets</title>
        <link rel="stylesheet" type="text/css" href="assets/style.css">
        <meta charset="UTF-8">
    </head>

    <body>
        <header>
            <nav class="menu">
                <ul>
                    <li class="drop-down">
                        <button>Principal</button>
                        <ul class="drop-down-content">
                            <li class="drop-down-item">
                                <button type="button"><a href="https://warna38.github.io/">Accueil</a></button>
                            </li><li class="drop-down-item">
                                <button type="button"><a href="https://warna38.github.io/">Wikis</a></button>
                            </li>
                        </ul>
                    </li>
                    <li class="drop-down">
                        <button>Projets</button>
                        <ul class="drop-down-content">
                            <li class="drop-down-item">
                                <button type="button"><a href="https://warna38.github.io/">Site web</a></button>
                            </li>
                        </ul>
                    </li>
                </ul>
            </nav>
        </header>
        <article id="website">
            <p>Mon site web :</p>
        </article>
        <footer>
            <p>Leave a like</p>
        </footer>
    </body>
</html>
"""
