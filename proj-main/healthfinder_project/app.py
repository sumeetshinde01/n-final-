from healthfinder import create_app

app = create_app()

print(app.url_map)  # This prints all registered routes to the terminal

if __name__ == "__main__":
    app.run(debug=True)
