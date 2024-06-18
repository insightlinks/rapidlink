from rapidlink import create_app

app = create_app()

if __name__ == "__main__":
    app.run(load_dotenv=True)
