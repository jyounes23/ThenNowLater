// Optional: Add AJAX handling for the "Add Task" form to avoid full page reloads
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('addTaskForm');
    if (form) {
      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
  
        try {
          const response = await fetch(form.action, {
            method: 'POST',
            body: formData
          });
          if (response.ok) {
            // After successful submission, reload the page or update the DOM to show the new task.
            location.reload();
          } else {
            console.error('Failed to add task.');
          }
        } catch (error) {
          console.error('Error:', error);
        }
      });
    }
  });