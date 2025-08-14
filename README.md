#  Markdown Note-taking App

A simple note-taking application that allows users to upload **Markdown** files, check grammar, save notes in the database, and view the HTML-rendered version.

https://roadmap.sh/projects/markdown-note-taking-app

---

##  Features
-  **Upload Markdown file** or submit text directly
-  **Grammar checking**
-  **Save notes** in the database
-  **Convert Markdown to HTML**

---

##  API Endpoints

| Method | Endpoint           | Description |
|--------|--------------------|-------------|
| `POST` | `/add`              | Save a note (Markdown text or file) |
| `GET`  | `/list`             | List all saved notes |
| `GET`  | `/render/{id}`      | Display HTML-rendered note |
| `POST` | `/check/{id}`       | Check grammar of the note |
