from app import APP

if __name__ == "__main__":
    APP.run(ssl_context='adhoc')  # Enable simple SSL certificate (HTTPS) temporary in production server
