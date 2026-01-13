// This script generates the consistent top navigation bar
document.addEventListener("DOMContentLoaded", function() {
    const headerHTML = `
    <header style="background: #004a99; color: white; padding: 1rem 5%; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: auto;">
            <div class="logo">
                <h1 style="font-size: 1.4rem; margin: 0; letter-spacing: 1px; font-family: 'Segoe UI', sans-serif;">Dr. Sherine Braganza</h1>
            </div>
            <nav style="display: flex; gap: 20px;">
                <a href="index.html" style="color: white; text-decoration: none; font-weight: 500; font-size: 0.95rem; padding: 5px 10px; border-radius: 4px;">Home</a>
                <a href="experience.html" style="color: white; text-decoration: none; font-weight: 500; font-size: 0.95rem; padding: 5px 10px; border-radius: 4px;">Experience</a>
                <a href="research.html" style="color: white; text-decoration: none; font-weight: 500; font-size: 0.95rem; padding: 5px 10px; border-radius: 4px;">Research</a>
                <a href="academic.html" style="color: white; text-decoration: none; font-weight: 500; font-size: 0.95rem; padding: 5px 10px; border-radius: 4px;">Academic</a>
            </nav>
        </div>
    </header>
    `;

    // Insert the header at the very top of the body
    document.body.insertAdjacentHTML('afterbegin', headerHTML);
    
    // Highlight the active page
    const currentPage = window.location.pathname.split("/").pop();
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.style.background = 'rgba(255,255,255,0.2)';
        }
    });
});