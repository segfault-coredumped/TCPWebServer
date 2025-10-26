# Simple HTTP Client-Server in Python

This project implements a basic HTTP client and server using Python's socket library. The server can serve HTML files, and the client can request them. It also demonstrates basic HTTP response handling, including 404 error handling.

## Features

- HTTP Server
  - Listens for incoming TCP connections.
  - Serves requested HTML files.
  - Returns a 404 Not Found page if the requested file does not exist.

- HTTP Client
  - Sends an HTTP GET request to the server.
  - Receives and displays the server's response.
  - Can test valid and invalid HTML files.

## How to Run

### Start the Server

python server.py

- The server listens on port 12000 by default.
- Make sure index.html (or your desired HTML file) is in the same directory as the server script.

### Run the Client

python client.py

- The client connects to 127.0.0.1 (localhost) and requests index.html by default.
- To test a non-existing file, uncomment the missing_file.html line in client.py.

## Example HTML (index.html)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to CSC 138</title>
</head>
<body>
    <h1>Welcome to CSC 138 Computer Networking</h1>
    <p>California State University</p>
    <img src="https://www.csus.edu/brand/_internal/_images/logo-imgs/primary_horizontal_3_color_tag_wht_hnd.jpg" alt="CSU Logo">
    <h2>Let's Dive into Networking!</h2>
    <img src="https://statehornet.com/wp-content/uploads/2014/02/bbb463840041c660a77114fe702370d8.jpg" alt="Funny Image">
</body>
</html>

## Notes

- The client displays the full HTTP response (header + body).
- The server uses TCP (SOCK_STREAM) for reliable data transmission.
- The server closes the connection after responding to a request. You can modify it to stay always on.
- time.sleep() in the client does not affect RTT; it's only for display purposes.

## License

This project is free to use for educational purposes.
