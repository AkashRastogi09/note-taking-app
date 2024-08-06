document.addEventListener('DOMContentLoaded', function() {
    fetchNotes();
});

function fetchNotes() {
    fetch('/api/notes')
        .then(response => response.json())
        .then(notes => {
            const notesDiv = document.getElementById('notes');
            notesDiv.innerHTML = '';
            notes.forEach(note => {
                const noteDiv = document.createElement('div');
                noteDiv.innerHTML = `<h2>${note.title}</h2><p>${note.content}</p>`;
                notesDiv.appendChild(noteDiv);
            });
        });
}

function addNote() {
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    fetch('/api/notes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, content })
    })
    .then(response => response.json())
    .then(note => {
        const notesDiv = document.getElementById('notes');
        const noteDiv = document.createElement('div');
        noteDiv.innerHTML = `<h2>${note.title}</h2><p>${note.content}</p>`;
        notesDiv.appendChild(noteDiv);
    });
}
