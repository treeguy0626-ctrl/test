PRIMARY_RED = "#D43C2C"
WARM_YELLOW = "#F4C542"
ACCENT_ORANGE = "#E67E22"
OFF_WHITE = "#FBF7F2"
CARD_WHITE = "#FFFFFF"
TEXT_DARK = "#2E2E2E"


def get_css():
    return f'''
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
        .shop-closed-overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(80,80,80,0.5);
            z-index: 1200;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 2rem;
            font-weight: bold;
            pointer-events: none;
        }}

    body {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        background-color: {OFF_WHITE};
        color: {TEXT_DARK};
    }}

    .main-header {{
        background: {CARD_WHITE};
        border-bottom: 1px solid rgba(0,0,0,0.06);
        padding: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }}

    .header-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }}

    .header-content {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
    }}

    .logo-section h1 {{
        font-size: 2rem;
        background: linear-gradient(135deg, {PRIMARY_RED}, {ACCENT_ORANGE});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .pro-max-text {{
        color: #999;
        font-size: 1.2rem;
        margin-left: 5px;
    }}

    .header-nav {{
        display: flex;
        gap: 8px;
        align-items: center;
        position: relative;
        flex-wrap: wrap;
    }}

    .nav-btn {{
        padding: 10px 16px;
        background-color: {PRIMARY_RED};
        color: white;
        text-decoration: none;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-weight: 600;
        font-size: 0.9rem;
        min-height: 44px;
        display: flex;
        align-items: center;
        white-space: nowrap;
    }}

    .hamburger {{
        display: none;
        flex-direction: column;
        cursor: pointer;
        gap: 5px;
        background: none;
        border: none;
        padding: 10px;
        min-height: 44px;
        align-items: center;
        justify-content: center;
    }}

    .hamburger span {{
        width: 25px;
        height: 3px;
        background-color: {TEXT_DARK};
        border-radius: 2px;
        transition: all 0.3s ease;
    }}

    .hamburger.active span:nth-child(1) {{
        transform: rotate(45deg) translate(10px, 10px);
    }}

    .hamburger.active span:nth-child(2) {{
        opacity: 0;
        display: none;
    }}

    .hamburger.active span:nth-child(3) {{
        transform: rotate(-45deg) translate(8px, -8px);
    }}

    .nav-menu {{
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        align-items: center;
    }}

    .nav-menu.mobile-hidden {{
        display: none !important;
    }}

    /* Mobile backdrop to block interaction with page when menu is open */
    .mobile-backdrop {{
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.22);
        z-index: 1099;
        transition: opacity 200ms ease;
        pointer-events: none;
    }}

    .mobile-backdrop.active {{
        display: block;
        z-index: 1100;
        pointer-events: auto;
    }}

    .nav-btn:hover {{
        background-color: #b82d1f;
    }}

    .logout-btn {{
        background-color: #e74c3c;
    }}

    .page-container {{
        max-width: 1200px;
        margin: 20px auto;
        padding: 0 20px;
    }}

    .big-title {{
        font-size: 3rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .logo-image {{
        max-height: 80px;
        width: auto;
        vertical-align: middle;
    }}

    .logo-image.login-logo {{
        max-height: 180px;
        width: auto;
    }}

    .header-content {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    .section-title {{
        font-size: 1.8rem;
        font-weight: 800;
        color: {PRIMARY_RED};
        margin: 25px 0 15px 0;
    }}

    .shop-card {{
        background: {CARD_WHITE};
        border-radius: 12px;
        padding: 15px;
        border: 1px solid rgba(0,0,0,0.04);
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        margin-bottom: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}

    .shop-info {{
        flex: 1;
    }}

    .status-badge {{
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }}

    .status-badge.open {{
        background-color: #2ecc71;
        color: white;
    }}

    .status-badge.closed {{
        background-color: #e74c3c;
        color: white;
    }}

    .status-badge.preparing {{
        background-color: {WARM_YELLOW};
        color: {TEXT_DARK};
    }}

    .btn {{
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        font-weight: 600;
    }}

    .btn-primary {{
        background-color: {PRIMARY_RED};
        color: white;
    }}

    .btn-primary:hover {{
        background-color: #b82d1f;
    }}

    .btn-secondary {{
        background-color: #95a5a6;
        color: white;
    }}

    .btn-small {{
        padding: 6px 12px;
        font-size: 0.9rem;
        margin-left: 10px;
    }}

    .btn-warning {{
        background-color: {WARM_YELLOW};
        color: {TEXT_DARK};
    }}

    .btn-danger {{
        background-color: #e74c3c;
        color: white;
    }}

    .login-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }}

    .login-card {{
        background: {CARD_WHITE};
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        max-width: 400px;
        width: 100%;
    }}

    .role-selector {{
        display: flex;
        gap: 20px;
        margin-bottom: 20px;
    }}

    .role-option {{
        display: flex;
        align-items: center;
        gap: 8px;
        cursor: pointer;
    }}

    .form-group {{
        margin-bottom: 15px;
    }}

    .form-group input,
    .form-group select {{
        width: 100%;
        padding: 10px;
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 8px;
        font-size: 1rem;
    }}

    .dashboard-layout {{
        display: grid;
        grid-template-columns: 1fr 280px;
        gap: 20px;
    }}

    .sidebar-updates {{
        background: {CARD_WHITE};
        border-radius: 12px;
        padding: 15px;
        border: 1px solid rgba(0,0,0,0.04);
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        height: fit-content;
        position: sticky;
        top: 20px;
        max-height: 500px;
        overflow-y: auto;
    }}

    .sidebar-title {{
        font-weight: 800;
        font-size: 0.95rem;
        color: {PRIMARY_RED};
        margin-bottom: 12px;
    }}

    .update-item {{
        font-size: 0.85rem;
        color: {TEXT_DARK};
        padding: 8px 0;
        border-bottom: 1px solid rgba(0,0,0,0.03);
    }}

    .category-section {{
        margin-bottom: 25px;
    }}

    .category-name {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {PRIMARY_RED};
        margin-bottom: 12px;
    }}

    .item-card {{
        background: {OFF_WHITE};
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}

    .item-info h4 {{
        font-size: 1rem;
        margin-bottom: 3px;
    }}

    .item-status {{
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
    }}

    .item-status.available {{
        background-color: #d4edda;
        color: #155724;
    }}

    .item-status.sold-out {{
        background-color: #f8d7da;
        color: #721c24;
    }}

    .management-card {{
        background: {CARD_WHITE};
        padding: 15px;
        border-radius: 8px;
        border: 1px solid rgba(0,0,0,0.04);
        margin-bottom: 15px;
    }}

    .management-card h3 {{
        margin-bottom: 12px;
        color: {PRIMARY_RED};
    }}

    .management-card input,
    .management-card select {{
        width: 100%;
        padding: 8px;
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 6px;
        margin-bottom: 10px;
    }}

    .item-management-row {{
        background: {OFF_WHITE};
        padding: 12px;
        border-radius: 8px;
        display: grid;
        grid-template-columns: 1fr 120px 120px 150px;
        gap: 10px;
        align-items: center;
        margin-bottom: 10px;
    }}

    .empty-message {{
        color: #999;
        font-style: italic;
        padding: 15px;
        text-align: center;
    }}

    .footer {{
        text-align: center;
        padding: 20px;
        color: #999;
        margin-top: 50px;
    }}

    .search-form {{
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }}

    .search-form > form {{
        display: flex;
        gap: 10px;
        width: 100%;
    }}

    .search-form input {{
        flex: 1;
        padding: 10px;
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 8px;
    }}

    .status-selector {{
        display: flex;
        gap: 10px;
        align-items: center;
    }}

    .status-btn {{
        padding: 8px 16px;
        border-radius: 6px;
        border: 2px solid transparent;
        cursor: pointer;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }}

    .status-btn.open {{
        background-color: #a9dfbf;
        color: #1e5631;
    }}

    .status-btn.open:hover {{
        background-color: #82d194;
    }}

    .status-btn.open.active {{
        background-color: #2ecc71;
        color: white;
        box-shadow: 0 4px 12px rgba(46, 204, 113, 0.4);
    }}

    .status-btn.closed {{
        background-color: #f5b7b1;
        color: #78281f;
    }}

    .status-btn.closed:hover {{
        background-color: #edacae;
    }}

    .status-btn.closed.active {{
        background-color: #e74c3c;
        color: white;
        box-shadow: 0 4px 12px rgba(231, 76, 60, 0.4);
    }}

    .status-btn.preparing {{
        background-color: #fceaa6;
        color: #7d6608;
    }}

    .status-btn.preparing:hover {{
        background-color: #fde9a0;
    }}

    .status-btn.preparing.active {{
        background-color: {WARM_YELLOW};
        color: white;
        box-shadow: 0 4px 12px rgba(244, 197, 66, 0.4);
    }}

    .login-role-buttons {{
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: center;
    }}

    .login-role-btn {{
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        font-weight: 600;
        font-size: 0.95rem;
        width: 50%;
        text-align: center;
        transition: all 0.3s ease;
    }}

    .login-role-btn.customer {{
        background-color: {PRIMARY_RED};
        color: white;
    }}

    .login-role-btn.customer:hover {{
        background-color: #b82d1f;
    }}

    .login-role-btn.vendor {{
        background-color: {ACCENT_ORANGE};
        color: white;
    }}

    .login-role-btn.vendor:hover {{
        background-color: #d35400;
    }}

    .error-message {{
        background-color: #f8d7da;
        color: #721c24;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 16px;
        border: 1px solid #f5c6cb;
    }}

    .dashboard-shop-title {{
        font-size: 2.2rem;
        font-weight: 900;
        background: linear-gradient(135deg, {PRIMARY_RED}, {ACCENT_ORANGE});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
    }}

    .header-right {{
        display: flex;
        gap: 20px;
        align-items: center;
    }}

    .login-indicator {{
        font-size: 0.9rem;
        color: {TEXT_DARK};
        font-weight: 500;
        padding: 6px 12px;
        background-color: {OFF_WHITE};
        border-radius: 6px;
    }}

    .login-indicator.vendor {{
        color: {PRIMARY_RED};
    }}

    .real-time-clock {{
        font-size: 0.95rem;
        color: {TEXT_DARK};
        font-weight: 500;
        font-family: 'Courier New', monospace;
        padding: 6px 12px;
        background-color: {OFF_WHITE};
        border-radius: 6px;
        min-width: 100px;
        text-align: center;
    }}

    .toggle-btn {{
        padding: 6px 12px;
        border-radius: 6px;
        border: none;
        cursor: pointer;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }}

    .toggle-btn.available {{
        background-color: #a9dfbf;
        color: #1e5631;
    }}

    .toggle-btn.available:hover {{
        background-color: #82d194;
    }}

    .toggle-btn.available.active {{
        background-color: #2ecc71;
        color: white;
        box-shadow: 0 2px 8px rgba(46, 204, 113, 0.3);
    }}

    .toggle-btn.unavailable {{
        background-color: #f5b7b1;
        color: #78281f;
    }}

    .toggle-btn.unavailable:hover {{
        background-color: #edacae;
    }}

    .toggle-btn.unavailable.active {{
        background-color: #e74c3c;
        color: white;
        box-shadow: 0 2px 8px rgba(231, 76, 60, 0.3);
    }}

    @media (max-width: 768px) {{
        .main-header {{
            padding: 10px 0;
            position: -webkit-sticky;
            position: sticky;
            top: 0;
            left: 0;
            right: 0;
            width: 100%;
            z-index: 1201;
        }}

        .header-content {{
            gap: 10px;
        }}

        .big-title {{
            font-size: 2rem;
        }}

        .logo-image {{
            max-height: 60px;
        }}

        .logo-image.login-logo {{
            max-height: 140px;
        }}

        .hamburger {{
            display: flex;
        }}

        .nav-menu {{
            display: none !important;
            position: fixed;
            top: 70px;
            left: 0;
            right: 0;
            flex-direction: column;
            background: {CARD_WHITE};
            border-bottom: 1px solid rgba(0,0,0,0.1);
            padding: 8px 0;
            gap: 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1200;
            width: 100vw;
            margin: 0;
            border-radius: 0;
        }}

        .nav-menu:not(.mobile-hidden) {{
            display: flex !important;
        }}

        .nav-btn {{
            padding: 14px 20px;
            font-size: 0.95rem;
            width: 100%;
            text-align: left;
            min-height: 48px;
            border-radius: 0;
            margin: 0;
            gap: 0;
        }}\n\n        .nav-btn:not(:last-child) {{\n            border-bottom: 1px solid rgba(0,0,0,0.03);\n        }}

        .page-container {{
            padding: 20px 15px 0 15px;
            margin: 15px auto;
        }}

        .section-title {{
            font-size: 1.4rem;
        }}

        .shop-card {{
            flex-direction: column;
            align-items: flex-start;
        }}

        .item-card {{
            flex-direction: column;
            gap: 10px;
        }}

        .item-card > div {{
            width: 100%;
        }}

        .status-badge {{
            padding: 6px 10px;
            font-size: 0.75rem;
        }}

        .btn {{
            padding: 10px 15px;
            font-size: 0.85rem;
            min-height: 44px;
        }}

        .btn-small {{
            padding: 8px 12px;
            font-size: 0.8rem;
        }}

        .form-group input,
        .form-group select {{
            padding: 12px;
            font-size: 1rem;
            min-height: 44px;
        }}

        .dashboard-layout {{
            grid-template-columns: 1fr;
        }}

        .item-management-row {{
            grid-template-columns: 1fr;
            gap: 8px;
        }}

        .sidebar-updates {{
            position: static;
            top: auto;
            max-height: 180px;
            overflow-y: auto;
            margin-top: 12px;
            padding-bottom: 8px;
        }}

        .search-form {{
            flex-direction: column;
        }}

        .search-form > form {{
            flex-direction: column;
        }}

        .search-form input {{
            width: 100%;
        }}

        .search-form button {{
            width: 100%;
        }}

        .status-selector {{
            flex-direction: column;
            width: 100%;
        }}

        .status-btn {{
            width: 100%;
            min-height: 44px;
        }}

        .login-card {{
            padding: 25px 20px;
            max-width: 100%;
            margin: 0 15px;
        }}

        .login-role-btn {{
            width: 100%;
            padding: 12px 20px;
            min-height: 48px;
        }}

        .item-info h4 {{
            font-size: 0.95rem;
        }}

        .category-name {{
            font-size: 1.1rem;
        }}

        .management-card {{
            padding: 12px;
        }}

        .dashboard-shop-title {{
            font-size: 1.6rem;
        }}
    }}

    @media (max-width: 480px) {{
        .page-container {{
            padding: 0 10px;
            margin: 10px auto;
        }}

        .big-title {{
            font-size: 1.5rem;
            gap: 5px;
        }}

        .logo-image {{
            max-height: 50px;
        }}

        .section-title {{
            font-size: 1.2rem;
        }}

        .shop-card {{
            padding: 12px;
        }}

        .item-card {{
            padding: 10px;
        }}

        .item-management-row {{
            gap: 6px;
        }}

        .nav-btn {{
            padding: 10px 12px;
            font-size: 0.85rem;
        }}

        .btn {{
            padding: 9px 12px;
            font-size: 0.8rem;
        }}

        .form-group input,
        .form-group select {{
            padding: 10px;
            font-size: 16px;
        }}

        .login-card {{
            padding: 20px 15px;
            margin: 0 10px;
        }}

        .error-message {{
            padding: 10px 12px;
            font-size: 0.9rem;
        }}

        .dashboard-shop-title {{
            font-size: 1.3rem;
        }}
    }}
    '''


def get_base_html(title: str, content: str, authenticated: bool = False, role: str = None, show_header: bool = True, extra_head: str = "") -> str:
    if authenticated:
        if role == 'vendor':
            nav_html = '<a href="/dashboard" class="nav-btn">Dashboard</a><a href="/shops" class="nav-btn">Shops</a>'
        else:
            nav_html = '<a href="/shops" class="nav-btn">Shops</a>'
        nav_html += '<a href="/search" class="nav-btn">⌕ Search</a>'
        nav_html += '<a href="/contact" class="nav-btn">Contact</a>'
        nav_html += '<a href="#" onclick="if(confirm(\'Are you sure you want to logout?\')){{window.location=\'/logout\'}}; return false;" class="nav-btn logout-btn">Logout</a>'
    else:
        nav_html = '<a href="/shops" class="nav-btn">Shops</a><a href="/search" class="nav-btn">⌕ Search</a><a href="/contact" class="nav-btn">Contact</a><a href="/login" class="nav-btn">Vendor Login</a>'

    header_html = ""
    if show_header:
        header_html = f'''
        <header class="main-header">
            <div class="header-container">
                <div class="header-content">
                    <img src="/static/logo2.png" alt="FoodHub Pro Max" class="logo-image">
                    <nav class="header-nav">
                        <button class="hamburger" id="hamburger" aria-label="Toggle menu">
                            <span></span>
                            <span></span>
                            <span></span>
                        </button>
                        <div class="nav-menu" id="navMenu">{nav_html}</div>
                    </nav>
                </div>
            </div>
        </header>
        <div class="mobile-backdrop" id="navBackdrop"></div>
        '''

    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>{get_css()}</style>
        {extra_head}
    </head>
    <body>
        {header_html}
        <main class="page-container">{content}</main>
        <footer class="footer"><p>&copy; 2025 FoodHub Pro Max.</p></footer>
        <script>
        (function(){{
            const hamburger = document.getElementById('hamburger');
            const navMenu = document.getElementById('navMenu');
            const navBackdrop = document.getElementById('navBackdrop');
            if (hamburger && navMenu) {{
                // Only add mobile-hidden class on mobile viewports (< 768px)
                function isMobile() {{
                    return window.innerWidth < 768;
                }}

                function updateMenuVisibility() {{
                    if (isMobile()) {{
                        navMenu.classList.add('mobile-hidden');
                        if (navBackdrop) navBackdrop.classList.remove('active');
                        hamburger.classList.remove('active');
                    }} else {{
                        navMenu.classList.remove('mobile-hidden');
                        if (navBackdrop) navBackdrop.classList.remove('active');
                        hamburger.classList.remove('active');
                    }}
                }}

                // Initialize menu visibility
                updateMenuVisibility();

                // Update on window resize
                window.addEventListener('resize', updateMenuVisibility);

                hamburger.addEventListener('click', function(e) {{
                    e.stopPropagation();
                    if (isMobile()) {{
                        const opened = navMenu.classList.contains('mobile-hidden');
                        hamburger.classList.toggle('active');
                        navMenu.classList.toggle('mobile-hidden');
                        if (!navMenu.classList.contains('mobile-hidden')) {{
                            if (navBackdrop) navBackdrop.classList.add('active');
                        }} else {{
                            if (navBackdrop) navBackdrop.classList.remove('active');
                        }}
                    }}
                }});

                // Close menu when clicking a nav link (only on mobile)
                navMenu.querySelectorAll('a').forEach(link => {{
                    link.addEventListener('click', function() {{
                        if (isMobile()) {{
                            hamburger.classList.remove('active');
                            navMenu.classList.add('mobile-hidden');
                            if (navBackdrop) navBackdrop.classList.remove('active');
                        }}
                    }});
                }});

                // Close menu when clicking outside or on backdrop (only on mobile)
                document.addEventListener('click', function(e) {{
                    if (isMobile() && !hamburger.contains(e.target) && !navMenu.contains(e.target)) {{
                        hamburger.classList.remove('active');
                        navMenu.classList.add('mobile-hidden');
                        if (navBackdrop) navBackdrop.classList.remove('active');
                    }}
                }});

                if (navBackdrop) {{
                    navBackdrop.addEventListener('click', function(e) {{
                        if (isMobile()) {{
                            hamburger.classList.remove('active');
                            navMenu.classList.add('mobile-hidden');
                            navBackdrop.classList.remove('active');
                        }}
                    }});
                }}
            }}
        }})();
        </script>
    </body>
    </html>
    '''
