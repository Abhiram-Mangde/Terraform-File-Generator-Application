document.getElementById('resourceForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const resourceType = document.getElementById('resourceType').value;
    let payload = { resourceType };
    if (resourceType === 'vm') {
        payload.cpu = document.getElementById('cpu').value;
        payload.ram = document.getElementById('ram').value;
        payload.disk = document.getElementById('disk').value;
    }
    const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await response.json();
    const fileBlocks = document.getElementById('fileBlocks');
    fileBlocks.innerHTML = '';
    Object.entries(data).forEach(([filename, content]) => {
        const block = document.createElement('div');
        block.style.marginBottom = '2rem';
        block.innerHTML = `
            <h3 style="margin-bottom:0.5rem;">${filename}.tf</h3>
            <button class="copy-btn" onclick="copyFileContent('${filename}')">Copy to Clipboard</button>
            <pre><code id="code_${filename}" class="language-hcl"></code></pre>
        `;
        fileBlocks.appendChild(block);
        document.getElementById(`code_${filename}`).textContent = content;
    });
    Prism.highlightAll();
    document.getElementById('outputSection').style.display = 'block';
});


function copyFileContent(filename) {
    const code = document.getElementById(`code_${filename}`).textContent;
    navigator.clipboard.writeText(code).then(() => {
        alert(`${filename}.tf copied to clipboard!`);
    });
}
