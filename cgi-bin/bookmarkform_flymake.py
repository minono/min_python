<html>
    <head>
        <meta http-equiv="content-type" content="tex/html;charset=utf-8">
    </head>
    <body>
        <h1>簡易ブックマーク</h1>
        <p>${messeage}</p>
        <form method="post" action="templatebbs.py">
            タイトル : <input type="text" name="title" size="40"
                              value="${title}" /><br />

            URL　　　: <input type="text" name="url" size="40"
                              value="${title}" /><br />

            <input type="hidden" name="post" value="1" />
 j           <input type="submit" />
        </form>

        ${bookmarks}

    </body>
</html>
