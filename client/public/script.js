const form = document.getElementById('upload-form');
const result = document.getElementById('result');
const preview = document.getElementById('preview');
const fileInput = document.getElementById('image-input');

// Mostrar previsualización de la imagen seleccionada
fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (file) {
    if (!file.type.startsWith('image/')) {
      alert('Por favor selecciona un archivo de imagen válido.');
      fileInput.value = '';  // Limpia la selección
      preview.style.display = 'none';
      preview.src = '';
      return;
    }
    const reader = new FileReader();
    reader.onload = (e) => {
      preview.src = e.target.result;
      preview.style.display = 'block';
    };
    reader.readAsDataURL(file);
  } else {
    preview.style.display = 'none';
    preview.src = '';
  }
});

// Enviar imagen subida por el usuario
form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const file = fileInput.files[0];
  if (!file) return alert('Selecciona una imagen');

  await enviarImagen(file);
});

// Función reusable para enviar imagen (File o Blob) al backend
async function enviarImagen(file) {
  const formData = new FormData();
  formData.append('file', file);

  result.textContent = 'Procesando...';

  try {
    const response = await fetch('/upload', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) throw new Error('Error en la predicción');

    const data = await response.json();

    // Mostrar resultados formateados
    const predictions = data.predictions;
    let html = '<ul>';
    predictions.forEach(pred => {
      html += `<li><strong>${pred.class}</strong>: ${(pred.probability * 100).toFixed(2)}%</li>`;
    });
    html += '</ul>';
    result.innerHTML = html;

    // Mostrar imagen en preview
    const reader = new FileReader();
    reader.onload = (e) => {
      preview.src = e.target.result;
      preview.style.display = 'block';
    };
    reader.readAsDataURL(file);

  } catch (err) {
    result.textContent = 'Error: ' + err.message;
  }
}

// Manejar click en imágenes de ejemplo
document.addEventListener('DOMContentLoaded', () => {
  const exampleImages = document.querySelectorAll('.example-image');

  exampleImages.forEach(img => {
    img.addEventListener('click', async () => {
      result.textContent = 'Procesando...';

      try {
        // Traer la imagen como Blob
        const response = await fetch(img.src);
        if (!response.ok) throw new Error('No se pudo cargar la imagen de ejemplo.');

        const blob = await response.blob();

        // Enviar el blob al backend (simulando archivo)
        await enviarImagen(new File([blob], 'example.jpg', { type: blob.type }));

      } catch (error) {
        result.textContent = 'Error: ' + error.message;
      }
    });
  });
});