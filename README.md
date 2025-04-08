<<<<<<< HEAD
# 📝 NOTECLI - A Simple Command-Line Notes Manager

NOTECLI is a Python-based Command-Line Interface (CLI) tool that allows users to securely create, read, update, and delete notes from the terminal. It integrates with Auth0 for authentication and MongoDB (via Atlas) as the backend database. Built with Flask, it offers a seamless way to manage your notes from any system.

---

## 🚀 Features

- ✅ **User Authentication** using Auth0  
- 📓 **Create**, 📝 **Read**, ✏️ **Update**, 🗑️ **Delete** notes  
- ☁️ Cloud-hosted backend using Flask + MongoDB  
- 🔐 Secure access with OAuth2 token-based auth  
- 🔌 Easily installable globally via PyPI  
- 🧪 Testable on any system using `notescli` commands  

---

## 📦 Installation

You can install NOTECLI globally on any system via PyPI:

```bash
pip install notescli-tool
```

> **Note:** Make sure Python (>=3.6) and `pip` are installed.

---

## 🔑 Authentication

NOTECLI uses Auth0 for login. You must log in before using note commands.

```bash
notescli login
```

- A browser window will open prompting Auth0 login.
- After login, you'll be asked to paste the token into the terminal.
- The token is securely stored for subsequent operations.

To logout:

```bash
notescli logout
```

To see the currently authenticated user:

```bash
notescli whoami
```

---

## 💻 CLI Commands

### Create a New Note

```bash
notescli create
```
- Prompts for note title and content
- Sends data securely to the server

### Read All Notes or a Specific Note

```bash
notescli read            # Show all your notes
notescli read <note_id>  # Show a single note by ID
```

### Update a Note

```bash
notescli update <note_id>
```
- Prompts for new title and content

### Delete a Note

```bash
notescli delete <note_id>
```

### Install (from GitHub)

```bash
notescli install
```
- (Optional) Custom command to reinstall the tool from GitHub (if configured)

---



## 🌐 Backend Server

- Runs on `Flask` (default port `5000`)
- Secured by OAuth2 via Auth0
- Stores notes in MongoDB Atlas
- Each note is associated with a unique Auth0 user ID

Example API endpoints:
- `GET /notes` – get all notes
- `POST /notes` – create a new note
- `GET /notes/<id>` – fetch a specific note
- `PUT /notes/<id>` – update a note
- `DELETE /notes/<id>` – delete a note

---

## 🔐 Security

- All endpoints require a valid **Bearer Token**
- Tokens are verified against Auth0
- Notes are scoped per user using `user_id`

---

## 📡 Deployment

You can deploy the backend using:

```bash
python server/app.py
```

Or run on a remote VM and point the client to the appropriate IP (e.g., `http://13.71.28.224:5000`).

---

## 🌍 Global Tool Installation (PyPI)

Once published to PyPI:

```bash
pip install notescli-tool
```

Then use anywhere:

```bash
notescli login
notescli create
notescli read
# etc.
```

> View on PyPI: [https://pypi.org/project/notescli-tool](https://pypi.org/project/notescli-tool)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## 🙋‍♀️ Author

**Maintainer:** Raaghavi

- 📧 Email: [krraaghavi@gmail.com](mailto:krraaghavi@gmail.com)  
- 💻 GitHub: [github.com/Raaghavi-K-R](https://github.com/Raaghavi-K-R/Notescli)  
- 🔗 LinkedIn: [linkedin.com/in/raaghavi-k-r](https://www.linkedin.com/in/raaghavi-k-r/)  

## 🔗 Useful Links

- 🔐 [Auth0](https://auth0.com/)
- ☁️ [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- 📦 [Publish Python Packages to PyPI](https://packaging.python.org/)

---

✨ Happy Noting with NOTECLI!
=======
# Notescli: A CLI Tool for taking notes with Auth0 Security
>>>>>>> 41573d58ff3ea5a5986c5c51461a829b2031a4f3
