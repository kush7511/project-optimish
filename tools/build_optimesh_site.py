from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ("Home", "index.html"),
    ("Shop", "shop.html"),
    ("About us", "about.html"),
    ("Services", "process.html"),
    ("Blog", "shop.html#testimonials"),
    ("Contact us", "contact.html"),
]

PRODUCTS = [
    ("Nordic Chair", "shop.html", "$50.00", "A soft modern chair with a clean profile and durable upholstery."),
    ("Kruzo Aero Chair", "classic.html", "$78.00", "A relaxed lounge chair designed for light, open interiors."),
    ("Ergonomic Chair", "eco.html", "$43.00", "A compact upholstered chair for dining, work, and everyday comfort."),
    ("Modern Sofa", "elite.html", "$96.00", "A deep green sofa with a calm studio presence."),
    ("Lounge Chair", "mesh.html", "$64.00", "A rounded accent chair for reading corners and living rooms."),
    ("Interior Set", "roller.html", "$88.00", "Curated pieces that bring the Furni studio look into one space."),
    ("Accent Chair", "security.html", "$58.00", "A soft silhouette with tapered legs and a compact footprint."),
    ("Studio Collection", "zipscreen.html", "$110.00", "Furniture selected for refined homes, studios, and hospitality spaces."),
]

COMMON_DESCRIPTION = (
    "Furni creates modern furniture, crafted interiors, and comfortable living spaces "
    "with a calm green studio theme."
)


def head(title, description=COMMON_DESCRIPTION):
    return f"""<head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <title>{title}</title>
   <meta name="description" content="{description}">
   <meta name="author" content="Furni">
   <link rel="icon" href="images/logo.png" type="image/png">
   <link rel="stylesheet" href="css/bootstrap.min.css">
   <link rel="stylesheet" href="css/font-awesome.min.css">
   <link rel="stylesheet" href="css/style.css">
   <link rel="stylesheet" href="css/optimesh-redesign.css">
</head>"""


def header(active):
    links = []
    for label, href in NAV:
        current = " active" if label == active else ""
        links.append(f'<li><a class="furni-nav-link{current}" href="{href}">{label}</a></li>')
    return f"""<header class="furni-header">
   <nav class="furni-nav" aria-label="Primary navigation">
      <a class="furni-logo" href="index.html">Furni<span>.</span></a>
      <input class="furni-toggle" type="checkbox" id="furni-menu" aria-label="Open navigation menu">
      <label class="furni-menu-button" for="furni-menu" aria-hidden="true"><span></span><span></span><span></span></label>
      <ul class="furni-menu">{''.join(links)}</ul>
      <div class="furni-actions">
         <a href="contact.html" aria-label="Account"><i class="fa fa-user-o" aria-hidden="true"></i></a>
         <a href="shop.html" aria-label="Cart"><i class="fa fa-shopping-cart" aria-hidden="true"></i></a>
      </div>
   </nav>
</header>"""


def footer():
    return """<footer class="furni-footer">
   <div class="furni-newsletter">
      <div class="newsletter-form">
         <h2><i class="fa fa-envelope-o" aria-hidden="true"></i> Subscribe to Newsletter</h2>
         <form action="contact.html">
            <input type="text" name="name" placeholder="Enter your name" aria-label="Enter your name">
            <input type="email" name="email" placeholder="Enter your email" aria-label="Enter your email">
            <button type="submit" aria-label="Subscribe"><i class="fa fa-paper-plane" aria-hidden="true"></i></button>
         </form>
      </div>
      <img src="images/furni-footer-reference.png" alt="" aria-hidden="true">
   </div>
   <div class="furni-footer-grid">
      <div class="footer-about">
         <a class="furni-footer-logo" href="index.html">Furni<span>.</span></a>
         <p>Donec facilisis quam ut purus rutrum lobortis. Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique. Pellentesque habitant</p>
         <div class="socials">
            <a href="#" aria-label="Facebook"><i class="fa fa-facebook" aria-hidden="true"></i></a>
            <a href="#" aria-label="Twitter"><i class="fa fa-twitter" aria-hidden="true"></i></a>
            <a href="#" aria-label="Instagram"><i class="fa fa-instagram" aria-hidden="true"></i></a>
            <a href="#" aria-label="LinkedIn"><i class="fa fa-linkedin" aria-hidden="true"></i></a>
         </div>
      </div>
      <nav aria-label="Footer menu">
         <a href="about.html">About us</a>
         <a href="process.html">Services</a>
         <a href="shop.html#testimonials">Blog</a>
         <a href="contact.html">Contact us</a>
      </nav>
      <nav aria-label="Support links">
         <a href="contact.html">Support</a>
         <a href="process.html">Knowledge base</a>
         <a href="contact.html">Live chat</a>
      </nav>
      <nav aria-label="Company links">
         <a href="process.html">Jobs</a>
         <a href="about.html">Our team</a>
         <a href="about.html">Leadership</a>
         <a href="contact.html">Privacy Policy</a>
      </nav>
      <nav aria-label="Product links">
         <a href="shop.html">Nordic Chair</a>
         <a href="classic.html">Kruzo Aero</a>
         <a href="eco.html">Ergonomic Chair</a>
      </nav>
   </div>
   <div class="furni-copyright">
      <p>Copyright &copy;2026. All Rights Reserved. &mdash; Designed with love by Untree.co Distributed By ThemeWagon</p>
      <div>
         <a href="#">Terms &amp; Conditions</a>
         <a href="#">Privacy Policy</a>
      </div>
   </div>
</footer>"""


def wrap(title, active, body, description=COMMON_DESCRIPTION):
    return f"""<!DOCTYPE html>
<html lang="en">
{head(title, description)}
<body class="furni-body">
{header(active)}
{body}
{footer()}
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""


def index():
    body = """<main>
   <section class="screenshot-section hero-shot" aria-label="Modern Interior Design Studio">
      <img src="images/furni-home-reference.png" alt="Furni homepage hero with Modern Interior Design Studio, navigation menu, account icon, and cart icon">
   </section>
   <section class="screenshot-section" aria-label="Crafted with excellent material product section">
      <img src="images/furni-products-reference.png" alt="Crafted with excellent material section showing Nordic Chair, Kruzo Aero Chair, and Ergonomic Chair">
   </section>
   <section class="screenshot-section" aria-label="Why Choose Us section">
      <img src="images/furni-why-reference.png" alt="Why Choose Us section with service icons and interior room image">
   </section>
   <section class="screenshot-section" id="testimonials" aria-label="Testimonials section">
      <img src="images/furni-testimonials-reference.png" alt="Testimonials section with customer quote and carousel arrows">
   </section>
   <section class="screenshot-section footer-shot" aria-label="Furni footer and newsletter section">
      <img src="images/furni-footer-reference.png" alt="Furni footer with newsletter, links, social icons, copyright, terms and privacy">
   </section>
</main>"""
    return f"""<!DOCTYPE html>
<html lang="en">
{head("Furni | Modern Interior Design Studio")}
<body class="furni-body index-reference">
{body}
</body>
</html>
"""


def product_tiles():
    return "\n".join(
        f"""<article class="furni-card">
      <div class="card-image"><img src="images/furni-products-reference.png" alt="{name}"></div>
      <h3>{name}</h3>
      <strong>{price}</strong>
      <p>{summary}</p>
      <a href="{href}">Explore</a>
   </article>"""
        for name, href, price, summary in PRODUCTS
    )


def shop():
    body = f"""<main>
   <section class="furni-page-hero">
      <p>Shop</p>
      <h1>Crafted with excellent material.</h1>
      <a class="furni-button" href="contact.html">Explore</a>
   </section>
   <section class="furni-products" id="products">
      {product_tiles()}
   </section>
   <section class="furni-testimonial-block" id="testimonials">
      <h2>Testimonials</h2>
      <p>&ldquo;Donec facilisis quam ut purus rutrum lobortis. Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique.&rdquo;</p>
      <strong>Maria Jones</strong>
      <span>CEO, Co-Founder, XYZ Inc.</span>
   </section>
</main>"""
    return wrap("Shop | Furni", "Shop", body)


def about():
    body = """<main>
   <section class="furni-page-hero">
      <p>About us</p>
      <h1>Why Choose Us</h1>
      <span>Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit.</span>
   </section>
   <section class="furni-why">
      <article><i class="fa fa-truck" aria-hidden="true"></i><h2>Fast &amp; Free Shipping</h2><p>Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit.</p></article>
      <article><i class="fa fa-shopping-bag" aria-hidden="true"></i><h2>Easy to Shop</h2><p>Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit.</p></article>
      <article><i class="fa fa-life-ring" aria-hidden="true"></i><h2>24/7 Support</h2><p>Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit.</p></article>
      <article><i class="fa fa-refresh" aria-hidden="true"></i><h2>Hassle Free Returns</h2><p>Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit.</p></article>
   </section>
</main>"""
    return wrap("About us | Furni", "About us", body)


def services():
    body = """<main>
   <section class="furni-page-hero">
      <p>Services</p>
      <h1>Modern interior design services for calm homes.</h1>
      <span>Every page keeps the same Furni theme, spacing, colors, typography, and footer style from the references.</span>
   </section>
   <section class="furni-split">
      <div>
         <h2>Interior Styling</h2>
         <p>Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique.</p>
      </div>
      <img src="images/furni-why-reference.png" alt="Modern interior room">
   </section>
</main>"""
    return wrap("Services | Furni", "Services", body)


def contact():
    body = """<main>
   <section class="furni-page-hero">
      <p>Contact us</p>
      <h1>Let us help design your next room.</h1>
   </section>
   <section class="furni-contact">
      <form action="#">
         <input type="text" placeholder="Enter your name" aria-label="Enter your name">
         <input type="email" placeholder="Enter your email" aria-label="Enter your email">
         <textarea rows="6" placeholder="Message" aria-label="Message"></textarea>
         <button class="furni-button" type="submit">Send Message</button>
      </form>
   </section>
</main>"""
    return wrap("Contact us | Furni", "Contact us", body)


def product_page(product):
    name, href, price, summary = product
    body = f"""<main>
   <section class="furni-page-hero">
      <p>Product</p>
      <h1>{name}</h1>
      <span>{summary}</span>
      <strong>{price}</strong>
      <a class="furni-button" href="contact.html">Request Quote</a>
   </section>
</main>"""
    return wrap(f"{name} | Furni", "Shop", body)


def write():
    pages = {
        "index.html": index(),
        "shop.html": shop(),
        "about.html": about(),
        "process.html": services(),
        "contact.html": contact(),
    }
    product_map = {
        "classic.html": PRODUCTS[1],
        "eco.html": PRODUCTS[2],
        "elite.html": PRODUCTS[3],
        "mesh.html": PRODUCTS[4],
        "roller.html": PRODUCTS[5],
        "security.html": PRODUCTS[6],
        "zipscreen.html": PRODUCTS[7],
        "insect.html": PRODUCTS[0],
    }
    for filename, product in product_map.items():
        pages[filename] = product_page(product)
    for name, content in pages.items():
        (ROOT / name).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    write()
