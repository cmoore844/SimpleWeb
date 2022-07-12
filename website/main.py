from website import create_app

app=create_app()

if __name__ == '__main__':
    app.run(debug=True) #starts the webserver. When change is made, the web server will be restarted